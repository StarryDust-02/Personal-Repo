from random import choice

class Data:
    is_fivestar = [False, True]
    _fivestars = ['Jean', 'Diluc', 'Qiqi', 'Keqing', 'Luna']
    _event_fivestars = ['Ganyu', 'Ayato', 'Venti', 'Eula', 'Keqing', 'Kokomi', 'Miko', 'Tartaglia',
    'Zhongli', 'Xiao', 'Hutao', 'Kazuha', 'Itto', 'Shogun', 'Albedo', 'Klee', 'Yoimiya', 'Ayaka']

    def __init__(self, odd: float=0.006, pity: bool=True) -> None:
        self.odd = odd
        self.pity = pity

    def is_event(self, char: str='Any') -> None:
        '''Boost the chosen character'''
        if char.capitalize() in self.event_fivestars:
            self._fivestars.append(char.capitalize())
        else:
            self._fivestars.append(choice(self.event_fivestars))
    
    def add_pity(self) -> None:
        '''Add pity on failed attempt'''
        self.odd += 0.0626
    
    def get_odds(self) -> list:
        return [1 - self.odd, self.odd]

    def get_event_fivestars(self) -> list:
        return self._event_fivestars
        
    
