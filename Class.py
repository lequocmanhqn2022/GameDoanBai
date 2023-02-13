import random

class Player:
    def __init__(self, name, score=60):
        self.name = name
        self.score = score
        self.card = None
    def guess(self,house_card):
        guess = input(f"{self.name}, bạn nghĩ thẻ của bạn nhỏ hơn hay lớn hơn hay bằng {house_card[1]} {house_card[0]}? (lớn/nhỏ/bằng): ")
        return guess
    def draw_card(self, deck):
        self.card = random.choice(deck)
        return self.card

class House:
    def __init__(self,score=60):
        self.score = score
        self.card = None
    def draw_card(self, deck):
        self.card = random.choice(deck)
        print(f"Nhà cái có lá : {self.card[1]} {self.card[0]}.")
        return self.card