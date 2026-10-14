def score(init,n):
    return sorted(init,reverse=True)[:n]
m=[1,3,213,545,244]
print(score(m,0))