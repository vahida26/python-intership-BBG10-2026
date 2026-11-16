#code error
age = "20"
next_year_age = age + 1
print("Next year I will be " + next_year_age)

# corrected code
age = 20
next_year_age = int(age) + 1
print("Next year I will be:" , next_year_age)

#explanation
#1.age="20" is a string, so we cannot add an integer to it directly.
#2. To fix this, we convert the string to an integer using int(age) before adding 1.
