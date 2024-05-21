from .serializers import CompanySerializer,EmployeeSerializer
from .models import Company,Employee
from rest_framework import viewsets


class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        company_id = self.request.query_params.get('company_id')
        if company_id is not None:
            queryset = queryset.filter(company_id = company_id)
        return queryset

