
import elgamal_decryption as ed

def test_square_and_multiply():
    y = int(input("Enter the base "))
    a = int(input("Enter the power "))
    n = int(input("Enter the prime number "))
    result = ed.square_and_multiply(y,a,n)
    print(result)


def test_multiplicative_inverse():
    b = int(input("Enter b^-1  "))
    a = int(input("Enter a "))
    result = ed.multiplicative_inverse(b,a)
    if (result == 0):
        print(" the inverse does not exist")
    else :
        print(" a^-1 mod b is {}".format(result))


def test_decrypt_elgamal():

    y1 = int(input("Enter y1 "))
    y2 = int(input("Enter y2 "))
    p = int(input("Enter the prime number "))
    a = int(input("Enter the power "))

    result = ed.decrypt_elgamal(y1,y2,p,a)
    print(result)
    message = ed.convert_to_text(result)
    print(message)


def test_convert_to_text():
    y1 = int(input("Enter a number  "))
    result =  ed.convert_to_text(y1)
    print(" the corressponding text is {}".format(result))


def test_decrypt_text():
    ed.decrypt_text()



test_decrypt_elgamal()
#test_convert_to_text()
