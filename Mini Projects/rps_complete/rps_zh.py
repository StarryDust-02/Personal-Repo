"""Rock Paper Scissors
(c) StarryDust
"""
from typing import Any
from support import start_counter, clear, game_state
import random

#### 通用变量
AI_DIFFICULTY = 0       # AI 的难度的变量

OPTION = ['r',
          'p',
          's']
SCORE = {'PLR': 0,      # 玩家的分数
         'COM': 0}      # 电脑的分数


#### 主要内容

def main_loop() -> None:
    """这个游戏的主进程。
    """
    game_running = False    # 管理游戏是否在进行的变量
    # TODO: 0.0. 通过 game_state() 将 game_running 改成 True
    game_running = game_state(game_running)


    # 新建内部变量 computer_score: int, player_score: int 并将它们归 0
    computer_score, player_score = 0, 0
    # 新建内部变量 counters: dict 用于计数玩家的偏好用于记仇 AI 
    counters = {'r': 0, 'p': 0, 's': 0}
    # TODO: 1.3. 新建一个用来计数玩家连续出某个选择的计数器变量给贪婪 AI

    # 新建一个游戏局数记录，每 10 局问一下玩家是否还要继续玩
    game_count = 0

    while game_running:
        # 让玩家选择在 OPTIONS 出招。
        player_choice = input('请选择出什么 (r/p/s): ')

        # 如果玩家选择无效，则让玩家重新选。
        if player_choice not in OPTION:
            # 直接清屏重来
            clear(0)

        # 如果玩家选择的有效，则让 AI 选择。
        else:
            # 更新计数板
            counters[player_choice] = counters[player_choice] + 1

            # 随机 AI
            ai_choice = random_ai(OPTION)

            # 偏好 AI
            if AI_DIFFICULTY == 1.1:
                ai_choice == rock_ai(OPTION)
            elif AI_DIFFICULTY == 1.2:
                ai_choice == paper_ai(OPTION)
            elif AI_DIFFICULTY == 1.3:
                ai_choice == scissors_ai(OPTION)
            
            # 记仇 AI
            elif AI_DIFFICULTY == 2:
                ai_choice == revenge_ai(OPTION, counters)
            
            # 贪婪 AI
            # N/A


        # 比较谁获胜，相应加分。
            if (player_choice == 'r' and ai_choice == 'p') or \
            (player_choice == 'p' and ai_choice == 's') or \
            (player_choice == 's' and ai_choice == 'r'):
                computer_score += 1
            elif player_choice == ai_choice:
                pass
            else:
                player_score += 1
            print(f'电脑选择：{ai_choice}')
            print(f'目前比分：玩家 {player_score}，电脑 {computer_score}')
            clear(3)
            game_count += 1

            # 终局
            if game_count >= 10:
                print('本轮游戏结束。')
                print(f'最终比分：玩家 {player_score}，电脑 {computer_score}')
                if player_score > computer_score:
                    print('恭喜您获胜了！')
                answer = input('再玩十局吗？(y/n)\n你的回答: ')
                if answer == 'y':
                    game_count = 0
                    clear(0)
                else:
                    clear(0)
                    print('感谢游玩！再见。')
                    game_running = game_state(game_running)


#### 程式

def random_ai(option: list) -> Any:
    """随机选择的 AI, 序号是 0
    输入：
        - option: 可选项
    输出：
        - 在 options 里面的随即一项
    """
    return random.choice(option)


def rock_ai(option: list) -> Any:
    """喜欢出石头的 AI, 序号是 1.0, 出石头的几率是 0.5
    输入：
        - option: 可选项
    输出：
        - 在 options 里面的随即一项, 石头有 0.5 几率
    """
    option.append('r')
    # >>> option == ['r', 'p', 's', 'r']
    # True
    return random.choice(option)


def paper_ai(option: list) -> Any:
    """喜欢出布的 AI, 序号是 1.1, 出布的几率是 0.5
    输入：
        - option: 可选项
    输出：
        - 在 options 里面的随即一项, 布有 0.5 几率
    """
    option.append('p')
    # >>> option == ['r', 'p', 's', 'p']
    # True
    return random.choice(option)


def scissors_ai(option: list) -> Any:
    """喜欢出剪刀的 AI, 序号是 1.2, 出剪刀的几率是 0.5
    输入：
        - option: 可选项
    输出：
        - 在 options 里面的随即一项, 剪刀有 0.5 几率
    """
    option.append('s')
    # >>> option == ['r', 'p', 's', 's']
    # True
    return random.choice(option)


def revenge_ai(option: list, counters: dict) -> Any:
    """喜欢记仇的 AI, 序号是 2, 有 0.5 的几率出克制玩家最常出的选择
    输入：
        - option: 可选项
        - counters: 一个记录玩家选择的字典
    输出：
        - 参考 counters 并在 options 里面选择一项, 有 0.5 出克制玩家最常出的选择的几率, 0.5 几率随机选择
    """
    ref_counters = random.choice([True, False])     # 决定是否参考 counters 的记录

    # 如果决定参考 counters 的记录
    if ref_counters:
        current_fav = random.choice(option)         # 目前观测到的玩家最喜欢的，初始随机选
        for key in counters.keys:
            if counters[key] > counters[current_fav]:
                current_fav = key
        # 接下来选克制玩家的选择
        if current_fav == 'r':
            return 'p'
        elif current_fav == 'p':
            return 's'
        else:
            return 'r'
    
    # 如果决定不参考 counters 的记录那就随机选
    else:
        return random.choice(option)  


#### 游戏设置

# 清屏
clear(0)

print('####################################\n'
      '#            石头剪刀布            #\n'
      '####################################')

AI_DIFFICULTY = input('请选择 AI 难度：\n'
                      '0 = 随机 AI \n'
                      '1 = 偏好 AI \n'
                      '2 = 记仇 AI \n'
                      '3 = 贪婪 AI \n'
                      '你的选择：')

# 检查难度是否有效，默认难度 0
if AI_DIFFICULTY not in [0, 1, 2, 3]:
    AI_DIFFICULTY = 0
elif AI_DIFFICULTY == 2:
    AI_DIFFICULTY = random.choice(1.1, 1.2, 1.3)


print('游戏马上开始...')
start_counter(5)


# 游戏主循环
main_loop()
