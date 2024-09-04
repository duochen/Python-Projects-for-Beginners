import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email server settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "your_email@gmail.com"
PASSWORD = "your_email_password"

def send_email(to_email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(message, 'plain'))
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def load_contacts(file_path):
    contacts = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                contacts.append(line.strip())
    except FileNotFoundError:
        print(f"{file_path} not found.")
    return contacts

def load_message_template(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"{file_path} not found.")
        return ""

def main():
    contacts_file = "contacts.txt"
    message_template_file = "message.txt"
    
    contacts = load_contacts(contacts_file)
    message_template = load_message_template(message_template_file)
    
    subject = input("Enter the subject of the email: ")
    
    for contact in contacts:
        message = message_template.replace("{name}", contact.split("@")[0])
        send_email(contact, subject, message)

if __name__ == "__main__":
    main()
