import click


@click.command()
@click.option('-p', '--params', nargs=2, type=float)
def set_params(params):
    """
    This function gets the duration and intervals from the command line

        Parameters:
        params (tuple(float)): the number of duration and intervals

        Returns:
        null:Returning value

    """
    click.echo(f'Parameters: {params}')
