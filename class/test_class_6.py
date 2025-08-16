# クラスの継承の基本例

# 親クラス（スーパークラス）
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model} のエンジンを始動します。")

# 子クラス（サブクラス）
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # 親クラスのコンストラクタを呼び出す
        self.doors = doors

    def open_doors(self):
        print(f"{self.doors} 枚のドアを開けました。")

# 子クラス（サブクラス）
class Motorcycle(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc

    def rev_engine(self):
        print(f"{self.cc}cc のエンジンをふかしました！")

# 使い方
car = Car("トヨタ", "プリウス", 4)
motorcycle = Motorcycle("ホンダ", "CB400", 400)

car.start_engine()      # 親クラスのメソッド
car.open_doors()        # 子クラス独自のメソッド

motorcycle.start_engine()  # 親クラスのメソッド
motorcycle.rev_engine()    # 子クラス独自のメソッド
