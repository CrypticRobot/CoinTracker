# English 中文版在下方
## 项目展示网址 http://198.13.40.197:3000/web/demo (小服务器别请求太多谢谢)
## CoinTracker
Flask Application Mostly For Cryptocurrency (Bitcoin) Tracking.
Language Python > 3.4

## Keys
1. OKEX `price` API ***doesn't*** need an accessKey/accessSecret.
2. OKEX `trade` API ***need*** an accessKey/accessSecret pair.

## Before You Run
1. `mkdir -p ./instance` to create a folder for your local configuration.
2. `touch ./instance/config.py` to create your local configurations.
3. Configurations in `./instance/config.py` will override those in [config.py](config.py).
4. What to config? See example values in [config.py](config.py).

## Test/Development/Production Environement
See `./docker` folder

---

## CoinTracker 价格跟踪器
一个比特币的价格跟踪器 Flask 需要 Python > 3.4

## 交易所 API 秘钥
1. OKEX `price` 价格 API ***不需要*** 公钥私钥.
2. OKEX `trade` 交易 API ***需要*** 公钥私钥，你要去 okex 申请.

## 第一次运行前
1. `mkdir -p ./instance` 在`run.py` 同层级新建一个名为`instance`的文件夹，存私人配置.
2. `touch ./instance/config.py` 新建一个文档存放你的私人配置.
3. 将你的私人配置写入 `./instance/config.py` 它会覆盖相对应的 [config.py](config.py) 中的原始值.
4. 参看[config.py](config.py) ，了解具体哪些值可以进一步配置

## 开发、测试、生产环境
去 `./docker` 文件夹看看
