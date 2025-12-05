import email

with open("sample_email.eml", "r", encoding="utf-8") as f:
    msg = email.message_from_file(f)

subject = msg["subject"]
body = msg.get_payload()

with open("eml_output.txt", "w", encoding="utf-8") as out:
    out.write(f"{subject} \n{body}")

print("Simple Email extraction completed")