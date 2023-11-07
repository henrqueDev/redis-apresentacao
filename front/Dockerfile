FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

# Copy local directories to the current local directory of our docker image (/app)
COPY . .
# Install node packages, install serve, build the app, and remove dependencies at the end
RUN npm install \
    && npm install -g serve \
    && npm run build \
    && rm -fr node_modules

EXPOSE 3001

# Start the app using serve command
CMD [ "serve", "-s", "build" ]