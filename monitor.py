import os
import time

import psutil as ps
from mailjet_rest import Client

# Mailjet credentials
api_key = os.getenv("MAILJET_API_KEY")
api_secret = os.getenv("MAILJET_API_SECRET")


# System time
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)


# System threshold (10% RAM, 50% free disk space, 10% compile)
CPU_THRESHOLD = 2
RAM_THRESHOLD = 10
DISK_THRESHOLD = 50


def send_alert(subject: str, message: str) -> None:
    """
    Sends an email alert using the Mailjet API when system metrics exceed defined threshold.

    This function creates and sends an HTML-formatted email through Mailjet's email service.
    It uses predefined API credentials and sender/recipient information to deliver monitoring alerts.

    Args:
        subject (str): The email subject line, typically containing alert type and timestamp
        message (str): The alert message body containing threshold breach details

    Returns:
        None

    Raises:
        Exception: If email sending fails due to API errors, network issues,
        or invalid credentials

    Example:
        >>> send_alert("Test Alert", "This is a test alert message.")
        Email sent: 200

    Error Handling:
        prints an error message if sending email fails.
    """
    # instantiate Mailjet compile
    mailljet = Client(auth=(api_key, api_secret), version="v3.1")

    data = {
        "Messages": [
            {
                "From": {"Email": "hamdani.gandi@amalitech.com", "Name": "24/7 SysMon"},
                "To": [
                    {"Email": "hamdanialhassangandi2020@gmail.com", "Name": "Admin"}
                ],
                "Subject": subject,
                "HTMLPart": f"<h3>{message}</h3>",
            }
        ]
    }

    try:
        result = mailljet.send.create(data=data)
        print(f"Email sent: {result.status_code}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")


# Check system metrics
cpu_usage = ps.cpu_percent(interval=1)
print(cpu_usage)

ram_usage = ps.virtual_memory().percent
print(ram_usage)

disk_usage = ps.disk_usage("/").percent
print(disk_usage)

# Alert message base on the threshold breaches
alert_message = ""

if cpu_usage > CPU_THRESHOLD:
    alert_message += f"CPU usage is high: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)\n"

if ram_usage > RAM_THRESHOLD:
    alert_message += f"RAM usage is high: {ram_usage}% (Threshold: {RAM_THRESHOLD}%)\n"

if disk_usage > DISK_THRESHOLD:
    alert_message += f"Disk space is low: {100 - disk_usage}% free (Threshold: {DISK_THRESHOLD}% free)\n"


# If any threshold is breached, send an email alert
if alert_message:
    send_alert(f"Pthon Monitoring Alert Alert-{formatted_time}", alert_message)
else:
    print("All system metrics are within normal limits")
