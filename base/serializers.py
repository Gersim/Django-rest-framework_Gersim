from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Advocate, Company


class CompanySerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True)
    logic_test = SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'

    def get_employee_count(self, obj):
        count = obj.advocate_set.count()
        return count

    def get_logic_test(self,a):
        return True


class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Advocate
        fields = ['username','bio','company']