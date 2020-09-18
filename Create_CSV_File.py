import os
try:
    import pandas as pd
except ModuleNotFoundError:
    os.system('python -m pip install pandas')
    import padas as pd


def create_csv(data, file_name):
    """Collect the results, tabulate it and will create a csv file

    Parameters:
    The parameter in the table are Ping, Upload and Download

    Returns:
    It will return the value from the arguments provided and create a csv file of the results in a tabular form

   """
    table = pd.DataFrame(data=data)
    path = f'data/{file_name}'

    if not os.path.exists(path):
        table.to_csv(path, index=False)
    else:
        table.to_csv(path, index=False, mode='a', header=False)
