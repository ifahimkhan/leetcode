class Player(object):
    def __init__(self, player_name='', n=3):
        self.player_name = player_name
        self.n = n
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.main_diag = 0
        self.anti_diag = 0
        
    def move(self, r, c):
        self.rows[r] += 1
        self.cols[c] += 1
        if r == c: self.main_diag += 1
        if r + c  + 1 == self.n: self.anti_diag += 1
        return self.n in [self.rows[r], self.cols[c], self.main_diag, self.anti_diag]

    
class Solution:
    def tictactoe(self, moves: List[List[int]], n=3) -> str:
        player_names = 'AB'
        board_size = 3
        players = [Player(player_name, board_size) for player_name in player_names]
        n_players = len(player_names)
        
        for i, (r, c) in enumerate(moves):
            turn = i % n_players
            player = players[turn]
            if players[turn].move(r, c): return players[turn].player_name
        
        return 'Pending' if len(moves) != board_size * board_size else 'Draw'
