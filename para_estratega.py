import os
import random

game_over = False
while not game_over:
  os.system("cls")

  print("Alumnos y sus notas de clases ")
  print()
  print("tabla de notas")
  print()
  print("{:^10}|{:^10}|".format("Nombre","Nota"))
  print("-"* 22)

  nalumnos=input("digita el munero de alumnos")

  for nombre, nota in nalumnos:
    nombre=input("digita nombre")
    nota=input("digita nota")

  opc = {"key1":(nombre),"key2":(nota)}

  for col1, col2 in opc: 
    print("{:^10}|{:^10}|".format(col1, col2,))
  else:
    print()













