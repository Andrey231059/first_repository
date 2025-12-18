# import pandas as pd


# # df = pd.read_csv('World-happiness-report-2024.csv')
# df = pd.read_csv('dz.csv')
# # print(df.head())
# # print(df.describe())
# # print(df.shape)
# # print(df.isnull().sum())
# #
# # print(df.info())
# # print(df[['Country name', 'Regional indicator']])
#
# group_s = df.groupby('City')['Salary'].sum()
# group_m = df.groupby('City')['Salary'].mean()
# print(group_s)
# print(group_m)

# Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам. Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:
#
# 1. Самостоятельно создайте DataFrame с данными
#
# 2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
#
# 3. Вычислите среднюю оценку по каждому предмету
#
# 4. Вычислите медианную оценку по каждому предмету
#
# 5. Вычислите Q1 и Q3 для оценок по математике:
#
# Q1_math = df['Математика'].quantile(0.25)
#
# Q3_math = df['Математика'].quantile(0.75)
#
# - можно также попробовать рассчитать IQR
#
# 6. Вычислите стандартное отклонение

# import pandas as pd
#
# data = {
#     'name': ['Даша', 'Саша', 'Коля', 'Петя', 'Таня', 'Лена', 'Наташа', 'Максим', 'Андрей', 'Ольга'],
#     'subject': ['математика', 'геометрия', 'русский язык', 'черчение', 'физика', 'математика', 'геометрия', 'математика', 'математика', 'физика'],
#     'score': [5, 5, 4, 4, 5, 3, 4, 3, 2, 5]
#         }
# df = pd.DataFrame(data)
# print(df.head())
# print(df.describe())
#
#
# # df['subject'] = df['subject'].astype('category')
# # print(df['subject'].cat.categories)
#
# subject_averages = df.groupby('subject')['score'].mean()
# print("Средние оценки по предметам:")
# print(subject_averages)
#
# subject_median = df.groupby('subject')['score'].median()
# print("Медианные оценки по предметам:")
# print(subject_median)
#
# # Q1_math = df.groupby('subject')['score'].quantile(0.25)
# #
# # Q3_math = df.groupby('subject')['score'].quantile(0.75)
# #
# # print(Q1_math)
# # print(Q3_math)
#
# # Фильтруем только математику
# math_scores = df[df['subject'] == 'математика']['score']
#
# print("Оценки по математике:")
# print(math_scores.tolist())
#
# # Вычисляем квантили
# Q1 = math_scores.quantile(0.25)  # Нижний (первый) квантиль
# Q3 = math_scores.quantile(0.75)  # Верхний (третий) квантиль
# median = math_scores.quantile(0.5)           # Медиана (второй квантиль)
# IQR = Q3 - Q1
#
# print(f"\nКвантили для математики:")
# print(f"Нижний квантиль (25%): {Q1}")
# print(f"Медиана (50%): {median}")
# print(f"Верхний квантиль (75%): {Q3}")
# print(f"Функция IQR: {IQR}")
#
# subject_std = df.groupby('subject')['score'].std()
# print("стандартные отклонения по предметам:")
# print(subject_std)

# 1. Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.
#
#
# # Параметры нормального распределения
#
# mean = 0 # Среднее значение
#
# std_dev = 1 # Стандартное отклонение
#
# num_samples = 1000 # Количество образцов
#
# # Генерация случайных чисел, распределенных по нормальному распределению
#
# data = np.random.normal(mean, std_dev, num_samples)
#
# 2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.
#
# import numpy as np
#
# random_array = np.random.rand(5) # массив из 5 случайных чисел
#
# print(random_array)
#
# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны


# import matplotlib.pyplot as plt
# import numpy as np
#
#
# # # Параметры нормального распределения
# # mean = 0       # Среднее значение
# # std_dev = 1    # Стандартное отклонение
# # num_samples = 1000  # Количество образцов
# #
# # # Генерация случайных чисел, распределенных по нормальному распределению
# # data = np.random.normal(mean, std_dev, num_samples)
# # print(data)
# #
# # plt.hist(data)
# # plt.xlabel("ось X")
# # plt.ylabel("ось Y")
# #
# # plt.grid(True)
# # plt.show()
#
#
# x = np.random.rand(5)
# print(x)
#
# y= np.random.rand(5)
# print(y)
#
# plt.scatter(x, y)
#
# plt.xlabel("ось Х")
# plt.ylabel("ось Y")
# plt.title("Тестовая диаграмма рассеяния")
#
# plt.show()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import csv
#
# driver = webdriver.Firefox()
# # URL страницы
# url = 'https://www.divan.ru/kaluga/category/divany'
#
# # Открытие страницы
# driver.get(url)
# time.sleep(5)
#
#
# # Явное ожидание загрузки элементов с ценами
# wait = WebDriverWait(driver, 10)
#
# try:
#     # Лучше всего использовать data-testid - он самый стабильный
#     prices = wait.until(
#         EC.presence_of_all_elements_located(
#             (By.XPATH, "//span[@class='ui-LD-ZU']")
#         )
#     )
#
#     print(f"Найдено {len(prices)} элементов с ценами")
#
#
# except Exception as e:
#     print(f"Ошибка: {e}")
#
# driver.quit()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import csv
# import matplotlib.pyplot as plt
# import pandas as pd
#
# # --- Настройка драйвера ---
# driver = webdriver.Firefox()  # Убедись, что у тебя установлен geckodriver
# url = 'https://www.divan.ru/kaluga/category/divany'
#
# print("Открываем страницу...")
# driver.get(url)
# time.sleep(5)  # Даем время на загрузку JS
#
# # --- Ожидание элементов ---
# wait = WebDriverWait(driver, 15)
#
# try:
#     print("Ищем элементы с ценами...")
#
#     # Используем data-testid="price" — самый стабильный селектор
#     price_elements = wait.until(
#         EC.presence_of_all_elements_located(
#             (By.XPATH, "//span[@data-testid='price']")
#         )
#     )
#
#     print(f"✅ Найдено {len(price_elements)} элементов с ценами.")
#
#     prices = []
#     for elem in price_elements:
#         try:
#             # Получаем текст цены (например, "28 990")
#             price_text = elem.text.strip()
#             # Убираем пробелы и преобразуем в число
#             price_clean = int(price_text.replace(' ', '').replace('\xa0', ''))
#             prices.append(price_clean)
#         except Exception as e:
#             print(f"⚠️ Не удалось обработать цену: {elem.text} | Ошибка: {e}")
#             continue
#
#     print(f"✅ Успешно извлечено {len(prices)} цен.")
#
#     # --- Сохраняем в CSV ---
#     csv_filename = 'divan_prices.csv'
#     with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Цена'])  # Заголовок
#         for price in prices:
#             writer.writerow([price])
#
#     print(f"💾 Цены сохранены в файл: {csv_filename}")
#
#     # --- Обработка данных ---
#     df = pd.DataFrame(prices, columns=['Цена'])
#     avg_price = df['Цена'].mean()
#     print(f"\n📊 Средняя цена дивана: {avg_price:,.0f} ₽")
#
#     # --- Построение гистограммы ---
#     plt.figure(figsize=(10, 6))
#     plt.hist(df['Цена'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
#     plt.title('Распределение цен на диваны')
#     plt.xlabel('Цена (₽)')
#     plt.ylabel('Количество диванов')
#     plt.grid(True, alpha=0.3)
#     plt.tight_layout()
#     plt.show()
#
# except Exception as e:
#     print(f"❌ Ошибка при парсинге: {e}")
#
# finally:
#     driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

# --- Автоматическая установка chromedriver ---
chromedriver_autoinstaller.install()

# --- Настройки Chrome ---
options = Options()
# options.add_argument('--headless')  # раскомментируй, чтобы скрыть браузер
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=options)

url = 'https://www.divan.ru/kaluga/category/divany'

print("🌐 Открываем страницу...")
driver.get(url)
time.sleep(10)  # Ждём полной загрузки

try:
    print("🔍 Ищем цены...")

    # Используем data-testid="price"
    price_elements = driver.find_elements("xpath", "//span[@data-testid='price']")

    prices = []
    for elem in price_elements:
        try:
            text = elem.text.strip()
            clean_price = int(text.replace(' ', '').replace('\xa0', ''))
            prices.append(clean_price)
        except Exception as e:
            print(f"⚠️ Не удалось обработать цену: '{text}' | Ошибка: {e}")

    print(f"✅ Найдено {len(prices)} цен.")

    # --- Сохраняем в CSV ---
    with open('divan_prices.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Цена'])
        for p in prices:
            writer.writerow([p])

    # --- Обработка данных ---
    df = pd.DataFrame(prices, columns=['Цена'])
    avg_price = df['Цена'].mean()
    print(f"\n📊 Средняя цена: {avg_price:,.0f} ₽")

    # --- Гистограмма ---
    plt.figure(figsize=(10, 6))
    plt.hist(df['Цена'], bins=20, color='lightgreen', edgecolor='black', alpha=0.7)
    plt.title('Распределение цен на диваны (divan.ru)')
    plt.xlabel('Цена (₽)')
    plt.ylabel('Количество')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"❌ Ошибка: {e}")

finally:
    driver.quit()
    print("\n✅ Браузер закрыт.")
print("\n🌐 Браузер закрыт.")

