def gen_squares(max_base):
    for n in range(max_base):
        yield  n**2

squares = gen_squares(6)
## for square in squares: print(square)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
