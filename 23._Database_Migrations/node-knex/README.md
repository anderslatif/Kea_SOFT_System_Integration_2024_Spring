# Knex.js

## Installation

https://knexjs.org/guide/#node-js

Install Knex.js locally:

```bash
$ npm install knex
```

Install the database driver (e.g. for MySQL):

```bash
$ npm install mysql2
```

## Configuration

Install Knex.js globally:

```bash
$ npm install -g knex
```

Initialize the project as a Knex project:

```bash
$ knex init
```

Update the `knexfile.js` with the database connection information. Example for mysql: 
https://knexjs.org/guide/#configuration-options


## Migrations

https://knexjs.org/guide/migrations.html#migration-cli

Make a new migration file (timestamps will be added to the start of the files to keep their orders intact):

```bash
$ knex migrate:make name
```

Run all migrations:

```bash
$ knex migrate:latest
```


## Seed

https://knexjs.org/guide/migrations.html#seed-files

Create a new seed file (recommend to start with a number to keep the order of the seed files):

```bash
$ knex seed:make seed_name
```

Run all seed files (runs in alphabetic order of file names):

```bash
$ knex seed:run
```