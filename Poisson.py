
import math
import random
import numpy as np
import copy

class Poison():

    def __init__( self, t: int = 3, Lambda: int = 5, N: int = 10 ** 5, beer_price: int = 350):
        self._t = t
        self._Lambda = Lambda
        self._N = N
        self._beer_price = beer_price

        # the current running index / day
        self._cur_index = 0

    def update( self ):

        n = np.random.poisson( self._Lambda * self._t )                                     # using numpy to generate random poisson val

        coins = []                                                                          # initialising with empty array

        if n != 0:

            coins = np.zeros((n, 1))                                                        # making it a numpy array

            for j in range(0, n):

                U = random.uniform(0, 1)                                                    # random values between 0 & 1

                coins[ j, 0 ] = ( U <= 2 / 5 ) * 5 + ( 2 / 5 < U <= 4 / 5 ) * 10 + ( U > 4 / 5 ) * 20
                # updating the (j, 0) entry of the array

        self._beer_list[ self._cur_index, 0 ] = int( np.sum(coins) >= self._beer_price )    # the sum of coins

        self._cur_index += 1
    
    def get_list( from_index: int = 0, to_index: int = None ):
        if( to is None ):
            to = self._cur_index

        print( 'returning sliced copy of private variable: self._beer_list!')
        return self._beer_list[ from_index: ]

if __name__ == "__main__":

    main()

def monte_carlo(t: int, Lambda: int, N: int, beer_price: int) -> tuple:

    beer = np.zeros((N, 1))                                                 # Initialising an empty matrix of zeros

    for i in range(0, N):

        n = np.random.poisson( Lambda * t )                                 # using numpy to generate random poisson val

        coins = []                                                          # initialising with empty array

        if n != 0:

            coins = np.zeros((n, 1))                                        # making it a numpy array

            for j in range(0, n):

                U = random.uniform(0, 1)                                    # random values between 0 & 1

                coins[ j, 0 ] = ( U <= 2 / 5 ) * 5 + ( 2 / 5 < U <= 4 / 5 ) * 10 + ( U > 4 / 5 ) * 20
                # updating the (j, 0) entry of the array

        beer[ i, 0 ] = int( np.sum(coins) >= beer_price )                          # the sum of coins

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
