# メソッドのオーバーライド（上書き）に関する継承の例

# 親クラス
class Animal:
    def speak(self):
        print("何かの動物が鳴いています。")

# 子クラス
class Dog(Animal):
    def speak(self):  # オーバーライド：親クラスの speak メソッドを上書き
        print("ワンワン！")

class Cat(Animal):
    def speak(self):  # オーバーライド
        print("ニャー！")

# 使い方
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()  # 子クラスでは上書きされたメソッドが呼ばれる
