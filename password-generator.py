import random

charst = "abcdefghijklmnopqrstuvwryzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!@#$%^&*(){}[]()"
length = int(input("enter length of your password: "))
password = ""

for a in range(length):
    password += random.choice(charst)

print(password)