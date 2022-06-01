x = ([1, 2, 'a', 'b'])
y = ([1, 'a', 'b', 0 , 15])
z = ([1, 2, 'aasf', '1', '123', 123])


def filter_list(x):
    new_list = []
    for i in x:
        if type(x) ==  int:
            new_list.append(x)
    return new_list