from django.shortcuts import render
from rest_framework.views import APIView
from .models import React
from .serializer import *
from rest_framework.response import Response


class ReactView(APIView):
    serializer_class = React_Serializer


    def get(self, request):
        detail = [{'Name':detail.Name, 'Detail':detail.Detail}
        for detail in React.objects.all()]
        return Response(detail)

    def post(self, request):
        serializer = React_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

