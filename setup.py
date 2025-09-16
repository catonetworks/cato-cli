import setuptools
from catocli import __version__

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
    license='Apache-2.0 license',
    author='Cato Networks',
    author_email='[email protected]',
    description="Cato Networks cli wrapper for the GraphQL API.",
    long_description='The package provides a simple to use CLI that reflects industry standards (such as the AWS cli), '
                     'and enables customers to manage Cato Networks configurations and processes via the [Cato Networks GraphQL API]'
                     '(https://api.catonetworks.com/api/v1/graphql2) easily integrating into '
                     'configurations management, orchestration or automation frameworks to support the DevOps model.',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)
