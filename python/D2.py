
----------------------practice7---------------------------

 入力される値
age


 標準入力からの値取得方法はこちらをご確認ください

 期待する出力値
18


# my method

character = {"name": "kirishima", "age": 18, "pc": "margaret"}

k = input()

for key in character:
    if key == k:
        print(character[key])


#right ans

character = {"name": "kirishima", "age": 18, "pc": "margaret"}
k = input()

print(character[k])


----------------------practice8---------------------------


右側のコードエリアに、あるキャラクターの情報を表した辞書 character と、追加したい key と value それぞれが代入された変数 k, v があります。
辞書の key が変数 k の値、 value が変数 v の値となるよう要素を追加してください。

 入力される値
gender girl

 標準入力からの値取得方法はこちらをご確認ください
 期待する出力値

{'name': 'kirishima', 'age': 18, 'pc': 'margaret', 'gender': 'girl'}


character = {"name": "kirishima", "age": 18, "pc": "margaret"}
# here already have input
k, v = input().split()


character[k] = v

print(character)



----------------------practice9---------------------------

key が整数値で、value が key の数値を 3 倍した値になるような辞書を生成・出力してください。
key の値は 0 から連続した整数入力される値 n 個とする。

 入力される値
5

 標準入力からの値取得方法はこちらをご確認ください

 期待する出力値
{0: 0, 1: 3, 2: 6, 3: 9, 4: 12}


n = int(input()) #input is 5

d = {x: x*3 for x in range(n)}
print(d)



----------------------practice10---------------------------

右側のコードエリアには、ローカル変数 name と敬称をつける関数 give_an_honorific が用意されています。
しかし、関数内でグローバル変数へ再代入しようとしたためエラーが起きてしまいます。
修正して、メッセージを正しく表示させてください。

 期待する出力値
kirishimasan


name = "kirishima"


def give_an_honorific():
    def name_and_honorific():
         c = name + "san"
         return c
    print(f"{name_and_honorific()}")


give_an_honorific()



----------------------practice11---------------------------

def rec_sum(n):
    print(f"n = {n}")
    if n == 0:
        return 0
        
    print(f"n : {n} + rec_sum : {rec_sum(n-1)}")
    return n + rec_sum(n-1)      #rec_sum(0) == 0 #rec_sum(1) == 1 #rec_sum(2) == 2 + 1(前一位) #rec_sum(3) == 3 + rec_sum(2)
    
rec_sum(10)


----------------------practice12---------------------------

 期待する出力値
3628800

def rec_product(n):
    # 以下にコードを記述 
    # print(n)
    if n == 1 :
        return 1
    
    return n * rec_product(n - 1)

print(rec_product(10))


----------------------practice13---------------------------

 期待する出力値
16


#my methods???
class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    # 以下にコードを記述
    
    def ram_expansion(self, expansion):
        self.ram_expansion = expansion


pc = PersonalComputer(8, 128)

pc.ram_expansion(16)

print(pc.ram_expansion)



#correct method
class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    # 以下にコードを記述
    def ram_expansion(self, expansion):
        self.ram += expansion


pc = PersonalComputer(8, 128)
pc.ram_expansion(8)
print(pc.ram)


----------------------practice14---------------------------

右側のコードエリアには、クラス PersonalComputer とインスタンス pc が用意されています。
ram と storage を増設するメソッド ram_and_storage_expansion 内で ram、storage それぞれを増設するメソッド ram_expansion、storage_expansion を実行してください。

 期待する出力値
16 256


class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def ram_expansion(self, gb):
        self.ram += gb

    def storage_expansion(self, gb):
        self.storage += gb

    def ram_and_storage_expansion(self, ram_gb, storage_gb):
        self.ram_expansion(ram_gb)
        self.storage_expansion(storage_gb)


pc = PersonalComputer(8, 128)
# print(pc.ram_expansion(11))
# print(pc.storage_expansion(20))
pc.ram_and_storage_expansion(8, 128) #this is mean i get this two elements into ram_gb And storage_gb

print(pc.ram, pc.storage)
# pc.ram_and_storage_expansion(8, 128)
# print(pc.ram, pc.storage)



----------------------practice15---------------------------

右側のコードエリアには、クラス PersonalComputer とインスタンス pc、ram を出力するコードが用意されています。
メンバ変数 ram ではなくクラス変数 ram を出力するよう修正してください。

 期待する出力値
64

class PersonalComputer:
    ram = 64 #HERE ALREADY DEFULT

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def ram_expansion(self, gb):
        self.ram += gb


pc = PersonalComputer(8, 128)

newpc = PersonalComputer(64, 128)
print(PersonalComputer.ram)



----------------------practice16---------------------------

 演習課題「アクセス制限」

右側のコードエリアには、クラス PersonalComputer とインスタンス pc が用意されています。
メンバ変数 ram にアクセス制限をかけて、クラスの外側からメンバ変数を自由に使うことができないようにしてください。

 期待する出力値

プライベート変数にはアクセスできません。

class PersonalComputer:
    def __init__(self, ram, storage):
        self.__ram = ram
        self.storage = storage


pc = PersonalComputer(8, 128)
try:
    pc.ram += 8
    print(pc.ram)
except:
    print("プライベート変数にはアクセスできません。")




----------------------practice17---------------------------

右側のコードエリアには、クラス とインスタンス と メンバ変数 を出力するコードが用意されています。
しかし、アクセス制限がかかっているためエラーが起きてしまします。
正しく取得できるよう修正してください。PersonalComputerpc__ram

 期待する出力値
8


class PersonalComputer:
    def __init__(self, ram, storage):
        self.__ram = ram
        self.storage = storage


    def print_fun(self):
        print(f"{self.__ram}")

pc = PersonalComputer(8, 128)

pc.print_fun()



----------------------practice18---------------------------

右側のコードエリアには、クラス PersonalComputer が用意されています。
PersonalComputer をスーパクラスにしたサブクラス Laptop を定義してください。

 期待する出力値
8


class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

# 以下にコードを記述

class Laptop(PersonalComputer):
    pass

laptop_pc = Laptop(8, 128)
print(laptop_pc.ram)


----------------------practice19---------------------------

 演習課題「スーパークラスのメソッドの利用」

右側のコードエリアには、クラス PersonalComputer のサブクラス Laptop とインスタンス laptop_pc が用意されています。
スーパークラスのメソッド ram_expansion を呼び出してください。
ただし、引数は 8 とします。

 期待する出力値
16

class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def ram_expansion(self, gb):
        self.ram += gb
        print(self.ram)


class Laptop(PersonalComputer):
    pass


laptop_pc = Laptop(8, 128)
# 以下にコードを記述

laptop_pc.ram_expansion(8)


----------------------practice20---------------------------


 演習課題「サブクラスのコンストラクタを定義」

右側のコードエリアには、クラス のサブクラス とインスタンス が用意されています。
サブクラス のコンストラクタを定義してください。
メンバ変数はスーパークラスの ram、storage に加えキーボード配列を表す key_layout とする。PersonalComputerLaptoplaptop_pcLaptop

 期待する出力値

jis


class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage


class Laptop(PersonalComputer):
    # 以下にコードを記述
    def __init__(self, ram, storage, key_layout):
        super().__init__(ram, storage) 
        self.key_layout = key_layout



laptop_pc = Laptop(8, 128, "jis")
print(laptop_pc.key_layout)


----------------------practice21---------------------------
右側のコードエリアには、クラス PersonalComputer のサブクラス Laptop とインスタンス laptop_pc が用意されています。
サブクラス Laptop にはバッテリーを表すメンバ変数 battery があります。引数で受け取った値を battery に足す、充電を表すメソッド charge を定義してください。


 期待する出力値

100


class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage


class Laptop(PersonalComputer):
    def __init__(self, ram, storage, key_layout, battery=50):
        super().__init__(ram, storage)
        self.key_layout = key_layout
        self.battery = battery

    # 以下にコードを記述
    def charge(self, elect):
        self.battery += elect
    
laptop_pc = Laptop(8, 128, "jis")
laptop_pc.charge(50)
print(laptop_pc.battery)


----------------------practice22---------------------------

 演習課題「サブクラスのメソッドを定義」

右側のコードエリアには、クラス のサブクラス が用意されています。
サブクラス をスーパクラスにしたサブクラス を定義してください。PersonalComputerLaptopLaptopPaizaBook

 期待する出力値

8 128 jis




class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage


class Laptop(PersonalComputer):
    def __init__(self, ram, storage, key_layout):
        super().__init__(ram, storage)
        self.key_layout = key_layout


# 以下にコードを記述
class PaizaBook(Laptop):
    pass

paizabook = PaizaBook(8, 128, "jis")
print(paizabook.ram, paizabook.storage, paizabook.key_layout)



----------------------practice23---------------------------

 演習課題「継承関係の確認」

右側のコードエリアには、クラス PaizaBook が用意されています。
このクラス PaizaBook の継承関係を出力してください。

 期待する出力値

(<class '__main__.PaizaBook'>, <class '__main__.Laptop'>, <class '__main__.PersonalComputer'>, <class 'object'>)


class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage


class Laptop(PersonalComputer):
    def __init__(self, ram, storage, key_layout):
        super().__init__(ram, storage)
        self.key_layout = key_layout


class PaizaBook(Laptop):
    pass


# 以下にコードを記述

print(PaizaBook.__mro__)

