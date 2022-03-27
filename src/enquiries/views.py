from django.core.mail import send_mail

from app.settings.development import DEFAULT_FROM_EMAIL
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Enquiry

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def send_enquiry_email(req):
  data = req.data

  try:
    subject = data['subject']
    name = data['name']
    email = data['email']
    message = data['message']
    from_email = data['email']
    recipient_list = [DEFAULT_FROM_EMAIL]

    send_mail(subject, message, from_email, recipient_list, fail_silently=True)

    enquiry = Enquiry(name=name, email=email, subject=subject)
    enquiry.save()

    return Response({'success': 'Your enquiry was successfully made'})
  except:
    return Response({'error': 'Enquiry was not sent. Please try again'})
