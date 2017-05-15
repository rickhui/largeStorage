import os
import fnmatch
import cx_Oracle
from configparser import ConfigParser

def extractFile(files):
	strFiles = str(files)
	print("strFiles:" + strFiles)
	strFiles.replace("\r", "")
	print("strFiles:" + strFiles)
	return strFiles.split(",")

def findOne(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def findPattern(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def main():
	parser = ConfigParser()
	parser.read('config.ini')
	
	path = parser.get('Setting', 'dirPath')
	print(parser.get('Bond Forward', 'dataschema1'))
	print(extractFile(parser.get('Bond Forward', 'dataschema1')))
	# print(find("config.ini", path))

	# Database part
	connection = cx_Oracle.connect('sde/sde@orcl')
	cursor = connection.cursor()
	querystring = "sqlldr xxxx"
	files = extractFile(parser.get('Bond Forward', 'dataschema1'))
	for file in files:



if __name__ == '__main__': main()






