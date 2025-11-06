if __name__ == "__main__":
    print("Hello, World!")

#编写一个链表实现的大整数加法
def add(a, b):
    # 反转链表
    a = a[::-1]
    b = b[::-1]
    carry = 0
    result = []
    for i in range(max(len(a), len(b))):
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0
        total = digit_a + digit_b + carry
        result.append(str(total % 10))
        carry = total // 10
    if carry:
        result.append(str(carry))
    return ''.join(result[::-1])

#编写一个减法函数
def subtract(a, b):
    # 反转链表
    a = a[::-1]
    b = b[::-1]
    borrow = 0
    result = []
    for i in range(max(len(a), len(b))):
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0
        total = digit_a - digit_b - borrow
        if total < 0:
            total += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(total))
    return ''.join(result[::-1]).lstrip('0') or '0'

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







