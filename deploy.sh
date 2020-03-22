curl -sSL https://raw.githubusercontent.com/TaibiaoGuo/bblog/master/docker-compose.yml -o docker-compose.yml \
&& docker stack up -c docker-compose.yml bblog \
&& rm docker-compose.yml

