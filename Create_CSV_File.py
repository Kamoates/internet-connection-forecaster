import pandas as pd
import os


def create_csv(data, file_name):
    """Collect the results, tabulate it and will create a csv file

    Parameters:
    The parameter in the table are Ping, Upload and Download

    Returns:
    It will return the value from the arguments provided and create a csv file of the results in a tabular form

   """
    speedtest = {'Ping': [data['ping']],
                 'Upload': [data['upload']],
                 'Download': [data['download']]}  # <--- paremove lahat ng to

    # <--- papalit ng pd.DataFrame(data=data)
    table = pd.DataFrame(speedtest, columns=['Ping', 'Upload', 'Download'])

    name = '/' + file_name + '.csv'

    # <--- papalit ng path to
    if not os.path.exists(r'C:\Users\benai\Documents\internet-connection-forecaster' + name):
        table.to_csv(r'C:\Users\benai\Documents\internet-connection-forecaster' +
                     name, index=False, header=True)
    else:
        table.to_csv(r'C:\Users\benai\Documents\internet-connection-forecaster' +
                     name, index=False, mode='a', header=False)
