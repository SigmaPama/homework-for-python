n = int(input("Число - "))
def fizz_buzz(n):
    for y in range (1, n + 1):
        if y % 3 == 1:
            print("Fizz")
        else:
            if y % 5 == 1:
                print("Buzz")
            else:
                if y % 3 == 1 and y % 5 == 1:
                    print("FizzBuzz")
                else:
                    print(y)
fizz_buzz(n)