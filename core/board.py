class Board:
    def __init__(self, size=3, win_condition=3):
        """
        Inicjalizuje planszę o zadanym rozmiarze i warunku zwycięstwa.
        """
        self.size = size
        self.win_condition = win_condition
        # Tworzymy dwywymiarowa tablice (N x N) i wypełniamy ją pustymi polami
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]

    def is_valid_move(self, row, col):
        # Sprawdza, czy ruch mieści się w granicach planszy i czy pole jest puste
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.grid[row][col] == ' '
        return False
    
    def make_move(self, row, col, player):
        # Wykonuje ruch gracza, jeśli jest on poprawny
        if self.is_valid_move(row, col):
            self.grid[row][col] = player
            return True
        return False
    
    def undo_move(self, row, col):
        # Cofnij ruch, ustawiając pole z powrotem na puste
        self.grid[row][col] = ' '

    def get_empty_cells(self):
        # Zwraca listę dostępnych ruchów w postaci krotek (row, col)
        return [(r, c) for r in range(self.size) for c in range(self.size) if self.grid[r][c] == ' ']
    
    def is_full(self):
        # Sprawdza, czy plansza jest pełna (remis)
        return len(self.get_empty_cells()) == 0
    
    def check_winner(self):
        # Sprawdza czy na planszy znajduje się wygrywająca sekwencja

        # Wektory kierunków: (wiersz, kolumna) -> Prawo, Dół, Skos w dół-prawo, Skos w dół-lewo
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for r in range(self.size):
            for c in range(self.size):
                current_mark = self.grid[r][c]
                if current_mark != ' ':
                    # Sprawdzamy wszystkie kierunki
                    for dr, dc in directions:
                        if self.check_sequence(r, c, dr, dc, current_mark):
                            return current_mark  # Zwraca symbol gracza, który wygrał
        return None  # Brak zwycięzcy
    
    def _check_sequence(self, start_row, start_col, d_row, d_col, player):
        # Sprawdza, czy w danym kierunku znajduje się wystarczająca liczba symboli gracza
        for i in range(self.win_condition):
            r = start_row + i * d_row
            c = start_col + i * d_col
            # Jeśli wyjdziemy poza plansze lub znak się nie zgadza, to sekwencja jest przerwana
            if r < 0 or r >= self.size or c < 0 or c >= self.size or self.grid[r][c] != player:
                return False
            return True
        
    def print_board(self):
        # Testowa mtetoda do wyświetlania planszy w konsoli
        for row in self.grid:
            print('|' + '|'.join([cell if cell != ' ' else ' ' for cell in row]) + '|')
        print()