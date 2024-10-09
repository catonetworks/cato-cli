import setuptools
from cato import __version__

setuptools.setup(
    name='cato',
    version=__version__,
    packages=setuptools.find_namespace_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "cato=cato.__main__:main"
        ]
    },
    install_requires=['urllib3', 'certifi', 'six'],
    package_data={
        '': ['vendor/*'],
    },
    python_requires='>=3.6',
    url='https://github.com/banderson0421/cato-cli',
    license='Apache-2.0 license',
    author='Brian Anderson',
    author_email='brian.anderson@catonetworks.com',
    description="Cato Networks cli wrapper for the GraphQL API.",
    long_description='The package provides a simple to use CLI that reflects industry standards (such as the AWS cli), '
                     'and enables customers to manage Cato Networks configurations and processes via the [Cato Networks GraphQL API]'
                     '(https://api.catonetworks.com/api/v1/graphql2) easily integrating into '
                     'configurations management, orchestration or automation frameworks to support the DevOps model.',
    classifiers=[
        "License :: OSI Approved :: Apache-2.0 license",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)
