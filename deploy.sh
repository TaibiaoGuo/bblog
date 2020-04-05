mkdir bblog \
&& cd bblog \
&& curl -sSL https://raw.githubusercontent.com/TaibiaoGuo/bblog/master/base.env -o base.env \
&& curl -sSL https://raw.githubusercontent.com/TaibiaoGuo/bblog/master/contracts.env -o contracts.env \
&& curl -sSL https://raw.githubusercontent.com/TaibiaoGuo/bblog/master/docker-compose.yml -o docker-compose.yml \
&& docker stack up -c docker-compose.yml bblog

