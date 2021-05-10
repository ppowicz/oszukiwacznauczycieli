# Oszukiwacz nauczycieli

Original idea to fool your teachers when they ask you to show your notes.
  

## Setup

### Installation of vulcan-api

*Microsoft Visual C++ version 14.0 or higher is required for this step!*
You can use any of these command-line inputs to install the API:

````
$ pip install vulcan-api
````
````
$ python -m pip install vulcan-api
````
````
$ git clone https://github.com/kapi2289/vulcan-api.git
$ cd vulcan-api
$ python -m pip install .
````

### Creating and registering account
Step by step process can be found here:
1. https://vulcan-api.readthedocs.io/en/latest/getting-started/02-keystore.html
2. https://vulcan-api.readthedocs.io/en/latest/getting-started/03-account.html

Keystore and Account both need to be contained in files with respective names:
````
oszukiwacznauczycieli/
	...
	
	keystore.json
	account.json
	
	...
````

### Settings explained
````python
maxLines = 75 # max length of the file
maxRows = 100 # max length of the individual line
startDate = datetime.date(2020, 9, 1) # date from witch api starts fetching
endDate = datetime.date(2021, 5, 10) # date to witch api fetches
filePrefix = "matematyka" # file prefix (followed by date)
fileExtension = ".txt"
subjectName = "Matematyka" # subject name to look for in fetched data
````

### Running actual code
````
$ python main.py
````

## Product
Product of the program is multiple files, named as stated in settings section, in directory `notes/`.
````
notes/
	AAAA YYYY-MM-DD.txt
	BBBB YYYY-MM-DD.txt
	CCCC YYYY-MM-DD.txt
	DDDD YYYY-MM-DD.txt
````

All files are full of junk data to imitate corrupted files that you can then send to your teacher saying that his/her computer can't open these notes.