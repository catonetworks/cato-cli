import setuptools
from catocli import __version__

# Read the README file for long description
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = (
        'The package provides a simple to use CLI that reflects industry standards (such as the AWS cli), '
        'and enables customers to manage Cato Networks configurations and processes via the [Cato Networks GraphQL API]'
        '(https://api.catonetworks.com/api/v1/graphql2) easily integrating into '
        'configurations management, orchestration or automation frameworks to support the DevOps model.'
    )

setuptools.setup(
    name='catocli',
    version=__version__,
    packages=setuptools.find_namespace_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "catocli=catocli.__main__:main"
        ]
    },
    install_requires=['urllib3', 'certifi', 'six'],
    package_data={
        'catocli': ['clisettings.json'],
        '': ['vendor/*'],
    },
    python_requires='>=3.6',
    url='https://github.com/Cato-Networks/cato-cli',
    author='Cato Networks',
    author_email='[email protected]',
    description="Cato Networks cli wrapper for the GraphQL API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ]
)
