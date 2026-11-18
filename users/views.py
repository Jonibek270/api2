from django.shortcuts import render

from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.views import APIView
from .utils import generate_otp
from .send_mail import send_otp_mail
from rest_framework.permissions import AllowAny


class RegisterView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data.get("email")
            otp = generate_otp()
            send_otp_mail(email, otp)
            return Response({
                "message": f"OTP sent to {email}\n\n Iltimos 5 daqiqa ichida akkountni tasdiqlang!",
                "status": status.HTTP_201_CREATED,
                "timestamp": timezone.localtime(timezone.now())
            })

        return Response({
            "message": "something went wrong!",
            "status": status.HTTP_400_BAD_REQUEST,
            "timestamp": timezone.localtime(timezone.now()),
        })