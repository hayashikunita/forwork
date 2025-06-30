# Pythonクラスの基本を学ぶサンプルプログラム

# クラス定義
class Dog:
    # 初期化メソッド（コンストラクタ）
    def __init__(self, name, age):
        self.name = name  # インスタンス変数 name
        self.age = age    # インスタンス変数 age

    # メソッド（関数）
    def bark(self):
        print(f"{self.name} がワンワン！と吠えました。")

    def introduce(self):
        print(f"こんにちは、僕の名前は {self.name}、{self.age} 歳です！")

    def birthday(self):
        self.age += 1
        print(f"{self.name} の誕生日です！{self.age} 歳になりました。")


# インスタンスを作成
dog1 = Dog("ポチ", 3)
dog2 = Dog("コロ", 5)

# メソッドを使う
dog1.introduce()
dog1.bark()
dog1.birthday()

print("---")

dog2.introduce()
dog2.bark()
