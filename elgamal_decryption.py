import math

def return_binary(x):
    binary = bin(x)
    binary = binary[2:]
    return binary


def square_and_multiply(y,a, n):
    x = return_binary(a)
    result = 1
    for i in range(len(x)):
        result = (result*result)%n
        if x[i] is '1':
            result = (result*y)%n
    return result



def multiplicative_inverse(b,a):
    a0 = a
    b0 = b
    t0 = 0
    t = 1
    q = math.floor(a0/b0)
    r = a0 - q*b0
    while(r >0):
        temp = (t0 - q*t)%a
        t0 =  t
        t = temp
        a0 = b0
        b0 = r
        q = math.floor(a0/b0)
        r = a0 - q*b0
    if(b0 != 1):
        return 0;
    else :
        return t

def convert_to_text(n):
    result = ""
    while( n>0):
        temp = n%26
        n = int(n/26)
        result+=chr(65+ temp)
    result = result[::-1]
    return result

def decrypt_elgamal(y1,y2, p, a ):
    # the elgamal decryption formula is y2 *(y1^a)^-1 mod p
    # temp =  y1^a
    temp = square_and_multiply(y1,a,p)
    temp_inverse = multiplicative_inverse(temp, p)
    y2 = y2%p
    result =  (y2*temp_inverse)%p
    return convert_to_text(result)


def decrypt_text():
    breakpoint()
    fp =  open('cipher_text.txt','r')
    a = 7899
    p = 31847
    result = fp.read()

    temp  = result.split('\n')
    x1 = temp[0].split('.')
    l1 = len(x1)
    x2 = temp[1].split('.')
    l2 = len(x2)
    x3 = temp[2].split('.')
    l3 = len(x3)
    x4 = temp[3].split('.')
    l4 = len(x4)
    index1 =index2 = index3 =  index4 = 0
    cipher_text= ""
    while(index1 <l1 and index2 <l2 and index3 <l3 and index4 <l4 ):
        cipher_text+=x1[index1]+"."+ x2[index2]+"." +x3[index3]+"."+ x4[index4]+"."
        index1+=1
        index2+=1
        index3+=1
        index4+=1
    cipher_text+=x1[index1]+"."+ x2[index2]




    text = ""
    cipher_text = cipher_text.split('.')


    for i in range(len(cipher_text)-4):
        temp = cipher_text[i].split('  ')
        y1 = int(temp[0])
        y2 = int(temp[1])
        message = decrypt_elgamal(y1,y2, p,a)
        text += message
    print(text)
decrypt_text()
