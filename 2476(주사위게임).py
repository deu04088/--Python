N = int(input())
m_list = []

for i in range(N):
    A, B, C = map(int, input().split())
    if A == B and B == C:
        m_list.append(10000 + A * 1000)
    elif A == B or A == C:
        m_list.append(1000 + A * 100)
    elif B == C:
        m_list.append(1000 + B * 100)
    else:
        m_list.append(max(A, B, C) * 100)
        
print(max(m_list))