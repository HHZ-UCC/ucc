FROM nginx:1.19.1
RUN rm /etc/nginx/conf.d/default.conf \ 
    && rm /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh

COPY ./templates/default.conf.template /etc/nginx/templates/