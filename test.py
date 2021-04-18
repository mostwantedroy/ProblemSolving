def maker(m):
    def inner(n):
        return m * n
    return inner

f1 = maker(2)
print(f1.__dict__)