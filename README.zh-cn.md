<!--
 * @Author: thinkvue@thinkvue.cn
 * @URL: https://thinkvue.com
 * @Date: 2020-05-25 20:55:07
 * @LastEditors: thinkvue@thinkvue.cn
 * @LastEditTime: 2020-05-25 23:38:52
 * @FilePath: \\GetOptions\\README.zh-cn.md
 * @Description:  
--> 
*************************************
# GetOptions中文说明  


********************************
## 说明

> 用于获取从控制台传递过来的参数，并把参数格式化为字典，例：

> `{'data':{'username':'root', 'password':'password','remember':True},'args':[]}`

> 如果参数不正确，则返回`{'errcode':int,'error':'error msg'}`

********************************
## 示例

```python
import GetOptions
params_config = {
        'host':     {'must': False,  'data': True,    'short': 'H',    'long': 'host',  'default': 'localhost'},
        'port':     {'must': False,  'data': True,    'short': 'O',    'long': 'port',  'default': 3306},
        'user':     {'must': True,   'data': True,    'short': 'U',    'long': 'user'},
        'passwd':   {'must': True,   'data': True,    'short': 'P',    'long': 'passwd'},
        'db':       {'must': True,   'data': True,    'short': 'D',    'long': 'db'},
        'init':     {'must': True,   'data': False,   'short': 'I',    'long': 'init'},
    }
print(GetOptions.get(params_config))
```
在控制台调用：
- `python3 test.py -H localhost -U root -P abc123 -D thinkvue -I abc 123`
打印结果：
- `{'data': {'host': 'localhost', 'port': 3306, 'user': 'root', 'passwd': 'abc123', 'db': 'thinkvue' , 'init': True}, 'args': ["abc", "123"]}`

********************************
## API及参数
只有一个公开函数：
`GetOptions.get(params_config, params=None, is_show_help=True)`

其中：
- `params_config`:必需参数，类型：`dict`，描述控制台参数的格式，一个`key`对应一个5个字段的字典
  + `key`：返回字段时的`key`
  + `must`:表示是否为必需参数，如果必需，未提供则报错返回
  + `data`:表示是否后面带了数据，例：`-i 3306`中`3306`为`-i`的数据
  + `short`:短名称，即`-i`,
  + `long`:长全称，即`--install`
  + `default`:默认值，如果`must`为`False`，且未提供，则把该字段设为默认值
- `params`:可选参数，类型：`list`，控制台选项，默认为`sys.argv`
- `is_show_help`：可选参数，类型：`bool`，如果出错时是否打印生成的帮助信息（列出根据`params_config`生成的命令格式）

********************************
## 注意

1. 不可以使用`-h`和`--help`，这两个为帮助说明，优先级最高，只要有这两个其中一个就会返回帮助文件不会返回其他结果；
2. 第一个非声明参数（返回结果放在`argv`里面的）不能是`-`或者`--`开头，否则会被认为是非法参数；
3. 支持多级调用，把`result['argv']`作为第二参数`params`即可。

********************************
## LICENSE

[MIT](./LICENSE)