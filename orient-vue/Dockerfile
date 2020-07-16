FROM nginx
 
RUN npm install

RUN npm run build

COPY orient-vue/dist/ /usr/share/nginx/html/
  
#COPY nginx/default.conf /etc/nginx/conf.d/default.conf
