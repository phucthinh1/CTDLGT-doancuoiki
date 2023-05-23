def PART(m,n):
    if (m==0):
        return 1
    if (n==0):
        return 0
    else:
        if (m<n):
            return (PART(m,m))
        else:
            return (PART(m,n-1)+PART(m-n,n))

if __name__ =='__main__':
    m = int(input("số phần thưởng là = "))
    n = int(input("số học sinh là = "))
    print("với", m,"phần thưởng thì chia có số cách chia là",PART(m,n))