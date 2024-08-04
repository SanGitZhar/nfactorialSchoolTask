import random, time

def generate():
    count = 10 #Задаем количество сообщений
    for i in range(count):
        interval = random.randint(1, 2) # Задаем интервал сообщений
        if i > 0:
            time.sleep(interval)
        timestamp = i * interval
        yield (timestamp, f"Message{i}")


    # Это функция генерации сообщений для нашей программы
    # Она создает последовательно сообщения "Message{i}"
    # Программа не предусматривает 2 сообщения в одном timestamp
    # Хотя данный момент я не проверял