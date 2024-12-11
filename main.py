print('              задание')
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(3, 5)
print_params('one', 8, False)

print('              задание')
print_params(b=25)
print_params(c=[1, 2, 3])

print('              задание')
values_list_ = ['one', 2, False]
values_dict_ = {'a':5, 'b':1, 'c':2}
print_params(*values_list_)
print_params(**values_dict_)

print('              задание')
values_list_2_ = [12, 'two']
print_params(*values_list_2_, 42)