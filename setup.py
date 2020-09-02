#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="scienco",
    version="0.1.1b0",
    author="Andrew Malchuk",
    author_email="andrew.malchuk@yandex.ru",
    description="Calculate the readability of text using one of a variety of computed indexes",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/amalchuk/scienco",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
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
        "Topic :: Text Processing :: Indexing",
        "Typing :: Typed"
    ],
    packages=["scienco", "scienco.indexes"],
    package_data={
        "scienco": ["py.typed"]
    },
    extras_require={
        "dev": ["coverage", "isort", "mypy", "pytest"]
    },
    python_requires=">=3.6, <4.0",
    include_package_data=True,
    zip_safe=False
)
