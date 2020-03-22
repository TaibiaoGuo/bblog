# eth server
创建以太坊节点服务
> 参考：[go-ethereum 文档](https://github.com/ethereum/go-ethereum)

## 端口信息

- 8545 HTTP-RPC接口监听端口
- 30303 以太坊对等节点通信端口

## 配置说明
可以将`0x0000000000000000000000000000000000000000`修改为自己的创建的钱包的公钥地址，geth初始化时会存入测试币。

`0x24736c9d1a4bef7483281f914206ba70be08c099`是一个测试公钥，
对应的私钥是`622C5B7B7BC8B728E07F6E04A9FDC5F46EC6273574E06D86AAA66259B3ECDD95`
> 仅供测试使用，请不要在真实环境中使用此对公私钥。

```
{
  "config": {
    "chainId": 2020,
    "homesteadBlock": 0,
    "eip150Block": 0,
    "eip155Block": 0,
    "eip158Block": 0,
    "byzantiumBlock": 0,
    "constantinopleBlock": 0,
    "petersburgBlock": 0
  },
  "alloc": {
      "0x24736c9d1a4bef7483281f914206ba70be08c099": { # 默认测试公钥
      "balance": "1000000"
      },
      "0x0000000000000000000000000000000000000000": { # 将此地址改为自己的钱包的地址
      "balance": "1000000"
      }
    },
  "coinbase": "0x0000000000000000000000000000000000000000", # 将此地址改为自己的钱包的地址
  "difficulty": "0x20000",
  "extraData": "",
  "gasLimit": "0x2fefd8",
  "nonce": "0x0000000000000042",
  "mixhash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "timestamp": "0x00"
}
```

|参数|	参数说明|
|---|---|
|chainId|	指定独立的区块链网络id|
|homesteadBlock|	若该值设置为0，标识使用的第2个版本|
|eip155Block|	eip是ethereum improvement proposal的缩写，你的链不会因为这些提议分叉，所以设置为0即可。|
|eip158Block|	同上|
|mixhash|	与nonce配合用于挖矿，有上一个区块链的一部分生成的哈希值。注意它和nonce必须要满足区块链黄皮书中说的条件。|
|nonce|	一个用于挖矿的64位随机数|
|difficulty|	设置当前区块链的难度|
|alloc|	给某个账户预分配以太坊币|
|coinbase|	旷工的账号|
|timestamp|	创世块的时间戳|
|parentHash|	上一个区块的hash值。创世块的为0|
|extraData|	32bytes大小的任意数据，每个区块都有，由miner来决定是否要在里面填什么。|
|gasLimit|	设置消耗gas的总量限制。用来限制包括区块和的交易信息的总和。私有链可以填最大。|


## 开发备注
默认会使用`genesis.josn`文件中的配置信息进行初始化，从创世块开始生成新的区块。

如果需要加入已有区块链网络，可以参考相关文档。