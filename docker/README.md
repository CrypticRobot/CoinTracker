# Before You Run
1. `mkdir volumes/varlibmysql` to create a folder for your database.

# Run
1. `dev/`: Go to `dev` folder, then, run from terminal `./up.sh` will bootstarp a development server. Visit `http://localhost/hello` to see the hello echo. To kill the server simply `Ctrl-C`

2. `prod/`: Go to `prod` folder, then, run from terminal `./up.sh` will bootstarp a development server. Visit `http://localhost/hello` to see the hello echo. To kill the server simply `Ctrl-C`. ***WARNING*** Must change the `MYSQL_PASSWORD` value in the `docker-compose.yml` to a secret value before you run the `up.sh`.
