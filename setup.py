from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cloudblast-py",
    version="0.1.0",
    author="rlko",
    author_email="rlko@duck.com",
    description="An unofficial Python wrapper for the CloudBlast API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rlko/cloudblast-py",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    setup_requires=["setuptools>=68.0.0"],
    install_requires=[
        "requests>=2.31.0",
    ],
)
