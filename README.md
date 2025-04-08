#CryptoBot – Śledzenie kursów kryptowalut

**CryptoBot** to prosty projekt stworzony w Pythonie z użyciem biblioteki `tkinter`, który umożliwia:
- Pobieranie aktualnych kursów kryptowalut (np. Bitcoin, Ethereum) z API CoinGecko
- Wyświetlanie danych w graficznym interfejsie użytkownika (GUI)
- Zapisywanie danych do pliku CSV
- Tworzenie wykresów zmian kursu na podstawie zapisanych danych

---

#Wymagania

- Python 3.8+
- `requests`
- `matplotlib` *(do wykresów)*

Zainstaluj wymagane biblioteki:

```bash
pip install requests matplotlib

Jak uruchomić

    Sklonuj repozytorium:

git clone https://github.com/TWOJA-NAZWA-UZYTKOWNIKA/CryptoBot.git
cd CryptoBot

    Uruchom aplikację:

python main.py

Wygląd aplikacji

    Wybierz nazwę kryptowaluty (np. bitcoin, ethereum)

    Kliknij „Pobierz i Zapisz”

    Cena zostanie wyświetlona i zapisana do pliku prices.csv

Wykresy

Aplikacja może generować wykresy zmian cen na podstawie zapisanych danych w CSV.

Przykładowy wykres: (screen tutaj, jeśli chcesz dodać)
Struktura projektu

cryptobot/
├── main.py             # Główne uruchomienie aplikacji
├── gui.py              # Interfejs użytkownika (Tkinter)
├── crypto.py           # Pobieranie kursów z API
├── csv_logger.py       # Logowanie danych do pliku CSV
├── utils.py            # (opcjonalne narzędzia)
├── prices.csv          # Plik z zapisanymi kursami (ignorowany w Git)
└── README.md           # Opis projektu

.gitignore

Projekt ignoruje:

    Pliki tymczasowe (__pycache__, .pyc)

    Konfigurację IDE (.idea/, .vscode/)

    Plik z danymi prices.csv

Autor

Daniel Wasiewicz

Projekt stworzony w ramach nauki na studiach