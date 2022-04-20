import random
ver = 0
while (ver == 0):      
        player = int(input("1 - камінь, 2 - ножниці, 3 - папір. "))
        if (player == 1 or player == 2 or player == 3):
            ver = 1    
if player == 1:
        print("Ви вибрали камінь.")  
if player == 2:
        print("Ви вибрали ножниці.") 
if player == 3:
        print("Ви вибрали папір.")  
comp = random.randint(1, 3)
if comp == 1:
        print("Компютер вибрав камінь.") 
if comp == 2:
        print("Компютер вибрав ножниці.")
if comp == 3:
        print("Компютер вибрав папір.")
if player == comp:
        win = 0
if player == 1 and comp == 2:
        win = 1 
if player == 1 and comp == 3:
        win = 2 
if player == 2 and comp == 1:
        win = 2  
if player == 2 and comp == 3:
        win = 1 
if player == 3 and comp == 1:
        win = 1
if player == 3 and comp == 2:
        win = 2
if win == 0:
        print("Нічия!")
if win == 1:
        print("Переміг гравець!")
if win == 2:
        print("Переміг комп'ютер!")