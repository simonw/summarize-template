from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="summarize-template",
    description="Show a summary of a Django or Jinja template",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/summarize-template",
    project_urls={
        "Issues": "https://github.com/simonw/summarize-template/issues",
        "CI": "https://github.com/simonw/summarize-template/actions",
        "Changelog": "https://github.com/simonw/summarize-template/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["summarize_template"],
    entry_points="""
        [console_scripts]
        summarize-template=summarize_template.cli:cli
    """,
    install_requires=["click"],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
