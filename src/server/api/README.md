# api server

## 配置项目
> 使用docker-compose启动时默认启用生产环境配置，无需修改

1、开发时通过修改`development.conf`，并将环境变量FLASK_ENV设为development。

2、生产环境通过传入环境变量或者修改`production.conf` 来修改配置。

## 启动流程
- 初始化api server配置
    - 通过环境变量FLASK_ENV 判断加载开发/生产环境配置重载配置
    - 利用环境变量的配置信息再次重载配置信息
- 等待Mysql server初始化完成
- 等待IPFS server初始化完成
- 等待Geth server初始化完成
    - 等待Geth启动完成
    - 等待智能合约部署完成   
- 开始正常响应web server 请求