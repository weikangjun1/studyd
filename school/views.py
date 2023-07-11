from django.shortcuts import render
from django.http import HttpResponse
from school.models import students, access

# Create your views here.


from .Serial import studentSerial
from rest_framework.views import APIView


class studentView(APIView):
    def get(self, request):
        MM = students.objects.all()
        Sdetail = studentSerial(initial=MM, many=True)
        return HttpResponse(Sdetail.data)
