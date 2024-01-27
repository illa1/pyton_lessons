print("\n---------------------")
print("-Кількість лабораторій-")
print("-----------------------", end="\n")

planet_area = int(input("+ Введіть площу планети: "))
big_laboratory_area = int(input("+ Введіть в : "))
middle_laboratory_area = int(input("+ Введіть с : "))
small_laboratory_area = int(input("+ Введіть м : "))

number_big_lab = planet_area // big_laboratory_area
planet_area = planet_area % big_laboratory_area

number_middle_lab = planet_area // middle_laboratory_area
planet_area = planet_area % middle_laboratory_area

number_small_lab = planet_area // small_laboratory_area
planet_area = planet_area % small_laboratory_area

