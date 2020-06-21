import setuptools

install_requires = [
    'pandas',
    'numpy',
]

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="actr-ms", # Replace with your own username
    version="0.0.1",
    author="Sebastian Blum",
    author_email="sebast.blum@gmail.com",
    description="Enable mental simulation of multiple cognitive models within the Cognitive Architecture ACT-R",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seblum/actcv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)