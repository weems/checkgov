import requests
from flask import Flask, render_template_string

app = Flask(__name__)

# Function to read domains from a file
def read_domains_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

# HTML template for the web page
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domain Status</title>
    <style>
        .up { color: green; }
        .down { color: red; }
    </style>
</head>
<body>
    <h1>Domain Status</h1>
    <ul>
        {% for domain, status in results.items() %}
            <li>{{ domain }} - <span class="{{ 'up' if status else 'down' }}">{{ '✔️' if status else '❌' }}</span></li>
        {% endfor %}
    </ul>
</body>
</html>
"""

def check_domain(domain):
    try:
        response = requests.get(domain, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

@app.route('/')
def index():
    domains = read_domains_from_file('domains.txt')
    results = {domain: check_domain(domain) for domain in domains}
    return render_template_string(html_template, results=results)

if __name__ == '__main__':
    app.run(debug=True)
