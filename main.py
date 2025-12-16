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

import pandas as pd

data = {
    'name': ['Даша', 'Саша', 'Коля', 'Петя', 'Таня', 'Лена', 'Наташа', 'Максим', 'Андрей', 'Ольга'],
    'subject': ['математика', 'геометрия', 'русский язык', 'черчение', 'физика', 'математика', 'геометрия', 'математика', 'математика', 'физика'],
    'score': [5, 5, 4, 4, 5, 3, 4, 3, 2, 5]
        }
df = pd.DataFrame(data)
print(df.head())
print(df.describe())


# df['subject'] = df['subject'].astype('category')
# print(df['subject'].cat.categories)

subject_averages = df.groupby('subject')['score'].mean()
print("Средние оценки по предметам:")
print(subject_averages)

subject_median = df.groupby('subject')['score'].median()
print("Медианные оценки по предметам:")
print(subject_median)

# Q1_math = df.groupby('subject')['score'].quantile(0.25)
#
# Q3_math = df.groupby('subject')['score'].quantile(0.75)
#
# print(Q1_math)
# print(Q3_math)

# Фильтруем только математику
math_scores = df[df['subject'] == 'математика']['score']

print("Оценки по математике:")
print(math_scores.tolist())

# Вычисляем квантили
Q1 = math_scores.quantile(0.25)  # Нижний (первый) квантиль
Q3 = math_scores.quantile(0.75)  # Верхний (третий) квантиль
median = math_scores.quantile(0.5)           # Медиана (второй квантиль)
IQR = Q3 - Q1

print(f"\nКвантили для математики:")
print(f"Нижний квантиль (25%): {Q1}")
print(f"Медиана (50%): {median}")
print(f"Верхний квантиль (75%): {Q3}")
print(f"Функция IQR: {IQR}")

subject_std = df.groupby('subject')['score'].std()
print("стандартные отклонения по предметам:")
print(subject_std)