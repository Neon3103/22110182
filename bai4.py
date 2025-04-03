def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

while True:
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n < 0:
            print("Lỗi: Vui lòng nhập số nguyên không âm!")
        else:
            break
    except ValueError:
        print("Lỗi: Bạn phải nhập một số nguyên!")
        
print("Fibonacci thứ", n, "là", fibonacci(n))
