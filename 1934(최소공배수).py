T = int(input())

def gcd(a, b):
    while b != 0:
        tmp = a%b
        a = b
        b = tmp
    return a
    
def lcm(a, b):
    return (a*b) // gcd(a, b)

for i in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))