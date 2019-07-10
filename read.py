data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		if len(data) % 1000 == 0 :
			print(len(data))
print('檔案讀取完了, 總共有',len(data),'筆資料')

print(data[0])


#分析
total = 0
for review in data:
	total += len(review)
print('每筆留言平均有',total/len(data),'字')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new),'筆留言小於100字')
print(new[0])
print(new[1])


good = []
for d in data:
	if 'good' in d :#檢查 good 在不在清單
		good.append(d)
print('共有',len(good), '筆留言提到good')


#小整理
#output = [運算for變數in清單 篩選條件]



#文字計數
#nasted forloop
wc = { } #word_count
for d in data: #d 一筆留言
	words = d.split() #words 裝著一筆留言一個一個字的清單 
	for word in words:
		if word in wc:
			wc[word] += 1 #從wc字典
		else:
			wc[word] = 1 #新增新的key進wc字典
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請輸入想查找的字: ')
	if word == 'q':
		print('感謝使用本查詢功能 ! ')
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('沒有出現過喔')

#出現空字串 出現多個空白也進入排行
