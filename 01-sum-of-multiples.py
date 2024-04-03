def sum_of_multiples(multiple, ceiling):
  upper_limit = ceiling // multiple
  return (upper_limit * (upper_limit + 1)) // 2 * multiple

def multiples_of_3_or_5():
  three = sum_of_multiples(3, 1000)
  five = sum_of_multiples(5, 1000)
  fifteen = sum_of_multiples(15, 1000)
  return (three + five) - fifteen

print(multiples_of_3_or_5())
