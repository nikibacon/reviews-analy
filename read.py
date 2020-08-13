data = []
count = 0
length = 0 
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        #print(len(data))-print 很慢,改善
        count += 1
        #if count % 1000 == 0: # %求餘數
            #print(len(data))

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
print(new[0])

good = []
for d in data:
  if 'good' in d:
      good.append(d)
print('一共有', len(good), '比留言裡有提到good')    
print(good[0])

good = [d for d in dara if 'good' in d]
快寫法,



# 文字計數

wc = {} # word_count
for d in data:
    words = d.split() # 預設就是切space,而且遇到連續space不會切會跳過
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # 新增新的key進wc字典 

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))
print(wc['Allen'])


while True:
    word = input('請問你想查什麼字:')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數是:', wc[word])
    else:
        print('這個字沒有出現過喔!')
print('感謝使用本查詢功能!')
