# Evernote Web Application UI Testing using Selenium with Python unittest framework
## Pre-requisites:
#### -Firefox browser
#### -Clone project
#### -Install required packages from requirement.txt

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
#### -Clone the repository
#### -Change current directory to clone repository location in local system
#### -Update test data: Valid, Invalid login credentials and notes in Evernote/TestDataUnittest.xlsx file (if only user wanted to try with new test data)
#### -Type following commands sequentially in commandline interface:
```
cd Evernote
pip install -r requirement.txt
python -m TestSuite
```
Once all test cases are exeuted successfull you can check console output from command line and html reports generated from Evernote/reports.

Upon succesful execution of test cases Console output should be similar to below:

![image](https://user-images.githubusercontent.com/105941762/169697436-4df68d18-a2da-443f-8229-2f6214399017.png)


HTML generated test report should display similar to below:

![image](https://user-images.githubusercontent.com/105941762/169696656-84b13dff-86d9-42dd-be59-f9017534be91.png)

## How to import Jenkins job to build and execute automation tests?
## Pre-requisites:
#### -ShiningPanda Jenkins plugin

### To Import Evernote build job:

#### -Open Jenkins
#### -Navigate to Dashboard
#### -Click on Manage Jenkins
#### -Click on Jenkins CLI under tools and Actions
#### -Download jenkins-cli.jar
#### -Open command line and navigate to jenkins-cli.jar download location
#### -Copy and paste the Evernote_JenkinsBuildJobExport.xml to the same location as jenkins-cli.jar
#### -execute below command after replacaing as per below:
Replace **http://server** with your jenkin server address in below command.
Replace **username:password** with your jenkins username and password in below command.
```
java -jar jenkins-cli.jar -s http://server -auth username:password create-job NewjobName < Evernote_JenkinsBuildJobExport.xml
```

Once job is imported successfully.
Open Jenkins and verify the created Newjob
![image](https://user-images.githubusercontent.com/105941762/169698049-990c8c29-2f68-4a2c-a740-e96c75deea5f.png)

open job and click on configure
#### Naviagte to Source Code Management -> GIT -> Repositories -> Credentials
#### select user jenkins credentials from dropdown
#### Build -> Custom Python Builder -> Home
#### Change directory path to you local machine python installation directory

Save job and Click on Build Now
upon successful completion: compile output should look like below:

![image](https://user-images.githubusercontent.com/105941762/169697043-4f16f990-fb70-40ce-8029-3f6652b42087.png)
