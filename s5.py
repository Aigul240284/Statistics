import numpy as np
import stats
from scipy.stats import ttest_ind, stats

# Ниже приведены диаметры коронарных артерий после приема нифедипина и плацебо. Позволяют
# ли приводимые ниже данные утверждать, что нифедипин влияет на диаметр коронарных артерий?
#  1. Выполнить расчеты в Python
#  2. Сделайте расчет в ручную
#  3. Сравните критерий Стьюдента и p-value со значениями, полученными в Python
x =np.array([2.5, 2.2, 2.6, 2, 2.1, 1.8,2.4, 2.3, 2.7, 2.7, 1.9])
y= np.array([2.5, 1.7, 1.5, 2.5, 1.4, 1.9, 2.3, 2.0, 2.6, 2.3, 2.2])
mx = np.mean(x)
my = np.mean(y)
sx=np.std(x, ddof=1)
sy=np.std(y, ddof=1)
nx=len(x)
ny=len(y)
t=(mx-my)/(sx**2/nx+sy**2/ny)**(1/2)

print(t) #1.328
q=2.086 # таблица стьюдента пересечение 0,005 и(10+10-2) 0.975 (100-0.05/2)
# n.t 1.328 меньше 2.086 не отклоняем, все ок
# stats.ttest_isamp(x,y)

t_statistic, p_value = ttest_ind(x, y, equal_var=False) # equal_var=False указывает на Welch's t-test

print(f"t-статистика: {t_statistic}")
print(f"p-value: {p_value}")


