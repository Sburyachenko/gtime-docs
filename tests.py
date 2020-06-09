


a = '3141592653589793238462643383279502884197169399375105820974944592'
b = '2718281828459045235360287471352662497757247093699959574966967627'


# a = '2345'
# b = '3456'

def mul(num1, num2):
    if len(num1) == 1:
        return int(num1)*int(num2)
    else:
        new_len = (len(num1) + 1) // 2
        print(new_len, len(num1[:new_len]))
        ac = mul(num1[:new_len], num2[:new_len])
        bd = mul(num1[new_len:], num2[new_len:])
        ad = mul(num1[:new_len], num2[new_len:])
        bc = mul(num1[new_len:], num2[:new_len])
        return ac * 10**(new_len*2) + (ad + bc) * 10**new_len + bd

print(mul(a, b))
print(int(a) * int(b))
