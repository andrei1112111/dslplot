from setuptools import setup, find_packages


setup(
    name="dslplot",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "antlr4-python3-runtime>=4.13.1",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0"
    ],
    author="Tishkin Andrei",
    author_email="atishkin060705@gmail.com",
    description="DSL for drawing graphs",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/andrei1112111/dslplot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
)
