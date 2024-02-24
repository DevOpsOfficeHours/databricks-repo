# Databricks notebook source
# This code generates a random number and checks if it is even or odd
import random

def generate_random_number():
    return random.randint(1, 100)

random_number = generate_random_number()

if random_number % 2 == 0:
    print("The random number is even.")
else:
    print("The random number is odd.")
