from setuptools import setup, find_packages

setup(
    name="dominosim",
    version="0.1.0",
    description="Python level editing library for Kyowob's Domino Simulator",
    author="qaptivator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)