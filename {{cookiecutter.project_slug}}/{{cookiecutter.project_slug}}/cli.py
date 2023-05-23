"""Console script for {{cookiecutter.project_slug}}."""

import sys

{% if cookiecutter.command_line_interface|lower == 'click' -%}
import click

@click.command()
def main():
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0

{% elif cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    # add args here
    return parser.parse_args()

def main():

    """Console script for {{cookiecutter.project_slug}}."""
    parser = argparse.ArgumentParser()
    return 0


{% else %}

def main():
    pass

{%- endif %}
if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
