from setuptools import setup, find_packages

setup(
    name="{{cookiecutter.project_slug}}",
    description="{{cookiecutter.project_description}}",
    author="Mark Smith",
    author_email="judy@judy.co.uk",
    
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        {% if cookiecutter.cli != "n" -%}
        "click      ~= 7.1",
        {%- endif %}
    ],
    extras_require={
        "dev": [
            "black",
            "pytest",
            "twine",
            "wheel",
        ]
    },
    {% if cookiecutter.cli != "n" -%}
    entry_points="""
        [console_scripts]
        {{cookiecutter.package_name}}={{cookiecutter.package_name}}:main
    """,
    {%- endif %}
)