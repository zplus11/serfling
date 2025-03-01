import setuptools

setuptools.setup(
    name = "serfling",
    version = "1.0.0",
    author = "Naman Taggar",
    description = "Serfling model regression using matrix approach",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    install_required = ["numpy>=1.21.0"],
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">3.5"
)
