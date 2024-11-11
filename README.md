# PySystemGuard

A Python-based system monitoring tool that tracks CPU, RAM, and disk usage metrics with email alerting capabilities.

![image](/resources/s.jpg)

## 🔍 Overview

PySystemGuard is a lightweight system monitoring solution that helps system administrators track server performance and receive email alerts when predifined thresholds are exceeded.
Built with Python and psutilk, it provides and easy-to-use framework for system monitoring and alerting.

## ✨ Features

- Real-time monitoring of:
    - CPU usage
    - RAM utilization
    - Disk space
- Configurable threshold alerts
- Email notifications via Mailjet API
- Easy to extend and customize

## 🚀 Prerequisites

- Python 3.6 or higher
- Mailjet account for email notifications
- Linux/Unix/Windows operating system

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/hamdani2020/PySystemGuard.git
cd PySystemGuard

```
2. Create and activate virtual environment:

```
python3 -m venv .venv # On Windows: python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
```

3. Install required packages:

```
pip install psutil mailjet_rest
```

## 📝 Configuration
1. Sign up for a free Mailjet account at [Mailjet](https://www.mailjet.com)
2. Create API credentials in the Mailjet Developer Portal
3. Set up environment variables (recommended) or update the config directly:

```
export MAILJET_API_KEY="your_api_key"
export MAILJET_API_SECRET="your_api_secret_key"
```

## 🎯 usage

1. Update the thresholds in `monitor.py`

```python
CPU_THRESHOLD = 2    # CPU usage percentage
RAM_THRESHOLD = 10   # RAM usage percentage
DISK_THRESHOLD = 50  # Disk usage percentage
```

2. Configure email settings:

```python
"From": {
    "Email": "your@email.com",
    "Name": "24/7 SysMon"
},
"To": [
    {
        "Email": "admin@email.com",
        "Name": "Admin"
    }
]
```

3. Run the monitoring script:

```bash
python monitor.py
```

## 📊 Sample Output

When threshold are exceeded, you'll receive an email alert like:

```
Subject: Python Monitoring Alert Alert-2024-11-11 14:30:25

CPU usage is high: 85% (Threshold: 80%)
RAM usage is high: 90% (Threshold: 85%)
Disk space is low: 15% free (Threshold: 20% free)
```

## 🔧 Customization

1. Modify threshold in `monitor.py`
2. Add additional metrics by extending the psutil implementation
3. Customize email templates in the `send_alert` function
4. Implement different notification methods (Slack, SMS, etc)

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments
- psutil for system monitoring capabilities
- Mailjet for email notification services
