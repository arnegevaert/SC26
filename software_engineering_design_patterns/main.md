---
options:
  end_slide_shorthand: true
  h1_slide_titles: true
  incremental_lists: true
theme:
  path: ../presenterm-theme.yaml
---
<!-- jump_to_middle -->
<!-- column_layout: [1, 1, 1] -->

<!-- column: 1 -->
# Saeyslab Conference 2026: Software Engineering

---

# Design patterns: Dependency Injection

```python +exec +line_numbers {1-3|5-10|12-14|1-14}
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
```
- What if we also want to send notifications via SMS?

---
# Design patterns: Dependency Injection

```python +exec +line_numbers {1-3|5-7|9-11|13-18|20-27|1-27}
class NotificationProvider:
    def send_notification(self, message: str, recipient: str):
        pass

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
```
