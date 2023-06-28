'''Setup file for the Atlas Client'''
import os
import sys
from setuptools import setup, find_packages
description = 'The offical Nomic python client.'

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
    
setup(
    name='nomic',
    version='2.0.1',
    url='https://github.com/nomic-ai/nomic',
    description=description,
    long_description=long_description,
    packages=find_packages(),
    author_email="support@nomic.ai",
    author="nomic.ai",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "click",
        "jsonlines",
        "loguru",
        'rich',
        'requests',
        'numpy',
        'pandas',
        'pydantic',
        'wonderwords',
        'tqdm',
        'cohere',
        'pyarrow',
    ],
    extras_require={
        'dev': [
            'black',
            'coverage',
            "pylint",
            "pytest",
            "myst-parser",
            "mkdocs-material",
            "mkautodoc",
            "twine",
            "mkdocstrings[python]",
            "mkdocs-jupyter",
            "pillow",
            "cairosvg"
        ]

    },
    entry_points={
        'console_scripts': ['nomic=nomic.cli:cli'],
    },
    include_package_data=True
)
