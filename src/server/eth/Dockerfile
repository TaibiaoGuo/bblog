FROM ethereum/client-go
WORKDIR /myeth
COPY . .

EXPOSE 8545 30303 30303/udp

ENTRYPOINT ["endpoint.sh"]