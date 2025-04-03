def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

n = int(input("Nhập số nguyên không âm n: "))
while n < 0:
    n=int(input("Vui lòng nhập một số nguyên không âm:"))
print(f"{n}! = {factorial_recursive(n)}")
