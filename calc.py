import datetime

file = open('zadan.txt','r')
dd = datetime.datetime.now()
dd = dd.strftime('%d.%m.%Y')
ss = datetime.datetime.now()
ss = ss.strftime('%H:%M:%S')
dd = str(dd)
ss = str(ss)

#Основной цикл
while True:
	for line in file:
		#переменные калькулятора
		s = line.split(' ')
		ob1 = float(s[0])
		ob2 = float(s[2])
		e = s[1]
		#Основной код условий калькулятора
		if e == '+':
			result = ob1 + ob2
		elif e == '-':
			result = ob1 - ob2
		elif e == '/':
			if ob1 == 0 or ob2 == 0:
				print('Я не могу делить на ноль')
				continue
			else:
				result = ob1 / ob2
		elif e == '*':
			result = ob1 * ob2
		else:
			print('я не могу это посчитать')
			
		otvet = str(ob1)+e+str(ob2)+' = '+str(result)
		print('Ответ:',otvet +'\n')
		
		#Запись ответов в файл reshenie
		result = str(result)
		ob1 = str(ob1)
		ob2 = str(ob2)
		k = open('reshenie_'+dd+'.txt','a+')
		k.write(ob1+e+ob2+'='+result+'     time: '+ss+'\n')
		k.close()
	file.close
input('')