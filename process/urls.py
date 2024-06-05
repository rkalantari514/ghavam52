from django.urls import path

from process.views import create_process
from sale.views import create_kind, edit_kind, delete_kind, create_producer, edit_producer, delete_producer

urlpatterns = [
    # path('', home_page,name="home"),
    # path('about-us', about_us,name="about_us"),
    # path('contact-us', contact_us,name="contact_us"),
    # path('projects', projects,name="projects"),
    # path('project/<prid>', project,name="project"),
    # path('articles/<ataype>', articles,name="articles"),
    # path('article/<arid>', article,name="article"),
    # path('testapi', testApi.as_view(), name="testapi"),

    path('process/creatprocess', create_process, name="creatprocess"),
    # path('sale/editkind/<kindid>', edit_kind, name="editkind"),
    # path('sale/deletekind/<kindid>', delete_kind, name="deletekind"),
    #
    # path('sale/creatproducer', create_producer, name="creatproducer"),
    # path('sale/editproducer/<proid>', edit_producer, name="editproducer"),
    # path('sale/deleteproducer/<proid>', delete_producer, name="deleteproducer"),

]

