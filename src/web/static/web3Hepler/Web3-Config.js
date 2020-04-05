/**
 * Copyright(c) 2018
 * Ulord core developers
 *
 * config
 * @author chenxin
 * @since 2018-08-29
 */
var Config = {

    // blog service url
    //SERVICE_URL: "http://192.168.14.21:5000",
    SERVICE_URL: "http://127.0.0.1:5000",//测试服务器
    //SERVICE_URL: "http:// 132.232.98.223/server",  //生产环境
    //SERVICE_URL: "http://bblog-api:5000",  //docker-compose环境

    // blog service url
    NET_ID: "2020",

    // contract name : AuthorModule
    CONTRACT_AUTHOR_MODULE: "AuthorModule",
    // contract name : UserModule
    CONTRACT_USER_MODULE: "UserModule",

    // contract address : AuthorModule
    CONTRACT_ADDRESS_AUTHOR_MODULE: "0x699385E10d026be73b527E04060d9987587d4706",
  //CONTRACT_ADDRESS_AUTHOR_MODULE: process.env.SC_AUTHOR_MODULE, // docker-compose环境，通过环境变量传入
    // contract address : UserModule
    CONTRACT_ADDRESS_USER_MODULE: "0x6B772ec08A657e8C5eAef8e5eC2292d5D1446d8F"
  //CONTRACT_ADDRESS_USER_MODULE: process.env.SC_USER_MODULE // docker-compose环境，通过环境变量传入

};

log(CONTRACT_ADDRESS_AUTHOR_MODULE)

























