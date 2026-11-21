def make_validator(min_value):
    def validator(num):
        return num >= min_value
    return validator

adult_validator = make_validator(18)
passing_validator = make_validator(40)

print("Age 20 vlid:", adult_validator(20))  # True
print("Age 15 valid:", adult_validator(15))  # False

print("Score 40 valid:", passing_validator(40))  # True
print("Score 35 valid:", passing_validator(35))  # False