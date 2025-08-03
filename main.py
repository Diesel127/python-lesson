import random
secret_number = random.randint(1, 100)
attempts = 0

print("Угадай число от 1 до 100")

while True:
    guess = int(input("Введи число: "))
    attempts += 1

    if guess == secret_number:
        print(f"✅ Правильно! Ты угадал за {attempts} попыток.")
        break
    elif guess < secret_number:
        print("🔼 Слишком маленькое.")
    else:
        print("🔽 Слишком большое.")