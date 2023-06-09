# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 12:52:14 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/19 12:54:10 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class ObjectC(object):
    def __init__(self, *args, **kwargs):
        for i, item in enumerate(args):
            attr = "var_" + str(i)
            setattr(self, attr, item)
        for item in kwargs:
            if item in self.__dict__:
                raise TypeError('arg already in __dict__')
            setattr(self, item, kwargs[item])
        
def what_are_the_vars(*args, **kwargs):
    try:
        return ObjectC(*args, **kwargs)
    except TypeError:
        return None


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)
