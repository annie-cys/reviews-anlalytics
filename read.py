data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())#把留言line一條一條加進去
		if len(data) % 1000 == 0 :# %餘數
			print(len(data))
print('檔案讀取完了, 總共有',len(data),'筆資料')# 印出data長度
total = 0
for review in data:
	total += len(review)
    #迴圈跑一次讀一筆, 每次讀完都加總算出總長度
    #review 第一次等於第一則, 第二次等於第二則
print('每筆留言平均有',total/len(data),'字')
#for loop的意思是把清單中的東西一個一個拿出來
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new),'筆留言小於100字')
print(new[0])
print(new[1])