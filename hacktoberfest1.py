# -*- coding: utf-8 -*-
"""Hacktoberfest1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jgI5HJmB_pbttnPNWWmqwjagS6sJeuWT
"""

#Q)Write a python program to print the following pattern using loop.
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *
n = int(input("Enter the number of rows: "))
for i in range(0, n):
  for j in range(0, i + 1):
    print("* ", end="")
  print()