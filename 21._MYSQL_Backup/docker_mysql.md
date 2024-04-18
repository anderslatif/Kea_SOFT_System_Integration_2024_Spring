### Use Docker

To make the guide easier to copy-paste from the following decisions have been made:

1. The container will be named `mysql-container`

2. The MySQL user is `root` the password will be `password`.

Run MySQL from Docker (Since I am running MySQL locally which is using the default port (`3306`) I map the port to `3307` on the host machine):

```bash
$ docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=password -p 3307:3306 -d mysql:latest
```

Interact with MySQL:

```bash
$ docker exec -it mysql-container mysql -uroot -p
```

Read file into the database (unfortunately you have to define the password in the command). (Replace `path/to/your/file.sql`):


```bash
$ docker exec -i mysql-container mysql -uroot -ppassword < <path/to/your/file.sql>
```

**NOTE: In the SQL script from mysqltutorial a database named `classicmodels` is created.**


Run `mysqldump` from Docker. (Replace `database_name`, `file_name.sql`):

```bash
docker exec mysql-container mysqldump -uroot -ppassword <database_name> > <file_name.sql>
```
