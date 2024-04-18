# Backup MySQL with the mysqldump tool


Get a sample database from here: 

https://www.mysqltutorial.org/getting-started-with-mysql/mysql-sample-database/

It will create a database called `classicmodels` with some tables and sample data.


## Running MySQL

[Run MySQL Locally](./locally_installed_mysql.md)

[Run MySQL in Docker](./docker_mysql.md)


## Create/Restore from SQL file

**NOTE: In the SQL script from mysqltutorial a database named `classicmodels` is created.**

Read it into the database:

```bash
$ mysql -u username -p < <file_name.sql>
```

Alternatively, you can also do this from the MySQL prompt:

```bash
mysql> USE <database_name>;
mysql> source <file_name.sql>;
```


## Backup into sql file

To backup a MySQL database (data + schema) use mysqldump:

```bash
$ mysqldump -u <username> -p <database_name> > <file_name.sql>
```

Ignore tables by adding: 

```bash
$ mysqldump -u <username> -p <database_name> --ignore-table=<table_name> > <file_name.sql>
```


