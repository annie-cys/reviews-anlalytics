data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		if len(data) % 1000 == 0 :# %餘數
			print(len(data))
print(len(data))# 印出data長度

print(data[0])
print('--------------')
print(data[1])

#print很花時間
