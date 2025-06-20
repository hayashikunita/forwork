# もう少し応用的なクラスのサンプル：継承とクラス変数

# 親クラス
class Animal:
    total_animals = 0  # クラス変数

    def __init__(self, name):
        self.name = name
        Animal.total_animals += 1

    def speak(self):
        print(f"{self.name} は何かを話そうとしている…")

    @classmethod
    def show_total(cls):
        print(f"動物の総数: {cls.total_animals} 匹")


# 子クラス（Animalを継承）
class Cat(Animal):
    def speak(self):
        print(f"{self.name} がニャーと鳴いています。")


class Bird(Animal):
    def speak(self):
        print(f"{self.name} がピヨピヨと鳴いています。")


# インスタンス作成
cat1 = Cat("ミケ")
bird1 = Bird("ピヨ")
bird2 = Bird("チュン")

# メソッド実行
cat1.speak()
bird1.speak()
bird2.speak()

# クラスメソッド実行
Animal.show_total()
