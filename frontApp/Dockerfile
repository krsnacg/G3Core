# Dockerfile
FROM node:18 as build

WORKDIR /app
COPY . /app/
RUN npm install
RUN npm run build --prod

# Stage 2 - Serve app with nginx
FROM nginx:alpine
COPY --from=build /app/dist/tu-proyecto-angular /usr/share/nginx/html