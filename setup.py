from setuptools import setup, find_packages

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="replace_accents",
    version="0.0.5",
    description="This package helps to replace accented characters with their corresponding non-accented ascii characters",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Rahul Madhani",
    author_email="madhani.rahul@gmail.com",
    packages=find_packages(),
    url="https://medium.com/@rahul.madhani/replace-accented-characters-in-python-pyspark-and-spark-sql-28844b6c783e",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    project_urls={
        "Documentation": "https://medium.com/@rahul.madhani/replace-accented-characters-in-python-pyspark-and-spark-sql-28844b6c783e",
        "Source": "https://github.com/madhanir/replace_accents",
    },
)
