#print("Славяна")
#print("14")

#number = 10
#print(number * 5)

#number2 = 7
#print(number + number2)

print("Добро пожаловать в квиз по стартапам!")
print("Ответь на следующие вопросы: ")

questions = ["1. Как называется компания, которая создается для развития новой идеи или инновационного продукта?", "2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли?", "3. Как называется капитал, который дают инвесторы на развитие стартапа?", "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?", "5. Какой план создают перед тем, как открывать стартап и занимать деньги?", "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?", "7. Как называется разница между выручкой и затратами компании?"]
answers = ["Стартап", "Инвестор", "Инвестиция", "MVP", "Бизнес-план", "Конкуренты", "Прибыль"]

score = 0

print(questions[0])
user_answer = input("Введите свой ответ: ")
if user_answer.lower() == answers[0].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[1])
user_answer = input("Введите свой ответ: ")
if user_answer.lower() == answers[1].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[2])
user_answer = input("Введите свой ответ: ")
if user_answer.lower() == answers[2].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[3])
user_answer = input("Введите свой ответ: ")
if user_answer.lower() == answers[3].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[4])
user_answer = input("Введите свой ответ: ")
if user_answer.lower() == answers[4].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[5])
user_answer = input("Введите свой ответ: ")
if user_answer.lower() == answers[5].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[6])
user_answer = input("Введите свой ответ: ")
if user_answer.lower() == answers[6].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(score)

if score > 5:
    print("Это отличный результат! Ты много знаешь о стартапах.")
elif score > 3:
    print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много о стартапах.")
else:
    print("Видимо, ты только начинаешь свой путь к стартапам! Ты ещё много чего узнаешь о мире, где мы живём.")

#print("Дискриминант")
#print("Программа помогает быстро высчитывать дискриминант. Нужно ввести квадратное уравнение и программа найдет дискриминант за тебя.")

#product = input("Введите продукт: ")
#money = int(input("Введите цену продукта: "))
#print("Сегодня скидки!")
#print("Вы купили", product, "за", money - 10, "рублей")

#game = input("какая твоя любимая игра? ") #спрашиваем любимую игру
#good = int(input("На скалько ты хорош(а) в этой игре от 1 до 10? "))

#gets hour
#hour = int(input("какой сейчас час? "))
#gets day
#day = int(input("какой сейчас день? "))
#gets month
#month = int(input("какой сейчас месяц? "))
#gets year
#year = int(input("какой сейчас год? "))
#displays information
#print("сейчас", hour, "часов", day, "число", month, "месяц", year, "год" )

#name = "Славяна"
#year = 2024
#message = "желаю удачи на ОГЭ!"
#print("Привет,", name, "которая из будущего, пишу это из", year, "года и", message)

#x = str("5")
#print(x)
#y = input(float())
#print(y)
