# MUTUALLY EXCLUSIVE OUTCOMES
# "error handling"
# one catches (catch) an error or it throws an exception ....
# value error is a datatype, like circle obj, live in classes ...
# try:
#     except:

def quadratic():
    try:
        a, b, c = eval(input('enter coefficients: '))
        disc = b * b - 4 * a * c
        sqrt_disc = math.sqrt(disc)
        denom = 2 * a
        root_1 = (-b + sqrt_disc) / denom
        root_2 = (-b + sqrt_disc) / denom
        print('root 1:', root_1, 'root 2:', root_2)
    # except:
    #         print('no real roots')