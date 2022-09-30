
import math
import random
import numpy as np
import copy

class Poison():

    def __init__( self, t: int = 3, Lambda: int = 5, N: int = 10 ** 5, beer_price: int = 350):
        self._t = t                                                                                 # the number of hours he works in one day
        self._Lambda = Lambda                                                                       # The expected number of people in one hour
        self._N = N                                                                                 # The upper limit on the cur_index
        self._beer_price = beer_price                                                               # the price of the beer

        # the current running index / day
        self._cur_index = 0

        # list that contains the 0s and 1s
        self._beer_list = np.array( [], dtype=int )

    def update( self ):
        # a new day, a fresh calculation to store in self._beer_list
        n = np.random.poisson( self._Lambda * self._t )                                             # using numpy to generate random poisson val

        coins = []                                                                                  # initialising with empty array

        if n != 0:

            coins = np.zeros((n, 1))                                                                # making it a numpy array

            for j in range(0, n):

                U = random.uniform(0, 1)                                                            # random values between 0 & 1

                coins[ j, 0 ] = ( U <= 2 / 5 ) * 5 + ( 2 / 5 < U <= 4 / 5 ) * 10 + ( U > 4 / 5 ) * 20   # short hand condition
                # updating the (j, 0) entry of the array

        # print( self._cur_index )
        # appending the new beer got or not got inside the beer list
        self._beer_list = np.append( self._beer_list, int( np.sum( coins ) >= self._beer_price ) )  # the sum of coins vs the price, happy sad

        # updating the cur index to next day
        self._cur_index += 1

    def get_list( self, from_index: int = 0, to_index: int = None ):
        """
        returns the self._beer_list
        """
        if( to_index is None ):
            to_index = self._cur_index

        print( 'accessing sliced copy of private variable: self._beer_list!, from index, ', from_index, 'to ', to_index )

        # an effective way to make sure no changes to inner things
        return copy.deepcopy( self._beer_list[ from_index : to_index + 1 ] )

    def get_cur_index( self ):
        """
        returns the current running index
        """
        return copy.deepcopy( self._cur_index )

    def get_mean_array( self ):
        return self._beer_list.mean()

def main():
    """
    go to the lower most if statement in global scope, if this seems out of place
    """
    t = 3
    Lambda = 5
    N = 10 ** 6
    beer_price = 120

    pois = Poison( t=t, Lambda=Lambda, N=N, beer_price=beer_price )

    till = 10**3

    # run till 10**3 entries, rendering self._N useless in this case
    while( pois.get_cur_index() < till ):
        pois.update()
        # print( pois.get_list() )

        print( pois.get_mean_array() )

if __name__ == "__main__":
    main()

