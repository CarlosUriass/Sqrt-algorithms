def square_root(number):
    for i in range(1, number + 1):
        if i * i == number:
            print(f'The square root of {number} is {i}')
            return  # Exit the function once the square root is found
    print(f'The number {number} does not have a perfect square root')

if __name__ == '__main__':
    number = int(input("What is the number to find the square root? "))
    square_root(number)
