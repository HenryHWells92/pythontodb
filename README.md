# Facilitating easy connections to databases from the Python command line

I originally wrote this code in the course of my work building a MySQL data warehouse at Fair Trade USA, and wanted to save it aside for future generalized use. 

To use this package, the user must have a 'creds.yml' file in their home directory (usually C:/users/[name]) containing the appropriate credentials for accessing the database. These creds should take the following format:

[SQL db name]: 
host: [db host address] 
user: [username] 
passwd: [password] 
db: [SQL db name]

Once the .yml file exists with the users credentials stored in it, this package can be pip installed and imported into python notebooks easily, as follows:

In your terminal:

clone this repo to your computer: 
git clone [ssh link for this repo]

install this repo as a package locally: 
python -m pip install [file path for this repo on your local computer]

Then, open python and run the following, and use functions from the MySQL module by calling the prefix 
import pythontodb.connpytomysql as connpytomysql
connpytomysql.[desired function here]
