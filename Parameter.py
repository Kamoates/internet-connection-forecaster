import pandas as pd

"""Collect the results, tabulate it and will create a csv file

    Parameters:
    The parameter in the table are Duration, Ping, Upload and Download

    Returns:
    It will return the value from the arguments provided and create a csv file of the results in a tabular form

   """


def __init__(self, duration, ping, upload, download):
    self.duration = duration
    self.ping = ping
    self.upload = upload
    self.download = download


data = {'Duration': [self.duration],
        'Ping': [self.ping],
        'Upload': [self.upload],
        'Download': [self.download]}


Parameter = pd.DataFrame(
    data, columns=['Duration', 'Ping', 'Upload', 'Download'])
Parameter.to_csv('C:\Users\benai\Documents\internet-connection-forecaster')
