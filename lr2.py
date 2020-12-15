x = [0,5]
h = 100  

x_i = []

def set(x):                             
	for i in range(0, h):
		if(i == 0 or i == h):
			x_i.append(x[i])
		else:
			dx = x_i[i-1]+(x[1]-x[0])/h
			x_i.append(dx)
			print(dx)
	return x_i


def f(x):
	return x



def summ_area(array):
	area = 0
	for i in range(len(array)-2):
		f_prev = f(array[i])        
		f_next = f(array[i+1])
		if(f_prev < f_next):
			area += (array[i+1] - array[i])*abs(f_prev)
		else:
			area += (array[i+1] - array[i])*abs(f_next) 
	print('Площадь:',area)
	return area

summ_area(set(x))

