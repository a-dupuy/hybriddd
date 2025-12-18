class Board:
    def __init__(self):
        self.size = 8
        self.grid = [['.' for _ in range(self.size)] for _ in range(self.size)]
        # Initial pions centraux (ligne 3 et 4, colonnes 3 et 4)
        self.grid[3][3] = 'O'  # D4 blanc (HU)
        self.grid[3][4] = 'X'  # E4 noir (IA)
        self.grid[4][3] = 'X'  # D5 noir
        self.grid[4][4] = 'O'  # E5 blanc

    def display(self):
        # Header avec backslash signature
        print(r'\ A B C D E F G H')
        for row in range(self.size):
            line = f"{row + 1} "  # Numéro de ligne
            for col in range(self.size):
                line += self.grid[row][col] + " "
            print(line.strip())  # Pas d'espace final