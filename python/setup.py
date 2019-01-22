import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyquip",
    version="0.0.1",
    author="Chris Wessells",
    author_email="chris@wessells.me",
    description="Packaged the quip api as provided by Quip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chriswessells/quip-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)