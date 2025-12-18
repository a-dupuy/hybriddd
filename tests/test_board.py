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

# Ajouts pour Story 2 (à append après les tests init + display)

@pytest.fixture
def board():
    return Board()

def test_get_valid_moves_initial_white(board):
    valid = board.get_valid_moves('O')
    expected = ['C5', 'D6', 'E3', 'F4']  # Correct pour 'O' (blanc)
    assert sorted(valid) == sorted(expected)

def test_get_valid_moves_initial_black(board):
    valid = board.get_valid_moves('X')
    expected = ['C4', 'D3', 'E6', 'F5']  # Correct pour 'X' (noir)
    assert sorted(valid) == sorted(expected)

def test_is_valid_move_valid_white(board):
    assert board.is_valid_move('D6', 'O')  # Un move valide pour 'O', ex. D6
    assert board.is_valid_move('C5', 'O')

def test_is_valid_move_invalid_out_of_bounds(board):
    assert not board.is_valid_move(('A0'), 'O')
    assert not board.is_valid_move(('H9'), 'O')
    assert not board.is_valid_move(('I1'), 'O')

def test_is_valid_move_invalid_occupied(board):
    assert not board.is_valid_move(('D4'), 'O')  # D4 déjà 'O'

def test_is_valid_move_no_flip(board):
    assert not board.is_valid_move(('A1'), 'O')  # Pas de flip possible

def test_place_piece_valid_flip_white(board):
    board.place_piece('D6', 'O')  # Un move valide
    # Checks flips, ex. flip D5 'X' -> 'O' (row4 col3)
    assert board.grid[4][3] == 'O'  # D5
    # Autres flips selon direction

def test_place_piece_raises_if_invalid(board):
    with pytest.raises(ValueError, match="Invalid move"):
        board.place_piece(('A1'), 'O')

# À venir : game loop avec input, IA random move, etc.