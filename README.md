# Cato Networks GraphQL API CLI

The package provides a simple to use CLI that reflects industry standards (such as the AWS cli), and enables customers to manage Cato Networks configurations and processes via the [Cato Networks GraphQL API](https://api.catonetworks.com/api/v1/graphql2) easily integrating into configurations management, orchestration or automation frameworks to support the DevOps model.

## Installation
    pip3 install cato

## Authentication - Setting up the required environment variables:
Set [environment variables](https://en.wikipedia.org/wiki/Environment_variable) to configure a token for authentication, and the specific hub endpoint, example:  

	export CATO_TOKEN="12345-abcde"  
    export CATO_HOST="12345-abcde" (defaults to https://api.catonetworks.com/api/v1/graphql2, add this environment variable for developoment purposes to specify alternative cato host)  
    export CATO_DEBUG=True (Optional to see cli debug logs in terminal output) 
	
[CLICK HERE](https://support.catonetworks.com/hc/en-us/articles/4413280536081-Generating-API-Keys-for-the-Cato-API) to see how create an API key to authenticate.

## Running the CLI
	cato -h
	cato query -h
	cato query entityLookup -h
	cato query entityLookup 10454 '{"type":"country"}`

## Check out run locally not as pip package
	git clone git@github.com:Cato-Networks/cato-cli.git
	cd cato-cli
	python3 -m cato -h

This CLI is a Python 3 application and has been tested with Python 3.6 -> 3.8
## Requirements:
    python 3.6 or higher
    
## Confirm your version of python if installed:
    Open a terminal
    Enter: python -V or python3 -V

## Usage:
    usage: cato <resource> <command> [options]

    CLI for query, and mutation operations via API.

    positional arguments:
      {entityLookup}
		entityLookup         entityLookup reference.

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit

## Installing the correct version for environment:
https://www.python.org/downloads/

