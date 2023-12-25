def square_root(number):
    guess = 1.0

    while (guess * guess) < number:
        guess += 0.00000001

        if abs(guess * guess - number) < 0.0001:  
            print(f'The square root of {number} is approximately {guess}')
            return
        
    print(f'The number {number} does not have a perfect square root')

if __name__ == '__main__':
    number = float(input("What is the number to find the square root? "))
    square_root(number)
