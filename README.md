# macos-hostname-api
An option for no touch deployments of MacOS computers to automatically name themselves based on their assigned serial number. During the setup process, the machine will do an HTTP GET with their serial number, prompting the server to lookup their serial number and return it's corresponding hostname.

An example XLSX is in the source files. Most asset managing systems will allow a simple export of this data.

The hostname naming convention was primarily designed for educational environments, based on the logic of the script it will name computers based on the tab named in data.xlsx in the following way:

#### For student one to one devices: 

```<graduating year><first letter of first name><surname>```

 e.g 2020jbloggs
  
#### For staff machines

```<'staff'><first letter of first name><surname>```
  
#### For loan devices

``` <studentloan/staffloan><loan number> ```
  
Additional customized tabs can be added to the XLSX file to follow the format of

```<tab name><corresponding column b value>```
  

# Usage

#### JSS/MDM Set Up
Script to be placed before AD Binding (change the url to the IP Address of the server)
```
url="<server ip address>:8080"
serialNumber=$(ioreg -c IOPlatformExpertDevice -d 2 | awk -F\" '/IOPlatformSerialNumber/{print $(NF-1)}')
computerName=$(curl "$url/$serialNumber")
scutil --set ComputerName "$computerName"
scutil --set LocalHostName "$computerName"
scutil --set HostName "$computerName"
```

#### Server Setup 
This has been tested to run on Ubuntu, CentOS, Windows Server

1. git clone git@github.com:lrajca/macos-hostname-api.git and cd into the macos-hostname-api
2. python3 -m pip install flask, xlrd
3. python3 run.py

#### XLSX File management
The XLSX file will need to be updated locally once any changes are made to the online version, to do this (once the API is running), browse to the following:

``` <ip address of server:8080/update> ```

e.g 192.168.0.1:8080/update

The page should return a "Spreadsheet Updated"


Once up and running you can test by browsing to 

``` <ip address of server:8080/><serial number in spreadsheet>


### To do:

- [ ] Docker deployment of application, running nginx and gunicorn for additional workers
