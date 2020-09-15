import speedtest as st
import time 

def speedtest (duration, interval):

    """Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value

   """
    number_of_loops = duration//interval
    print(number_of_loops)
    for _ in range(number_of_loops):
        print('okay')
        time.sleep(interval)

speedtest(10, 2)