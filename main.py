if __name__ == "__main__":
    print("Hello, World!")

#编写一个加法函数
def add(a, b):
    return a + b

#编写一个减法函数
def subtract(a, b):
    return a - b

#编写一个字符串减法函数
def subtract(a, b):
    return a - b

#编写一个play class
class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def increase_score(self, points):
        self.score += points

    def decrease_score(self, points):
        self.score -= points


# player 加法函数
def test_increase_score():
    player = Player("Alice", 10)
    player.increase_score(5)
    assert player.score == 15

#player 减法函数
def test_decrease_score():
    player = Player("Bob", 20)
    player.decrease_score(7)
    assert player.score == 13







