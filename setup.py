#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["Click>=7.0"]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="João Vitor F. Cavalcante",
    author_email="jvfecav@gmail.com",
    python_requires=">=3.7",
    install_requires=requirements,
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    name="ardigen_test",
    packages=find_packages(include=["ardigen", "ardigen.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/jvfe/ardigen_test",
    version="0.1.0",
    zip_safe=False,
)
