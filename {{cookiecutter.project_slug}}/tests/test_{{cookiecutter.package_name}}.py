{% if cookiecutter.cli != "n" -%}
from click.testing import CliRunner

{% endif -%}
import {{cookiecutter.package_name}}

{% if cookiecutter.cli != "n" -%}
def test_main():
    runner = CliRunner()
    result = runner.invoke({{cookiecutter.package_name}}.main)
    assert result.exit_code == 0
{%- else %}
def test_main():
    assert {{cookiecutter.package_name}}.main() is None
{%- endif %}
