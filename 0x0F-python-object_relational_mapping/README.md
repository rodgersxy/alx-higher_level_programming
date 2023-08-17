# 0x0F. Python - Object-relational mapping

# Install MySQLdb module version 2.0.x

`$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
`
## if get an installation error 
`Fix it by installing pkg-config as follows:
$ sudo apt install pkg-config`

# Install SQLAlchemy module version 1.4.x
`$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'`

# To start MySQL
`
service mysql start
mysql -u root -p
`
