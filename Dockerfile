FROM nginx:1.11.1-alpine
MAINTAINER clement LE CORRE <clement@le-corre.eu>
COPY web/ /usr/share/nginx/html
