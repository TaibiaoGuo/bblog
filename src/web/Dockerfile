# bblog-web dockerfile
# 将node-轻量版作为基础环境
FROM node:lts-alpine as builder
LABEL maintainer="TaibiaoGuo github.com/TaibiaoGuo/bblog"
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# 安装依赖并编译
RUN npm run build

# nginx 作为http服务器
FROM nginx:stable-alpine as production-stage
LABEL maintainer="TaibiaoGuo github.com/TaibiaoGuo/bblog"
COPY --from=builder /app/dist /user/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
