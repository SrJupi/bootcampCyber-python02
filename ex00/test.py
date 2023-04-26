from ft_reduce import ft_reduce
from ft_map import ft_map
from ft_filter import ft_filter
from functools import reduce

if __name__ == "__main__":
    print("ft_reduce Tests")
    # Test case 1: sum a list of integers
    def add(x, y):
        return x + y

    assert ft_reduce(add, [1, 2, 3, 4, 5]) == reduce(add, [1, 2, 3, 4, 5])

    # Test case 2: multiply a list of integers
    def multiply(x, y):
        return x * y

    assert ft_reduce(multiply, [1, 2, 3, 4, 5]) == reduce(multiply, [1, 2, 3, 4, 5])

    # Test case 3: find the maximum value in a list of integers
    def maximum(x, y):
        return x if x > y else y


    assert ft_reduce(maximum, [1, 2, 3, 4, 5]) == reduce(maximum, [1, 2, 3, 4, 5])


    # Test case 4: concatenate a list of strings
    def concatenate(x, y):
        return x + y


    assert ft_reduce(concatenate, ['a', 'b', 'c', 'd']) == reduce(concatenate, ['a', 'b', 'c', 'd'])


    # Test case 5: sum a list of integers with an initial value
    def add_with_initial(x, y):
        return x + y

    assert ft_reduce(add_with_initial, [1, 2, 3, 4, 5], 10) == reduce(add_with_initial, [1, 2, 3, 4, 5], 10)

    # Test case 6: multiply a list of integers with an initial value
    def multiply_with_initial(x, y):
        return x * y


    assert ft_reduce(multiply_with_initial, [1, 2, 3, 4, 5], 10) == reduce(multiply_with_initial, [1, 2, 3, 4, 5], 10)


    # Test case 7: find the maximum value in a list of integers with an initial value
    def maximum_with_initial(x, y):
        return x if x > y else y


    assert ft_reduce(maximum_with_initial, [1, 2, 3, 4, 5], 0) == reduce(maximum_with_initial, [1, 2, 3, 4, 5], 0)


    # Test case 8: concatenate a list of strings with an initial value
    def concatenate_with_initial(x, y):
        return x + y


    assert ft_reduce(concatenate_with_initial, ['a', 'b', 'c', 'd'], 'x') == reduce(concatenate_with_initial, ['a', 'b', 'c', 'd'], 'x')
    print('ft_reduce tests OK')


    print('ft_map tests')
    # Test case 1: map a list of integers to their squares
    def square(x):
        return x ** 2

    assert list(ft_map(square, [1, 2, 3, 4, 5])) == list(map(square, [1, 2, 3, 4, 5]))


    # Test case 2: map a list of strings to their uppercase versions
    def uppercase(x):
        return x.upper()


    assert list(ft_map(uppercase, ['apple', 'banana', 'kiwi', 'pear', 'grape'])) == list(map(uppercase, ['apple', 'banana', 'kiwi', 'pear', 'grape']))

    # Test case 3: map a list of dictionaries to a list of their values
    data = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Charlie'}
    ]

    assert list(ft_map(lambda x: x['name'], data)) == list(map(lambda x: x['name'], data))


    # Test case 4: map an empty list
    def square(x):
        return x ** 2


    assert list(ft_map(square, [])) == list(map(square, []))


    # Test case 5: map a list to a different type
    def to_string(x):
        return str(x)


    assert list(ft_map(to_string, [1, 2, 3, 4, 5])) == list(map(to_string, [1, 2, 3, 4, 5]))

    print('ft_map tests OK')

    print("ft_filter tests")


    # Test case 1: filter a list of integers by even numbers
    def is_even(x):
        return x % 2 == 0


    assert list(ft_filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == list(filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


    # Test case 2: filter a list of strings by length
    def is_long_enough(x):
        return len(x) >= 5


    assert list(ft_filter(is_long_enough, ['apple', 'banana', 'kiwi', 'pear', 'grape'])) == list(filter(is_long_enough, ['apple', 'banana', 'kiwi', 'pear', 'grape']))


    # Test case 3: filter a list of dictionaries by value
    def has_value_greater_than_5(x):
        return x['value'] > 5


    data = [
        {'id': 1, 'value': 2},
        {'id': 2, 'value': 7},
        {'id': 3, 'value': 1},
        {'id': 4, 'value': 9},
        {'id': 5, 'value': 4}
    ]

    assert list(ft_filter(has_value_greater_than_5, data)) == list(filter(has_value_greater_than_5, data))


    # Test case 4: filter an empty list
    def is_even(x):
        return x % 2 == 0


    assert list(ft_filter(is_even, [])) == list(filter(is_even, []))


    # Test case 5: filter a list where no element satisfies the condition
    def is_greater_than_10(x):
        return x > 10


    assert list(ft_filter(is_greater_than_10, [1, 2, 3, 4, 5])) == list(filter(is_greater_than_10, [1, 2, 3, 4, 5]))

    print("ft_filter tests ok")



