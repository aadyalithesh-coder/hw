import math

angle_degrees = 45


angle_radians = math.radians(angle_degrees)


sine_val = math.sin(angle_radians)
cosine_val = math.cos(angle_radians)
tangent_val = math.tan(angle_radians)


print(f"Angle: {angle_degrees}°")
print(f"Sine:    {round(sine_val, 4)}")
print(f"Cosine:  {round(cosine_val, 4)}")
print(f"Tangent: {round(tangent_val, 4)}")
