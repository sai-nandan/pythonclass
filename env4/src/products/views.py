from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(*args, **kwargs):
#     return HttpResponse('<h1>This is products page</h1>')

# def home(request, *args, **kwargs):
#     product = {
#         'title':'Carriera',
#         'price':'4,50,000',
#         'color':'Black',
#         'brand':'Tag Heuar'
#     }
#     # return HttpResponse("<h1>This is professors page</h1>")
#     return render(request,"product.html",product)

def home(request, *args, **kwargs):
    product = {
        'range':range(10),
        'productlist':[
            {
                'title':'Big daddy',
                'price':'15,000',
                'color':'Black',
                'brand':'Diesel'
            },
            {
                'title':'Carriera',
                'price':'4,50,000',
                'color':'Black',
                'brand':'Tag Heuar'
            },
            {
                'title':'Gold Edition',
                'price':'10,000',
                'color':'Gold',
                'brand':'Police'
            },{
                'title':'Big daddy',
                'price':'15,000',
                'color':'Black',
                'brand':'Diesel'
            },
            {
                'title':'Carriera',
                'price':'4,50,000',
                'color':'Black',
                'brand':'Tag Heuar'
            },
            {
                'title':'Gold Edition',
                'price':'10,000',
                'color':'Gold',
                'brand':'Police'
            }
        ]
        
    }
    # return HttpResponse("<h1>This is professors page</h1>")
    return render(request,"product.html",product)
