# Python program to find simple interest
# for given principal amount, time and
# rate of interest.

def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (p * t * r)/100

    print('The Simple Interest is', si)
    return si


# Driver code
simple_interest(8, 6, 8)


# Python program to find Compound Interest
# for given principal amount, time and
# rate of interest.


def Compound_Interest(Principle, Time, Rate):
    Amount = Principle * (pow((1 + Rate / 100), Time))
    Compound_interest = Amount - Principle
    print("Compound Interest: %.2f" % Compound_interest)
    return Compound_interest


Compound_Interest(8, 6, 8)
