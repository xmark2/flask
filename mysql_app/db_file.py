# https://www.w3schools.com/python/python_mysql_select.asp


# import mysql.connector
import pandas as pd
import sqlalchemy
from utils import os_util as u
import json
import os
import pprint

import bz2
import pickle
import _pickle as cPickle

import numpy as np


pp = pprint.PrettyPrinter(indent=4)

con = sqlalchemy.create_engine('mysql+pymysql://root:hello@localhost')

def show_dbs():
    cursor = con.execute('show DATABASES')
    dbs = cursor.fetchall()

    dbs = [db[0] for db in dbs]
    return dbs


def generate_db_model(dbs):
	db_model = {}
	for db in dbs:
		cursor = con.execute('show tables from '+db)
		tables = cursor.fetchall()
		tables = [x[0] for x in tables]
		db_model.update({db: tables})
	return db_model

def compressed_pickle(title, data):
	with bz2.BZ2File(title + '.pbz2', 'w') as f: 
		cPickle.dump(data, f)

def index_marks(nrows, chunk_size):
    return range(1 * chunk_size, (nrows // chunk_size + 1) * chunk_size, chunk_size)

def split(dfm, chunk_size):
    indices = index_marks(dfm.shape[0], chunk_size)
    return np.split(dfm, indices)

dbs = show_dbs()
db_model = generate_db_model(dbs)
# print(dbs)
# pp.pprint(db_model)

for db in dbs:
	tables = db_model[db]
	tables = [u.mkdir('data/'+db+'/'+x) for x in tables]


df = pd.read_sql("select * from INFORMATION_SCHEMA.columns", con)

df = df[['TABLE_SCHEMA','TABLE_NAME','COLUMN_NAME']]
df = df.loc[df['TABLE_SCHEMA'] == 'retail_db']

columns = df['COLUMN_NAME'].values.tolist()

field_matches = {}
for column in columns:
	indexes = []
	tables = []
	fields = []
	for index, row in df.iterrows():
		if column in row['COLUMN_NAME']:
			indexes.append(index)
			tables.append(row['TABLE_NAME'])
			fields.append(row['COLUMN_NAME'])
	dic = {'indexes':indexes,'tables':tables,'fields':fields}
	if len(indexes)>1:		
		field_matches.update({column:dic})

print(field_matches)

with open('data/fields.json','w') as json_file:
    json.dump(field_matches,json_file,indent=4, sort_keys=True)

# print(df.columns)

# columns = df.columns

# for col in columns:


# df.to_csv('data/columns.csv')
# compressed_pickle(file, columns)

# dbs = [dbs[3]]
# for db in dbs:
# 	print(db)
# 	tables = db_model[db]
# 	for table in tables:
# 		print(table)
# 		df = pd.read_sql('select * from '+db+'.'+table, con)
# 		print(df)
# 		# file = 'data/'+db+'/'+table+'/'
# 		# compressed_pickle(file, records)
# 		df_chunks = split(df, 1000)
# 		print('\n\n')
# 		print(df_chunks[0])
# 		print('\n\n')
# 		print(df_chunks[-1])
# 		break




# cursor = con.execute('show tables from '+db)
# tables = cursor.fetchall()


# tables = engine.fetchall()
# print(tables)

# df = pd.read_sql_table('categories', engine)
# print(df.head())

# pp.pprint(db_model)
# print(dbs[3])
# print(db_model[dbs[3]])


# mycursor = con.cursor()
# db = dbs[3]
# table = db_model[dbs[3]][0]
# mycursor.execute('select * from '+db+'.'+table)
# records = mycursor.fetchall()
# print(records)

# rootdir = 'data'
# for root, subdirs, files in os.walk(rootdir):
# 	print(root)
	# print('subdirs'+str(subdirs))
    # db_model.update({db: tables})
# with open('db_model.json','w') as json_file:
#     json.dump(db_model,json_file,indent=4, sort_keys=True)


