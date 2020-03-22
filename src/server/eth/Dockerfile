FROM ethereum/client-go
COPY . .

EXPOSE 8545 30303 30303/udp

ENTRYPOINT ["sh","endpoint.sh"]