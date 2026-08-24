import setuptools
from setuptools.command.install import install
from pathlib import Path
import re
import subprocess
import sys

version_source = Path(__file__).parent / 'catocli' / '__init__.py'
version_match = re.search(
    r'^__version__\s*=\s*["\']([^"\']+)["\']',
    version_source.read_text(encoding='utf-8'),
    re.MULTILINE,
)
if version_match is None:
    raise RuntimeError(f'Unable to find __version__ in {version_source}')
__version__ = version_match.group(1)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        # Run the post-install script
        try:
            subprocess.call([sys.executable, '-m', 'catocli.post_install'])
        except Exception as e:
            print(f"Note: Could not run post-install setup: {e}")
            print("To enable tab completion manually, run: python -m catocli.post_install")

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
    cmdclass={
        'install': PostInstallCommand,
    },
    install_requires=[
        'argcomplete>=3.1,<4',
        'certifi>=2024.8.30',
        'python-dateutil>=2.9.0.post0,<3',
        'six>=1.16,<2',
        'urllib3>=2.7.0,<3',
    ],
    package_data={
        'catocli': ['clisettings.json'],
    },
    python_requires='>=3.10',
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
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ]
)
