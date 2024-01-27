print("\n-----------------------------")
print("-співідношення учнів у класі-")
print("-----------------------------", end="\n")

number_girls = int(input("Введіть кількість дівчат: "))
number_boys = int(input("Введіть кількість хлопців: "))

#print(type(number_girls), type(number_boys), end="\n\n")#

all_students = number_girls + number_boys
pecent_girls = int(number_girls * 100 / all_students)
pecent_boys = 100 - pecent_girls

#print(f"дівчат{pecent_girls}%, хлопців {pecent_boys}%")#
print("дівчат" + str(pecent_girls) + "%", "хлопців" + str(pecent_boys) + "%")
print("\n------ кінець програми ------")
print("\n\n\n")