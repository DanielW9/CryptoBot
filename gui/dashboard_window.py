import tkinter as tk
from tkinter import messagebox
from utils.crypto_fetcher import CryptoFetcher
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


class CryptoDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("CryptoBot - Dashboard")
        self.root.geometry("700x500")
        self.root.resizable(False, False)


        tk.Label(root, text="Wybierz kryptowalutę:").pack(pady=10)
        self.crypto_choice = tk.StringVar(root)
        self.crypto_choice.set("bitcoin")
        crypto_options = ["bitcoin", "ethereum", "dogecoin", "litecoin", "cardano"]
        self.crypto_menu = tk.OptionMenu(root, self.crypto_choice, *crypto_options)
        self.crypto_menu.pack()

        tk.Button(root, text="Pobierz dane", command=self.fetch_data).pack(pady=10)


        self.figure, self.ax = plt.subplots(figsize=(12, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack()

    def fetch_data(self):
        crypto_id = self.crypto_choice.get().lower()
        try:

            df = CryptoFetcher.fetch_crypto_history(crypto_id)


            current_price_url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
            current_price_response = requests.get(current_price_url)
            current_price_data = current_price_response.json()
            current_price = current_price_data.get(crypto_id, {}).get("usd", "Brak danych")


            messagebox.showinfo("Aktualna cena",
                                f"{crypto_id.capitalize()} na dzień dzisiejszy wynosi: ${current_price}")


            df['date'] = pd.to_datetime(df['date']).dt.strftime('%d-%m')


            self.ax.clear()


            self.ax.plot(df['date'], df['price'], marker='o', markersize=4, linestyle='-', color='blue')

            self.ax.set_title(f'Ceny {crypto_id.capitalize()} (30 dni)')
            self.ax.set_xlabel('Data')
            self.ax.set_ylabel('Cena (USD)')


            self.ax.tick_params(axis='x', rotation=45, labelsize=8)


            self.ax.set_xticks(df['date'][::5])  # Co 5 datę na osi X
            self.ax.set_xticklabels(df['date'][::5], rotation=45, fontsize=8)

            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się pobrać danych: {e}")
