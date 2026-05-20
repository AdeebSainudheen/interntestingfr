try:
	import pymysql
	pymysql.install_as_MySQLdb()
except Exception:
	# pymysql is optional for local development when using SQLite
	pass
