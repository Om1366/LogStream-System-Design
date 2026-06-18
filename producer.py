import random
from datetime import datetime

levels = ["INFO", "WARN", "ERROR"]

messages = [
    "User Login",
    "Payment Success",
    "Database Connection Failed",
    "CPU Usage High",
    "API Timeout"
]

sources = [
    "AuthService",
    "PaymentService",
    "MonitoringService"
]


def generate_log():
    return {
        "timestamp": str(datetime.now()),
        "source": random.choice(sources),
        "level": random.choice(levels),
        "message": random.choice(messages)
    }