from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .models import Book
from .serializers import BookSerializers


class BookView(ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class CreateBookView(ModelViewSet):
    serializer_class = BookSerializers
    queryset = Book.objects.all()
