# bblog-web dockerfile
# 将node-轻量版作为基础环境
FROM node:10 as builder
LABEL maintainer="TaibiaoGuo github.com/TaibiaoGuo/bblog"
RUN npm install -g http-server
WORKDIR /app
COPY package*.json ./
RUN npm i
COPY . .
# 安装依赖并编译
#RUN npm run build
# CMD [ "http-server", "dist" ]
CMD ["npm","run","dev"]

# nginx 作为http服务器
# FROM nginx:stable-alpine as production-stage
# LABEL maintainer="TaibiaoGuo github.com/TaibiaoGuo/bblog"
# COPY --from=builder /app/dist /user/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]
