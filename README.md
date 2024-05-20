# Welcome to W2FA!

**W2FA is An open source project** Aiming to provide **A free OTP Over WhatsApp API** Solution for GitHub community Projects. I highly encourage anyone to contribute to this Open Repo to Bring Advance Security & Authentication for open source projects. **This is a prototype of a  work in progress**  however feel free to use The code however you wish as longest its used legally.


# Requirements

 1. Python 3.
 2. PyAutoGUI Library.
 3. A registered WhatsApp Account to send OTP from.



#  To Be Done:
This part highlights the works that needs to be completed on the project
| Task |Progress  |
|--|--|
| Creating of OTP Generation Function | Done |
| Creation of OTP push function through WhatsApp API | Done |
| Creation of OTP Check Function | Done |
| Adapt Selenium Library instead of WebBrowser  | Ongoing   |
| Adding Function invoke for after OTP Verification | Ongoing |
| Add Hashing Function for Exchanging Hash of OTP For Verification process | Yet to Be Done |
| Add Extra Security layer by hash salting | Yet To Be Done |
| Add Argument passing Functionality | Yet To Be Done |




# Configuring the Environment:



## In Debian based Operating System

    sudo apt install python3
    pip3 install PyAutoGUI
    pip3 install random
    pip3 install webbrowser

if you're planning to use run the script in a non Virtual Environment add `--break-system-packages` Keep in mind this is not recommended as it may cause the system to become unstable.
