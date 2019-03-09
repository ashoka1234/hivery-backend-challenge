"""
Please use this script to initialize and populate the person and company
mongodb collections
Usage:
python manage.py init --people resources/people.json --companies resources/companies.json
"""

import click
import logging
import json
from pathlib import Path

from challenge.db import connect, WriteAPI

LOG = logging.getLogger(__name__)


@click.group(help=__doc__)
@click.option('--config', '-c', help="Pass the configuration file to access the database",
              type=click.Path(exists=True))
@click.pass_context
def cli(ctx, config):
    """ Creates the database object from configuration file.
        Used to pass the database for other click functions.
    """
    ctx.obj = dict()
    ctx.obj['db'] = connect(cfg_file_path=config)

    if (Path(__file__).parent / 'resources/fruits.json').exists():
        with open( Path(__file__).parent / 'resources/fruits.json') as fd:
            ctx.obj['fruits'] = set(json.load(fd))
    else:
        ctx.obj['fruits'] = {"orange", "apple", "banana", "strawberry"}


@cli.command()
@click.option('--people', help="A json file containing a list of person documents",
              type=click.Path(exists=True))
@click.option('--companies', help="A json file containing a list of companies",
              type=click.Path(exists=True))
@click.pass_obj
def init(ctx, people, companies):
    """
    Initialize the database. Populate the database with people data and company data
    """

    write_db = WriteAPI(ctx['db'])
    write_db.init_db()

    if people:
        with open(people, 'r') as fd:
            people_ = json.load(fd)
        write_db.add_people(people_, ctx['fruits'])

    if companies:
        with open(companies, 'r') as fd:
            companies_ = json.load(fd)
        write_db.add_companies(companies_)


if __name__ == '__main__':
    cli()
