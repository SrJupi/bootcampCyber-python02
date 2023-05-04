# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 12:59:12 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/27 17:25:27 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import os


def parse_time(exec_time):
    if exec_time > 1:
        exec_time = f"{exec_time:8.3f} s "
    else:
        exec_time *= 1000
        exec_time = f"{exec_time:8.3f} ms"
    return exec_time


def log(namefile='logger.log'):
    def decorator(func):
        def inner(*args, **kwargs):
            start_time = time.time()
            response = func(*args, *kwargs)
            exec_time = parse_time(time.time() - start_time)
            name = " ".join(word.lower().capitalize() for word in func.__name__.split('_')).ljust(18)
            my_log = f"({os.getlogin()})Running: {name[0:18]} [ exec-time = {exec_time} ]\n"
            with open(namefile, 'a') as f:
                f.write(my_log)
            return response

        return inner

    return decorator
