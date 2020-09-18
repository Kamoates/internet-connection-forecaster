import time
import subprocess
from collections import defaultdict


def check_speed(duration, intervals):
    """Summary or Description of the Function

        Parameters:
        argument1 (int): Description of arg1

        Returns:
        int:Returning value
   """
    number_of_loops = duration//intervals
    speedtest_command = 'speedtest-cli --csv'

    # getting headers
    headers = subprocess.Popen('speedtest-cli --csv-header',
                               stdout=subprocess.PIPE).stdout.readline().rstrip().decode('UTF-8').split(',')

    # initialized dictionary
    result_dictionary = defaultdict(list)

    for _ in range(number_of_loops):
        print('Running ...')
        raw_result = subprocess.Popen(
            speedtest_command, stdout=subprocess.PIPE).stdout
        result = raw_result.readline().rstrip().decode('UTF-8').split(',')

        # add result to the dictionary
        for header, value in zip(headers, result):
            result_dictionary[header].append(value)

        print('Done!\n')

        time.sleep(intervals)

    return result_dictionary
