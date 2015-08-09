Cheetah-2.4.4.tar.gz## About CodoGen

CodeGen是基于Python实现的代码生成器，采用```cheetah```技术（类似j2ee的```velocity```），你可以根据相应配置去定制不同的模板，再根据模板生成自己想要的代码。

- __优点__：小巧、高效
- __缺点__：模板方面需要适应学习

### 使用准备

- python
- easy_install 或者 pip （可选）
- cheetah

#### python

python，一般Linux发行版本默认安装，可以使用，windows系统请自行Google安装教程。

####easy_install 或者 pip （可选）

easy_insall的作用和perl中的cpan，ruby中的gem类似，都提供了在线一键安装模块的傻瓜方便方式，而pip是 easy_install的改进版，提供更好的提示信息，删除package等功能。老版本的python中只有easy_install，没有pip。

具体资料及安装教程请自行Google。

#### cheetah

cheetah是基于python的一个模板框架，详细信息请参考：

- [https://wiki.python.org/moin/Cheetah](https://wiki.python.org/moin/Cheetah)
- [http://www.cheetahtemplate.org/](http://www.cheetahtemplate.org/)
  
基于easy_install安装

```
$ easy_install cheetah
```

基于pip安装

```
$ pip install cheetah
```

基于安装包安装

```
$ wget https://pypi.python.org/packages/source/C/Cheetah/Cheetah-2.4.4.tar.gz#md5=853917116e731afbc8c8a43c37e6ddba
$ tar -zxvf Cheetah-2.4.4.tar.gz
$ cd Cheetah-2.4.4/
$ python setup.py install
```

### 使用

- init.conf 初始配置文件
- templates/ 目录下用于存放自定义的模板文件

#### 初始化配置

```
#模板名称，可以是一个，也可以是多个，多个时，英文逗号隔离，并且要与下面的＃输入文件对应，一个模板生成一个文件
templateName=BOTemplate.tmpl,ServiceTemplate.tmpl
#输出路径
outputPath=./
#输出文件，可以是一个，也可以是多个，多个时，英文逗号隔离。
outputFileName=Student.java,StudentService.java

#可变替换参数，这些参数在模板文件中定义，等号右面的值是需要替换的，支持列表与字典及复杂对象，用于模板中的循环
#常用方法
packagePath=com.zhanggz.entity
className=student
#列表用法 
list=['one','two','three']
#字典用法
dict={'property':'name', 'type':'String'}
#复杂对象用法
properties=[{'property':'name', 'type':'String'}, {'property':'age', 'type':'Integer'}, {'property':'birthday', 'type':'date'}]
```

#### 模板使用

```
#参数引用 
$parameter
#列表参数引用
$parameters[1]
#字典参数引用
$parameters.type
#如需要拼接，请加{}
${classNmae}Service
#引用参数首字母大写
$parameter.capitalize()
# if使用
#if $parameter == 'xxx'
your code....
#end if
# for 循环
#for $prop in $properties
your code...
#end for
```

详细请参考[《官方手册》](http://www.cheetahtemplate.org/docs/users_guide.pdf)
