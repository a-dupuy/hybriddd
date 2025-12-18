# src/core/board.py

class Board:
    def __init__(self):
        self.size = 8
        self.grid = [['.' for _ in range(self.size)] for _ in range(self.size)]
        # Initial Othello setup: blanc 'O' en D4/E5, noir 'X' en E4/D5
        self.grid[3][3] = 'O'  # D4 (row 3, col 3)
        self.grid[3][4] = 'X'  # E4
        self.grid[4][3] = 'X'  # D5
        self.grid[4][4] = 'O'  # E5

    def display(self):
        print("\\ A B C D E F G H")
        for i in range(self.size):
            row_str = f"{i+1} "
            for j in range(self.size):
                row_str += self.grid[i][j] + " "
            print(row_str.strip())

    def _coord_to_indices(self, coord: str) -> tuple[int, int]:
        """'A1' -> (row=0, col=0)"""
        if not isinstance(coord, str) or len(coord) != 2:
            raise ValueError("Coord must be like 'A1'")
        col = ord(coord[0].upper()) - ord('A')
        row = int(coord[1]) - 1
        if not (0 <= col < self.size and 0 <= row < self.size):
            raise ValueError("Out of bounds")
        return row, col

    def get_valid_moves(self, player: str) -> list[str]:
        opponent = 'X' if player == 'O' else 'O'
        valid = []
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == '.':
                    if self._would_flip(i, j, player, opponent):
                        valid.append(f"{chr(ord('A') + j)}{i+1}")
        return sorted(valid)

    def is_valid_move(self, coord: str, player: str) -> bool:
        try:
            row, col = self._coord_to_indices(coord)
            if self.grid[row][col] != '.':
                return False
            opponent = 'X' if player == 'O' else 'O'
            return self._would_flip(row, col, player, opponent)
        except ValueError:
            return False

    def _would_flip(self, row: int, col: int, player: str, opponent: str) -> bool:
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            found_opponent = False
            while 0 <= r < self.size and 0 <= c < self.size and self.grid[r][c] == opponent:
                found_opponent = True
                r += dr
                c += dc
            # Après la séquence d'opponent, doit être player (et pas break sur '.')
            if found_opponent and 0 <= r < self.size and 0 <= c < self.size and self.grid[r][c] == player:
                return True
        return False

    def place_piece(self, coord: str, player: str):
        row, col = self._coord_to_indices(coord)
        if self.grid[row][col] != '.':
            raise ValueError("Case occupied")
        opponent = 'X' if player == 'O' else 'O'
        if not self._would_flip(row, col, player, opponent):
            raise ValueError("Invalid move: no flips")
        
        self.grid[row][col] = player
        self._flip_pieces(row, col, player, opponent)

    def _flip_pieces(self, row: int, col: int, player: str, opponent: str):
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            to_flip = []
            while 0 <= r < self.size and 0 <= c < self.size and self.grid[r][c] == opponent:
                to_flip.append((r, c))
                r += dr
                c += dc
            if 0 <= r < self.size and 0 <= c < self.size and self.grid[r][c] == player:
                for fr, fc in to_flip:
                    self.grid[fr][fc] = player