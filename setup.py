import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ostorlab",
    version="0.0.0",
    author="Amine LEMAIZI",
    author_email="contact@lemaizi.com",
    description="A personal machine learning library made for experimental purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aminelemaizi/ostorlab",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
    ],
    python_requires='>=3.6',
)
