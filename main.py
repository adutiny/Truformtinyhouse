from flask import Flask, render_template, request
import logging
import smtplib, ssl
from email.message import EmailMessage

 

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

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        # get the data from the form
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # store the data in a file
        with open('contact_info.txt', 'a') as file:
            file.write(f'Name: {name}\nEmail: {email}\nMessage: {message}\n\n')
        
        # send the thank you email
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com" 
        sender_email = 'woodypythoncoding@gmail.com'
        password = 'iwsjxcmahzfbcsjd'
        subject = 'Thank you for contacting us'
        body = 'Thank you for reaching out to us! Did you want to setup a Free Consultation? or if you have any questions please feel free to call or text 917.626.4394  '
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = email
        msg.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg)
        
        # render the template
        return render_template('thankyou.html')

        # send the contact information email
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com" 
        sender_email = 'woodypythoncoding@gmail.com'
        password = 'iwsjxcmahzfbcsjd'
        receiver_email = 'adutinyhouse@gmail.com'
        receiver_email = 'nycrandy@gmail.com'
        subject = 'New Contact Information'
        body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg)
    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.run(host= '0.0.0.0' ,debug=True)


