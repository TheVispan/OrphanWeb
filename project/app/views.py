from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Orphans
from .models import Relatives


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'login'

#Функция поиска
def search(request):
    max = "9999-12-31" #Максимально доступная даты
    min = "0001-01-01"# Минимально доступня дата
    if request.method == "GET":
        #Получаные данные из ajax запроса
        search_text = request.GET['search_text']
        #Проверка поля поиска
        orphans = Orphans.objects.all()
        if search_text != "":
            #фильтрация по строке поиска
            search = Orphans.objects.filter(Q(number__iregex=search_text) | Q(name__iregex=search_text) | Q(gender__gendername__iregex=search_text) | Q(placeofbirth__iregex=search_text) | Q(orphan__iregex=search_text))
            orphans = orphans.intersection(search)
        # Проверка поля "даты рождения"
        if len(request.GET['from_birthdate']) != 0 or len(request.GET['to_birthdate']) != 0:
            # Проверка на пустую дату в поле "от"
            if len(request.GET['from_birthdate']) == 0:
                birthdate = Orphans.objects.filter(dateofbirth__range=(min, request.GET['to_birthdate']))
            # Проверка на пустую дату в поле "до"
            if len(request.GET['to_birthdate']) == 0:
                birthdate = Orphans.objects.filter(dateofbirth__range=(request.GET['from_birthdate'], max))
            # Проверка на наличие даты в двух полях
            if len(request.GET['from_birthdate']) != 0 and len(request.GET['to_birthdate']) != 0:
                birthdate = Orphans.objects.filter(dateofbirth__range=(request.GET['from_birthdate'], request.GET['to_birthdate']))
            # Сравнивание множеств на сходство
            orphans = orphans.intersection(birthdate)
        # Проверка поля "даты поступления"
        if len(request.GET['from_date_of_receipt']) != 0 or len(request.GET['to_date_of_receipt']) != 0:
            # Проверка на пустую дату в поле "от"
            if len(request.GET['from_date_of_receipt']) == 0:
                date_of_receipt = Orphans.objects.filter(dateofbirth__range=(min, request.GET['to_date_of_receipt']))
            # Проверка на пустую дату в поле "до"
            if len(request.GET['to_date_of_receipt']) == 0:
                date_of_receipt = Orphans.objects.filter(dateofbirth__range=(request.GET['from_date_of_receipt'], max))
            # Проверка на наличие даты в двух полях
            if len(request.GET['from_date_of_receipt']) != 0 and len(request.GET['to_date_of_receipt']) != 0:
                date_of_receipt = Orphans.objects.filter(dateofbirth__range=(request.GET['from_date_of_receipt'], request.GET['to_date_of_receipt']))
            # Сравнивание множеств на сходство
            orphans = orphans.intersection(date_of_receipt)
        # Проверка чекбокса "показать отчисленных"
        if request.GET['expelled'] == "true":
            expelled = Orphans.objects.filter(expelled__icontains="1")
            orphans = orphans.intersection(expelled)
        # Проверка поля даты отчисления
        if len(request.GET['from_date_of_deduction']) != 0 or len(request.GET['to_date_of_deduction']) != 0:
            # Проверка на пустую дату в поле "от"
            if len(request.GET['from_date_of_deduction']) == 0:
                date_of_deduction = Orphans.objects.filter(dateofbirth__range=(min, request.GET['to_date_of_deduction']))
            # Проверка на пустую дату в поле "до"
            if len(request.GET['to_date_of_deduction']) == 0:
                date_of_deduction = Orphans.objects.filter(dateofbirth__range=(request.GET['from_date_of_deduction'], max))
            # Проверка на наличие даты в двух полях
            if len(request.GET['from_date_of_deduction']) != 0 and len(request.GET['to_date_of_deduction']) != 0:
                date_of_deduction = Orphans.objects.filter(dateofbirth__range=(request.GET['from_date_of_deduction'], request.GET['to_date_of_deduction']))
            # Сравнивание множеств на сходство
            orphans = orphans.intersection(date_of_deduction, expelled)
        # Проверка чекбокса "показать сирот"
        if request.GET['orphan'] == "true":
            orphan = Orphans.objects.filter(orphan__icontains="1")
            # Сравнивание множеств на сходство
            orphans = orphans.intersection(orphan)
        # Проверка чекбокса "показать инвалидов"
        if request.GET['disable'] == "true":
            disable = Orphans.objects.filter(disable__icontains="1")
            # Сравнивание множеств на сходство
            orphans = orphans.intersection(disable)
        # Проверка комбобокса "группы"
        if request.GET['select'] != "-":
            groups = Orphans.objects.filter(group__groupname__icontains=request.GET['select'])
            # Сравнивание множеств на сходство
            orphans = orphans.intersection(groups)
        return JsonResponse(serializers.serialize('json', orphans), safe=False)

class OrphanCreateView(LoginRequiredMixin, CreateView):
    model = Orphans
    template_name = 'orphan_new.html'
    fields = ['number', 'name', 'gender','dateofbirth','placeofbirth','orphan','dateofreceipt','dateofdeduction']

class RelativeView(LoginRequiredMixin, ListView):
    model = Relatives
    template_name = 'relative.html'

