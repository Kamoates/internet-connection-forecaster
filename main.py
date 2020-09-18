import os
from speedtest import check_speed
from Create_CSV_File import create_csv

try:
    import click
except ModuleNotFoundError:
    os.system('python -m pip install click')


@click.command()
@click.option('-p', '--params', nargs=3, help='Duration:FLOAT Interval:FLOAT filename:String')
def set_params(params):
    """
    Collect all parameters from the command line interface (CLI) then execute check_speed() and create_csv()

        Parameters:
        params (tuple): the number of duration and intervals, and the filename

        Returns:
        null: Returning value

    """
    # checking internet speed
    try:
        data = check_speed(int(params[0]), int(params[1]))
        filename = params[2] + '.csv'
    except ValueError as e:
        print(f'Error: {e}, please check your inputs!')
        return

    # saving data to csv
    print('saving to csv ...')
    create_csv(data, filename)
    print('DONE! :)')
