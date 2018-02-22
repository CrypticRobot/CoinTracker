# English 中文版在文末
## Before You Run
1. `mkdir volumes/varlibmysql` to create a folder for your database.

## Run
1. `dev/`: Go to `dev` folder, then, run from terminal `./up.sh` will bootstarp a development server. Visit `http://localhost/hello` to see the hello echo. To kill the server simply `Ctrl-C`

2. `prod/`: Go to `prod` folder, then, run from terminal `./up.sh` will bootstarp a development server. Visit `http://localhost/hello` to see the hello echo. To kill the server simply `Ctrl-C`. ***WARNING*** Must change the `MYSQL_PASSWORD` value in the `docker-compose.yml` to a secret value before you run the `up.sh`.

---

## 在运行之前
1. `mkdir volumes/varlibmysql` 本层运行，新建一个文件夹存放数据库

## 开发/运行
1. 开发`dev/`: `cd dev/` 进入dev文件夹, 运行 `./up.sh` 启动测试服务器. 测试网站会运行在 `localhost` 访问`http://localhost/hello` 看看服务器跑起来了没. `Ctrl-C`关闭测试服务器

2. 生产环境`prod/`: `cd prod/` 进入prod文件夹, 运行 `./up.sh` 启动生产服务器. 访问`http://localhost/hello` 看看服务器跑起来了没. `Ctrl-C`关闭测试服务器
***严重警告*** 生产环境运行前必须更改 `docker-compose.yml` 文件中的 `MYSQL_PASSWORD`, `MYSQL_ROOT_PASSWORD`的值，不要用默认值.
