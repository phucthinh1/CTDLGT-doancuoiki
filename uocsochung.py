def uscln(a,b):
    if (b == 0):
        return a
    return uscln(b,a % b)
if __name__ =='__main__':
    a = int(input("nhập a = "))
    b = int(input("nhập b = "))
    print("ước số chung lớn nhất của", a, "và", b, "là : ",uscln(a,b))
