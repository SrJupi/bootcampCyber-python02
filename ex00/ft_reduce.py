# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/25 12:13:37 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/25 12:25:57 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from collections.abc import Iterable

def ft_reduce(func, iterable):
    '''Filter the result of function apply to all elements of the iterable.
Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
Return:
    An iterable.
    None if the iterable can not be used by the function.
'''
    if not callable(func):
        raise TypeError(f"'{type(func).__name__}' is not callable")
    if not isinstance(iterable, Iterable):
        raise TypeError(f"'{type(iterable).__name__}' is not iterable")
    if len(iterable) == 0:
        raise TypeError('ft_reduce() of empty sequence with no initial value')
    result = iterable[0]
    for item in iterable[1:]:
        result = func(result, item)
    return result
