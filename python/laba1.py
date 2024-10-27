import math

def solve(a, b, c):
    D = b ** 2 - 4 * a * c
    if(D < 0): #check frist sqrt
        return None
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    
    roots = []
    
    if x1 >= 0: #roots of биквадратное
        roots.append(math.sqrt(x1))
        roots.append(-math.sqrt(x1))
    
    if x2 >= 0:
        roots.append(math.sqrt(x2))
        roots.append(-math.sqrt(x2))
    
    if len(roots) == 0:
        return None  
    
    return roots

def main():
    while(True):
        try:
            coef = list(map(float, input().split())) #разбиение ввода
            break
        except ValueError:
            print("Error")
    a = coef[0] #coefs
    b = coef[1]
    c = coef[2]
    result = solve(a, b, c)
    if result is None:
        print(None)
    else:
        print(result)

main()
