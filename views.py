
from django.core import paginator
from django.shortcuts import render,redirect
from pymongo.read_preferences import Primary
from .models import Employee
from django.http import HttpResponse
# from myapp.forms import DataForm
import xlwt
import csv
import pymongo
from django.conf import settings
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.datastructures import MultiValueDictKeyError
from .forms import EmployeeForm
from django.contrib import messages
my_client = pymongo.MongoClient(settings.DB_NAME)

dbname = my_client['123a']
collection_name = dbname["myapp_employee"]
global employee
employee = Employee.objects.all()

def welcome(request):
    
    return render(request, 'data.html', {'employee': employee})

def form(request):
    
    return render(request, 'form.html')

def pagination(request):
    collection_name.find().sort('time',pymongo.DESCENDING)
    paginator = Paginator(employee, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'data.html', context={'employee':page_obj})

def edit(request,Id):
    employee = Employee.objects.get(Id=Id)
    return render(request, 'edit.html', {'employee':employee})
    
def update(request,Id):
    employee = Employee.objects.get(Id=Id)
    form = EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
    return redirect("/")

def search(request):
    page_number = request.GET.get('page')
    if not page_number:
        global employee_search
        global social_network
        social_network = request.POST.get('Social_Network', "")
        key = request.POST.get('Key_word', "")
        # re_pat = re.compile(str(social_network))
        # re_pat1 = re.compile(str(key))

        # if ( not social_network and key == ''):
        #     myquery = {"Social_Network": {"$regex": re_pat}}
            
        # elif(key != None and social_network != ""):
        #     myquery = {"Social_Network":{"$regex": re_pat},"Key_word":{"$regex": re_pat1}}
            
        # elif(social_network != None and social_network == "" and key != None):
        #     myquery = {"Key_word": {"$regex": re_pat1}}
            
        # myquery = {"Social_Network":{"$regex": re_pat},"Key_word":{"$regex": re_pat1}}
        # mydoc = collection_name.find(myquery)
        # print("mydoc", mydoc)
        
        # employee = []
        # for i in mydoc:
        #     employee.append(i)
        # print(len(employee))
        employee_search = Employee.objects.filter(Social_Network__icontains=social_network, Key_word__icontains=key)

    paginator = Paginator(employee_search,20)
    page_obj = paginator.get_page(page_number)
    return render(request, 'data.html', {'choice':social_network ,'employee':page_obj})

def export_excel(request):
    
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Id', 'Social_Network', 'Key_word', 'Names', 'Link_post', 'post', 'comment', 'device','location','time']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()

    rows = Employee.objects.all().values_list('Id', 'Social_Network', 'Key_word', 'Names', 'Link_post', 'post', 'comment', 'device','location','time')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

def export_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Id', 'Social_Network', 'Key_word', 'Names', 'Link_post', 'post', 'comment', 'device','location','time'])

    users = Employee.objects.all().values_list('Id', 'Social_Network', 'Key_word', 'Names', 'Link_post', 'post', 'comment', 'device','location','time')
    for user in users:
        writer.writerow(user)

    return response
