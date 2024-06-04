from django.urls import path

from sale.views import creatkind

urlpatterns = [
    # path('', home_page,name="home"),
    # path('about-us', about_us,name="about_us"),
    # path('contact-us', contact_us,name="contact_us"),
    # path('projects', projects,name="projects"),
    # path('project/<prid>', project,name="project"),
    # path('articles/<ataype>', articles,name="articles"),
    # path('article/<arid>', article,name="article"),
    # path('testapi', testApi.as_view(), name="testapi"),

    path('sale/creatkind', creatkind, name="creatkind"),

]

