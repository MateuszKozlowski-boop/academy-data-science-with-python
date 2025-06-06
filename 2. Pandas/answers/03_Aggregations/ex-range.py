# part 1

chickweight['weight'].max() - chickweight['weight'].min()

# part 2
def my_range(col):
    return col.max() - col.min()

my_range(chickweight['weight'])

# bonus
(lambda col: col.max() - col.min())(chickweight['weight'])