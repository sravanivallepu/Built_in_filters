from django.shortcuts import render

# Create your views here.
def built_in_filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'filters Are THE funCtionalitieS USED for pErforMing some OperatiONS on DATA that WE are sending THROUGH backEnd to Frontend','dt':dt,'c':0}
    return render(request,'built_in_filters.html',d)
