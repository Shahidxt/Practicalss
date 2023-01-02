
# S.I = (1000 × 5 × 2)/100 = 100

def SimpleInterest():
    rate = 2
    InitalA = 1000
    months = 5
    return (InitalA*months*rate) // 100


# Calculate:
# Total P+I (A)
# Using the formula A = P(1 + r/n)nt
# Principal (P): $
# 10,000.00
# Annual Rate (R): %
# 3.875
# Compound (n):	Compounding
# Monthly
# Time (t in years):
# ex. 1.5 yr = 18 mo
# 7.5

def CompundInterest():
    rate = 18
    InitalA = 5000
    time = 2
    return InitalA*((1+rate/100)**time-1)


print(SimpleInterest())
