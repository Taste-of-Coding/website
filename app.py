from flask import Flask, render_template, request
import smtplib, ssl
import sys
from email.message import EmailMessage

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("main.html")


@app.route("/enquiry", methods=["POST", "GET"])
def email_enquiry():

    if request.method == "POST":
        if "recipient email" in request.form and "firstname" in request.form:
            recipient_email = request.form["recipient email"]
            firstname = request.form["firstname"]
            subject = request.form["subject"]
            context = request.form["context"]
            email_tmp_file = request.form["templatelist"]
            smtp_server = "smtp.gmail.com"
            sender_email = "your email"
            password = "your app password"

            # load an email template
            with open(f"./templates/emails/{email_tmp_file}.txt") as f:
                email_template = f.read()
            content = email_template.format(firstname=firstname, context=context)

            # setup email message
            msg = EmailMessage()
            msg.set_content(content)
            msg['Subject'] = subject

            # setup smtp server and send email
            smtp_context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, 587) as server:
                server.ehlo()
                server.starttls(context=smtp_context)
                server.ehlo()
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient_email, msg.as_string())

            return "200"

        else:
            return "recipient email or firstname not found."

    else:
        return render_template("email.html")

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
        if arg == "local":
            app.run("0.0.0.0", port=2021, debug=True)

