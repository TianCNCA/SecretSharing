<<<<<<< HEAD
import Primes
import Polynomials
=======
import string
import ShamirMath
>>>>>>> branch 'master' of https://Tian_Chen@bitbucket.org/Spartibartfast/comp4140shamir.git

def string_to_int(input_string):
    """
    convert a string to an integer by doing a 128 based addition
    we assume the input_string are all ascii characters
    """
    output_int = 0

    for c in input_string:
        output_int = output_int * 128 + ord(c)

    return output_int


def int_to_string(input_int):
    """
    convert a int into an integer by doing a 128 based division
    we assume the input are all ascii characters
    """
    if input_int < 0 :
        raise Exception("Error: integer can't be negative")

    output_string = ""

    while input_int > 0:
        i = input_int % 128
        input_int /= 128
        output_string += chr(i)

    return output_string[::-1]


def secret_int_to_points(secret_int, threshold, num_shares):
    """
    split a secret (integer) into multiple shares in the form of (x, y)
    this is done by sample a random polynomial f for which f(0) equals to the
    secret
    """
<<<<<<< HEAD
    #TODO check threshold against num_shares
    prime = Primes.get_large_enough_prime([secret_int, threshold])
=======
    #error checking on threshold???
    prime = ShamirMath.get_large_enough_prime([secret_int, threshold])
>>>>>>> branch 'master' of https://Tian_Chen@bitbucket.org/Spartibartfast/comp4140shamir.git

    if not prime:
        raise Exception("Error: secret too long")

    coefficients = ShamirMath.generate_random_polynomial(threshold - 1, secret_int, prime)
    points = ShamirMath.calculate_polynomial_points(coefficients, num_shares, prime)

    return points


def point_to_share_string(point):
    """
    convert a point (x, y) into a string tuple in the form of
    (index_string, share_string)
    """

    x, y = point
    index_string = int_to_string(x)
    share_string = int_to_string(y)

    return (index_string, share_string)


def share_string_to_point(share):
    """
    convert a share in the form of (index_string, share_string) to
    a point of form (x, y)
    """
    index_string = share[0]
    share_string = share[1]

    x = string_to_int(index_string)
    y = string_to_int(share_string)

    return (x, y)


def points_to_secret_int(points):
    """
    reconstruct a polynomial using given points
    then calculate the secret by f(0)
    this is done through lagrange interpolation
    """
    x_values, y_values = zip(*points)
<<<<<<< HEAD
    prime = Primes.get_large_enough_prime(y_values)
    free_coefficient = Polynomials.lagrange_interpolation(0, x_values, y_values, prime)
    secret_int = free_coefficient  # the secret_int is the free coefficient
=======
    prime = ShamirMath.get_large_enough_prime(y_values)
    free_coefficient = ShamirMath.lagrange_interpolation(0, x_values, y_values, prime)
    secret_int = free_coefficient  # the secret int is the free coefficient
>>>>>>> branch 'master' of https://Tian_Chen@bitbucket.org/Spartibartfast/comp4140shamir.git

    return secret_int


class ShamirScheme(object):
    def __init__(self):
        pass


    def split_secret(self, secret_string, num_shares, threshold):
        secret_int = string_to_int(secret_string)
        points = secret_int_to_points(secret_int, threshold, num_shares)
        shares = []

        for point in points:
            shares.append(point_to_share_string(point))

        return shares


    def recover_secret(self, shares):
        """
        Shares: A list of tuples of the form [(index, share), ...]
        Takes a list of shares as tuples and reconstructs the secret
        """
        points = []

        for share in shares:
            points.append(share_string_to_point(share))

        secret_int = points_to_secret_int(points)
        secret_string = int_to_string(secret_int)

        return secret_string
