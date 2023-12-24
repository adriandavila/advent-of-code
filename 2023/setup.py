from setuptools import find_namespace_packages, setup

setup(
    name="aoc-2023",
    packages=find_namespace_packages(include=["2023", "2023/*"]),
)
