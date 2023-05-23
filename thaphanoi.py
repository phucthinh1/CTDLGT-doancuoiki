#thaphanoi
def towerofhanoi(n,source,destination,auxiliary):
    if n==1:
        print("chuyển đĩa 1 từ cột",source,"tới cột",destination)
        return
    towerofhanoi(n-1,source,auxiliary,destination)
    print("chuyển đĩa",n,"từ cột ",source,"tới cột",destination)
    towerofhanoi(n-1,auxiliary,destination,source)

if __name__ == '__main__':
    n = int(input("số đĩa : "))
    towerofhanoi(n,'A','B','C')