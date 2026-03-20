from flask import Flask, render_template

app = Flask(__name__)

# Route for Home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for Dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route for Story page
@app.route('/story')
def story():
    return render_template('story.html')

# Route for About page
@app.route('/about')
def about():
    return render_template('index.html', section='about')

# Route for Contact page
@app.route('/contact')
def contact():
    return render_template('index.html', section='contact')

if __name__ == '__main__':
    app.run(debug=True)