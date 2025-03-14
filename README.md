# Streamlit with Nginx Reverse Proxy

This is a simple example of how to deploy a Streamlit app with Nginx as a reverse proxy.

## Usage

1. Create virtual environment and install dependencies:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

2. Run the Streamlit app:

    ```bash
    streamlit run app.py --server.baseUrlPath streamlit --server.port 8501
    streamlit run app.py --server.baseUrlPath streamlit2 --server.port 8502
    ```

3. Run the Nginx server:

    Assuming you have Nginx installed.

    Copy the Nginx location configuration file to your Nginx configuration's `server` block:

    ```conf
    location /streamlit {
        proxy_pass http://0.0.0.0:8501;  # Proxy requests to Streamlit app
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_http_version 1.1;
        proxy_set_header Connection keep-alive;
        proxy_read_timeout 1000;  # Increase timeout
        proxy_send_timeout 1000;  # Increase timeout
    }

    location /streamlit2 {
        proxy_pass http://0.0.0.0:8502;  # Proxy requests to Streamlit app
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_http_version 1.1;
        proxy_set_header Connection keep-alive;
        proxy_read_timeout 1000;  # Increase timeout
        proxy_send_timeout 1000;  # Increase timeout
    }
    ```

4. Restart Nginx:

    ```bash
    sudo systemctl restart nginx
    ```

5. Access the Streamlit app through the Nginx server (assuming Nginx is running on `localhost` at port `80`):

    http://localhost/streamlit<br/>
    http://localhost/streamlit2
