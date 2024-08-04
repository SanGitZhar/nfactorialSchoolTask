import mesaage_generator


class Logger:
    
    def __init__(self):
        self.messages = {}  #Сообщения хранятся в виде {'сообщение 1': timestamp, 'сообщение 2': timestamP}
        self.max_capacity = 100

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.messages:                    #Проверка на уникальность сообщения
            if timestamp < self.messages[message] + 10: #Достаем timestamp по ключу message и проверяем на то что timestamp на 10
                return False
            else:
                self.messages[message] = timestamp #Обновляем timestamp у сообщения
                return True
        else:
            if len(self.messages) >= self.max_capacity: #Проверка на заполненность
                self.clean(timestamp)                   #Вызов функции очистки
            self.messages[message] = timestamp
            return True


    def clean(self, timestamp):     # Удаляем сообщения которые старше 10 секунд 
        keys_to_delete = []         
        for message, time in self.messages.items(): # Собираем все сообшения которые не попадают в диапазон -10:0
            if timestamp >= time + 10:
                keys_to_delete.append(message)

        for key in keys_to_delete:
            del self.messages[key]  


    def loggerSize(self):
        return f"{len(self.messages)},  in logger you have:{self.messages.keys()}"
    
      
def main():
    logger = Logger()
    gen = mesaage_generator.generate()  # Инициализация генератора сообщений
    for timestamp, message in gen:      
        if logger.shouldPrintMessage(timestamp, message):
            print(message)
        
    print(logger.loggerSize())
    

main()


    # Изначально хотел запустить некий таймер. Но я не силен в Многопоточном программировании
    # for t in range(100):
    #     timerFunc(t)
    #     print (t)

    