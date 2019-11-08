import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Fasta",  # ALBERTO AVILA GARCIA
    version="0.0.1",
    author="ALBERTO AVILA GARCIA",
    author_email="beto.avila_im@yahoo.com.mx",
    description="Class (named Fasta) to manipulate DNA sequences from .fasta files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
