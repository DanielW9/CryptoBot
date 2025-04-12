# CryptoBot – Śledzenie kursów kryptowalut

**CryptoBot** to aplikacja stworzona w Pythonie z użyciem biblioteki `tkinter`, która umożliwia:
- Pobieranie aktualnych kursów kryptowalut (np. Bitcoin, Ethereum, Dogecoin, Litecoin) z API CoinGecko
- Wyświetlanie danych w graficznym interfejsie użytkownika (GUI)
- Zapisywanie danych do pliku CSV
- Tworzenie wykresów przedstawiających zmiany kursów kryptowalut na podstawie zapisanych danych

---

## Wymagania

- Python 3.8+
- `requests`
- `matplotlib`
- `pandas`

Zainstaluj wymagane biblioteki:

```bash
pip install -r requirements.txt

Jak uruchomić

    Sklonuj repozytorium:

git clone https://github.com/DanielW9/CryptoBot.git
cd CryptoBot

    Uruchom aplikację:

python main.py

Wygląd aplikacji

    Aplikacja posiada ekran logowania, w którym użytkownik może się zalogować lub zarejestrować.

    Po zalogowaniu użytkownik zostaje przeniesiony do głównego ekranu, gdzie może wybrać kryptowalutę (np. Bitcoin, Ethereum) i kliknąć przycisk „Pobierz dane”.

    Cena wybranej kryptowaluty zostaje wyświetlona na ekranie i zapisana do pliku data/crypto_history.csv.

Funkcje

    Pobieranie kursów kryptowalut: Aplikacja łączy się z API CoinGecko i pobiera dane o cenach kryptowalut.

    Tworzenie wykresów: Aplikacja generuje wykresy przedstawiające zmiany ceny wybranej kryptowaluty w czasie na podstawie zapisanych danych.

    Logowanie i rejestracja użytkownika: Użytkownicy mogą się logować oraz rejestrować w aplikacji, a ich dane są przechowywane w pliku data/users.csv.

Struktura projektu

cryptobot/
├── main.py             # Główne uruchomienie aplikacji
├── gui/                # Folder z plikami GUI
│   ├── login_window.py # Ekran logowania
│   └── dashboard_window.py  # Główny ekran z wykresami
├── utils/              # Folder z pomocniczymi plikami
│   ├── crypto_fetcher.py   # Pobieranie danych z API
│   └── file_handler.py      # Obsługa plików (logowanie użytkowników)
├── data/               # Folder z danymi użytkowników i historii kursów
│   ├── crypto_history.csv   # Historia kursów kryptowalut
│   └── users.csv           # Plik z danymi użytkowników
├── requirements.txt     # Zależności do zainstalowania
├── .gitignore           # Ignorowanie plików tymczasowych
└── README.md            # Opis projektu

Zawartość plików

    data/crypto_history.csv: Plik zawierający historię kursów kryptowalut (data, cena).

    data/users.csv: Plik zawierający dane użytkowników (login, hasło).

    gui/: Folder zawierający wszystkie pliki GUI aplikacji (logowanie, wykresy).

    utils/: Folder zawierający pomocnicze skrypty, takie jak pobieranie danych z API i zarządzanie użytkownikami.

Ignorowanie plików

Projekt ignoruje następujące pliki i foldery:

    Pliki tymczasowe (__pycache__, .pyc, .pyo, .log)

    Konfiguracje IDE (np. .idea/, .vscode/)

    Pliki danych (data/crypto_history.csv, data/users.csv)

Autor

Daniel Wasiewicz

Projekt stworzony w ramach nauki na studiach.