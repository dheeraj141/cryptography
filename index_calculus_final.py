import Dixon_Random_Square  as ds
import fieldmath as fp
import numpy as np

def factors(n, factor_base):
    """Factors the numbers and returns the factors of the number
    and also whether it is divisable over the factor ase or not"""


    divisors = np.zeros(len(factor_base), dtype = np.int64)
    for i in factor_base:
        if (n%i == 0):
            index =  np.where(factor_base == i)
            while(n%i ==0):
                n = n//i
                divisors[index]+=1

    if(n != 1 ):
        return 0, 0
    else :
        return 1, divisors



def calculate(beta,factor_base, primitive, prime, log_values):
    #log_values = np.array([1,4279788,37320, 6579816, 8808251, 36054, 8750564], dtype = np.int64)
    divisable = 0
    order = 59407
    result = 0;
    s =1
    while(s<(prime-2)):

        num1 = ds.square_and_multiply(primitive,s,prime)
        num1 = (num1*beta)%prime

        divisable, divisors = factors(num1,factor_base)
        if(divisable == 1):
            sum = 0
            for i in range(len(divisors )):
                sum = (sum + log_values[i]*divisors[i])%(prime-1)
            sum = (sum-s)%(prime-1)
            if(sum <order):
                return sum
        s+=1





def main():
    divisors = []
    number = []
    """making 25  equations for index calculus attacks computing the logarithms
    of the number base """
    factor_base =np.array([2,3,5,7], dtype=np.int64)
    primitive =2317547
    prime = 10930889
    count = 1
    while(len(divisors) < 4):
        num = ds.square_and_multiply(primitive,count,prime )

        divisable, temp = factors(num, factor_base)
        if(divisable ==1):
            divisors.append(temp)
            number.append(count)
        count+=1
    row = 4; column = len(factor_base)+1;
    mat = np.ones((row,column), dtype = np.int64)
    result = np.ones((row,column), dtype = np.int64)
    for i in range(row):
        for j in range(column-1):
            mat[i][j] = int(divisors[i][j])
    temp_array = np.ones ((row,1), dtype = np.int64)
    for i in range(row):
        temp_array[i] = int(number[i])

    mat[:, len(factor_base)] = np.transpose(temp_array)

    log_values = [26152, 6627, 26841, 8299]

    beta = int(input("enter the value of beta"))
    e1 = calculate(beta, factor_base, primitive, prime, log_values)
    print(" the value is {}".format(e1))






















if __name__ =="__main__":
    breakpoint()
    main()
