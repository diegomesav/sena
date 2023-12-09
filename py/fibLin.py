"""def fibonacci(n):
  res = [0,1]
  actual = 2
  for actual in range(n+1):
    fib = res[actual-2] + res[actual-1]
    res.insert(actual,fib)
    actual += 1
  return res[n]

print(fibonacci(79))"""

def fix_me(nested_list):
    final_list = []
    indexAux = 1
    for a_list in nested_list:
        partial_sum = 0
        for basic_element in a_list:
            partial_sum += basic_element

        if partial_sum % 2 == 0 or indexAux % 2 == 0:
            partial_sum *= -1
        indexAux += 1

        final_list.append(partial_sum)

    return final_list

print(fix_me([[1], [2]]))
print(fix_me([[1, 2], [3, 4]]))
print(fix_me([[1, 2], [3, 4], [-1, -4]]))
print(fix_me([[1, 2, 18], [3, 4, 2], [-1, 5, 6, 7]]))
print(fix_me([[1, 2, 18], [3, 4, 2], [-1, 5, 6, 7], [1], [], [1, 2, 56, 2]]))
