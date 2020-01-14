### Production

Uses gunicorn + nginx.

1. Update the environment variables.
2. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). No mounted folders. To apply changes, the image must be re-built.
