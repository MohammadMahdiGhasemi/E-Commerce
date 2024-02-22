from datetime import timezone
import random
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from rest_framework import status 
from rest_framework .views import APIView
from .models import Address ,Person ,OTP
from .serializers import AddressSerializer ,PersonSerializer , UserLoginSerializer
from rest_framework.response import Response
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.views import View

class UserView(APIView):
    model = Person
    serializer_class = PersonSerializer

    def get(self, request):
        persons = self.model.objects.all()
        serializer = self.serializer_class(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if 'email' in request.data:
            email = request.data['email']
            user = self.model.objects.filter(email=email).first()

            if not user:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            otp_code = random.randint(100000, 999999)  
            OTP.objects.create(user=user, otp_code=str(otp_code))

            # Send OTP via Email
            subject = 'Your OTP Code'
            html_message = render_to_string('otp_email.html', {'otp_code': otp_code})
            plain_message = strip_tags(html_message)
            from_email = 'ghasemi.ferdosi@gmail.com'  # Set your email here
            to = user.email
            send_mail(subject, plain_message, from_email, [to], html_message=html_message)

            return Response({'message': 'OTP sent to your email'}, status=status.HTTP_200_OK)
        else:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            user = self.model.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = self.model.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user.is_active = False  # Soft delete by marking inactive
        user.save()
        return Response({'message': 'User deleted'}, status=status.HTTP_200_OK)

class UserLoginPage(View):
    def get(self , request):
        return render(request, 'index.html')

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if not user.email_verified:
                return Response({'error': 'Email is not verified'}, status=status.HTTP_400_BAD_REQUEST)
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            return Response({'access_token': str(access_token), 'refresh_token': str(refresh)}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserRegistrationView(APIView):
    serializer_class = PersonSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Generate verification token
            token = PasswordResetTokenGenerator().make_token(user)
            # Create verification link
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            verification_url = reverse('verify-email') + f'?token={token}&uidb64={uidb64}'
            # Send verification email
            subject = 'Verify your email address'
            message = f'Hi {user.first_name},\n\nPlease click the link below to verify your email address:\n\n{verification_url}'
            send_mail(subject, message, 'ghasemi.ferdosi@gmail.com', [user.email])
            return Response({'message': 'User registered. Check your email for verification.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VerifyEmailView(APIView):
    def get(self, request):
        token = request.GET.get('token')
        uidb64 = request.GET.get('uidb64')
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = Person.objects.get(pk=uid)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return HttpResponseBadRequest('Invalid token')
            user.email_verified = True
            user.save()
            return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return HttpResponseBadRequest('Invalid token')
class AddressView(APIView):
    model=Address
    serializer= AddressSerializer
    def get(self , request):
        addresses= self.model.objects.all()
        srz_data=self.serializer(instance=addresses , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        srz_data= self.serializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request , pk):
        address= self.model.objects.get(pk =pk)
        srz_data=self.serializer(instance=address , data=request.data ,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        address = self.model.objects.get(pk=pk)
        address.is_active = False 
        address.save()
        return Response({'message': 'Address  deleted'})