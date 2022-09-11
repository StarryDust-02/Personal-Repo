"""Unit 1 Data Type

>>> a = 1
>>> type(a)
<class 'int'>

>>> b = [1, 2]
>>> type(b)
<class 'list'>

>>> c = False
>>> type(c)
<class 'bool'>

>>> d = 3.14
>>> type(d)
<class 'float'>

>>> e = {2, 3}
>>> type(e)
<class 'set'>

We have:
>>> a_lst = [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', True, [1, 2], [False], False]

Demo, only bool
>>> [item for item in a_lst if type(item) == bool]
[True, False]

We want to have a list only containing strings
>>> string_lst = [item for item in a_lst if type(item) == str]
>>> string_lst == ['a', 'b']
True

>>> a_lst = a_lst[:8]

We want a list only containing even numbers.
>>> even_lst = [item for item in a_lst if item % 2 == 0]
>>> even_lst == [2, 4, 6, 8]
True

Make everything in even list +1
>>> odd_lst = [item + 1 for item in even_lst]
>>> odd_lst == [3, 5, 7, 9]
True

Multiply each element in even and odd list
>>> lst = [odd_lst[i] * even_lst[i] for i in range(4)]
>>> lst == [6, 20, 42, 72]
True

"""
