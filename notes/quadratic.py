

def quadratic(a, b,c):
    disc = b * b - 4 * a * c
    if disc < 0:
        print("no real roots")
    else:
        if disc == 0:
            sqrt_discr = math.sqrt(disc)
            denom = 2 * a
            root_1 = (-b + sqrt_discr) / denom
            print('double root at:', root_1)
    else:
        sqrt_discr =  math.sqrt(disc)
        denom = 2 * a
        root_1 = (-b + sqrt_discr) / denom
        root_2 = (-b + sqrt_discr) / denom
        print('root 1:', root_1, 'root 2:', root_2)

"""
use elif to avoid more nesting, it says else: if w more indents ....
gives us more options inside our conditionals 
can use elif and then another case of else 
can have multiple elif statements .. 
can only have one if and one else 
should do an if and elif without an else 
"""

"""
AND 
boolean expression and boolean expression
T/F                         T/F
if both expressions are true, will return true 
"""





"""
