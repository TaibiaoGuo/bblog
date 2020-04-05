# api server

## 启动流程
- 初始化api server配置
- 等待Mysql server初始化完成
- 等待IPFS server初始化完成
- 等待Geth server初始化完成
    - 等待Geth启动完成
    - 等待智能合约部署完成   
- 开始正常响应web server 请求