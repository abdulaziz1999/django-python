from import_export import resources
from .models import Students

# Create your models here.


class StudentsResource(resources.ModelResource):
    class Meta:
        model = Students
