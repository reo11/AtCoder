n = int(input())
a = list(map(int, input().split()))
student = []
for i in range(n):
    student.append([a[i], i+1])
student.sort(reverse=True)
num = [x[1] for x in student]
ans = list(map(str, num))

print("\n".join(ans))
