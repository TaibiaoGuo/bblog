# BBlog
BBlog（BlockchainBlog）是一个用数字货币打赏博文的博客demo，
如果您和您的朋友在同一个区块链网络中分别部署了此项目，
那么你们互相之间可以使用数字货币来打赏彼此的博文。


### 如何运行
下载本项目，在根目录运行（需要安装docker）
```
docker-compose up
```
等待服务编译和部署完成，打开 `http://localhost`即可进入主界面。


> 如果你需要运行本项目或者搭建开发环境，计算机需先安装Docker
> 并正确设置`科学上网`或者`国内docker镜像源`，更多信息请参见
> [docker安装方法](https://www.runoob.com/docker/windows-docker-install.html)。

### 代码贡献说明

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
服务运行会建构`VIP`类型的服务网络，并将web服务的`81`端口和sol服务的`8545`映射到主机相应端口。

#### 服务开发语言

|服务 |功能|语言 |框架 |
|---|---|---|---|
|web| web展示界面，供用户使用| js|vue |
|api|给web服务调用的后端服务 |python|flask |
|sol|以太坊节点服务 |solidity | |
|ipfs|存储博文中的图片的服务 | | |
|mysql|维护用户信息等数据的服务 | | |

#### 配置参考和修改说明

#### 鸣谢

本项目的最初源代码基于 `UlordChain/blog-demo`项目，本项目只是完善以下内容：

* 完善了项目文档，以方便教学
* 使用docker打包，方便部署和使用
* 添加了一点功能