FROM nginx:latest
COPY . /usr/share/nginx/html/
WORKDIR /usr/share/nginx/html
RUN ls -l
EXPOSE 80
CMD ["nginx", "-g", "daemon off"]
