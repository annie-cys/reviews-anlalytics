data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		if len(data) % 1000 == 0 :# %餘數
			print(len(data))
print('檔案讀取完了, 總共有',len(data),'筆資料')# 印出data長度
total = 0
for review in data:
	total += len(review)
    #迴圈跑一次讀一筆, 每次讀完都加總算出總長度
print('每筆留言平均有',total/len(data),'字')

