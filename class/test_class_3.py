# カプセル化とプロパティの例

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # 外部から直接アクセスできないようにする（カプセル化）

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount}円を預けました。現在の残高: {self.__balance}円")
        else:
            print("預ける金額は0円より多くなければいけません。")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount}円を引き出しました。現在の残高: {self.__balance}円")
        else:
            print("引き出せる金額を超えています。")

    @property
    def balance(self):
        return self.__balance


# 使い方
account = BankAccount("田中さん", 10000)
account.deposit(3000)
account.withdraw(5000)
print(f"最終残高: {account.balance}円")

# 外部から直接 __balance にアクセスはできない（エラーになる）
# print(account.__balance)  # これはエラーになります
