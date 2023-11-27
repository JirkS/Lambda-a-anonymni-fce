pole = [100.10, 323.2, 355.9, 214.19, 87.0]
pole2 = list(map(lambda x: x * 1.3, pole))
print(pole2)

pole3 = list(filter(lambda x: x > 120.0, pole))
print(pole3)

pole4 = list(map(lambda x: x * 1.3 - 5, filter(lambda x: x > 110.0, pole)))
print(pole4)

