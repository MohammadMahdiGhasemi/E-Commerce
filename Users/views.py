from datetime import timezone
import random
from django.shortcuts import render
from rest_framework import status 
from rest_framework .views import APIView
from .models import Address ,Person ,OTP
from .serializers import AddressSerializer ,PersonSerializer
from rest_framework.response import Response
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class UserView(APIView):
    model=Person
    serializer=PersonSerializer 
    def get(self , request):
        persons= self.model.objects.all()
        srz_data=self.serializer(instance=persons , many =True)
        return Response(srz_data.data , status=status.HTTP_200_OK)
    
    def post(self, request):
        if 'phone_number' in request.data:
            phone_number = request.data['phone_number']
            user = self.model.objects.filter(phone_number=phone_number).first()

            if not user:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            otp_code = random.randint(100000, 999999)  # Generate a random 6-digit OTP
            OTP.objects.create(user=user, otp_code=str(otp_code))

            # Send OTP via Email
            subject = 'Your OTP Code'
            html_message = render_to_string('otp_email.html', {'otp_code': otp_code})
            plain_message = strip_tags(html_message)
            from_email = 'your_email@gmail.com'  # Set your email here
            to = user.email
            send_mail(subject, plain_message, from_email, [to], html_message=html_message)

            return Response({'message': 'OTP sent to your email'}, status=status.HTTP_200_OK)
        else:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def login_with_otp(self, request):
        phone_number = request.data.get('phone_number')
        otp_code = request.data.get('otp_code')

        user = self.model.objects.filter(phone_number=phone_number).first()

        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        otp = OTP.objects.filter(user=user, otp_code=otp_code).order_by('-created_at').first()

        if not otp or (timezone.now() - otp.created_at).seconds > 300:
            return Response({'error': 'Invalid OTP or expired'}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        return Response({'token': str(refresh.access_token)}, status=status.HTTP_200_OK)    
    def put(self , request , pk):
        user= self.model.objects.get(pk =pk)
        srz_data=self.serializer(instance=user , data=request.data ,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , pk):
        user = self . model.objects.get(pk=pk)
        user.is_active=False
        user.save()
        return Response({'message':'User deleted'})    
    
    
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