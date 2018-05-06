
import numpy as np
import pandas as pd 
import time
import random
import sys

delay = 0
delay1 = 0.5


def printkrasivo(s):
	s = printwithotstup(s)
	s = s + '\n'
	strtoprint = ''
	for i in s:
		strtoprint = strtoprint + str(i)
		sys.stdout.write('\r\r' + (strtoprint) + '')
		time.sleep(0.02)


def printwithotstup(s):
	otstup = (40 - len(s)) // 2
	return(otstup * ' ' + s)


def screen():
	printkrasivo('████████████████████████████████████████')
	printkrasivo('█─███─█────█───█────█───█──█──██████████')
	printkrasivo('█──█──█─██─██─██─██─██─███───███████████')
	printkrasivo('█─█─█─█────██─██────██─████─████████████')
	printkrasivo('█─███─█─██─██─██─█─███─███───███████████')
	printkrasivo('█─███─█─██─██─██─█─██───█──█──██████████')
	printkrasivo('████████████████████████████████████████')
	printkrasivo('████████████████████████████████████████')
	printkrasivo('█────█─██─█────█─███──█──█───█───█───███')
	printkrasivo('█─██─█──█─█─██─█─████───██─████─██─█████')
	printkrasivo('█────█─█──█────█─█████─███───██─██───███')
	printkrasivo('█─██─█─██─█─██─█─█████─█████─██─████─███')
	printkrasivo('█─██─█─██─█─██─█───███─███───█───█───███')
	printkrasivo('████████████████████████████████████████')


def main():
	while True:
		printkrasivo('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
		printkrasivo('1.Input completed matrix')
		printkrasivo('2.Generate matrix')
		printkrasivo('3.Load your matrix')
		printkrasivo('4.Generate matrix to file')
		printkrasivo('5.Exit to program')
		vibor = int(input(printwithotstup('Input value: ')))

		if vibor == 1:
			time.sleep(delay)
			printkrasivo('↓Your matrix↓')
			time.sleep(1)
			matrix = np.array([
				[1,2,3,4,5,6,7,8,9,10],
			 	[11,12,13,14,15,16,17,18,19,20],
				[21,22,23,24,25,26,27,28,29,30],
				[31,32,33,34,35,36,37,38,39,40],
				[41,42,43,44,45,46,47,48,49,50]
				]).reshape(25, 2)
			printkrasivo('Matrix:')
			print(str(matrix))
			printkrasivo('Min value  matrix: ' + str(matrix.min()))
			printkrasivo('Max value  matrix: ' + str(matrix.max()))
			printkrasivo('First value matrix: ' + str(matrix[0]))
			printkrasivo('Second value matrix: ' + str(matrix[2]))
			printkrasivo('Matrix analysis completed!')

		if vibor == 2:
			z = int(input(printwithotstup('Input value matrix: ')))
			matrix = np.random.random(z).reshape(int(z / 2), 2)
			printkrasivo('↓Your matrix↓')
			print(matrix)
			printkrasivo('Min value  matrix: ' + str(matrix.min()))
			printkrasivo('Max value  matrix: ' + str(matrix.max()))
			printkrasivo('First value matrix: ' + str(matrix[0]))
			printkrasivo('Second value matrix: ' + str(matrix[2]))
			printkrasivo('Matrix analysis completed!')

		if vibor == 3:
			matrix = open('t.txt', 'r')
			matrix2 = matrix.read()
			matrix = matrix2.split(' ')
			for i in range(0, len(matrix)):
				matrix[i] = int(matrix[i])
			if len(matrix) % 2 == 1:
				printkrasivo(printwithotstup('Will remove last value: ' + str(matrix[len(matrix) - 1])))
				matrix.remove(matrix[len(matrix) - 1])
			arr5 = np.array(matrix).reshape(int(len(matrix) / 2), 2)
			printkrasivo('↓Your matrix↓')
			print(arr5)
			printkrasivo('Min value  matrix: ' + str(arr5.min()))
			printkrasivo('Max value  matrix: ' + str(arr5.max()))
			printkrasivo('First value matrix: ' + str(arr5[0]))
			printkrasivo('Second value matrix: ' + str(arr5[2]))
			printkrasivo('Matrix analysis completed!')

		if vibor == 4:
			printkrasivo('1. Random matrix')
			printkrasivo('2. Not random matrix')
			vibor1 = int(input(printwithotstup('Input value: ')))
			ll = []
			if vibor1 == 1:
				l = int(input(printwithotstup('length of matrix: ')))
				maxv = int(input(printwithotstup('input max value: ')))
				printkrasivo('Pls..Wait)')
				for i in range(0, l):
					if i < l - 1:
						ll.append(str(random.randrange(0, maxv)) + ' ')
					else:
						ll.append(str(random.randrange(0, maxv)))
			if vibor1 == 2:
				l = int(input(printwithotstup('length of matrix: ')))
				printkrasivo('Pls..Wait)')
				for i in range(0, l):
					if i < l - 1:
						ll.append(str(i) + ' ')
					else:		
						ll.append(str(i))
			file1 = open('t.txt', 'w')
			if ll != []:
				for i in ll:
					file1.write(i)
				file1.close()	
				printkrasivo('Matrix generated!')	
			else:
				pass

		if vibor == 5:
			print
			printkrasivo('GoodBay!)')
			time.sleep(delay * 3)
			exit()


if __name__ == '__main__':
	screen()
	main()














































