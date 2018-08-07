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


print(data[0])
print('------------')
print(data[1])
