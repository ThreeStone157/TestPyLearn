#coding: utf-8


def slices():
	L = ["张三", "李四", "王五", "赵六", "魁七"]
	L2 = list(range(100))
	r = []
	i = 0
	for j in L:
		r.append(j)
		i += 1
		if i == 3:
			break
	print(L[0: 3])
	print(L[0:])
	print(L[:9])
	print(L[0])
	print(r)
	print(L2)
	print(L2[-10:])

def trim(s):
	if len(s) < 1:
		print(len(s))
		return s
	elif s[-1] == " ":
		s = s[0: -1]
		s = trim(s)
	elif s[0] ==" ":
		s = s[1:]
		s = trim(s)
	return s

def digui(s, i):
	if i < 5:
		i += 1
		digui(s, i)
	return s
def ranges():
	L = [X * X for X in range(1, 11)]
	print(L)
	L2 = [m+n for m in "ABC" for n in "ZXY"]
	print(L2)
	d = {'x': 'A', 'y': 'B', 'z': 'C'}
	for k, v in d.items():
		print(k+":"+v)

def createCounter():
    f = [0]
    def counter():
      f[0] =f[0] +1
      return f[0]
    return counter



def test1(*args, **kw):
	print(type(args), type(kw))


if __name__ =="__main__":
	# if trim('hello  ') != 'hello':
	# 	print('测试失败!')
	# elif trim('  hello') != 'hello':
	# 	print('测试失败!')
	# elif trim('  hello  ') != 'hello':
	# 	print('测试失败!')
	# elif trim('  hello  world  ') != 'hello  world':
	# 	print('测试失败!')
	# elif trim('') != '':
	# 	print('测试失败!')
	# elif trim('    ') != '':
	# 	print('测试失败!')
	# else:
	# 	print('测试成功!')
	# ranges()
	# test1()
	A = createCounter()
	print(A(), A())
	print(A())
	print(A())

	print(A())


