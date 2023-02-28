from flask import Flask, render_template, request

app = Flask(__name__,template_folder="Templates")
@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        # do something with the email address
        return render_template('signup.html', email=email)

if __name__ == '__main__':
    app.run(host= '0.0.0.0' ,debug=True)


