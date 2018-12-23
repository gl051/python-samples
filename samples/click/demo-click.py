import click


# Multiple commands can be grouped
@click.group()
def cli():
    pass


@click.command()
@click.option('--schema', default=None, help='Redshift schema')
@click.argument('table')
def unload(schema, table):
    # TBD: get S3 from env variable.
    uri = schema + "." + table if schema else table
    print(f'Unloading from {uri} to S3 ...')


@click.command()
@click.option('--schema', default=None, help='Redshift schema')
@click.argument('table')
@click.argument('s3path')
def load(schema, table, s3path):
    uri = schema + "." + table if schema else table
    print(f'Loading {s3path} to {uri} ...')


cli.add_command(load)
cli.add_command(unload)

if __name__ == '__main__':
    cli()
    print('Done.')
