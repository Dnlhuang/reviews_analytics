data = []  # 空清單
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:  # %用來求餘數
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)

print('每筆留言平均是', sum_len / len(data), '個字')

new = []
for d in data:
	if len(d) < 100:
		new.append(d) # 把字數小於100的留言，加入清單(new)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[100])


good = []
for g in data:
	if 'good' in g:
		good.append(g)
print('一共有', len(good), '筆留言提到good')
print(good[0])


good = [g for g in data if 'good ' in g]  #等於第26~29行
# output = [(number-1) for number in reference if number % 2 == 0]
print(good)

bad = ['bad' in g for g in data]  #第41~43行
print(bad)

bad = []
for d in data:
	bad.append('bad' in d)
print(bad)