# 多重継承のサンプル

# 親クラスその1
class Flyer:
    def fly(self):
        print("空を飛びます！")

# 親クラスその2
class Walker:
    def walk(self):
        print("地面を歩きます！")

# 子クラスが両方の親クラスを継承
class Bird(Flyer, Walker):
    def chirp(self):
        print("チュンチュン！")

# インスタンス作成
bird = Bird()
bird.fly()    # Flyerクラスのメソッド
bird.walk()   # Walkerクラスのメソッド
bird.chirp()  # Birdクラス独自のメソッド
