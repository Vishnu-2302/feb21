n=int(input('enter the number : '))
ascii_value=97
for c in range(1,n+1):
	for r in range(1,n+1):
		print(chr(ascii_value),end='  ')
		ascii_value+=1
	print('\n')