for num in range(1, 101):
    string = ''
    # ここから記述

    if (num % 3 == 0) and (num % 5 == 0):#3x5 = 15の倍数のとき
        string = 'FizzBuzz'
    elif (num % 3 == 0) and (num % 5 != 0):#3の倍数であり、5の倍数でないとき
        string = 'Fizz'
    elif (num % 3 != 0) and (num % 5 == 0):#5の倍数であり、3の倍数でないとき
        string = 'Buzz'
    else:
        string = num


    # ここまで記述

    print(string)