# BBlog
BBlog（BlockchainBlog）是一个用数字货币打赏博文的博客demo，
如果您和您的朋友在同一个区块链网络中分别部署了此项目，
那么你们互相之间可以使用数字货币来打赏彼此的博文。


### 如何运行

#### Windows
下载本项目，在项目根目录运行（需要安装docker,且支持docker stack）

```
docker stack up -c docker-compose.yml bblog
```

#### Linux
在终端直接运行此命令即可自动部署
```
curl -sSL https://raw.githubusercontent.com/TaibiaoGuo/bblog/master/deploy.sh -o deploy.sh && chmod +x deploy.sh && ./deploy.sh && rm deploy.sh
```
等待服务编译和部署完成，打开 `http://localhost:8080`即可进入主界面。


> 如果你需要搭建开发环境，计算机需先安装Docker
> 并正确设置`科学上网`或者`国内docker镜像源`，更多信息请参见
> [docker安装方法](https://www.runoob.com/docker/windows-docker-install.html)。

### 项目说明

#### 项目结构
```
.
├── docker-compose.yml # docker-compose部署脚本
├── doc # 文档
└── src # 源代码
    ├── server # 后端代码
    │   ├── api # 后端API服务
    │   ├── eth # 以太坊节点服务
    │   ├── ipfs # IPFS节点服务
    │   └── sol # 智能合约源码和部署脚本
    └── web # 前端代码
```

#### 服务间关系
服务运行会建构`VIP`类型的服务网络，并将web服务的`8080`端口和eth服务的`8545`映射到主机的`8080`和`8545`端口。

#### 服务开发语言

|服务 |功能|语言 |框架 |
|---|---|---|---|
|web| web展示界面，供用户使用| js|vue |
|api|给web服务调用的后端服务 |python|flask |
|sol|以太坊节点服务 |solidity | |
|ipfs|存储博文中的图片的服务 | | |
|mysql|维护用户信息等数据的服务 | | |

#### 配置参考和修改说明

|环境变量名 |值|注释|
|---|---|---|
| SC_AUTHOR_MODULE| |合约地址|
|SC_USER_MODULE||合约地址|
|PRIVATE_KEY|622C5B7B7BC8B728E07F6E04A9FDC5F46EC6273574E06D86AAA66259B3ECDD95||
|MAIN_ADDRESS|0x24736c9d1a4bef7483281f914206ba70be08c099||
|ETH_PROVIDER|http://bblog-eth:8545|区块链服务接入点|
|API_PROVIDER|http://bblog-api:5000|api服务接入点|


### TODO
 * 区块链浏览器功能

### 鸣谢

本项目基于 `UlordChain/blog-demo`项目，本项目在其之上只添加了一点点新功能：

* 重构项目结构，方便理解
* 添加项目文档，方便教学
* 使用环境变量代替硬编码变量，方便修改
* 使用docker-compose打包项目，方便部署和使用
* 上传打包好的镜像到阿里云，方便国内拉取
* 添加了一点功能
* 修复了一些安全漏洞

### 许可协议
MIT License