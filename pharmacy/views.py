from rest_framework import generics, filters, permissions
from .models import Medicine
from .serializers import MedicineSerializer

class MedicineListCreateView(generics.ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
