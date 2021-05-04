def extendedGCD(a, b):
    # find the great common divisor od a and b
    # a*xi + b*yi = ri
    if b == 0:
        return (1, 0, a)
    # a*x1 + b*y1 = a
    x1 = 1
    y1 = 0
    # a*x2 + b*y2 = b
    x2 = 0
    y2 = 1
    while b != 0:
        q = a / b
        # ri = r(i-2) % r(i-1)
        r = a % b
        a = b
        b = r
        # xi = x(i-2) - q*(i-1)
        x = x1 - q*x2
        x1 = x2
        x2 = x
        #yi = y(i-2) - q*y(i-1)
        y = y1 - q*y2
        y1 = y2
        y2 = y
    return (x1, y1, a)




def EX_GCD(a, b, arr):    # 扩展欧几里得
    if b == 0:
        arr[0] = 1
        arr[1] = 0
        return a
    g = EX_GCD(b, a % b, arr)
    t = arr[0]
    arr[0] = arr[1]
    arr[1] = t - int(a / b) * arr[1]
    return g


def ModReverse(a, n):    # ax=1(mod n) 求a模n的乘法逆x
    arr = [0, 1]
    gcd = EX_GCD(a, n, arr)
    if gcd == 1:
        return (arr[0] % n + n) % n
    else:
        return -1

'''
a = 21
b = 25
arr = [0,1]
print(a,'模',b,'的乘法逆：',ModReverse(a,b))
print(a,'和',b,'的最大公约数：',EX_GCD(a,b,arr))
print(arr[1],'×',b,'+',arr[0],'×',a,'= 1')
'''


def computeD(fn, e):
    # find d s.t.  e*d = 1 mod fn
    (x, y, r) = extendedGCD(fn, e)
    # y maybe < 0, so convert it
    if y < 0:
        return fn + y
    return y


def KeyGeneration(p, q, e):   # Euclidean extension algorithm
    n = p * q
    fn = (p-1)*(q-1)
    # d = computeD(fn, e)
    arr = [0, 1]
    gd = EX_GCD(fn, e, arr)
    if arr[1] < 0:
        d = arr[1] + fn
    else:
        d = arr[1]
    return d, n


# time：O(logN)
def pow_mod(a, b, c):
    ans = 1
    base = a % c
    if b == 0:
        return 1 % c
    while b != 0:
        if b % 2 != 0:
            ans = (ans * base) % c
        # b = b >> 1  # 右移一位，相当于除2
        b = b // 2
        base = (base * base) % c
    return ans

'''
p_r = int(input('please input a big prime number in the decimal system: \n'))
q_r = int(input('please input another big prime number in the decimal system: \n'))
e_r = int(input('please input e in the decimal system: \n'))
'''
p_r = 18443
q_r = 49891
e_r = 19

m_r = int(input('please input the ciphertext: \n'))
# m_r = 88455713

# tt = 70479679275221115227470416418414022368270835483295235263072905459788476483295235459788476663551792475206804459788476428313374475206804459788476425392137704796792458265677341524652483295235534149509425392137428313374425392137341524652458265677263072905483295235828509797341524652425392137475206804428313374483295235475206804459788476306220148
# c_r = tt % (p_r*q_r)

c_r = pow(m_r, e_r, p_r*q_r)
(d, n) = KeyGeneration(p_r, q_r, e_r)
print(d, divmod(e_r*d, (p_r-1)*(q_r-1)))
decode_m = pow_mod(c_r, d, n)
print("the plaintext is: " + str(decode_m))

print(divmod(3*4, 7))
