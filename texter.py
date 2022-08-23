import keyboard
from time import sleep

# inputs
msg = input("Mensagem: ")
n = int(input("Quantidade: "))

# contador
counter = 3

for i in range(0, counter):
    print(f"{i + 1}...")
    sleep(0.5)

print("Já!")
sleep(0.5)

# 5 por segundo
for i in range(0, n):
    keyboard.write(f"{i + 1} - {msg}")
    keyboard.press_and_release('enter')
    sleep(0.2)