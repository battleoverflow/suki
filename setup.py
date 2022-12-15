"""
    Owner: Hifumi1337 (https://github.com/hifumi1337)
    Project: Suki
    License: BSD 2-Clause
"""

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "suki",
    version = "0.0.5",
    author = "Hifumi1337",
    description = "Suki is a Python package manager created to make file organization more easily accessible",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/hifumi1337/suki",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    packages = [
        "suki"
    ],
    install_requires=[
        "argparse",
        "faye"
    ],
    scripts=["suki/suki.py"],
    entry_points={
        'console_scripts': ["suki=suki.suki:Suki.main"]
    },
    python_requires = ">=3.6"
)