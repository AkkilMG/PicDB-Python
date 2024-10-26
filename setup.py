# (c) 2024 Akkil MG (https://github.com/AkKiLMG)

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="py-picdb",
    version="0.1.0",
    description="Command-line tool and library for PicDB API, which provides storage for images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Akkil MG",
    author_email="akkilcharanmg@gmail.com",
    url="https://github.com/AkkilMG/PicDB-Python",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "picdb=picdb.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
