import numericalDeriv

h = .01
x = 0

def f(x):
    f = 49*x**6 + 48*x**5 + 3*x**4 + 39*x**2 +23*x + 35
    return f

def forwardF(f, x, h):
    hand_x = 294*x**5 + 240*x**4 + 14*x**3 + 78**x
    forward_x = numericalDeriv.forwardDiff(f, x, h)
    return f, hand_x, forward_x

f, hand_x, forward_x = forwardF(f, x, h)

print(f, " ", hand_x, " ", forward_x)