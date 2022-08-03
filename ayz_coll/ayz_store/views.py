from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Order, Customer, Employee


def index(request):
    return render(request, "index.html")


def employee(request):
    my_employees = Employee.objects.all().values()
    template = loader.get_template('employee.html')
    context = {
        'my_employees': my_employees,
    }
    return HttpResponse(template.render(context, request))


def customer(request):
    my_customers = Customer.objects.all().values()
    template = loader.get_template('customer.html')
    context = {
        'my_customers': my_customers,
    }
    return HttpResponse(template.render(context, request))


def orders_(request):
    my_orders = Order.objects.all().values()
    template = loader.get_template('orders.html')
    context = {
        'my_orders': my_orders,
    }
    return HttpResponse(template.render(context, request))


def delete(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return HttpResponseRedirect(reverse('orders_'))


def delete_cus(request, id):
    cus = Customer.objects.get(id=id)
    cus.delete()
    return HttpResponseRedirect(reverse('customer'))


def delete_emp(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return HttpResponseRedirect(reverse('employee'))


def add_cus(request):
    template = loader.get_template('add_cus.html')
    return HttpResponse(template.render({}, request))


def add_order(request):
    template = loader.get_template('add_order.html')
    return HttpResponse(template.render({}, request))


def add_emp(request):
    template = loader.get_template('add_emp.html')
    return HttpResponse(template.render({}, request))


def add_record_emp(request):
    id_ = request.POST['emp_id']
    name_ = request.POST['name']
    sal = request.POST['salary']
    emp = Employee(name=name_, salary=sal, emp_id=id_)
    emp.save()
    return HttpResponseRedirect(reverse('employee'))


def add_record_cus(request):
    id_ = request.POST['cus_id']
    name_ = request.POST['name']
    cus = Customer(name=name_, cust_id=id_)
    cus.save()
    return HttpResponseRedirect(reverse('customer'))


def add_record_order(request):
    id_ = request.POST['order_id']
    gb_ = request.POST['given_by']
    at_ = request.POST['assigned_to']
    bill = request.POST['bill']
    if Employee.objects.filter(emp_id=at_).exists():
        assign = Employee.objects.get(emp_id=at_)
    else:
        HttpResponse("This employee doesn't exist")
    if Customer.objects.filter(cust_id=gb_).exists():
        cus = Customer.objects.get(cust_id=gb_)
    else:
        HttpResponse("This customer doesn't exist")
    order_ = Order(order_id=id_, assigned_to=assign, given_by=cus, bill=bill)
    order_.save()
    return HttpResponseRedirect(reverse('orders_'))
