

# ThingsBoard

- Systen Administrator: sysadmin@thingsboard.org / sysadmin
- Tenant Administrator: tenant@thingsboard.org / tenant
- Customer User: customer@thingsboard.org / customer


# Install cerbot

1. Exec into the container with `docker exec -ti nginx /bin/bash`
2. Run  `apt-get update  && apt-get install certbot python-certbot-nginx  &&  certbot --nginx`
3. ` apt-get update && \
     apt-get install software-properties-common && \
     add-apt-repository universe && \
     add-apt-repository ppa:certbot/certbot &&