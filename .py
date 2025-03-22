import random

# print(random.randint(0,5)) <----ต่างกันตรง choice ออกมาหลายตัว
symbols = ['🍒',' 🍇', '🍉', '7️⃣']

print('welcome to machine !!!')
ads = input("R U READY GLAMBLER????")
while True:
  re = str(input('play ?  Y  or  N  :'))
  if re == 'Y' or 'y':
    print(random.choices(symbols, k=3)*1)
  else:
    print('Thnkyou for playing')
    break

