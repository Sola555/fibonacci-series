value = int(input("Until what number do you want toe fibonacci to go?"))
def fibonacci(n):
  a = 1
  b = 1
  while (a < n):
    print(a)
    c = a+b
    a = b
    b = c
fibonacci(value)