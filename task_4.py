# Задача 4. Есть ли статистически значимые различия в росте
# дочерей?
# Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169, 165
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160, 163

from scipy import stats

alpha = 0.05
m = [172, 177, 158, 170, 178, 175, 164, 160, 169, 165]
d = [173, 175, 162, 174, 175, 168, 155, 170, 160, 163]

a, b = stats.ttest_rel(m, d)
print(a,b)
if b > alpha:
    print('Нулевая гипотеза не отвергается различий нет')
else:
    print('Нулевая гипотеза отвергается различия есть')

# Так как p-value больше alpha(0.05) следовательно нулевую гипотезу не отвергаем, статистически значимых различий в росте дочерей нет.
