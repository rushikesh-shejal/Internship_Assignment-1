def even_generator(n):
	for i in range(1,n):
		if i%2==0:
			yield i
			
num=int(input("Enter the range of even numbers::"))
result=even_generator(num)
for items in result:
	print(items)