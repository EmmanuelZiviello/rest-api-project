import os
import requests
from dotenv import load_dotenv

import jinja2

load_dotenv()

DOMAIN=os.getenv("MAILGUN_DOMAIN")
#email html
template_loader=jinja2.FileSystemLoader("templates")
template_env=jinja2.Environment(loader=template_loader)
#email html

#funzione html email
def render_template(template_filename,**context):
    return template_env.get_template(template_filename).render(**context)
#funzione html email

def send_simple_message(to,subject,body,html):#funzione di mailgun
    return requests.post(
  		f"https://api.mailgun.net/v3/{DOMAIN}/messages",
  		auth=("api", os.getenv("MAILGUN_API_KEY")),
  		data={"from": f"Emmanuel Ziviello <mailgun@{DOMAIN}>",
  			"to": [to],
  			"subject": subject,
  			"text": body,
            "html":html
        }
    )#fino ad html è email solo testo

def send_user_registration_email(email,username):
    return send_simple_message(
        email,
        "Successfully signed up!",
        f"Hi {username}! You have successfully signed up to the Stores REST API!",
        #fin qui è per email normali senza jinja 2
        render_template("email/action.html",username=username)
    )