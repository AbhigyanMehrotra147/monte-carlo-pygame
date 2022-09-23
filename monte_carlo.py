import math
import random
import numpy as np


def monte_carlo(t: int, Lambda: int, N: int, beer_price: int) -> tuple:

    """
    :param t: total number of customers that come
    :param Lambda: intensity of possion distribution
    :param N: number of iterations for the program
    :param beer_price: price of 1 beer
    :return: the probabilty of getting the beer and relative error.
    :note:
    """
    beer = np.zeros((N, 1))                                                 # Initialising an empty matrix of zeros

    for i in range(0, N):

        n = np.random.poisson( Lambda * t )                                 # using numpy to generate random poisson val

        coins = []                                                          # initialising with empty array

        if n != 0:

            coins = np.zeros((n, 1))                                        # making it a numpy array

            for j in range(0, n):

                U = random.uniform(0, 1)                                    # random values between 0 & 1

                coins[j, 0] = (U <= 2 / 5) * 5 + (2 / 5 < U <= 4 / 5) * 10 + (U > 4 / 5) * 20
                # updating the (j, 0) entry of the array

        beer[i, 0] = (np.sum(coins) >= beer_price)                          # the sum of coins

    l_hat = np.mean(beer)                                                   # mean number of times, is able to buy beer
    reErr_hat = np.std(beer) / (math.sqrt(N) * l_hat)                       # the relative error of mean

    return l_hat


def main():
    t = 3
    Lambda = 5
    N = 10 ** 6
    beer_price = 350

    l_hat, relErr_hat = monte_carlo(t, Lambda, N, beer_price)
    print("l_hat = ", l_hat)
    print("relErr_hat = ", relErr_hat)


if __name__ == "__main__":

    main()

