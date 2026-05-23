from flask import Flask
from prometheus_client import start_http_server, Counter
import random, time

app = Flask(__name__)
# Metric to track requests
REQUEST_COUNT = Counter('app_requests_total', 'Total requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return "Enterprise Monitoring Demo: Running on Kubernetes!"

if __name__ == '__main__':
    start_http_server(8000) # Metrics port
    app.run(host='0.0.0.0', port=5000) # App port