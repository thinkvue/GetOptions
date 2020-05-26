#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 :Author: thinkvue@thinkvue.cn
 :URL: https://thinkvue.com
 :Date: 2020-05-25 15:38:11
 :LastEditors: thinkvue@thinkvue.cn
 :LastEditTime: 2020-05-25 23:21:08
 :FilePath: \\GetOptions\\GetOptions\\GetOptions.py
 :Description:  
"""

__all__ = ["get"]

def get(params_config, params=None, is_show_help=True):
    """标准化处理参数

    根据提供的params_config参数，提供参数params中的字段，返回字典
    params_config例：
        {
            'username':
                {'must':False,'data':True,'short':'U','long':'username','default':'root'},
            'password':
                {'must':True,'data':True,'short':'P','long':'password'},
            'remember':
                {'must':False,'data':False,'short':'R','long':'remember'},
        }
    其中：
        username：返回字段时的key
        must:表示是否为必需参数，如果必需，未提供则报错返回
        data:表示是否后面带了数据，例：-i 3306中3306为-i的数据
        short:短名称，即-i,
        long:长全称，即--install
        default:默认值，如果must为False，且未提供，则把该字段设为默认值
    成功返回：{'data':{'username':'root', 'password':'password','remember':True},'args':[]}
    失败返回：{'errcode':int,'error':'error msg'}

     :param params_config: dict,每个key对应包含must（是否必须）、data（是否含有数据）、short（短名称）、long（长名称）等4个字段的字典
     :param params:list,系统参数 默认为sys.params
     :param is_show_help:bool,是否显示帮助信息，默认为True
     :return: {dict} : 例：{'data':{'username':'root', 'password':'password','remember':True},'args':[]}
    """
    import getopt
    import sys
    if not params:
        params = sys.argv
    ret_dict = {}
    options = ''
    long_options = []
    readme = params[0]+" "
    for key1, dict1 in params_config.items():
        has_add = False
        short = dict1.get('short')
        long_tmp = dict1.get('long')
        has_data = dict1.get('data')
        must = dict1.get('must')
        if(short):
            options += (short+':' if has_data else short)
            readme_tmp = '-%s' % short
            if(has_data):
                readme_tmp = '%s <%s>' % (readme_tmp, key1)
            if not must:
                readme_tmp = '[%s]' % readme_tmp
            readme += readme_tmp+"  "
            has_add = True
        if(long_tmp):
            long_options.append(long_tmp+'=' if has_data else long_tmp)
            if not has_add:
                readme_tmp = '--%s ' % long_tmp
                if(has_data):
                    readme_tmp += '%s <%s> ' % (readme_tmp, key1)
                if not must:
                    readme_tmp = '[%s]' % readme_tmp
    try:
        opts, args = getopt.getopt(params[1:], options, long_options)
    except getopt.GetoptError as e:
        if is_show_help:
            print('\033[1;31;43m Parameters not in the setting: \033[0m')
            print(e)
            print("\nHelp: \n", readme)
        return {'errcode': -1, 'error': 'Parameters not in the setting:'+e.__str__()}
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            if is_show_help:
                print(readme)
            return {'errcode': 0, 'error': readme}
        for key, dict1 in params_config.items():
            if opt in ('-'+dict1.get('short'), '--'+dict1.get('long')):
                ret_dict[key] = arg if arg else True
    error = ""
    for key, dict1 in params_config.items():
        if key not in ret_dict:
            if dict1.get('must'):
                error += '  -%s <%s>' % (dict1.get('short'), key)
            elif dict1.get('default'):
                ret_dict[key] = dict1.get('default')
    if error:
        if is_show_help:
            print("\033[1;31;43mMissing parameters:  \033[0m")
            print(error)
            print('\nHelp: \n', readme)
        return {'errcode': -1, 'error': 'Missing parameters: '+error}
    return {'data': ret_dict, 'args': args}


if __name__ == "__main__":
    import sys
    params_config = {
        'port':     {'must': False,  'data': True,    'short': 'O',    'long': 'port',  'default': 3306},
        'host':     {'must': False,  'data': True,    'short': 'H',    'long': 'host',  'default': 'localhost'},
        'user':     {'must': True,   'data': True,    'short': 'U',    'long': 'user'},
        'passwd':   {'must': True,   'data': True,    'short': 'P',    'long': 'passwd'},
        'db':       {'must': True,   'data': True,    'short': 'D',    'long': 'db'},
    }
    params = sys.argv if len(sys.argv) > 1 else ['test.py', '-H','localhost','-U','root','-P','abc123','-D','thinkvue']
    print(get(params_config, params))