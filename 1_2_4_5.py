def main():
    #1 zadanie
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    number = int(input())
    print(f'Факториал числа {number} равен {factorial(number)}')

    #2 zadanie
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    n = int(input())
    result = fibonacci(n)
    print(f'{n}-е число Фибоначчи равно {result}')

    #4 zadanie
    def prime_recursive(n, div=2):
        if n == 0 or n == 1:
            return False
        if n == div:
            return True
        if n % div == 0:
            return False
        return prime_recursive(n, div + 1)
    number = int(input())
    if prime_recursive(number):
        print(f"Число {number} является простым.")
    else:
        print(f"Число {number} не является простым.")

    #5 zadanie
    def max_recursive(arr):
        if len(arr) == 1:
            return arr[0]
        else:
            max_rest = max_recursive(arr[1:])
            return arr[0] if arr[0] > max_rest else max_rest
    numbers = [3, 8, 1, 10, 5]
    max_num = max_recursive(numbers)
    print(f"Максимальное число в списке {numbers} равно {max_num}.")


if __name__ == '__main__':
    main()
