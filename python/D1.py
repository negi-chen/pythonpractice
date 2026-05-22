

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



----------------------practice4---------------------------

4. 期待する出力値

[2.1, 3.8, 5.2]


li = list(map(float, input().split()))

print(li)




----------------------practice5---------------------------

 入力される値

3
8
1
3

 標準入力からの値取得方法はこちらをご確認ください

 期待する出力値

[8, 1, 3]



#method one
li = []

# print(li)

n = int(input())

# print(n)  this means below code will run n times 

for i in range(n):

    val = int(input())    
    li.append(val)
    
print(li)



# method two
n = int(input())

li = [int(input()) for i in range(n)]

print(li)





----------------------practice6---------------------------


演習課題「複数行、複数列の入力」

右のコードエリアには、与えられる入力の行数 n を受け取るコードがあります。

n 行の入力をリストにして受け取ってください。

また、各行を空白区切りのリストとして受け取り二重リストとして受け取るよう、このコードを修正してください。

 入力される値

2

paiza 株式会社

霧島 京子

 標準入力からの値取得方法はこちらをご確認ください

 期待する出力値

[['paiza', '株式会社'], ['霧島', '京子']]




# ----------method 1-----------

# so there are first int means that user will input the int number of format



# so here i will know how many i need to load  

n = int(input()) 



# this is to initilate the list 

li = [] 



# for debug

# print(n)

# print(li)



for c in range(n):

    # print(input())

    x = input()

    # print(x)

    li.append(x.split())

    # print(li)

print(li)

    

    # for y in li:

    #     print(y.split())


# ----------method 2-----------


    n = int(input())

li = [input().split() for i in range(n) ]

print(li)

