import click


@click.command()
@click.option('-p', '--params', nargs=2, type=float)
def set_params(params):
    """
    This function gets the duration and intervals from the command line

        Parameters:
        params (dict:float): the number of intervals

        Returns:
        null:Returning value

    """
    click.echo(f'Parameters: {params}')
