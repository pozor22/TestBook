from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from .models import Book
from .serializers import BookSerializers


class BookView(ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class CreateBookView(ModelViewSet):
    serializer_class = BookSerializers
    queryset = Book.objects.all()


class DeleteBookView(DestroyAPIView):
    serializer_class = BookSerializers
    queryset = Book.objects.all()


class UpdateBookView(UpdateAPIView):
    serializer_class = BookSerializers
    queryset = Book.objects.all()
