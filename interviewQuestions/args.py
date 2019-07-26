# a  *args  **kwargs


def function(a, *args, **kwargs):
    print(type(a))
    print(type(args))
    print(type(kwargs))
    print(a)
    print(args)
    print(kwargs)


function(1, 2, 3)
function(6, 7, 8, 9, b=1, c=2, d=3)


