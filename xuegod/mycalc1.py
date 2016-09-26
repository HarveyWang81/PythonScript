def jia(x,y):
	return (x+y)
def jian(x,y):
	return (x-y)
def cheng(x,y):
	return (x*y)
def chu(x,y):
	return (x/y)
func_dict = {'+':jia,'-':jian,'*':cheng,'/':chu}
oper_set = {'+','-','*','/'}
#运算符集合
#一行来输入，并且完成单项运算就OK
#2 *     3
#2+3
result = 0
while True:
	mystr = input('请输入你要做的操作:')
	mystr_set = set(mystr.strip())
	#去掉空格 变成集合
	oper = (mystr_set&oper_set).pop()
	#取出运算符
	num1 = int(mystr.split(oper)[0])
	num2 = int(mystr.split(oper)[1])
	result = func_dict[oper](num1,num2)
	print('结果是:',result)

mylist = [1,2,-3]

def getsum(mylist):
	mysum = 0
	for var in mylist:
		mysum += var
	return mysum

#
#阶段考核：不允许抄袭
#功能1：
#可以实现多位数字混合四则运算 + - * /
# 2 + 11 - 23 * 17 / 32  和真正的计算器得出的结果一致
#并且是一行

#不考虑有括号的

# 优先级  
# +- 低于 乘除 

def jiajian(*arg):
	res = 0
	for var in arg:
		res += var

#就一步

def chengchu(oper,*arg):
	res = 0
	if oper == '*':
		for var in arg:
			res *= arg
	if oper == '/':
		for var in arg:
			res /= arg

