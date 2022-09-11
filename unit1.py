"""Unit 1 Data Type

Fill in the Todo statements.

>>> a = 'Todo: type something'
>>> type(a)
<class 'int'>

>>> b = 'Todo: type something'
>>> type(b)
<class 'list'>

>>> c = 'Todo: type something'
>>> type(c)
<class 'bool'>

>>> d = 'Todo: type something'
>>> type(d)
<class 'float'>

>>> e = 'Todo: type something'
>>> type(e)
<class 'set'>

We have:
>>> a_lst = [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', True, [1, 2], [False], False]

Demo, only bool
>>> [item for item in a_lst if type(item) == bool]
[True, False]

We want to have a list only containing strings
>>> string_lst = 'Todo: type something'
>>> string_lst == ['a', 'b']
True

>>> a_lst = a_lst[:8]

We want a list only containing even numbers.
>>> even_lst = 'Todo: type something'
>>> even_lst == [2, 4, 6, 8]
True

Make everything in even list +1
>>> odd_lst = 'Todo: type something'
>>> odd_lst == [3, 5, 7, 9]
True

Multiply each element in even and odd list
>>> lst = 'Todo: type something'
>>> lst == [6, 20, 42, 72]
True
"""
