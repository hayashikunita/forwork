# 演算子のオーバーロード（+演算子の使い方を定義）

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __add__ メソッドを定義して、+ 演算子で Point クラスのインスタンス同士を足せるようにしています。
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    # __str__ でインスタンスを文字列としてきれいに表示できます。
    def __str__(self):
        return f"({self.x}, {self.y})"


# 使い方
p1 = Point(2, 3)
p2 = Point(4, 1)
p3 = p1 + p2  # __add__ が呼び出される

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p1 + p2 = {p3}")
