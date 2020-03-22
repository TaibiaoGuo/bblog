# bblog-web dockerfile
# 将node-轻量版作为基础环境
FROM node:latest as builder

WORKDIR /app
COPY . .
# 安装依赖并编译
RUN npm i && npm run build

# nginx 作为http服务器
FROM nginx:latest
COPY nginx.conf /etc/nginx
COPY --from=builder /app/dist /user/share/nginx/html/
EXPOSE 80
