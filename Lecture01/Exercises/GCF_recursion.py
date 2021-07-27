# Euclidean algorithm
# https://zh.wikipedia.org/zh-cn/%E8%BC%BE%E8%BD%89%E7%9B%B8%E9%99%A4%E6%B3%95

def gcf(a,b):
    if b == 0:
        return a
    else:
        return gcf(b,a % b)

a=int(input())
b=int(input())
print(gcf(a,b))
