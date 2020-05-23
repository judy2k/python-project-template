'''
{{cookiecutter.package_name}} - {{cookiecutter.project_description}}
'''

{% if cookiecutter.cli != "n" -%}
import click
{%- endif %}


{% if cookiecutter.cli != "n" -%}
@click.command()
{%- endif %}
def main():
    print("Hello, World!")


if __name__ == '__main__':
    main()
