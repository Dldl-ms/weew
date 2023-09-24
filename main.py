from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='/static')

# Dummy user data for demonstration purposes.
# In a real application, you should use a database to store user information.
users = [
    {'username': 'user1','email':'wow@weew.com' , 'password': 'password1'},
    {'username': 'user2','email':'wew@woow.com' , 'password': 'password2'}
]

@app.route('/')
def home():
    return 'Welcome to the login page. <a href="/login">Login</a> New to the website? <a href="/signin">Register</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the username and password are valid.
        for user in users:
            if user['username'] == username and user['password'] == password and user['email'] == email:
                return render_template('login.html', error=f'Hello, {username}! You are logged in.')

        # If the credentials are not valid, display an error message.
        error = 'Invalid credentials. Please try again.'
        return render_template('login.html', error=error)

    # If the request method is GET, render the login form.
    return render_template('login.html', error='')

@app.route('/signin', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        users.append({'username': username, 'email':email , 'password': password})      
     
        return redirect(url_for('home'))
    return render_template('signin.html', eror='')

print(users)

if __name__ == '__main__':
    app.run(debug=True)