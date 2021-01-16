data = []
count = 0
with open("reviews.txt","r") as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 100000 == 0: #求餘數，此行代表當讀取1000筆才印一次
            print(len(data))
print("檔案讀取完畢，總共有",len(data),"筆資料")

sum_len = 0
for d in data:
    sum_len += len(d)
print("留言平均長度為",sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print("一共有",len(new),"筆留言長度小於100")
print(new[0])