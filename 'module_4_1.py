from fake_math import divide_ as fk_div
from true_math import divide_ as tr_div

result1 = fk_div(69, 3)
result2 = fk_div(12, 0)
result3 = tr_div(49, 7)
result4 = tr_div(13, 0)
print(result1)
print(result2)
print(result3)
print(result4)