# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 12:59:12 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/20 12:24:59 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from random import randint
import os

def parse_time(exec_time):
    if exec_time > 1:
        exec_time = f"{exec_time:8.3f} s "
    else:
        exec_time *= 1000
        exec_time = f"{exec_time:8.3f} ms"
    return exec_time

def log(namefile='machine.log'):
    def decorator(func):
        def inner(*args, **kwargs):
            start_time = time.time()
            response = func(*args, *kwargs)
            exec_time = parse_time(time.time() - start_time)
            name = " ".join(word.lower().capitalize() for word in func.__name__.split('_')).ljust(18)
            my_log= f"({os.getlogin()})Running: {name[0:18]} [ exec-time = {exec_time} ]\n"
            with open(namefile, 'a') as f:
                f.write(my_log)
            return response
        return inner
    return decorator

class CoffeeMachine():
    water_level = 100
    
    @log()
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log()
    def boil_water(self):
        return "boiling..."

    @log()
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log()
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    
    machine.make_coffee()
    machine.add_water(70)    
