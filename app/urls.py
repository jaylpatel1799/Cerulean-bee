from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("artwork", views.artwork, name="artwork"),
    #    Artwork Routes
    path("create-artwork",
         views.create_artwork, name="create_artwork"),
    path("edit-artwork/<int:id>",
         views.edit_artwork, name="edit_artwork"),
    path("view-artwork/<int:id>",
         views.view_artwork, name="view_artwork"),
     path("delete-artwork/<int:id>",
         views.delete_artwork, name="delete_artwork"),

    #     Employee Work Routes
    path("employee", views.employee, name="employee"),
    path("create-employee",
         views.create_employee, name="create_employee"),
    path("edit-employee/<int:id>",
         views.edit_employee, name="edit_employee"),
    path("view-employee/<int:id>",
         views.view_employee, name="view_employee"),
     path("delete-employee/<int:id>",
         views.delete_employee, name="delete_employee"),

    #    Print Order Routes
    path("print-orders", views.print_orders, name="print_orders"),
    path("create-print-order",
         views.create_print_order, name="create_print_order"),
    path("edit-print-order/<int:id>",
         views.edit_print_order, name="edit_print_order"),
    path("view-print-order/<int:id>",
         views.view_print_order, name="view_print_order"),
     path("delete-print-order/<int:id>",
         views.delete_print_order, name="delete_print_order"),

    #     Cost Analysis Routes
    path("cost-analysis", views.cost_analysis, name="cost_analysis"),
    path("create-cost-analysis",
         views.create_cost_analysis, name="create_cost_analysis"),
    path("edit-cost-analysis/<int:id>",
         views.edit_cost_analysis, name="edit_cost_analysis"),
    path("view-cost-analysis/<int:id>",
         views.view_cost_analysis, name="view_cost_analysis"),
    path("delete-cost-analysis/<int:id>",
         views.delete_cost_analysis, name="delete_cost_analysis"),

    #     Logout
    path("logout", views.logout, name="logout"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
