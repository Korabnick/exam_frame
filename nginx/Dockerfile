FROM nginx:1.27.5-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

RUN apk add --no-cache apache2-utils
RUN htpasswd -b -c /etc/nginx/.htpasswd admin Sirius2025

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]  