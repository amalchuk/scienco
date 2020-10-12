#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from setuptools import setup

setup(
    name="scienco",
    version="0.2.0",
    author="Andrew Malchuk",
    author_email="andrew.malchuk@yandex.ru",
    description="Calculate the readability of text using one of a variety of computed indexes",
    long_description=Path(__file__).with_name("README.md").read_text("utf-8"),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/amalchuk/scienco",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Natural Language :: Russian",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Text Processing :: Indexing",
        "Typing :: Typed"
    ],
    project_urls={
        "Documentation": "https://scienco.readable.pw",
        "Source": "https://gitlab.com/amalchuk/scienco"
    },
    python_requires=">=3.6, <4.0",
    packages=["scienco", "scienco.indexes", "scienco.metrics"],
    package_data={
        "scienco": ["py.typed"]
    },
    include_package_data=True,
    zip_safe=False
)
