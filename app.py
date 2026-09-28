import time
import random
from prometheus_client import start_http_server, Counter

# Create a custom metric: a Counter to track fake page views
PAGE_VIEWS = Counter('fake_app_page_views_total', 'Total number of fake page views', ['page_type'])

if __name__ == '__main__':
    # Start the Prometheus metrics server on port 8000
    start_http_server(8000)
    print("Fake app running and exporting metrics on port 8000...")
    
    # Simulate website traffic indefinitely
    pages = ['home', 'login', 'dashboard', 'checkout']
    while True:
        random_page = random.choice(pages)
        PAGE_VIEWS.labels(page_type=random_page).inc()
        time.sleep(random.uniform(0.1, 1.0)) # Random sleep to mimic real traffic

