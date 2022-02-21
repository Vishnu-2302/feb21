n=int(input('enter the number : '))
for c in range(1,n+1):
	for r in range(1,n-c+2):
		print('*',end='  ')
	print('\n')