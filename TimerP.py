import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_format = f'{mins:02d}:{secs:02d}'
        print(timer_format, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Время вышло!")

# Установите время в секундах
timer_duration = 5  # Пример: 5 секунд

countdown_timer(timer_duration)
