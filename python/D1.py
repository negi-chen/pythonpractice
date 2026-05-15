



li = ["kirishima", "rokumura", "midorikawa"]

# 以下にコードを追加

s = "san"
# c = range(3) -> no need

# li.append(s) -> this will add one more string inside sansan


# method one not we want

# for i in  range(len(li)): #i is each word and then i have to add them into li 
#     print(f"{li[i]}{s}")
    
#     # print(f"{li}{s}")

# kirishimasan
# rokumurasan
# midorikawasan

# method two
for i in range(len(li)):
    li[i] = li[i] + s
    
print (li)