# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    TinyStatistician.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lsulzbac <lsulzbac@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/25 12:06:17 by lsulzbac          #+#    #+#              #
#    Updated: 2023/04/25 12:09:03 by lsulzbac         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

class TinyStatistician:
    
    def mean(self, values):
        if len(values) == 0:
            return None
        try:
            values = values.flatten().tolist()
        except:
            pass
        return sum(values)/len(values)

    def median(self, values):
        if len(values) == 0:
            return None
        try:
            values = values.flatten().tolist()
        except:
            pass
        values = sorted(values)
        if len(values) % 2 == 0:
            
            return (values[len(values)//2] + values[len(values)//2 - 1]) / 2
        return values[len(values)//2]
        
    def quartile(self, values):
        if len(values) == 0:
            return None
        try:
            values = values.flatten().tolist()
        except:
            pass
        values = sorted(values)
        middle = len(values) // 2
        if len(values) % 2 == 0:
            return [self.median(values[:middle]), self.median(values[middle:])]
        return [self.median(values[:middle+1]), self.median(values[middle:])]
        
    def var(self, values):
        mean = self.mean(values)
        if not mean:
            return None
        result = 0
        for item in values:
            result += (item - mean) ** 2
        return result/(len(values))
        
    def std(self, values):
        return math.sqrt(self.var(values)) 
