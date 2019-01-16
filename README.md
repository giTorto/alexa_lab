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
- edit the working directory: /home/giulianTrt/alexa_lab/pt1_basic_skill
- edit the source directory:  /home/giulianTrt/alexa_lab/pt1_basic_skill
- edit the wsgi:  /var/www/giuliantrt_pythonanywhere_com_wsgi.py
- set up the endpoint on alexa skill endpoint: https://giulianTrt.pythonanywhere.com/
- test

Now you have to configure a Skill:
- Login to your AWS account or create one if needed: https://developer.amazon.com/it/alexa-skills-kit
- Go to your alexa console: https://developer.amazon.com/alexa/console/ask

Set up your echo using same account as above, following the instructions. If you use a different account you will not be able to test your app


# Create an Alexa Skill through UI:
 - first invocation name and name
 - intent schema
 - build
 - set the endpoint

# Beyond default slots and context
- adding default slots
- managing context

# Multimodality: Alexa Presentation Language
-

# References:
https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development
https://developer.amazon.com/docs/custom-skills/create-and-edit-custom-slot-types.html
https://developer.amazon.com/blogs/alexa/post/2af6851b-0216-4e82-9aba-6fa2aec755d5/how-to-get-started-with-the-new-alexa-presentation-language-to-build-multimodal-alexa-skills
https://developer.amazon.com/docs/custom-skills/display-template-reference.html
https://developer.amazon.com/blogs/alexa/post/12826e9e-e06a-4ab4-a583-8e074709a9f3/how-to-build-alexa-skills-for-echo-show
https://developer.amazon.com/docs/custom-skills/display-interface-reference.html#full-json-response

https://developer.amazon.com/blogs/alexa/post/2af6851b-0216-4e82-9aba-6fa2aec755d5/how-to-get-started-with-the-new-alexa-presentation-language-to-build-multimodal-alexa-skills
https://developer.amazon.com/alexa/console/ask/displays
https://developer.amazon.com/docs/custom-skills/create-and-edit-custom-slot-types.html