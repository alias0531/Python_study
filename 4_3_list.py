student = ["egoing", "sori", "maru"]
grades= [2, 1, 4]

print("student[1]", student[1])
print("len(student)", len(student))

print("min(grades)", min(grades))
print("max(grades)", max(grades))

import statistics as st

print("st.mean(grades)", st.mean(grades))

import random
print("random.choice(student)", random.choice(student))