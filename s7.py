from scipy import stats
import numpy as np

group1 = [1000, 1380, 1200]
group2 = [1400, 1600, 1180, 1220]

statistic, pvalue = stats.mannwhitneyu(group1, group2, alternative='two-sided')

print(f"Статистика U: {statistic}")
print(f"P-значение: {pvalue}")

# Интерпретация результатов
alpha = 0.05  # Уровень значимости
if pvalue < alpha:
    print("Различие между группами статистически значимо.")
else:
    print("Различие между группами статистически незначимо.")

# Средние расходы на обследование одного больного до ознакомления с расходами коллег
#
# X = np.array([20, 17, 14, 42, 50, 62, 8, 49, 81, 54, 48, 55, 56])
# Y = np.array([20, 26, 1, 24, 1, 47, 15, 7, 65, 9, 21, 36, 30])
#
# Средние расходы на лечение одного больного до ознакомления с расходами коллег
#
# X = np.array([32, 41, 51, 29, 76, 47, 60, 58, 40, 64, 73, 66, 73])
# Y = np.array([42, 90, 71, 47, 56, 43, 137, 63, 28, 60, 87, 69, 50])
# Произошли ли изменения на расходы и лечение?
X = np.array([20, 17, 14, 42, 50, 62, 8, 49, 81, 54, 48, 55, 56])
Y = np.array([20, 26, 1, 24, 1, 47, 15, 7, 65, 9, 21, 36, 30])
X1 = np.array([32, 41, 51, 29, 76, 47, 60, 58, 40, 64, 73, 66, 73])
Y1 = np.array([42, 90, 71, 47, 56, 43, 137, 63, 28, 60, 87, 69, 50])
WilconsResul1 = stats.wilcoxon(X,Y)
WilconsResul2 =stats.wilcoxon(X1,Y1)
print(WilconsResul1,WilconsResul2)
import numpy as np
from scipy import stats

# Данные по расходам на обследование
X_obследование = np.array([20, 17, 14, 42, 50, 62, 8, 49, 81, 54, 48, 55, 56])
Y_obследование = np.array([20, 26, 1, 24, 1, 47, 15, 7, 65, 9, 21, 36, 30])

# Данные по расходам на лечение
X_лечение = np.array([32, 41, 51, 29, 76, 47, 60, 58, 40, 64, 73, 66, 73])
Y_лечение = np.array([42, 90, 71, 47, 56, 43, 137, 63, 28, 60, 87, 69, 50])


def analyze_mannwhitney(group1, group2, description):
    statistic, pvalue = stats.mannwhitneyu(group1, group2, alternative='two-sided')
    alpha = 0.05
    print(f"Анализ для {description}:")
    print(f"  Статистика U: {statistic}")
    print(f"  P-значение: {pvalue}")
    if pvalue < alpha:
        print("  Различие между группами статистически значимо.")
    else:
        print("  Различие между группами статистически незначимо.")


analyze_mannwhitney(X_obследование, Y_obследование, "расходов на обследование")
analyze_mannwhitney(X_лечение, Y_лечение, "расходов на лечение")

import numpy as np
from scipy import stats

# Данные по расходам на обследование
X_obследование = np.array([20, 17, 14, 42, 50, 62, 8, 49, 81, 54, 48, 55, 56])
Y_obследование = np.array([20, 26, 1, 24, 1, 47, 15, 7, 65, 9, 21, 36, 30])

# Данные по расходам на лечение
X_лечение = np.array([32, 41, 51, 29, 76, 47, 60, 58, 40, 64, 73, 66, 73])
Y_лечение = np.array([42, 90, 71, 47, 56, 43, 137, 63, 28, 60, 87, 69, 50])


def analyze_mannwhitney(group1, group2, description):
    statistic, pvalue = stats.mannwhitneyu(group1, group2, alternative='two-sided')
    alpha = 0.05
    print(f"Анализ для {description}:")
    print(f"  Статистика U: {statistic}")
    print(f"  P-значение: {pvalue}")
    if pvalue < alpha:
        print("  Различие между группами статистически значимо.")
    else:
        print("  Различие между группами статистически незначимо.")


analyze_mannwhitney(X_obследование, Y_obследование, "расходов на обследование")
analyze_mannwhitney(X_лечение, Y_лечение, "расходов на лечение")

import numpy as np
from scipy.stats import friedmanchisquare

# При исследовании препарата для снижения кровяного давления у больных 3 раза измерялся
# сердечный выброс. Менялся ли сердечный выброс?  Найти критерий вручную, проверьте значение
# функцией и интерпретируйте результат с использованием p-value

A = np.array([3.5, 3.3, 4.9, 3.6])
B = np.array([8.6, 5.4, 8.8, 5.6])
C = np.array([5.1, 8.6, 7.7, 5.0])

# Объединяем данные в одну матрицу, где каждая строка - пациент, а столбцы - измерения
data = np.array([A, B, C])

# Выполняем тест Фридмана
statistic, pvalue = friedmanchisquare(*data)

print("Статистика теста Фридмана:", statistic)
print("P-значение:", pvalue)

alpha = 0.05  # Уровень значимости
if pvalue < alpha:
    print("Есть статистически значимые различия в сердечном выбросе между измерениями.")
else:
    print("Статистически значимых различий в сердечном выбросе между измерениями нет.")

    # Даны  значения  проницаемости  сосудов  сетчатки gr1(здоровые  пациенты), gr  2(поражение  в области центральной ямки), gr3(в
    # области центральной ямки и на периферии). Сравнить данные, относящиеся к разным видам поражения.
    # gr1 = ([0.5, 0.7, 1, 1.2, 1.4])
    # gr2 = ([1.3, 1.45, 1.6, 1.7, 1.8])
    # gr3 = ([6.2, 12.6, 13.2, 14.1, 14.2])

import numpy as np
from scipy.stats import kruskal

gr1 = np.array([0.5, 0.7, 1, 1.2, 1.4])
gr2 = np.array([1.3, 1.45, 1.6, 1.7, 1.8])
gr3 = np.array([6.2, 12.6, 13.2, 14.1, 14.2])

statistic, pvalue = kruskal(gr1, gr2, gr3)

print("Статистика теста Краскела-Уоллиса:", statistic)
print("P-значение:", pvalue)

alpha = 0.05
if pvalue < alpha:
    print("Есть статистически значимые различия в проницаемости сосудов сетчатки между группами.")
else:
    print("Статистически значимых различий в проницаемости сосудов сетчатки между группами нет.")


