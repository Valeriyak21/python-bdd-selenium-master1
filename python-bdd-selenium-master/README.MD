
##  cucumber-python is a framework for API/UI testing using cucumber framework

## Pre-requisites
1. Latest version of python https://www.python.org/downloads/
2. Code Editor such as VSCode https://code.visualstudio.com/

## Virtual Environment Setup
1. Run `pip install virtualenv`
2. Run `python -m venv venv/your_env`
3. Activate the virtual environment : `.\your_venv\Scripts\activate`
> To deactivate simply run `deactivate`
4. Replace `config.example.ini` with your modified `config.ini`

## Requirements Setup
After the virtual environment has been setup;
1. Run `pip install -r requirements.txt` This should download and add all dependencies from requirements.txt file.

## Run cases
1. Run `behave --no-capture filename.feature` or `behave --no-capture --tags=@<tagName> filename.feature`
2. Run `behave -f plain --no-capture filename.feature` to print logs from print statements.
3. Run `behave -f plain --no-capture --tags=@<tagName> filename.feature` to print logs and run specific tests by providing tag.
