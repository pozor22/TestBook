from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserBook
from .serializers import UserBookSerializers


class CreateUserBookView(APIView):
    serializer_class = UserBookSerializers
    model = UserBook

    def post(self, request):
        serializer_for_writing = self.serializer_class(data=request.data)
        serializer_for_writing.is_valid(raise_exception=True)
        serializer_for_writing.save()
        return Response(data=serializer_for_writing.data, status=status.HTTP_201_CREATED)
