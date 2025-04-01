"""
solution for computing the number of alive rabbits after n months while
also keeping in mind that rabbits die after m months.

the months before any rabbits start dying off, i.e. when n ≤ m can be described
by the recurrence relation of the Fibonacci numbers. The months after this,
i.e. when n > m, can be described by the following formula:
Fn = Fn-1 + Fn-2 - Fn-(m+1)
"""
n = 6
m = 3
bunnies = [1, 1]
months = 2
while months < n:
    if months < m:
        bunnies.append(bunnies[-2] + bunnies[-1])
    elif months == m:
        bunnies.append(bunnies[-2] + bunnies[-1] - 1)
    else:
        bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(
            m + 1)])
    months += 1
print(bunnies[-1])
