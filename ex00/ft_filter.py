# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/25 12:13:37 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/25 12:17:50 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from collections.abc import Iterable


def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
Return:
    An iterable.
    None if the iterable can not be used by the function.
"""
    if not callable(function_to_apply):
        raise TypeError(f"'{type(function_to_apply).__name__}' is not callable")
    if not isinstance(iterable, Iterable):
        raise TypeError(f"'{type(iterable).__name__}' is not iterable")
    return (item for item in iterable if function_to_apply(item))