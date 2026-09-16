class NotificationProvider:
    def send_notification(self, message: str, recipient: str):
        raise NotImplementedError()

class EmailProvider(NotificationProvider):
    def send_notification(self, message: str, recipient: str):
        print(f"Sending Email to {recipient}: {message}")

class SMSProvider(NotificationProvider):
    def send_notification(self, message: str, recipient: str):
        print(f"Sending SMS to {recipient}: {message}")

class NotificationService:
    def __init__(self, notificationProvider: NotificationProvider):
        self.notificationProvider = notificationProvider

    def send_notification(self, message: str, recipient: str):
        self.notificationProvider.send_notification(message, recipient)

if __name__ == "__main__":
    email_provider = EmailProvider()
    email_service = NotificationService(email_provider)
    email_service.send_notification("Hello via Email!", "abc@example.com")

    sms_provider = SMSProvider()
    sms_service = NotificationService(sms_provider)
    sms_service.send_notification("Hello via SMS!", "123-456-7890")
