from urllib import response
from cv2 import line
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from datetime import date
from .filters import FormFilter
from django.contrib.auth.decorators import login_required
# Create your views here.

# def index(request):
#     return render(request, 'examsection/index.html', {'r': RemunerationForm.objects.all()})

def report_txt(request, bid):
    ob = StaffDetails.objects.filter(billid=bid)
    lines=[]
    for i in  ob:
        record = i.Name_Of_Staff + '|' + i.Name_of_Bank +  '|' + i.Bank_Location + '|' + i.ifsc + '|' + i.acc_num + '\n'
        lines.append(record         )
    response = HttpResponse(content_type='txt/plain')
    response['Content-Disposition'] = 'attachment; filename=report.txt'
    response.writelines(lines)
    return response

def details(request):
    form = RModelForm(request.POST or None)
    if(request.method == 'POST'):
        if form.is_valid():
            bid = request.POST['bid'] 
            exam = request.POST['exam']
            sub = request.POST['sub']
            branch = form.cleaned_data.get("branch")
            sname = request.POST['sname']
            mob = request.POST['mob']
            des = form.cleaned_data.get("designation")
            clg = request.POST['clg']
            bname = request.POST['bank']
            loc = request.POST['loc']
            ifsc = request.POST['ifsc']
            accnum = request.POST['acc']

            ob = StaffDetails(billid=bid, Name_Of_Exam=exam, Name_Of_Sub=sub,
            branch=branch, Name_Of_Staff=sname, MobileNum=mob, designation=des,
            Name_of_College=clg, Name_of_Bank=bname, Bank_Location=loc, ifsc=ifsc,
            acc_num=accnum)

            ob.save()

    return render(request, "examsection/details.html", {'form':form})

def bill(request, id):
    form = BModelForm(request.POST or None)
    if(request.method == 'POST'):
        if form.is_valid():
            staff = StaffDetails.objects.get(pk=id)
            print(staff.Name_Of_Staff)
            work = form.cleaned_data.get("nature_of_work")
            papers =request.POST['papers']
            rate = request.POST['rate']
            ddays = request.POST['dadays']
            drate = request.POST['darate']
            tdays = request.POST['tadays']
            trate = request.POST['tarate']

            ob = RemunerationDetails(staff=staff, nature_of_work=work, 
            number_of_papers=papers, rate=rate, da_days=ddays, da_rate=drate,
            ta_days=tdays, ta_rate=trate)

            ob.save()
            obs = StaffDetails.objects.all()
            myFilter = FormFilter(request.GET, queryset=obs)
            obs=myFilter.qs
            return render(request, "examsection/rem.html", {'obs': obs, 'myFilter':myFilter})


    return render(request, "examsection/bill.html", {'form': form})


def consReport(request):
    idlist=[]
    obs = StaffDetails.objects.all()
    for i in obs:
        idlist.append(i.billid)
    idlist = set(idlist)
    myFilter = FormFilter(request.GET, queryset=obs)
    obs = myFilter.qs
    for i in obs:
        print(i.Name_Of_Staff, '|', i.Name_of_Bank, '|', i.ifsc)
    return render(request, 'examsection/report.html', {'obs':obs, 'myFilter':myFilter, 'idlist':idlist})


def remuneration(request):
    obs = StaffDetails.objects.all()
    myFilter = FormFilter(request.GET, queryset=obs)
    obs=myFilter.qs
    return render(request, "examsection/rem.html", {'obs': obs, 'myFilter':myFilter})


def index(request):
    return render(request, "examsection/examsection.html")

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



def genRL(request, id):
    ob = StaffDetails.objects.get(id=id)
    today = date.today()
     
    data = {
        'billid':ob.billid,
        'name_of_exam': ob.Name_Of_Exam,
        'name_of_sub': ob.Name_Of_Sub,
        'branch': ob.branch,
        'name_of_staff': ob.Name_Of_Staff,
        'mobile': ob.MobileNum,
        'des':ob.designation,
        'name_of_clg': ob.Name_of_College,
        'today': today.strftime("%d.%m.%Y"),
        'today1': today.strftime("%B %d, %Y"),
       
    }
    pdf = render_to_pdf("examsection/relieving.html", data)
    return HttpResponse(pdf, content_type='application/pdf')
    


def genbill(request, id):
    ob=RemunerationDetails.objects.get(pk=id)
    data = {
        'billid':ob.staff.billid,
        'name_of_exam': ob.staff.Name_Of_Exam,
        'name_of_sub': ob.staff.Name_Of_Sub,
        'branch': ob.staff.branch,
        'name_of_staff': ob.staff.Name_Of_Staff,
        'mobile': ob.staff.MobileNum,
        'des':ob.staff.designation,
        'name_of_clg': ob.staff.Name_of_College,
        'name_of_bank': ob.staff.Name_of_Bank,
        'bank_loc': ob.staff.Bank_Location,
        'ifsc': ob.staff.ifsc,
        'accno': ob.staff.acc_num,
        'nature_of_work': ob.nature_of_work,
        'number_of_papers': ob.number_of_papers,
        'rate': ob.rate,
        'da_days': ob.da_days,
        'da_rate': ob.da_rate,
        'ta_days': ob.ta_days,
        'ta_rate': ob.ta_rate,
        'rem_total': ob.getRemuneration(),
        'da_amt': ob.getDAAmount(),
        'ta_amt': ob.getTAAmount(),
        'grand_total': ob.remTotal(),
        'in_words': ob.get_total_words()
    }

    pdf = render_to_pdf("examsection/genbill.html", data)
    return HttpResponse(pdf, content_type='application/pdf')
    # if pdf:
    #     response = HttpResponse(pdf, content_type='application/pdf')
    #     filename = "Remuneration Bill for %s" %(ob.Name_Of_Staff)
    #     content = "inline; filename='%s'" %(filename)
        
    # return HttpResponse("HI")