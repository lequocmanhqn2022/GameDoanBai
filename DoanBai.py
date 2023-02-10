import random
import mysql.connector

# Bộ bài
SUITES = ["Spade", "Club", "Diamond", "Heart"]
GROUPS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
DECK = [(suite, group) for suite in SUITES for group in GROUPS] + [("Joker", "Black"), ("Joker", "Red")]
REWARD = 20
JOIN_FEE = 25
WIN_CONDITION = 1000
LOSE_CONDITION = 30

class Player:
    def __init__(self, name, score=60):
        self.name = name
        self.score = score
        self.card = None
    def guess(self,house_card):
        guess = input(f"{self.name}, bạn nghĩ thẻ {self.card[1]} {self.card[0]} của bạn nhỏ hay lớn hơn {house_card[1]} {house_card[0]}? (Nhấn 'lớn', 'nhỏ' hoặc 'bằng'): ")
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
# So sánh bài
def compare_cards(player_card, house_card):
    if(player_card[0]=="Joker"):
        player_suites = 4
        player_gruop = 13
        house_gruop=GROUPS.index(house_card[1])
        house_suites=SUITES.index(house_card[0])
    elif(house_card[0]=="Joker"):
        player_gruop=GROUPS.index(player_card[1])
        player_suites=SUITES.index(player_card[0])
        house_suites = 4
        house_gruop = 13
    else:
        player_gruop=GROUPS.index(player_card[1])
        player_suites=SUITES.index(player_card[0])
        house_gruop=GROUPS.index(house_card[1])
        house_suites=SUITES.index(house_card[0])
        
    if player_gruop > house_gruop:
        return "lớn"
    elif player_gruop < house_gruop:
        return "nhỏ"
    else:
        if player_suites > house_suites:
            return "lớn"
        elif player_suites < player_suites:
            return "nhỏ"
        else:
            return "bằng"
# vòng chơi
def play_round(player, house, deck, reward):
    player.draw_card(deck)
    house.draw_card(deck)
    result = compare_cards(player.card, house.card)
    guess = player.guess(house.card)

    if result == guess:
        print(f"{player.name} có lá : {player.card[1]} {player.card[0]}")
        print(f"Tuyệt! {player.name} được {reward} điểm.")
        return reward
    else:
        if(reward==20):
            new_reward=0
        else:
            new_reward=int(reward/2)
        print(f"{player.name} có lá : {player.card[1]} {player.card[0]}")
        print(f"Sai! {player.name} thua {new_reward} điểm.")
        return 0
# Play game
def play_game(player, house, deck,reward=REWARD):
    print(f'{player.name} bắt đầu với {player.score} điểm.')
    player.score = player.score - JOIN_FEE
    print(f'{player.name} trả {JOIN_FEE} điểm để bắt đầu. Còn {player.score} điểm','\n')
    # Điều kiện thắng
    while True and player.score >= LOSE_CONDITION and player.score < WIN_CONDITION :
        new_reward=play_round(player, house, deck, reward=reward)
        reward=new_reward
        print('\n')
        if(reward < WIN_CONDITION):
            request = input(f'Quyết định "tiếp tục" hay "dừng lại" :')
            if(request=="tiếp tục"):
                if(reward>0):
                    reward*=2
                    print(f'Phần thưởng vòng sau là {reward} điểm.')
                else:
                    reward=REWARD
                    print(f'Phần thưởng vòng sau là {reward} điểm.')
            else:
                player.score += reward
                break
        else:
            player.score +=reward
    print(f'Bạn đã dừng với {player.score} điểm.')

play_game(player=Player(name=input(f'Bạn tên là : ')),house=House(),deck=DECK)
