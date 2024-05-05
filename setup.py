from setuptools import setup, find_packages

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="replace_accents",
    version="0.0.4",
    description="This package helps to replace accented characters with their corresponding non-accented ascii characters",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Rahul Madhani",
    author_email="madhani.rahul@gmail.com",
    packages=find_packages(),
)
