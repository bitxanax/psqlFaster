import os, sys, time
def main ():
	sudo_password, pg_password, dbname, username, table_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
	os.system('systemctl start postgresql.service')
	if table_name != "-":
		os.system('echo "{}" | sudo -s set PGPASSWORD = {} && psql -d {} -U {} -w -c "SELECT * FROM {}"'.format(sudo_password, pg_password, dbname, username, table_name))
	else:
		os.system('echo "{}" | sudo -s set PGPASSWORD = {} && psql -d {} -U {} -w'.format(sudo_password, pg_password, dbname, username))

if __name__ == "__main__":
	main()
