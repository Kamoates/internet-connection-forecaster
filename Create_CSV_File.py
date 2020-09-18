import pandas as pd
import os
path = os.getcwd()


def create_csv(data, file_name):
    """Collect the results, tabulate it and will create a csv file

    Parameters:
    The parameter in the table are Ping, Upload and Download

    Returns:
    It will return the value from the arguments provided and create a csv file of the results in a tabular form

   """
    try:

        table = pd.DataFrame({'Ping': [data['ping']], 'Upload': [data['upload']], 'Download': [
                             data['download']]}, columns=['Ping', 'Upload', 'Download'])

        name = '/' + file_name + '.csv'

        if not os.path.exists(path + name):
            table.to_csv(path + name, index=False, header=True)
        else:
            table.to_csv(path + name, index=False, mode='a', header=False)

    except ImportError:
        print('Please import pandas')
