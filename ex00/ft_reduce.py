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
from functools import reduce


def ft_reduce(function_to_apply, iterable, initializer=None):
    """Filter the result of function apply to all elements of the iterable. Args: function_to_apply: a function
    taking an iterable. iterable: an iterable object (list, tuple, iterator). initializer:  If the optional
    initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default
    when the iterable is empty. Return: An iterable. None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError(f"'{type(function_to_apply).__name__}' is not callable")
    if not isinstance(iterable, Iterable):
        raise TypeError(f"'{type(iterable).__name__}' is not iterable")
    iterator = iter(iterable)
    if initializer is None:
        try:
            initializer = next(iterator)
        except StopIteration:
            raise TypeError('ft_reduce() of empty sequence with no initial value')
    for item in iterator:
        initializer = function_to_apply(initializer, item)
    return initializer