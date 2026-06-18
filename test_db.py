from database import save_log

test_log = {
    "source": "TestService",
    "level": "INFO",
    "message": "MongoDB Connection Successful"
}

save_log(test_log)

print("Log inserted successfully!")