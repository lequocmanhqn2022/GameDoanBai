import random


# Bộ bài
SUITES = ["Spade", "Club", "Diamond", "Heart"]
GROUPS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
DECK = [(suite, group) for suite in SUITES for group in GROUPS] + [("Joker", "Black"), ("Joker", "Red")]

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