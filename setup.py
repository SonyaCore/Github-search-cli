from os import path
from setuptools import setup, find_packages

DIR = path.dirname(path.realpath(__file__))
NAME = "github-search-cli"
VERSION = "0.3" 
README = path.join(DIR, "README.md")
DESCRIPTION = "Github-search-cli"
LONG_DESCRIPTION = open(README, "r", encoding="utf-8").read()

setup(
        name=NAME, 
        version=VERSION,
        author="Sonya Core",
        author_email="sonyacore@protonmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['requests'],
    entry_points={
        "console_scripts": [
            "github = Github.__main__:main",
        ]
    },
        keywords=['python', 'github-rest','github-search-cli','github'],
        classifiers= [
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",  
            "Environment :: Console",
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            'Intended Audience :: System Administrators',
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Unix",
            "Operating System :: POSIX",
        ]
)