# English Version 中文版在最后
## Database Structure
See [database.py](database.py)

## Database Operations
See [transactions.py](transactions.py)

## API/WEB interface
See [views.py](views.py)
```
all <> are optional parameters and its reference value
/hello - hello word

/test - test api to okex

/web/demo - demo page

/api/price? - api price list endpoint
target=ltc&
against=btc&
limit=<100>&
after=<1519086540>&
before=<1519087020>&
time_elapse=<1>&
time_unit=<min>

/api/price/first? - api price oldest record endpoint
target=ltc&
against=btc&
time_elapse=<1>&
time_unit=<min>

/api/price/last? - api price newest record endpoint
target=ltc&
against=btc&
time_elapse=<1>&
time_unit=<min>
```

## JS/CSS
See `./static` folder

## HTML
See `./templates` folder

## OKEX API
See `./okcoin` folder

## Cron Jobs (Fetch Data)
See [conjobs.py](cronjobs.py)

---
## 数据库结构定义
[database.py](database.py)

## 数据库操作
[transactions.py](transactions.py)

## API接口 web 访问节点
[views.py](views.py)
```
所有 <> 里面的都是可选不填的，以及它的 参考 值
/hello - hello word

/test - 测试 okex 的通讯

/web/demo - demo 页面

/api/price? - api price 列表 endpoint
target=ltc&
against=btc&
limit=<100>&
after=<1519086540>&
before=<1519087020>&
time_elapse=<1>&
time_unit=<min>

/api/price/first? - api price 最老的一条数据 endpoint
target=ltc&
against=btc&
time_elapse=<1>&
time_unit=<min>

/api/price/last? - api price 最新的一条数据 endpoint
target=ltc&
against=btc&
time_elapse=<1>&
time_unit=<min>
```
## JS/CSS
`./static` 文件夹

## HTML模板
`./templates` 文件夹

## OKEX交易所 API
`./okcoin` 文件夹已打包

## Cron Jobs (定时抓数据)
[conjobs.py](cronjobs.py)