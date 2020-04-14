'''
{{cookiecutter.package_name}} - {{cookiecutter.project_description}}
'''

{% if cookiecutter.cli != "n" -%}
import click


@click.command()
{%- endif %}
def main():
    print("Hello, World!")


if __name__ == '__main__':
    main()
