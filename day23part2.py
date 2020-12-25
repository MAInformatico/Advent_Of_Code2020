from functools import reduce

class Cupnode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def gen(self, count):
        cur = self
        for _ in range(count):
            yield cur
            cur = cur.next

class Game:
    def __init__(self, data):
        self.min_cup = min(data)
        self.max_cup = max(data)
        self.cups = {value: Cupnode(value) for value in data}

        def link(prev, cup):
            prev.next = cup
            return cup

        last_cup = reduce(link, self.cups.values())
        self.current = last_cup.next = self.cups[data[0]]

    def play(self, count):
        for _ in range(count):
            *checked, self.current.next = self.current.gen(5)

            try_value = self.current.value
            while self.cups[try_value] in checked:
                try_value -= 1
                if try_value < self.min_cup:
                    try_value = self.max_cup

            destination = self.cups[try_value]
            checked[-1].next = destination.next
            destination.next = checked[1]

            self.current = self.current.next

    def result(self, value, count):
        return (itercup.value for itercup in self.cups[value].next.gen(count))



if __name__ == '__main__':
    data = "467528193" #Provided by the exercise
    data = list(map(int, data))
    '''
    game = Game(data)
    game.play(100)
    print("".join(map(str, game.result(1, 8))))
    '''

    data = list(map(int, data)) + list(range(10, 1000001))
    game = Game(data)
    game.play(10000000)
    cup_a, cup_b = game.result(1, 2)
    print(cup_a*cup_b)
