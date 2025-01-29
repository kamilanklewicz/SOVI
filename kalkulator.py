#!/usr/bin/env python3


#Author kanklewicz
#Version Beta

# Prosty kalkulator w Pythonie

# Funkcje operacji
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Nie można dzielić przez zero"

# Menu kalkulatora
print("Wybierz operację:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")

# Pobranie wyboru użytkownika
operation = input("Wprowadź numer operacji (1/2/3/4): ")

# Pobranie liczb od użytkownika
num1 = float(input("Wprowadź pierwszą liczbę: "))
num2 = float(input("Wprowadź drugą liczbę: "))

# Wykonanie operacji
if operation == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operation == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Nieprawidłowy wybór")

