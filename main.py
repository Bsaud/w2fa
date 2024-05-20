import time,webbrowser, pyautogui, random

#'https://api.whatsapp.com/send?phone=””&text=”"'

def send_otp(phone_no,otp):
    webbrowser.open(f'https://api.whatsapp.com/send?phone="{phone_no}"&text=Your OTP is: {otp}')
    time.sleep(30)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrl', 'w')


def gen_otp():
    return random.randint(100000,999999)

    

while True:
    otp=str(gen_otp())
    phone_no=input("Enter Your Phone Number: ")
    send_otp(phone_no,otp)
    tobechecked_otp=input("Enter the OTP: ")
    if str(otp) == str(tobechecked_otp):
        print("OTP Verified!")
        break
    else:
        print("The Entered OTP Doesnt match the sent one: Verification Failed!")

