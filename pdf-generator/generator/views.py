from uuid import uuid4
from rest_framework import (
    views,
    permissions,
    status,
)
from rest_framework.response import Response
from reportlab.pdfgen import canvas


class PdfView(views.APIView):
    permission_classes = (
        permissions.AllowAny,
    )

    def post(self, request, *args, **kwargs):
        # response = Response(content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="test.pdf"'
        days = {day: 0 for day in range(1, 32)}
        for row in request.data:
            days[row['day']] = row['hours']

        file_name = str(uuid4())
        file_path = f'media/{file_name}.pdf'

        pdf = canvas.Canvas(file_path)
        offset = 800
        for key in days.keys():
            row_text = f"Dzien {key} | {days[key]} godzin."
            pdf.drawString(50, offset, row_text)
            offset -= 20

        pdf.showPage()
        pdf.save()
        return Response(
            {'file_url': f'http://localhost:8000/{file_path}'},
            status=status.HTTP_200_OK
        ) # response

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
