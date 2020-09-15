import pandas as pd
import os


def create_csv(ping, upload, download):
    """Collect the results, tabulate it and will create a csv file

    Parameters:
    The parameter in the table are Ping, Upload and Download

    Returns:
    It will return the value from the arguments provided and create a csv file of the results in a tabular form

   """
    data = {'Ping': [ping],
            'Upload': [upload],
            'Download': [download]}

    table = pd.DataFrame(data, columns=['Ping', 'Upload', 'Download'])

    if not os.path.exists(r'C:\Users\benai\Documents\internet-connection-forecaster\Parameter.csv'):
        table.to_csv(
            r'C:\Users\benai\Documents\internet-connection-forecaster\Parameter.csv', index=False, header=True)
    else:
        table.to_csv(r'C:\Users\benai\Documents\internet-connection-forecaster\Parameter.csv',
                     index=False, mode='a', header=False)


create_csv(10, 10, 19)
