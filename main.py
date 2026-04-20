import pygame
import sys
from gui.window import GameWindow
from game.board import Board

def main():
    # Na razie ustawiamy parametry na sztywno
    # W przyszlosci zrobimy menu startowe
    SIZE = 5
    WIN_CONDITION = 4

    # 1. Inicjalizacja modeli
    board = Board(size=SIZE, win_condition=WIN_CONDITION)
    window = GameWindow(board)

    current_player = 'X'
    running = True
    game_over = False

    # Pierwsza rysowanie planszy
    window.update()

    # 2. Główna pętla gry
    while running:
        for event in pygame.event.get():
            # Zamknięcie okna krzyżykiem
            if event.type == pygame.QUIT:
                running = False

            # Reakcja na kliknięcie myszką
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                # Pobieramy pozycję kliknięcia i konwertujemy na indeksy planszy
                row, col = window.get_click_pos(pygame.mouse.get_pos())

                # Jeśli ruch jest poprawny
                if board.make_move(row, col, current_player):
                    window.update()  # Odświeżamy planszę

                    # Sprawdzamy, czy ten ruch zakończył grę
                    winner = board.check_winner()
                    if winner:
                        print(f" Gracz {winner} wygrał!")
                        game_over = True
                    elif board.is_full():
                        print("Koniec gry! Mamt remis!")
                        game_over = True
                    else:
                        # Zmiana gracza
                        current_player = 'O' if current_player == 'X' else 'X'

    # Po zakończeniu gry zamykamy Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()