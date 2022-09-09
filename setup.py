from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-sandstorm-support",
    description="Authentication and permissions for Datasette on Sandstorm",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-sandstorm-support",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-sandstorm-support/issues",
        "CI": "https://github.com/simonw/datasette-sandstorm-support/actions",
        "Changelog": "https://github.com/simonw/datasette-sandstorm-support/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["datasette_sandstorm_support"],
    entry_points={"datasette": ["sandstorm_support = datasette_sandstorm_support"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    python_requires=">=3.7",
)
