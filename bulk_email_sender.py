import pandas as pd
import zmail

def send_bulk_emails(input_file, sender_email, sender_password):
    # Read input file
    df = pd.read_csv(input_file)  # Assuming CSV format, adjust accordingly
    
    # Connect to Zoho Mail SMTP server
    server = zmail.server(sender_email, sender_password)

    # Iterate over each recipient
    for index, row in df.iterrows():
        recipient_email = row['Email']
        subject = row['Subject']
        message = row['Message']
        
        # Compose email
        mail = {
            'Subject': subject,
            'Content': message
        }
        
        # Send email to recipient
        server.send_mail(sender_email, recipient_email, mail)

    print("Bulk emails sent successfully.")

if __name__ == "__main__":
    input_file = 'sample_bulk_email.csv'  # Update with your input file name
    sender_email = 'your_email@example.com'  # Update with your Zoho Mail email
    sender_password = 'your_password'  # Update with your Zoho Mail password

    send_bulk_emails(input_file, sender_email, sender_password)
