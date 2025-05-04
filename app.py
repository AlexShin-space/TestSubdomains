from flask import Flask

app = Flask(__name__)
app.config['SERVER_NAME'] = 'domain-testing-server-for-landing-business.onrender.com'  # Or yourdomain.onrender.com in production

@app.route('/')
def main_index():
    return "You are visiting the main domain"

@app.route('/', subdomain='toothpaste')
def product_landing_1():
    return "Welcome to the TOOTHPASTE subdomain"

@app.route('/', subdomain='cooler')
def product_landing_2():
    return "Welcome to the COOLER subdomain"

@app.route('/', subdomain='<subdomain>')
def wildcard_subdomain(subdomain):
    return f"You are visiting the subdomain: {subdomain}"

if __name__ == '__main__':
    app.run()
