""" Flask project setup file. """

from setuptools import find_packages, setup

setup(
    name="flask-template",
    use_scm_version=True,
    description="Template for kickstarting flask projects.",
    packages=find_packages()
)