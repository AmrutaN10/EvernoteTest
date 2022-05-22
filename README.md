# Evernote Web APP UI Testing using Selenium with Python unittest framework
## Pre-requisites:
#### -Firefox browser
#### -Install required packages from requirement.txt

change current directory to clone repository location in local system and type following pip command to install required packages:
```
pip install -r requirement.txt
```
### Helper module:
It contains all common import libraries
### Locator module:
It contains all the web elements and their respective locations that are being used in UI testing
### Page Object module:
It contains all the web page classes contains web elements and action methods
### TestSuite script:
It contains all the 4 test scenarios source code in unittest module framework.
### reports module:
It contains html test execution results summary reports

## How to execute automation tests?
change current directory to clone repository location in local system and type following commands in commandline interface:
```
cd Evernote
python -m TestSuite
```
once test cases are exeuted successfull you can check console output from command line and html reports generated from Evernote/reports