data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		#print(len(data))-print 很慢,改善
		count += 1
		if count % 1000 == 0: # %求餘數
			print(len(data))

		
print(len(data))
print(data[0])

