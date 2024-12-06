# История: соперничество двух команд - Мастера кода и Волшебники данных.

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
# tasks_total = 82
# time_avg = 45.2
# challenge_result = 'Победа команды Волшебники данных!'

# Использование %:
# Переменные: количество участников первой команды (team1_num)
print('В команде Мастера кода участников: %(team1_num)s!'% {'team1_num': 5})

# Переменные: количество участников в обеих командах (team1_num, team2_num).
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!" % {'team1_num': 5, 'team2_num': 6})

# Использование format():
# Переменные: количество задач решённых командой 2 (score_2).
print("Команда Волшебники данных решила задач: {}!" .format(score_2))

# Переменные: время за которое команда 2 решила задачи (team1_time).
print("Волшебники данных решили задачи за {:.1f} с!".format(team1_time))

# Использование f-строк:
# Переменные: количество решённых задач по командам: score_1, score_2
print(f'Команды решили {score_1} и {score_2} задач.')

# Переменные: исход соревнования (challenge_result).
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
challenge_result = result
print(f"challenge_result = {challenge_result}")

# Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!.")

