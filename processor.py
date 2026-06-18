from datetime import datetime


def process_log(log):

    log["timestamp"] = str(datetime.now())

    log["processed_at"] = str(datetime.now())

    if "level" not in log:
        log["level"] = "INFO"

    return log