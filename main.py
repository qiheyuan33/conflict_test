if __name__ == "__main__":
    print("Hello, World!")

#编写一个大整数的加法函数
def add(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    carry = 0
    result = []
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(a[i]) + int(b[i]) + carry
        carry = digit_sum // 10
        result.append(str(digit_sum % 10))
    if carry:
        result.append(str(carry))
    return ''.join(reversed(result))


#编写一个减法函数
def subtract(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    borrow = 0
    result = []
    for i in range(max_len - 1, -1, -1):
        digit_diff = int(a[i]) - int(b[i]) - borrow
        if digit_diff < 0:
            digit_diff += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(digit_diff))
    return ''.join(reversed(result)).lstrip('0') or '0'

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







