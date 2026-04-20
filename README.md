# Kółko i Krzyżyk N x N (Tic-Tac-Toe) z AI ⭕❌

Projekt zrealizowany w ramach przedmiotu **Projektowanie i Analiza Algorytmów (projekt II)**. 
Celem projektu jest implementacja rozszerzonej wersji klasycznej gry "Kółko i krzyżyk", w której gracz może zdefiniować dowolny rozmiar kwadratowej planszy (N x N) oraz liczbę znaków w rzędzie wymaganych do zwycięstwa.

Aplikacja posiada graficzny interfejs użytkownika (GUI) oraz oponenta sterowanego sztuczną inteligencją.

## 🚀 Funkcjonalności
* **Dynamiczna plansza:** Możliwość wyboru dowolnego rozmiaru pola gry (np. 3x3, 5x5, 10x10).
* **Elastyczne zasady:** Definiowanie liczby znaków (w poziomie, pionie lub po skosie) potrzebnych do wygrania rundy.
* **Sztuczna Inteligencja:** Przeciwnik komputerowy bazujący na algorytmie **MinMax**.
* **Optymalizacja AI:** Zastosowanie **odcinania Alpha-Beta** w celu znacznego przyspieszenia analizy drzewa gry na większych planszach.
* **Graficzny Interfejs Użytkownika:** Intuicyjne menu oraz czytelna plansza do gry.

## 🛠️ Technologie i Architektura
Projekt został napisany w języku **Python** i opiera się na wzorcu architektonicznym separującym logikę gry od interfejsu graficznego (MVC).

**Struktura projektu:**
* `core/` - Niezależny silnik gry (stan planszy, weryfikacja ruchów i warunków zwycięstwa).
* `ai/` - Moduł sztucznej inteligencji (MinMax, Alpha-Beta, heurystyki).
* `gui/` - Interfejs graficzny użytkownika.
* `main.py` - Główny skrypt uruchamiający grę.

## ⚙️ Uruchomienie lokalne

1. Sklonuj repozytorium:
   ```bash
   git clone <LINK_DO_TWOJEGO_REPOZYTORIUM>
   cd paa_projekt_tictactoe