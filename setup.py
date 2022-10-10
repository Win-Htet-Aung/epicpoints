import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "epicpoints",
    version = "0.1.0",
    author = "Win Htet Aung",
    author_email = "whaung1998@gmail.com",
    description = "About points",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Win-Htet-Aung/epicpoints",
    # project_urls = {
    #     "Bug Tracker": "package issues URL",
    # },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # package_dir = {"": "src"},
    packages = setuptools.find_packages(),
    python_requires = ">=3.10"
)