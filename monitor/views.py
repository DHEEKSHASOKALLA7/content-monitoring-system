from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from .models import Keyword, Flag
from .services import run_scan


# 🔹 API ROOT (optional but recommended)
class ApiRootView(APIView):
    def get(self, request):
        return Response({
            "endpoints": {
                "keywords": "/api/keywords/",
                "scan": "/api/scan/",
                "flags": "/api/flags/",
                "update_flag": "/api/flags/<id>/"
            }
        })


# 🔹 CREATE KEYWORD
class KeywordCreateView(APIView):
    def post(self, request):
        name = request.data.get("name")

        if not name:
            return Response(
                {"error": "Keyword required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        keyword, created = Keyword.objects.get_or_create(name=name)

        if created:
            return Response(
                {"message": "Keyword added"},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"message": "Keyword already exists"},
                status=status.HTTP_200_OK
            )


# 🔹 RUN SCAN
class ScanView(APIView):
    def post(self, request):
        run_scan()
        return Response(
            {"message": "Scan completed"},
            status=status.HTTP_200_OK
        )


# 🔹 LIST FLAGS
class FlagListView(APIView):
    def get(self, request):
        flags = Flag.objects.select_related('keyword', 'content_item')

        data = []
        for f in flags:
            data.append({
                "id": f.id,
                "keyword": f.keyword.name,
                "content_title": f.content_item.title,
                "score": f.score,
                "status": f.status,
                "last_reviewed": f.last_reviewed
            })

        return Response(data, status=status.HTTP_200_OK)


# 🔹 UPDATE FLAG
class FlagUpdateView(APIView):
    def patch(self, request, id):
        try:
            flag = Flag.objects.get(id=id)
        except Flag.DoesNotExist:
            return Response(
                {"error": "Flag not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        status_value = request.data.get("status")

        if status_value not in ['pending', 'relevant', 'irrelevant']:
            return Response(
                {"error": "Invalid status"},
                status=status.HTTP_400_BAD_REQUEST
            )

        flag.status = status_value
        flag.last_reviewed = timezone.now()
        flag.save()

        return Response(
            {"message": "Updated"},
            status=status.HTTP_200_OK
        )
