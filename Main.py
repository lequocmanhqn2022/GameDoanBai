import random
import Play
import Class

REWARD = 20
JOIN_FEE = 25
WIN_CONDITION = 1000
LOSE_CONDITION = 30


# Play game
def play_game(player, house, deck,reward=REWARD):
    while True:
        print(f'{player.name} bắt đầu với {player.score} điểm.')
        player.score = player.score - JOIN_FEE
        print(f'{player.name} trả {JOIN_FEE} điểm để bắt đầu. Còn {player.score} điểm','\n')
        # Điều kiện thắng
        while True and player.score >= LOSE_CONDITION and player.score < WIN_CONDITION :
            new_reward=Play.play_round(player, house, deck, reward=reward)
            reward=new_reward
            print('\n')
            if(reward < WIN_CONDITION):
                request = input(f'Quyết định "tiếp tục" hay "dừng lại"(y/n) :')
                if(request=="y"):
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
        rs=input("Bạn muốn chơi tiếp hay dừng lại (y/n) :")
        if(rs=='y'):
            continue
        else:
            break

play_game(player=Class.Player(name=input(f'Bạn tên là : ')),house=Class.House(),deck=Play.DECK)
