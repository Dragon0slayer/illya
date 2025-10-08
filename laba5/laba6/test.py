from throttle_decorator import throttle
import time

@throttle(3)
def say_hello():
    print("Привіт! Функція виконана.")

print("Спробуємо викликати функцію кілька разів:")
say_hello()
time.sleep(1)
say_hello()
time.sleep(2)
say_hello()
