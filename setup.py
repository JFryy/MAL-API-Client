import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="malclient",
    version="0.1.5",
    author="James Fotherby",
    author_email="fotherby1@gmail.com",
    description=
    "A small client library for interfacing with MyAnimeList Rest API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fotherbyy/MAL-API-Client",
    install_requires=['requests'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
