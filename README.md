# Vaccine Notifier 
### Description
This notifies you over email about the availiblity of vaccine in your area. It uses selenium and runs an automated browser in the background.
 **Happy Vaccination** :)

### Setup
```pip install -r requirements.txt```

### Configuration
All changes are to be done [here](main.py) from line 85.
Things to be changed are :
- Phone Number: Please enter the registered phone number for easy login
- Pin code: Please enter your pin code for checking the vaccine availiblity in your area
- Sender's email address: Currently this project uses SMTP library, which requires a less secure google account. I would suggest you to google it up. It can be done easily. (PS. Make a new account/use extra account for this.)
- Password: Enter the password of the less secure account here. For easy smtp login.(This is safe as this stays with you off the record)
- Reciever's email address: This is a list of email addresses you wanna recieve notifications to.
  
### Run Script
```
git clone https://github.com/Siddharthm10/VaccineNotifier.git
cd VaccineNotifier
pip install -r requirements.txt
python3 main.py
```
**NOTE** You will have to enter the otp once the program starts :)

###TODO
- [ ] Use Google api for sending mails

### All contribution are invited 
I wish to make this code easy to use for everyone. All suggestions and contributions are invited :)
Stay safe 
