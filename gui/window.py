import pygame

# Kolory używane w grze (RGB)
BG_COLOR = (28, 170, 156)  # Morski / turkusowy
LINE_COLOR = (23, 145, 135)  # Ciemniejszy morski
X_COLOR = (84, 84, 84)  # Ciemny szary
O_COLOR = (242, 235, 211)  # Złamana biel

class GameWindow:
    def __init__(self, board, width=600, height=600):
        self.board = board
        self.width = width
        self.height = height
        # Dynamiczne obliczanie rozmiaru kratki na podstawie rozmiaru planszy
        self.cell_size = width // board.size

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(f"Kolko i Krzyzyk - {board.size}x{board.size} (Wygrywa: {board.win_condition})")

    def draw_grid(self):
        """Rysuje tło i linie siatki."""
        self.screen.fill(BG_COLOR)
        for i in range(1, self.board.size):
            # Linie pionowe
            pygame.draw.line(self.screen, LINE_COLOR, (i * self.cell_size, 0), (i * self.cell_size, self.height), 5)
            # Linie poziome
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * self.cell_size), (self.width, i * self.cell_size), 5)
    def draw_marks(self):
        # Iteruje przez planszę i rysuje X lub O w odpowiednich miejscach
        for row in range(self.board.size):
            for col in range(self.board.size):
                mark = self.board.grid[row][col]
                if mark != ' ':
                    # Wyznaczanie środka danej kratki
                    center_x = col * self.cell_size + self.cell_size // 2
                    center_y = row * self.cell_size + self.cell_size // 2

                    if mark == 'X':
                        offset = self.cell_size // 4
                        pygame.draw.line(self.screen, X_COLOR, (center_x - offset, center_y - offset), (center_x + offset, center_y + offset), 8)
                        pygame.draw.line(self.screen, X_COLOR, (center_x + offset, center_y - offset), (center_x - offset, center_y + offset), 8)
                    elif mark == 'O':
                        radius = self.cell_size // 3
                        pygame.draw.circle(self.screen, O_COLOR, (center_x, center_y), radius, 8)
    
    def update(self):
        # Odświeża ekran, rysując siatkę i znaki
        self.draw_grid()
        self.draw_marks()
        pygame.display.flip()

    def get_click_pos(self, mouse_pos):
        # Konwertuje pozycję kliknięcia na indeksy planszy
        x, y = mouse_pos
        row = y // self.cell_size
        col = x // self.cell_size
        return row, col