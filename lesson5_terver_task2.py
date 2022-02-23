# Задача 1
# Продавец утверждает, что средний вес пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
# ```
# 202, 203, 199, 197, 195, 201, 200, 204, 194, 190
# ```
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что уровень значимости равен 1%?
# Найдите P-значение для данного теста и укажите его в качестве ответа.

import numpy as np
from scipy import stats


def statistic(samples: np.ndarray) -> float:
    return (samples.mean() - 200) / (samples.std(ddof=1) / np.sqrt(samples.shape[0]))


cookies = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])

n = cookies.shape[0]
S = statistic(cookies)

p_left = stats.t.cdf(S, df=n - 1)
p_right = 1 - stats.t.cdf(S, df=n - 1)

pvalue = 2 * min(p_left, p_right)

print(round(pvalue, 8))

#  P-значение = 0.3145666 больше выбранного нами уровня значимости, гипотезу можно принять
