import random
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
logitud=int(input("Por favor ingresa la logitud de tu contraseña: "))
contrasenia=""
for i in range(logitud):
    contrasenia+=random.choice(caracteres)
print(f"esta es tu contraseña: {contrasenia}")
print("esta es tu contraseña: ", contrasenia)