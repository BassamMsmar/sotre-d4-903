<<<<<<< HEAD
from .models import Company


def get_company_date(request):
    data = Company.objects.last()
=======
from .models import Company


def get_company_date(request):
    data = Company.objects.last()
>>>>>>> origin
    return {'company_data':data}