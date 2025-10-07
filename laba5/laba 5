import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import pygame
import openpyxl
import pytz
import dateutil.parser
import tzdata
import urllib3

# Блок 1: NumPy
try:
    arr = np.array([1, 2, 3, 4, 5])
    print("NumPy масив:", arr)
except Exception as e:
    print("NumPy помилка:", e)

# Блок 2: Pandas
try:
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    print("Pandas DataFrame:\n", df)
except Exception as e:
    print("Pandas помилка:", e)

# Блок 3: Requests
try:
    r = requests.get("https://api.github.com")
    print("Requests статус-код:", r.status_code)
except Exception as e:
    print("Requests помилка:", e)

# Блок 4: Matplotlib
try:
    plt.plot([1,2,3], [4,5,6])
    plt.title("Простий графік")
    plt.close()  # закриваємо, щоб не відкривати вікно
    print("Matplotlib графік створено")
except Exception as e:
    print("Matplotlib помилка:", e)

# Блок 5: Pygame
try:
    pygame.init()
    print("Pygame ініціалізовано")
    pygame.quit()
except Exception as e:
    print("Pygame помилка:", e)
