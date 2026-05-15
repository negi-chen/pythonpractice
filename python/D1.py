

----------------------practice1---------------------------

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



----------------------practice2---------------------------

li = ["paiza", "kirishima", "python"]

# ここから下の行を足してください

# for first one
# x = enumerate(li)
# print(x)  ->  <enumerate object at 0x4f0b03e5cae0>


# # for second 
# x = enumerate(li)
# for i in x:
#     print(i)
    
#     |
#     V
# (0, 'paiza')
# (1, 'kirishima')
# (2, 'python')
    


# for third
x = enumerate(li)
for i, a in x:
    print(i, a)
#     |
#     V
0 paiza
1 kirishima
2 python


----------------------practice3---------------------------

3.
 期待する出力値

['0', '30', '7', '813', '43']

# method one

# a = [0, 30, 7, 813, 43]

# # 以下のコードを修正してください
# b =  [str(x) for x in a ]
# # print(x)
# # b = []
# print(b)



# method two

a = [0, 30, 7, 813, 43]
b =[]
# 以下のコードを修正してください

for x in a :
    b.append(str(x))
    
print(b)
