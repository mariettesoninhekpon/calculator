#Calculatrice

operator = input("taper le signe de l'opération:\n") #demande et stocke l'opérateur
firstNumber = input("taper le premier nombre:\n") #demande et stocke le premier nombre
secondNumber = input("taper le second nombre:\n") #demande et stocke le second nombre
result = 0 #stocke le résultat

if operator == "+": #si l'opérateur est +, fais une addition des deux nombres
    result = int(firstNumber) + int(secondNumber)
elif operator == "-": #si l'opérateur est -, fais une soustraction des deux nombres
    result = int(firstNumber) - int(secondNumber)
elif operator == "*": #si l'opérateur est *, fais une multiplication des deux nombres
    result = int(firstNumber) * int(secondNumber)
elif operator == "/": #si l'opérateur est /, fais une division des deux nombres
    result = int(firstNumber) / int(secondNumber)

print("le résultat de votre opération est :", result) #affiche le résultat dans la console
