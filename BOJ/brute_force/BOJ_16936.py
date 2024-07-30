# 브루트 포스 - 16936번 - 나3곱2
## 배열이 주어지면 나3곱2의 결과 배열로 바꿔서 출력하기
## arr의 숫자 한개씩 가져옴 (i)
#       - 이전 숫자 : i//2 or i*3
#       - 다음 숫자 : i*2 or i//3

n = int(input())
arr = list(map(int, input().split()))
ans = []

ans.append(arr[0])
arr.pop(0)

while len(arr) != 0:
    input_num = arr[0]  # ans[0]의 앞 // ans[-1] 의 뒤 에만 올 수 있음
    if input_num * 2 == ans[0] or input_num == ans[0] * 3:
        arr.pop(0)
        ans.insert(0, input_num)
        # print("arr=", arr, "ans=", ans)
        continue
    if input_num * 3 == ans[-1] or input_num == ans[-1] * 2:
        arr.pop(0)
        ans.append(input_num)
        # print("arr=", arr, "ans=", ans)
        continue
    arr.pop(0)
    arr.append(input_num)
    # print("arr=", arr, "ans=", ans)

# print(ans)
for i in ans:
    print(i, end=" ")