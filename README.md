# Bulk Email Sending Using Zoho Mail

## Overview

This script facilitates the sending of bulk emails through Zoho Mail with customized subjects and messages for each recipient. It allows for direct and individualized communication from the sender to each recipient without revealing other recipients' email addresses.

## Requirements

- Python 3.x
- `zmail` library (`pip install zmail`)
- `pandas` library (`pip install pandas`)

## Setup

1. **Clone the Repository**: Clone or download the script from the repository.

2. **Install Dependencies**: Install required libraries using pip:
    ```bash
    pip install zmail pandas
    ```

3. **Update Configuration**: Open the script (`bulk_email_sender.py`) and update the following variables:
    ```python
    sender_email = 'your_zoho_email@example.com'  # Update with your Zoho Mail email
    sender_password = None  # Leave this blank or set to None
    input_file = 'sample_bulk_email.csv'  # Update with your input file name
    ```

4. **Prepare Input File**: Create a CSV file with the following structure:
    ```csv
    Email,Subject,Message
    recipient1@example.com,Hello from Zoho Mail,"Dear recipient1,

    This is a personalized message for recipient1.

    Best regards,
    Your Name"
    ```

5. **Run the Script**:
    ```bash
    python bulk_email_sender.py
    ```

## Input File Format

- The input file should be in CSV format.
- It should contain columns: `Email`, `Subject`, and `Message`.

## Script Description

- The script reads the input file containing recipient email addresses, subjects, and messages.
- It connects to the Zoho Mail SMTP server and sends personalized emails to each recipient.
- Recipients cannot see each other's email addresses as emails are sent individually.

## Notes

- For security reasons, it's recommended to generate an app-specific password or access token for Zoho Mail authentication.
- Ensure that the input file is correctly formatted and that column names match the script's expectations.
