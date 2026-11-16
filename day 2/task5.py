height_cm = "175"
weight_kg = "68.5"

#convert the string into numeric types
height_cm = int(height_cm)
weight_kg = float(weight_kg)

#convert height into meters
height_m = height_cm / 100
print("Height in meters:", height_m)
print("weight in kg:", weight_kg)

#calculate BMI
BMI = weight_kg / (height_m * height_m)
print("BMI:", round(BMI,2))