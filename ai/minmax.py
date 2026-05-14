import math

class AI:
    def __init__(self, ai_player='O', human_player='X', max_depth=4):
        """
        Inicjalizacja sztucznej inteligencji.
        max_depth określa, na ile ruchów do przodu patrzy AI. 
        Dla planszy 5x5 głębokość 4 to dobry kompromis między szybkością a inteligencją.
        """
        self.ai_player = ai_player
        self.human_player = human_player
        self.max_depth = max_depth

    def get_best_move(self, board):
        """Wywołuje algorytm MinMax i zwraca najlepszy ruch w formie krotki (wiersz, kolumna)."""
        best_score = -math.inf
        best_move = None
        
        available_moves = board.get_empty_cells()
        
        # Prosta heurystyka: Jeśli to pierwszy ruch w grze, zajmij środek (oszczędza czas obliczeń)
        if len(available_moves) == board.size * board.size:
            return (board.size // 2, board.size // 2)

        for (row, col) in available_moves:
            # AI wykonuje wirtualny ruch
            board.make_move(row, col, self.ai_player)
            # Ocenia ten ruch za pomocą MinMaxa
            score = self.minimax(board, 0, -math.inf, math.inf, False)
            # Cofa wirtualny ruch
            board.undo_move(row, col)
            
            # Jeśli ten ruch jest lepszy niż dotychczasowe, zapisuje go
            if score > best_score:
                best_score = score
                best_move = (row, col)
                
        return best_move

    def minimax(self, board, depth, alpha, beta, is_maximizing):
        """Rekurencyjny algorytm przeszukiwania drzewa gry z odcinaniem Alpha-Beta."""
        
        # 1. Sprawdzenie warunków końcowych (Ktoś wygrał, remis, lub limit głębokości)
        winner = board.check_winner()
        if winner == self.ai_player:
            return 10 - depth  # AI wygrywa (im płycej/szybciej, tym lepiej, stąd odjęcie depth)
        elif winner == self.human_player:
            return -10 + depth # Gracz wygrywa (im głębiej uciekniemy przed przegraną, tym lepiej)
        elif board.is_full() or depth == self.max_depth:
            return 0 # Remis lub osiągnięto limit głębokości (brak pewnej wygranej w tym oknie)

        # 2. Ruch AI (szukanie najwyższego wyniku)
        if is_maximizing:
            max_eval = -math.inf
            for (row, col) in board.get_empty_cells():
                board.make_move(row, col, self.ai_player)
                eval = self.minimax(board, depth + 1, alpha, beta, False)
                board.undo_move(row, col)
                
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break # Odcięcie Beta - nie ma sensu sprawdzać dalej
            return max_eval
            
        # 3. Ruch Gracza (AI symuluje, że gracz gra optymalnie i szuka najniższego wyniku)
        else:
            min_eval = math.inf
            for (row, col) in board.get_empty_cells():
                board.make_move(row, col, self.human_player)
                eval = self.minimax(board, depth + 1, alpha, beta, True)
                board.undo_move(row, col)
                
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break # Odcięcie Alpha
            return min_eval