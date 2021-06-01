profit_of_all = []

# Recursive function to
# return gcd of a and b
def __gcd(a, b):
    if (b > a):
        a,b = b,a
    

#--one simple loop for GCD 
    while(a%b != 0):
        x,a = a,b
        b = x%b

#--If one or both values are negative
    if(b < 0):
        b *= -1

    return b
    
# Calculating GCD of an array.
def find_Gcd(crr, n):
    result = crr[0];
    for i in range(1, n):
        result = __gcd(crr[i], result);
    return result;


def profitRatio(amountArr, timeTrr, n):
    i = 0;
    
    crr = [0] * n;
    for i in range(n):
        crr[i] = amountArr[i] * timeTrr[i];
    

    Share = find_Gcd(crr, n);
    
    for i in range(0,n):
        profit_of_all.append(int(crr[i]/Share))
    
    final_profit(profit_of_all,350000)

    
def final_profit(ratio_of_all,overall_profit):
    overall = 0
    for i in ratio_of_all:
        overall += i
        print(i,end=" ")
    for i in range(len(ratio_of_all)):
        profit = (ratio_of_all[i]/overall * overall_profit)
        ratio_of_all[i] = profit

    heena = 0
    ravindra = 0
    print()
    
    for i in range(0,8):
        heena += ratio_of_all[i]
    print("heena : ",heena)
        
    for i in range(8,9):
        ravindra += ratio_of_all[i]
    print("ravindra : ", ravindra)

amountArr = [300000, 200000,100000, 100000, 100000, 100000, 100000, 100000, 1700000];
timeTrr = [60, 30, 75, 75, 75, 62, 60, 59, 60]

n = len(amountArr)

profitRatio(amountArr, timeTrr, n)

