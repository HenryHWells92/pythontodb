# Facilitating easy connections to MySQL databases in Python:
# Henry Wells - adapted from other prior code from FTUSA's data team
# Last updated 15 July 2019

# importing necessary modules:

import sqlalchemy, pymysql, yaml, os, re, datetime, numpy, pandas as pd 
from sqlalchemy import create_engine, MetaData # use to create connection to DB
from sqlalchemy.ext.declarative import declarative_base # use to map Python classes to the DB's schema
from sqlalchemy.orm import sessionmaker, create_session, contains_eager, joinedload, relationship # create session
from sqlalchemy import Table # enables organizing of data frames in to mysql Tables

# Below: Function to access a .yml file with the user's database credentials and use them to create a connection to a database:
def set_sql_creds():
    allcreds = yaml.load(open(os.path.expanduser('~')+'\\creds.yml'))
    credstring = input("Specify your sql database here: ")
    creds = allcreds[credstring]
    engine = create_engine('mysql+pymysql://'+creds['user']+':'+creds['passwd']+'@'+creds['host']+'/'+
                           creds['db']+'?charset=utf8', echo=True)
    base = declarative_base(engine)
    metadata = MetaData(bind=engine)
    return [creds, engine, base, metadata, credstring]


""" Run the following commands to log into database using creds.yml file 
and store components of credentials (username, password, host, port, db name) to be used later: """
sqlcreds = set_sql_creds()
dbcreds = sqlcreds[0]
engine = sqlcreds[1]
base = sqlcreds[2]
metadata = sqlcreds[3]
dbname = sqlcreds[4]


# Below: Function to use to connect to FTUSA's MySQL databases, and read data from a table in the database to a pandas DataFrame:

def sql_to_dataframe(query):
    # Takes a raw SQL query in the form of a string, and returns a pandas dataframe.
    results = engine.execute(query).fetchall();
    df = pd.DataFrame(results);
    df.columns = results[0].keys();
    return df 

# Example call of sql_to_dataframe(), and calls of pymysql and sqlalchemy commands to connect to database:
# data = sql_to_dataframe("SELECT * from active_producer_list WHERE active_timeframe = 2018")
# Run a line similar to the above, then use commands such as data.head(20) or access data.shape or data.columns to see basic attributes of data frame


# Example line of code to write a pandas DataFrame to an existing table in a MySQL database:
# chlist.to_sql(name = 'active_producer_list', con = tcdcon.engine, if_exists = 'append', chunksize=500, index=False)

# 'chlist' in the above command denotes the DataFrame being written to the database
# 'name' argument specifies the table to write the data to (in the database)
# 'con' argument specifies database connection info (created above in this script from .yml file)
# 'if_exists = "append"' tells the .to_sql function to add the rows of data in the DataFrame chlist to the end of the table, if the table in
#       'name' arg already exists in the database (it is advised to only write data to tables that have been created already!)
# 'chunksize' argument tells the .to_sql function to batch upload data 500 rows at a time - this makes it easier to write larger data sets all in one command
# index = False simply tells the .to_sql function to not create a new index column when uploading the data to the table (one should already be specified in MySQL)
