#!/bin/sh

##########################################
# @Time     :2020/2/24 7:50 PM
# @Author   :TaibiaoGuo
# @FileName :entrypoint.sh
# @Github   :https://github.com/TaibiaoGuo
# @Describe :
###########################################

echo "[info] eth init !"
mkdir db
geth --datadir "./db" init ./genesis.json
echo "[info] eth init success !"

echo "[info] eth server start !"
# 可以将ethbase是挖矿奖励发放地址，可以修改为自己的地址，这里默认为测试地址
geth --datadir "./db" --rpc --rpcaddr=0.0.0.0 --rpcport 8545 --rpccorsdomain "*" --rpcapi "eth,net,web3,personal,admin,shh,txpool,debug,miner" --nodiscover --maxpeers 30 --networkid 2020 --port 30303 --mine --minerthreads 1 --etherbase "0x24736c9d1a4bef7483281f914206ba70be08c099" --nousb

