# alexa_lab
This repository contains some basic scripts and examples for the Alexa lab

# Install stuff
```
virtualenv -p python3 alexa_lab_venv
source /home/giulianTrt/alexa_lab/bin/activate
pip install flask-ask
pip install cryptography==2.1.4
```

To run an alexa skill you need to have a secure connection. To test from your local machine: https://ngrok.com/download,
to run it from somewhere else:  https://www.pythonanywhere.com

After ngrok is installed:
```
ngrok http 5000
```

# How to set it up from pythonanywhere?
- Create an account
- open console

## from python anywhere console:
```
virtualenv -p python3 alexa_lab_venv
source /home/giulianTrt/alexa_lab_venv/bin/activate
pip install flask-ask
pip install cryptography==2.1.4
git clone https://github.com/giTorto/alexa_lab.git
```

## from out of the console
- edit venv: /home/giulianTrt/alexa_lab_venv
- edit the working directory: /home/giulianTrt/alexa_lab
- edit the source directory:  /home/giulianTrt/alexa_lab
- edit the wsgi:  /var/www/giuliantrt_pythonanywhere_com_wsgi.py
- set up the endpoint on alexa skill endpoint: https://giulianTrt.pythonanywhere.com/
- test

Now you have to configure a Skill:
- Login to your AWS account or create one if needed: https://developer.amazon.com/it/alexa-skills-kit
- Go to your alexa console: https://developer.amazon.com/alexa/console/ask

Set up your echo using same account as above, following the instructions. If you use a different account you will not be able to test your app


Create an Alexa Skill through UI:
 - first invocation name and name
 - intent schema
 - build
 - set the endpoint
