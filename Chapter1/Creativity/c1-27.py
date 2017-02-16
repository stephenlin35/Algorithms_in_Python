
def factors(n):
    k = 1
    factor_storage = []
    while k * k < n:
        if n % k == 0:
            yield k
            factor_storage.append(n // k)
        k += 1
    if k * k == n:
        yield k
    factor_storage.reverse()
    for i in factor_storage:
        yield i

for i in factors(100):
    print(i)
        
