# 분할 정복 - 11444번 - 피보나치 수 6
## 행렬곱으로 피보나치 수 원리 공부하기!!
MOD = 1_000_000_007

def matrix_mult(A, B):
    # 행렬 곱셈 (mod 적용)
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
         (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
         (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]

def matrix_pow(matrix, n):
    # 행렬 제곱 (분할정복, O(log n))
    result = [[1, 0], [0, 1]]  # 단위 행렬
    base = matrix

    while n > 0:
        if n % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        n //= 2

    return result

def fibo(n):
    # 피보나치 수 계산 (행렬 제곱 활용)
    if n == 0:
        return 0
    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, n - 1)
    return result[0][0]

n = int(input().strip())
print(fibo(n))
