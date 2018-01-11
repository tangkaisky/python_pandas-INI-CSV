#coding: utf-8

import pandas as pd
import sys,os
import ConfigParser


# read ini
path = 'D:\\block_conception.ini'
cfg = ConfigParser.ConfigParser()
cfg.read(path)

print '读取配置文件成功\n'

sections = cfg.sections()
# print "options",sections
options = cfg.options(sections[2])
# print options

#creat a Dic 代码->概念股名称
Dic_0 = {}
for m in range(1,3):
	List_0 = []
	for n in range(len(options)):
		# try:
		List_0.append(cfg.get(sections[m],options[n]))
		# except ConfigParser.NoOptionError:
		# 	print "mistake"
		# 	continue
	Dic_0[sections[m]] = List_0 

#creat a dataFrame
df = pd.DataFrame(data=Dic_0,index=options)
print '显示构建的概念股dataframe\n',df

#df to csv 
df.to_csv('D:\\df.csv')
# print List_0