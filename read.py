data = []
count = 0
length = 0 
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		#print(len(data))-print 很慢,改善
		count += 1
		if count % 1000 == 0: # %求餘數
			print(len(data))

		length += len(line)

avg_len = length / len(data)

		
print('檔案讀取完畢, 總共有', len(data), '筆資料')
print('留言平均長度總共有', avg_len, '個字')



print('第一筆留言:')
print(data[0])

#篩選概念

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')


