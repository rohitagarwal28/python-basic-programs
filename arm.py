def arm():
    num=int(input("enter the number"))
    sum=0
    while num>0:
        r=num%10
        sum=sum+r**3
        num=num//10
    print(sum)
arm()
