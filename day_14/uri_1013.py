def max_num(a, b):
    if a > b:
        return a
    return b

def abs(x):
    if x >= 0:
        return x
    return -x

inp = input()
inp = inp.split()
a, b, c = int(inp[0]), int(inp[1]), int(inp[2])

m_num = max_num(a, max_num(b, c))
# s_m = max_num(b, c) if m_num == a else max_num(
#     c, a) if m_num == b else max_num(a, b)

if m_num == a:
    s_m = max_num(b, c)
elif m_num == b:
    s_m = max_num(c, a)
else:
    s_m = max_num(a, b)   

res = (m_num + s_m + abs(m_num - s_m)) / 2 

print(f"{int(res)} eh o maior")
