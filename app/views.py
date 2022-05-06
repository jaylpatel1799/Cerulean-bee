import datetime
from email import message
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import UserData, ArtworkOrder, Employee, PrintOrder, ProjectCostAnalysis

# Create your views here.
def index(request):
    if request.method == "GET":
        try:
            if request.session['username']:
                return HttpResponseRedirect(reverse("app:dashboard"))
            else:
                return HttpResponseRedirect(reverse("app:login"))
        except:
            return HttpResponseRedirect(reverse("app:login"))


def login(request):
    if request.method == "GET":
        return render(request, "app/login.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            form = UserData.objects.get(username=username, password=password)
            if form:
                request.session['username'] = username
            return HttpResponseRedirect(reverse("app:index"))

        except Exception as e:
            print(e, username)
            return render(request, "app/login.html", {
                "message": "username or password is incorrect"
            })


def signup(request):
    if request.method == "GET":
        return render(request, "app/signup.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            form = UserData(username=username, password=password)
            form.save()
            request.session['username'] = username
            return HttpResponseRedirect(reverse("app:index"))
        except:
            return render(request, "app/signup.html", {
                "message": "User already exist",
            })


def dashboard(request):
    if request.method == "GET":

        data = {
            "artworkCount": 0,
            "employeeCount": 0,
            "printOrder": 0,
            "cost": 0
        }

        data["artworkCount"] = ArtworkOrder.objects.all().count()
        data["employeeCount"] = Employee.objects.all().count()
        data["printOrder"] = PrintOrder.objects.all().count()
        data["cost"] = ProjectCostAnalysis.objects.all().count()

        return render(request, "app/dashboard.html", {
            "route": "dashboard",
            "data": data,
        })


# Artwork


def artwork(request):
    if request.method == "GET":
        orders = ArtworkOrder.objects.all()
        return render(request, "app/artwork.html", {
            "route": "artwork",
            "orders": orders
        })


def create_artwork(request):
    if request.method == "GET":
        return render(request, "app/createArtwork.html", {
            "route": "artwork"
        })
    else:
        customer_name = request.POST['customer_name']
        email = request.POST["email"]
        phone = request.POST["phone"]
        discount = float(request.POST["discount"])
        order_date = request.POST["order_date"]
        approved_date = request.POST["approved_date"]
        scheduled_date = request.POST["scheduled_date"]
        total_price = float(request.POST["total_price"])
        apparel_item = request.POST["apparel_item"]
        event = request.POST["event"]
        base_color = request.POST["base_color"]
        theme = request.POST["theme"]
        maximum_color = request.POST["maximum_color"]
        art_location = request.POST["art_location"]
        description = request.POST["description"]
        cost = int(request.POST["cost"])
        employee = request.POST["employee"]
        complete_date = request.POST["complete_date"]
        colors = request.POST["colors"]

        print(order_date)

        try:
            form = ArtworkOrder(customer_name=customer_name, email=email, phone=phone, discount=discount,
                                order_date=order_date, approved_date=approved_date, scheduled_date=scheduled_date, total_price=total_price, apparel_item=apparel_item,
                                event=event, base_color=base_color, theme=theme, maximum_color=maximum_color, art_location=art_location, description=description, cost=cost, employee=employee,
                                complete_date=complete_date, colors=colors)
            form.save()
            return HttpResponseRedirect(reverse("app:artwork"))
        except Exception as e:
            print(e)
            return render(request, "app/createArtwork.html", {
                "message": "Something went wrong",
            })


def edit_artwork(request, id):
    if request.method == "GET":
        data = ArtworkOrder.objects.get(id=id)
        return render(request, "app/createArtwork.html", {
            "route": "artwork",
            "edit": True,
            "data": data,
        })
    else:
        try:
            form = ArtworkOrder.objects.get(id=id)
            form.customer_name = request.POST['customer_name']
            form.email = request.POST["email"]
            form.phone = request.POST["phone"]
            form.discount = float(request.POST["discount"])
            form.order_date = request.POST["order_date"]
            form.approved_date = request.POST["approved_date"]
            form.scheduled_date = request.POST["scheduled_date"]
            form.total_price = float(request.POST["total_price"])
            form.apparel_item = request.POST["apparel_item"]
            form.event = request.POST["event"]
            form.base_color = request.POST["base_color"]
            form.theme = request.POST["theme"]
            form.maximum_color = request.POST["maximum_color"]
            form.art_location = request.POST["art_location"]
            form.description = request.POST["description"]
            form.cost = int(request.POST["cost"])
            form.employee = request.POST["employee"]
            form.complete_date = request.POST["complete_date"]
            form.colors = request.POST["colors"]

            form.save()
            return HttpResponseRedirect(reverse("app:artwork"))
        except Exception as e:
            print(e)
            return render(request, "app/createArtwork.html", {
                "edit": True,
                "message": "Something went wrong",
            })

def view_artwork(request, id):
    if request.method == "GET":
        data = ArtworkOrder.objects.get(id=id)
        return render(request, "app/createArtwork.html", {
            "route": "artwork",
            "edit": True,
            "data": data,
            "readonly": "readonly"
        })

def delete_artwork(request,id):
    try:
        ArtworkOrder.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse("app:artwork"))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(reverse("app:artwork"))


"""
    Employee
"""
def employee(request):
    if request.method == "GET":
        employees = Employee.objects.all()
        return render(request, "app/employee.html", {
            "route": "employee",
            "employees": employees
        })


def create_employee(request):
    if request.method == "GET":
        return render(request, "app/createEmployee.html", {
            "route": "employee"
        })
    else:
        employee_name = request.POST['employee_name']
        work_type = request.POST["work_type"]
        phone = request.POST["phone"]
        date = request.POST["date"]
        start_time = request.POST["start_time"]
        project = request.POST["project"]
        art_item = request.POST["art_item"]
        task = request.POST["task"]
        end_time = request.POST["end_time"]

        try:
            form = Employee(employee_name=employee_name, work_type=work_type, phone=phone, date=date, start_time=start_time,
                            project=project, art_item=art_item, task=task, end_time=end_time)
            form.save()
            return HttpResponseRedirect(reverse("app:employee"))
        except Exception as e:
            print(e)
            return render(request, "app/createEmployee.html", {
                "message": "Something went wrong",
                "route": "employee"
            })


def edit_employee(request, id):
    if request.method == "GET":
        data = Employee.objects.get(id=id)
        return render(request, "app/createEmployee.html", {
            "route": "employee",
            "edit": True,
            "data": data,
        })
    else:
        try:
            form = Employee.objects.get(id=id)
            form.employee_name = request.POST['employee_name']
            form.work_type = request.POST["work_type"]
            form.phone = request.POST["phone"]
            form.date = request.POST["date"]
            form.start_time = request.POST["start_time"]
            form.project = request.POST["project"]
            form.art_item = request.POST["art_item"]
            form.task = request.POST["task"]
            form.end_time = request.POST["end_time"]

            form.save()
            return HttpResponseRedirect(reverse("app:employee"))
        except Exception as e:
            print(e)
            return render(request, "app/createEmployee.html", {
                "message": "Something went wrong",
                "edit": True,
                "route": "employee"
            })


def view_employee(request, id):
    if request.method == "GET":
        data = Employee.objects.get(id=id)
        return render(request, "app/createEmployee.html", {
            "route": "employee",
            "edit": True,
            "data": data,
            "readonly": "readonly"
        })


def delete_employee(request,id):
    try:
        Employee.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse("app:employee"))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(reverse("app:employee"))

"""
    Print Orders
"""


def print_orders(request):
    if request.method == "GET":
        orders = PrintOrder.objects.all()
        return render(request, "app/printOrder.html", {
            "route": "orders",
            "orders": orders
        })


def create_print_order(request):
    if request.method == "GET":
        return render(request, "app/createPrintOrder.html", {
            "route": "orders"
        })
    else:
        customer_name = request.POST["customer_name"]
        emailid = request.POST["emailid"]
        phone = request.POST["phone"]
        orderdate = request.POST["orderdate"]
        artdate = request.POST["artdate"]
        duedate = request.POST["duedate"]
        setupcharge = request.POST["setupcharge"]
        deposit = request.POST["deposit"]
        discount = request.POST["discount"]
        totalcost = request.POST["totalcost"]
        apparelorderdate = request.POST["apparelorderdate"]
        filmdate = request.POST["filmdate"]
        printdate = request.POST["printdate"]
        delivereddate = request.POST["delivereddate"]
        basecolor = request.POST["basecolor"]
        vendorname = request.POST["vendorname"]
        xsnumber = request.POST["xsnumber"]
        xscharge = request.POST["xscharge"]
        snumber = request.POST["snumber"]
        scharge = request.POST["scharge"]
        mnumber = request.POST["mnumber"]
        mcharge = request.POST["mcharge"]
        lnumber = request.POST["lnumber"]
        lcharge = request.POST["lcharge"]
        xlnumber = request.POST["xlnumber"]
        xlcharge = request.POST["xlcharge"]
        xxlnumber = request.POST["xxlnumber"]
        xxlcharge = request.POST["xxlcharge"]
        unitbaseprice = request.POST["unitbaseprice"]
        colorcharge = request.POST["colorcharge"]
        blankprice = request.POST["blankprice"]
        locationsize = request.POST["locationsize"]
        colorchange = request.POST["colorchange"]
        colorlist = request.POST["colorlist"]
        finalcost = request.POST["finalcost"]

        try:
            form = PrintOrder(customer_name=customer_name, emailid=emailid,
                              phone=phone, orderdate=orderdate, artdate=artdate, duedate=duedate, setupcharge=setupcharge, deposit=deposit, discount=discount, totalcost=totalcost, apparelorderdate=apparelorderdate, filmdate=filmdate, printdate=printdate, delivereddate=delivereddate, basecolor=basecolor, vendorname=vendorname, xsnumber=xsnumber, xscharge=xscharge, snumber=snumber, scharge=scharge, mnumber=mnumber, mcharge=mcharge, lnumber=lnumber, lcharge=lcharge, xlnumber=xlnumber, xlcharge=xlcharge, xxlnumber=xxlnumber, xxlcharge=xxlcharge, unitbaseprice=unitbaseprice, colorcharge=colorcharge, blankprice=blankprice, locationsize=locationsize, colorchange=colorchange, colorlist=colorlist, finalcost=finalcost)
            form.save()
            return HttpResponseRedirect(reverse("app:print_orders"))
        except Exception as e:
            print(e)
            return render(request, "app/createPrintOrder.html", {
                "message": "Something went wrong",
                "route": "orders"

            })


def edit_print_order(request, id):
    if request.method == "GET":
        data = PrintOrder.objects.get(id=id)
        return render(request, "app/createPrintOrder.html", {
            "route": "orders",
            "edit": True,
            "data": data,
        })
    else:
        try:
            form = PrintOrder.objects.get(id=id)

            form.customer_name = request.POST["customer_name"]
            form.emailid = request.POST["emailid"]
            form.phone = request.POST["phone"]
            form.orderdate = request.POST["orderdate"]
            form.artdate = request.POST["artdate"]
            form.duedate = request.POST["duedate"]
            form.setupcharge = request.POST["setupcharge"]
            form.deposit = request.POST["deposit"]
            form.discount = request.POST["discount"]
            form.totalcost = request.POST["totalcost"]
            form.apparelorderdate = request.POST["apparelorderdate"]
            form.filmdate = request.POST["filmdate"]
            form.printdate = request.POST["printdate"]
            form.delivereddate = request.POST["delivereddate"]
            form.basecolor = request.POST["basecolor"]
            form.vendorname = request.POST["vendorname"]
            form.xsnumber = request.POST["xsnumber"]
            form.xscharge = request.POST["xscharge"]
            form.snumber = request.POST["snumber"]
            form.scharge = request.POST["scharge"]
            form.mnumber = request.POST["mnumber"]
            form.mcharge = request.POST["mcharge"]
            form.lnumber = request.POST["lnumber"]
            form.lcharge = request.POST["lcharge"]
            form.xlnumber = request.POST["xlnumber"]
            form.xlcharge = request.POST["xlcharge"]
            form.xxlnumber = request.POST["xxlnumber"]
            form.xxlcharge = request.POST["xxlcharge"]
            form.unitbaseprice = request.POST["unitbaseprice"]
            form.colorcharge = request.POST["colorcharge"]
            form.blankprice = request.POST["blankprice"]
            form.locationsize = request.POST["locationsize"]
            form.colorchange = request.POST["colorchange"]
            form.colorlist = request.POST["colorlist"]
            form.finalcost = request.POST["finalcost"]

            form.save()
            return HttpResponseRedirect(reverse("app:print_orders"))
        except Exception as e:
            print(e)
            return render(request, "app/createPrintOrder.html", {
                "message": "Something went wrong",
                "edit": True,
                "route": "orders"
            })


def view_print_order(request, id):
    if request.method == "GET":
        data = PrintOrder.objects.get(id=id)
        return render(request, "app/createPrintOrder.html", {
            "route": "orders",
            "edit": True,
            "data": data,
            "readonly": "readonly"
        })


def delete_print_order(request,id):
    try:
        PrintOrder.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse("app:print_orders"))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(reverse("app:print_orders"))

"""
        Cost analysis
"""
def cost_analysis(request):
    if request.method == "GET":
        orders = ProjectCostAnalysis.objects.all()
        return render(request, "app/projectCostAnalysis.html", {
            "route": "analysis",
            "orders": orders
        })


def create_cost_analysis(request):
    if request.method == "GET":
        return render(request, "app/createProjectCost.html", {
            "route": "analysis"
        })
    else:
        project_name = request.POST["project_name"]
        event_name = request.POST["event_name"]
        item_name = request.POST["item_name"]
        customer_name = request.POST["customer_name"]
        phone = request.POST["phone"]
        mc_item_1 = request.POST["mc_item_1"]
        mc_unitcost_1 = request.POST["mc_unitcost_1"]
        mc_pricecharge_1 = request.POST["mc_pricecharge_1"]
        mc_units_1 = request.POST["mc_units_1"]
        mc_cost_1 = request.POST["mc_cost_1"]
        mc_revenue_1 = request.POST["mc_revenue_1"]
        totalcost = request.POST["totalcost"]
        totalrevenue = request.POST["totalrevenue"]
        lc_employee_1 = request.POST["lc_employee_1"]
        lc_task_1 = request.POST["lc_task_1"]
        lc_time_1 = request.POST["lc_time_1"]
        lc_rate_1 = request.POST["lc_rate_1"]
        lc_cost_1 = request.POST["lc_cost_1"]
        mc_item_2 = request.POST["mc_item_2"]
        mc_unitcost_2 = request.POST["mc_unitcost_2"]
        mc_pricecharge_2 = request.POST["mc_pricecharge_2"]
        mc_units_2 = request.POST["mc_units_2"]
        mc_cost_2 = request.POST["mc_cost_2"]
        mc_revenue_2 = request.POST["mc_revenue_2"]
        lc_employee_2 = request.POST["lc_employee_2"]
        lc_task_2 = request.POST["lc_task_2"]
        lc_time_2 = request.POST["lc_time_2"]
        lc_rate_2 = request.POST["lc_rate_2"]
        lc_cost_2 = request.POST["lc_cost_2"]
        lc_total= request.POST["lc_total"]
        material_charge = request.POST["material_charge"]
        artwork_fees = request.POST["artwork_fees"]
        fixed_charges = request.POST["fixed_charges"]
        total_discounts = request.POST["total_discounts"]
        net_profits = request.POST["net_profits"]

        try:
            form = ProjectCostAnalysis(project_name=project_name,event_name=event_name,item_name=item_name,customer_name=customer_name,
            phone=phone,mc_item_1=mc_item_1,mc_unitcost_1=mc_unitcost_1,mc_pricecharge_1=mc_pricecharge_1,mc_units_1=mc_units_1,
            mc_cost_1=mc_cost_1,mc_revenue_1=mc_revenue_1,mc_item_2=mc_item_2,mc_unitcost_2=mc_unitcost_2,mc_pricecharge_2=mc_pricecharge_2,
            mc_units_2=mc_units_2,mc_cost_2=mc_cost_2,mc_revenue_2=mc_revenue_2,totalcost=totalcost,totalrevenue=totalrevenue,lc_employee_1=lc_employee_1,
            lc_task_1=lc_task_1,lc_time_1=lc_time_1,lc_rate_1=lc_rate_1,lc_cost_1=lc_cost_1,lc_employee_2=lc_employee_2,lc_task_2=lc_task_2,
            lc_time_2=lc_time_2,lc_rate_2=lc_rate_2,lc_cost_2=lc_cost_2,lc_total=lc_total,material_charge=material_charge,
            artwork_fees=artwork_fees,fixed_charges=fixed_charges,total_discounts=total_discounts,net_profits=net_profits)
            form.save()
            return HttpResponseRedirect(reverse("app:cost_analysis"))
        except Exception as e:
            print(e)
            return render(request, "app/createProjectCost.html", {
                "message": "Something went wrong",
                "route": "analysis"

            })


def edit_cost_analysis(request, id):
    if request.method == "GET":
        data = ProjectCostAnalysis.objects.get(id=id)
        return render(request, "app/createProjectCost.html", {
            "route": "analysis",
            "edit": True,
            "data": data,
        })
    else:
        try:
            form = ProjectCostAnalysis.objects.get(id=id)

            form.project_name = request.POST["project_name"]
            form.event_name = request.POST["event_name"]
            form.item_name = request.POST["item_name"]
            form.customer_name = request.POST["customer_name"]
            form.phone = request.POST["phone"]

            form.mc_item_1 = request.POST["mc_item_1"]
            form.mc_unitcost_1 = request.POST["mc_unitcost_1"]
            form.mc_pricecharge_1 = request.POST["mc_pricecharge_1"]
            form.mc_units_1 = request.POST["mc_units_1"]
            form.mc_cost_1 = request.POST["mc_cost_1"]
            form.mc_revenue_1 = request.POST["mc_revenue_1"]
            form.totalcost = request.POST["totalcost"]
            form.totalrevenue = request.POST["totalrevenue"]

            form.lc_employee_1 = request.POST["lc_employee_1"]
            form.lc_task_1 = request.POST["lc_task_1"]
            form.lc_time_1 = request.POST["lc_time_1"]
            form.lc_rate_1 = request.POST["lc_rate_1"]
            form.lc_cost_1 = request.POST["lc_cost_1"]

            form.mc_item_2 = request.POST["mc_item_2"]
            form.mc_unitcost_2 = request.POST["mc_unitcost_2"]
            form.mc_pricecharge_2 = request.POST["mc_pricecharge_2"]
            form.mc_units_2 = request.POST["mc_units_2"]
            form.mc_cost_2 = request.POST["mc_cost_2"]
            form.mc_revenue_2 = request.POST["mc_revenue_2"]
            
            form.lc_employee_2 = request.POST["lc_employee_2"]
            form.lc_task_2 = request.POST["lc_task_2"]
            form.lc_time_2 = request.POST["lc_time_2"]
            form.lc_rate_2 = request.POST["lc_rate_2"]
            form.lc_cost_2 = request.POST["lc_cost_2"]
            form.lc_total= request.POST["lc_total"]

            form.material_charge = request.POST["material_charge"]
            form.artwork_fees = request.POST["artwork_fees"]
            form.fixed_charges = request.POST["fixed_charges"]
            form.total_discounts = request.POST["total_discounts"]
            form.net_profits = request.POST["net_profits"]

            form.save()
            return HttpResponseRedirect(reverse("app:cost_analysis"))
        except Exception as e:
            print(e)
            return render(request, "app/createProjectCost.html", {
                "message": "Something went wrong",
                "edit": True,
                "route": "analysis"
            })


def view_cost_analysis(request, id):
    if request.method == "GET":
        data = ProjectCostAnalysis.objects.get(id=id)
        return render(request, "app/createProjectCost.html", {
            "route": "analysis",
            "edit": True,
            "data": data,
            "readonly": "readonly"
        })



def delete_cost_analysis(request,id):
    try:
        ProjectCostAnalysis.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse("app:cost_analysis"))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(reverse("app:cost_analysis"))

def logout(request):
    try:
        request.session.flush()
        return HttpResponseRedirect(reverse("app:login"))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(reverse("app:login"))
