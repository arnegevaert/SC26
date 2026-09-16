class EmailProvider:
    def send_email(self, message: str, recipient: str):
        print(f"Sending Email to {recipient}: {message}")

class NotificationService:
    def __init__(self):
        self.email_provider = EmailProvider()

    def send_notification(self, message, recipient):
        self.email_provider.send_email(message, recipient)

if __name__ == "__main__":
    emailService = NotificationService()
    emailService.send_notification("Hello via Email!", "abc@example.com")
