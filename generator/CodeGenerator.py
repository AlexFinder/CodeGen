# coding=utf-8
'''
Created on Aug 8, 2015

@author: alex
'''
from Cheetah.Template import Template


# 替换模板参数
def modelClass(data):
    # 如果同时加载多个模板  
    tmpls = data['templateName'].split(',')
    fileNames = data['outputFileName'].split(',')
    if(len(tmpls) != len(fileNames)):
        print 'init.conf read template error...'
        return
    for i in range(len(tmpls)):
        templatePath = './templates/' + tmpls[i]
        code = Template(file=templatePath, searchList=[data])
        saveFile(code.__str__(), data['outputPath'] + "/" + fileNames[i])
    
    
# 保存文件
def saveFile(code, path):
    f = open(path, 'w+')
    f.write(code)
    f.close()
    
# 读取配置文件
def readConfig(data):
    try:
        file = open('init.conf', 'r')
        for line in file.readlines():
            line = line.strip()
            # 排除‘＃’的注释项
            if(len(line) == 0 or line[0] == '#'):
                continue
            # 检查不合法配置
            values = line.split('=')
            if(len(values) != 2):
                print 'init.conf error...(%s)' % values
                return 
            # 将配置参数读取保存,注意处理复杂元数据
            if('[' in values[1] or '{' in values[1]):
                data[values[0]] = eval(values[1])
            else:
                data[values[0]] = values[1]
        file.close()
    except IOError:
        print 'init.conf not found...'
        if file:
            file.close()
    
def main():
    data = {}
    readConfig(data)
    modelClass(data)
    
if __name__ == '__main__':
    main()
    
    
