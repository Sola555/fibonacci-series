value = int(input("Until what number do you want to fibonacci to go?"))
def fibonacci(n):
  a = 1
  b = 1
  while (a < n):
    print(a)
    c = a+b
    a = b
    b = c
  Phi = b/a
  print("Phi is (φ or ϕ): {}".format(Phi))
fibonacci(value)
