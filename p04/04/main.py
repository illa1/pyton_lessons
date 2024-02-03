import os
os.system("clear")

print(7 == 7)
print(7 >= 7)
print(7 < 7)

x = int(input("Введіть число: "))

answer = "Error"

if x >= 5:
    if x <= 10:
        answer = " ok "

print(answer)