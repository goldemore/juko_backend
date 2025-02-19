from rest_framework import viewsets, mixins
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactRequestSerializer

class ContactRequestCreateView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ContactRequestSerializer

    def perform_create(self, serializer):
        # Данные заявки
        name = self.request.data.get('name')
        company_name = self.request.data.get('company_name')
        email = self.request.data.get('email')
        phone = self.request.data.get('phone_number')
        comment = self.request.data.get('comment', "No Message")

        # Тема и текст письма
        subject = "New request from contact page"
        message = (
            f"<html>"
            f"<body>"
            f"<h3>New Request Details</h3>"
            f"<p><strong>Name:</strong> {name}</p>"
            f"<p><strong>Company Name:</strong> {company_name}</p>"
            f"<p><strong>Email:</strong> {email}</p>"
            f"<p><strong>Phone number:</strong> {phone}</p>"
            f"<p><strong>Message:</strong> {comment}</p>"
            f"</body>"
            f"</html>"
        )

        # Кому отправлять
        admin_email = "site@buz-group.com"

        try:
            send_mail(subject, message, 'site@buz-group.com', [admin_email], html_message=message)
            return Response({"message": "Email sent successfully."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error sending email: {e}")
            return Response({"error": "Failed to send email."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
