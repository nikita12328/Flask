from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dcbe456b65ee12a127af010e84054b7f24dc0910'


@app.route('/')
def index():
    context = {
        'title': 'Main Page'
    }
    return render_template('index.html', context=context)


@app.route('/clothes')
def clothes():
    context = {
        'title': 'Clothes'
    }
    return render_template('clothes.html', context=context)


@app.route('/shoes')
def shoes():
    context = {
        'title': 'Shoes'
    }
    return render_template('shoes.html', context=context)


@app.route('/accessories')
def accessories():
    context = {
        'title': 'Shoes'
    }
    return render_template('accessories.html', context=context)


@app.route('/about')
def about():
    context = {
        'title': 'About Page'
    }
    return render_template('about.html', context=context)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        message = request.form['message']
        flash('Your message was sent!', category='success')
    context = {
        'title': 'Contact Page'
    }
    return render_template('contact.html', context=context)


@app.errorhandler(404)
def page_not_found(error):
    context = {
        'title': 'Unknown Page'
    }
    return render_template('page404.html', context=context), 404


if __name__ == '__main__':
    app.run(debug=True)
