from django.core.mail import EmailMultiAlternatives

def send_email_thread(subject, body, to_email):
    email = EmailMultiAlternatives(
        subject,
        body="Your appointment has been confirmed successfully.",
        to=[to_email]
    )
    email.attach_alternative(body, "text/html")
    email.send()