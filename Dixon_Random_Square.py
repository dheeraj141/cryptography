import numpy as np

import math

def factors(n, factor_base, result):
    """Factors the numbers and returns the factors of the number
    and also whether it is divisable over the factor ase or not"""

    factors = np.zeros(len(factor_base), dtype = np.int32)
    if (n <0):
        factors[0] = 1
        n = -n
    if(n <=1):
        return 0,0
    for i in factor_base[1:]:
        if (n%i == 0):
            index =  np.where(factor_base == i)
            while(n%i ==0):
                n = n//i
                factors[index]+=1

    if(n != 1 ):
        return 0, 0
    else :
        for i in factors:
            result+=str(i)
        return 1, result

def square_and_multiply(y,a, n):
    """ calculating the exponentiation of a number modulo p
    y^a mod n  """
    x = bin(a)
    x = x[2:]
    result = 1
    for i in range(len(x)):
        result = (result*result)%n
        if x[i] is '1':
            result = (result*y)%n
    return result



def xor_strings(x1, x2):
    flag =  1
    for i in range(len(x1)):
        temp =  (int(x1[i])%2) ^ (int(x2[i])%2)
        if (temp == 1):
            flag = 0
            break
    return flag


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)


def check_perfect_square(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            flag =  xor_strings(l[i], l[j])
            if (flag):
                return i,j
    return 0,0


def calculate_number(s, factor_base):
    result =  1
    for i in range(len(s)):
        if s[i] != "0":
            result*= pow(factor_base[i], int(s[i])//2)
    return result


def add_string(x1,x2):
    result = ""
    for i in range(len(x1)):

        result+= str(int(x1[i]) + int(x2[i]))
    return result



def check_perfect_square1(number, number_factors, n, factor_base):
    x1,x2  = check_perfect_square(number_factors)
    if(x1 != x2):
        #LHS x1^2 * X2^2
        temp1 = (number[x1]*number[x2]%n)
        #RHS
        resulting_string = add_string(number_factors[x1], number_factors[x2])

        num  =  calculate_number(resulting_string, factor_base)
        factor1  = gcd(temp1+ num, n)
        if (factor1 >1 ):
            return factor1
        if (temp1-num != 0):
            factor2 = gcd(temp1 -num, n)
            if (factor2 >1):
                return factor2


def dixon_random_square(n):
    #breakpoint()
    factor_base =np.array([-1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31], dtype=np.int32)
    number_factors = []
    number = []

    temp =""
    i = 1
    while(len(number) < 15):
        x = math.floor(np.sqrt(i*n))
        # m = X^2
        m = square_and_multiply(x,2,n)
        divisable, temp = factors(m,factor_base,temp  )
        if (divisable!= 0):
            number.append(x)
            number_factors.append(temp)
        temp = ""
        # n = (X+1)^2
        x_square = square_and_multiply(x+1,2,n)
        divisable, temp = factors(x_square,factor_base,temp  )
        if (divisable!= 0):
            number.append(x+1)
            number_factors.append(temp)
        i+=1
    return number, number_factors





def main():
    n = 256961
    factor_base =np.array([-1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31], dtype=np.int32)
    number, number_factors = dixon_random_square(n)
    print(" The numbers factored over factor base are {}", number)
    x = check_perfect_square1(number, number_factors,n, factor_base)
    y = n//x
    print(" the factors of the number are {}  and {}".format(x,y))




if __name__ =="__main__":
    main()
