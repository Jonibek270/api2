from django.core.mail import send_mail

def send_otp_mail(email,otp):
    send_mail(
        subject="OTP Verification",
        message=f"OTP Verification for {email}",
        from_email="navrozovjonibek54@gmail.com",
        recipient_list=[email],
        fail_silently=False,

    )
    return f"The mail was sent to {email}"