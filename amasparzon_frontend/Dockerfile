#Build vue project

from node:12.18.3-alpine AS build
WORKDIR /app
COPY package.json ./
COPY . .
RUN npm run build

#create webserver (ngnix)

FROM nginx:1.19.0-alpine AS prod-stage
COPY --from=build /app/dist/ /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]