# tests/test_board.py
import pytest
from src.core.board import Board  # Import du module à implémenter

def test_board_init_correct_size_and_initial_pieces():
    board = Board()
    assert board.size == 8
    assert board.grid[3][3] == 'O'  # Ligne 4 (index 3), colonne D (index 3) -> blanc
    assert board.grid[3][4] == 'X'  # Ligne 4, colonne E -> noir
    assert board.grid[4][3] == 'X'  # Ligne 5, colonne D -> noir
    assert board.grid[4][4] == 'O'  # Ligne 5, colonne E -> blanc
    # Toutes les autres cases vides
    for i in range(8):
        for j in range(8):
            if (i, j) not in [(3,3), (3,4), (4,3), (4,4)]:
                assert board.grid[i][j] == '.'

def test_display_board_initial(capsys):
    board = Board()
    board.display()  # Appel à la méthode display
    captured = capsys.readouterr()
    expected_output = """\\ A B C D E F G H
1 . . . . . . . .
2 . . . . . . . .
3 . . . . . . . .
4 . . . O X . . .
5 . . . X O . . .
6 . . . . . . . .
7 . . . . . . . .
8 . . . . . . . .
"""
    assert captured.out == expected_output