from django.http import HttpResponse
from django.shortcuts import render
from news.models import news
from final_1.models import final_mode
from django.core.paginator import Paginator
from form1.models import form1
from django.core.mail import send_mail

# Create your views here.
from final_1.models import final_mode

def homepage(request):
    final = news.objects.all()
    aa = {'aa':final}

    send_mail(
    "Testing mail",
    "test message",
    "charuldubay.com",
    ["akshatdwivedi189.com"],
    fail_silently=False,
                    )
    return render(request,'index.html',aa)

def news_final(request,newsid):
    final_news = news.objects.get(news_slug = newsid)
    aa = {'bb':final_news}
    return render(request,'news.html',aa)
    #print(newsid)
    
def final(request):
    f1 = final_mode.objects.all()
    if request.method == 'POST':
        try:
            st = request.POST.get('servicename')
            if st!=None:
                pass
                f1 = final_mode.objects.filter(occ__icontains=st)
        except:
            pass
    # for i in f1:
    #     print(i.first_name)
    
    data = {'d1':f1}
    return render(request,'final.html',data)



def sample(request):
    f2 = final_mode.objects.all()
    # for i in f2:
    #     print(i.first_name)
    #     print(i.last_name)
    #     print(i.occ)
    p = Paginator(f2,2)
    page_number = request.GET.get('page')
    serviceDataFinal = p.get_page(page_number)
    print(page_number)
    data_final = {'data':serviceDataFinal}
    return render(request,'final_1.html',data_final)




def form_1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        website = request.POST.get('website')
        message = request.POST.get('message')
        en = form1(name1 = name,eamil1 =email,phone1 =  number,website1 = website,message1 =message )
        en.save()
        n = 'data filled'
    return render(request,'fill_form.html',{'n':n})