import pyspeedtest as st
import time

def check_speed(duration, intervals):
    """Summary or Description of the Function

        Parameters:
        argument1 (int): Description of arg1

        Returns:
        int:Returning value
   """
    number_of_loops = duration//intervals
    for _ in range(number_of_loops):
        
        time.sleep(intervals)

check_speed(5, 2)