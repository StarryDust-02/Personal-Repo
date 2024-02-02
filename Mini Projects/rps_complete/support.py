from os import system, name
from time import sleep


#### 辅助程式
#### 请仔细阅读但是不要做更改。

def start_counter(seconds: int) -> None:
    """
    开始游戏的倒计时。
    """
    if seconds > 0:
        print(f'{seconds}...')
        sleep(1)
        start_counter(seconds - 1)
    else:
        clear(0)

def clear(seconds: int) -> None:
    """
    清屏程式：
        1. 停留 seconds 秒
        2. 清屏
    
    """
    
    sleep(seconds)
    # windows
    if name == 'nt':
        _ = system('cls')
 
    # mac and linux
    else:
        _ = system('clear')


def game_state(state: bool) -> bool:
    """改变游戏状态的程式。
    
    输入：
        - state: 目前游戏是否正在进行的状态
    输出：
        - 和之前相反的 state
    """
    return not state
    
