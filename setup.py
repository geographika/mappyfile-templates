import re
from setuptools import setup
from io import open

(__version__,) = re.findall(
    '__version__ = "(.*)"', open("mappyfile_templates/__init__.py").read()
)


def readme():
    with open("README.rst", "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="mappyfile-templates",
    version=__version__,
    description="A mappyfile plugin to update Mapfiles with templates",
    long_description=readme(),
    classifiers=[
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",  # minimum required due to use of annotations
        "Intended Audience :: Developers",
    ],
    url="https://github.com/geographika/mappyfile_templates",
    author="Seth Girvin",
    author_email="sethg@geographika.co.uk",
    license="MIT",
    packages=["mappyfile_templates"],
    install_requires=["mappyfile>=0.9", "pyyaml"],
    entry_points={"mappyfile.plugins": "mappyfile_templates = mappyfile_templates"},
    zip_safe=False,
)
