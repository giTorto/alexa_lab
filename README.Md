

```
virtualenv -p python3 alexa_lab
pip install flask-ask
pip install cryptography==2.1.4
```

To run an alexa skill you need to have a secure connection. To test from your local machine: https://ngrok.com/download,
to run it from somewhere else:  https://www.pythonanywhere.com

After ngrok is installed:
```
ngrok http 5000
```


Now you have to configure a Skill:
- Login to your AWS account or create one if needed: https://developer.amazon.com/it/alexa-skills-kit
- Go to your alexa console: https://developer.amazon.com/alexa/console/ask

Set up your echo using same account as above, following the instructions. If you use a different account you will not be able to test your app


Create an Alexa Skill through UI:
