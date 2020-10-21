from flask import Flask,render_template,request

from flask_mail import Mail,Message

#import email_db

app= Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "malliksiddharth@gmail"
app.config['MAIL_PASSWORD'] = "1$Bhadrak"
app.config['MAIL_USE_TLS'] =  False
app.config['MAIL_USE_SSL'] = True

mail =Mail(app)

@app.route('/')
def index():
	return render_template("home.html")

@app.route('/send_message',methods=['POST'])
def send_message():
	if request.method == "POST":
		email = request.form['email']
		subject = request.form['subject']
		msg = request.form['message']
		message = Message(subject,sender="malliksiddharth@gmail.com",recipients=[email]
		message.body = msg
		mail.send(message)
		success = "Message sent"
		return render_template("result.html",success=success)




"""
@app.route('/email',  methods=['POST'])
def configure_email():
	email_info = {}
	sender = request.form['sender']
	receiver = request.form['receiver']
	sub = request.form['sub']
	Message = request.form['Message']

    email_info['sender'] = sender
    email_info['receiver'] = receiver
    email_info['sub'] = sub
    email_info['Message'] = Message

    print (email_info)
    save
"""








if __name__ == "__main__":
	app.run(debug=True)







