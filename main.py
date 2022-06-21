import string
from functools import wraps
import time
import keyboard
import random


def timekeeping(func):
    """Decorator used to measure the time of execution of a function"""

    def wrapper_timekeeping(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f'\nMeasured time: {(end_time - start_time):.2f}s')
        return result

    return wrapper_timekeeping


def repeat(n):
    """Decorator used to repeatedly call a function n times"""

    def decorate(func):
        @wraps(func)
        def wrapper_repeat(*args, **kwargs):

            result = None
            for i in range(n):
                print(f'Round {i + 1}:')
                result = func(*args, **kwargs)
            return result

        return wrapper_repeat

    return decorate


def reflex_time(func):
    """Decorator that has the same name as the decorated function
    It is used for counting from 3 to 1 before the beginning of each round"""
    def wrapper(*args, **kwargs):

        # Counting from 3 to 1
        for i in range(3, 0, -1):
            print(f'{i}...')
            time.sleep(1)

        result = func(*args, **kwargs)
        return result

    return wrapper


@repeat(5)
@reflex_time
@timekeeping
def reflex_time():
    """Small game that generates a random character and stops when you press the correct key"""

    # Generate a random letter
    random_key = random.choice(string.ascii_letters)
    print(f'\nQuick! Press \"{random_key}\" to measure your reflex')

    # Loop the function until the user presses the correct key
    while True:
        if keyboard.is_pressed(random_key):
            break


# Start the program
reflex_time()
