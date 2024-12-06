class MancalaBoard:
    def __init__(self):
        self.board = {
            'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 4, 'F': 4,
            'G': 4, 'H': 4, 'I': 4, 'J': 4, 'K': 4, 'L': 4,
            1: 0, 2:0
        }
        self.player1_pits = ['A', 'B', 'C', 'D', 'E', 'F']
        self.player2_pits = ['G', 'H', 'I', 'J', 'K', 'L']
        self.player1_store = 1
        self.player2_store = 2

        self.opponent_pits = {
            'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K', 'F': 'L',
            'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D', 'K': 'E', 'L': 'F'
        }

        self.next_pit = {
            'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1',
             1: 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G', 'G': 2,
             2: 'A'
        }

        def possibleMoves(self, player):
            if player == 1:
                return [pit for pit in self.player1_pits if self.board[pit] > 0]
            elif player == 2:
                return [pit for pit in self.player2_pits if self.board[pit] > 0]
            
        def doMove(self, player, pit):
            if pit not in self.board or self.board[pit] == 0:
                raise ValueError("Invalid move: The selected pit is empty or does not exist.")
            
            seeds = self.board[pit]
            self.board[pit] = 0
            current_pit = pit

            while seeds > 0:
                current_pit = self.next_pit[current_pit]
                if (player == 1 and current_pit == 2) or (player == 2 and current_pit == 1):
                    continue
                self.board[current_pit] += 1
                seeds -= 1

            if current_pit in (self.player1_pits if player == 1 else self.player2_pits) and self.board[current_pit] == 1:
                opposite_pit = self.opponent_pits[current_pit]
                if self.board[opposite_pit] > 0:
                    self.board[player] += self.board[opposite_pit] + 1
                    self.board[opposite_pit] = 0
                    self.board[current_pit] = 0

            return current_pit == player 