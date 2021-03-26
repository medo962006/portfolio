def sqrt(arg):
        for i in range(arg):
            if i **2 == arg:
                print('the square root of {} is {}'.format(arg , i))
                break
sqrt(int(input('input a number to square root it: ')))