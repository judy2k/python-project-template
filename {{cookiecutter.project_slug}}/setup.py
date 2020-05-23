from setuptools import setup, find_packages

EXTRAS_REQUIRE = {
    'tests': [
        "pytest",
        "coverage[toml]>=5.0.2",
    ],
}
EXTRAS_REQUIRE['dev'] = EXTRAS_REQUIRE['tests'] + [
    "black",
    "twine",
    "wheel",
]

setup(
    name="{{cookiecutter.project_slug}}",
    description="{{cookiecutter.project_description}}",
    version='0.0.0',
    author="Mark Smith",
    author_email="judy@judy.co.uk",
    
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        {% if cookiecutter.cli != "n" -%}
        "click      ~= 7.1",
        {%- endif %}
    ],
    extras_require=EXTRAS_REQUIRE,
    {% if cookiecutter.cli != "n" -%}
    entry_points="""
        [console_scripts]
        {{cookiecutter.package_name}}={{cookiecutter.package_name}}:main
    """,
    {%- endif %}
)