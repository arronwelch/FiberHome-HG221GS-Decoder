'''
a program to decode FiberHome HG221GS FiberCat telecomadmin password 
wget http://192.168.1.1/cgi-bin/baseinfoSet.cgi

"baseinfoSet_TELECOMACCOUNT":"telecomadmin",
"baseinfoSet_TELECOMPASSWORD":"114&73&55&110&69&37&53&113&",
"baseinfoSet_USERACCOUNT":"useradmin",
"baseinfoSet_USERPASSWORD":"57&71&72&50&76&",

设备类型	EPON
生产厂家	FiberHome
设备型号:	HG221GS
硬件版本号:	HS.V2.0
软件版本号:	E60D1.00MA000
'''
code='114&73&55&110&69&37&53&113&'[:-1]    # "baseinfoSet_TELECOMPASSWORD":"114&73&55&110&69&37&53&113&"
list=map(int,code.split('&'))
result=[]
for i in list:
	if i > 57:
		i-=4
	result.append(chr(i))
print (''.join(result))    # output password:nE7jA%5m


