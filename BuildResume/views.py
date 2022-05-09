from django.shortcuts import render
from .models import user
class p1:
    pass
class des:
    pass
# This function is called when a request is sent to login page
def login(request):
    req=request.GET
    if "uname" in req:
        u1=user()
        u1.name=req["uname"]
        u1.mail=req["mail"]
        u1.phone=req["phone"]
        u1.password=req["pwd"]
        u1.save()
    return render(request,"BuildResume/login.html")
# This function is called when a request is sent to resume page
def resume(request):
    req=request.GET
    des.bgcol=req["bgc"]
    des.rescol=req["rc"]
    des.border_type=req["borderstyle"]
    des.font=req["font"]
    des.gen_font=req["gfont"]
    d2=des()
    p2=p1()
    return render(request,"BuildResume/resume.html",{"design":d2,"data":p2})
# This function is called when a request is sent to signup page
def signup(request):
    return render(request, "BuildResume/signup.html")
# This function is called when a request is sent to details page
def details(request):
    req=request.GET
    users=user.objects.all()
    name=req["uname"]
    pwd=req["pwd"]
    for i in users:
        if i.name==name and i.password==pwd:
            return render(request, "BuildResume/details.html")
        elif i.name==name and i.password!=pwd:
            return render(request, "BuildResume/invalidcredentials.html")
    return render(request,"BuildResume/nouser.html",{"user":{"name":name}})
# This function is called when a request is sent to design page
def design(request):
    req=request.GET
    p1.name=req["fname"]+" "+req["lname"]
    p1.email=req["mail"]
    p1.phone=req["phone"]
    p1.about=req["about"]
    p1.portfolio=req["portfolio"]
    p1.github=req["github"]
    p1.linkedin=req["linkedin"]
    p1.exp=req["exp"]
    p1.project=req["project"]
    p1.tenth=[req["school"],req["10pass"],req["10score"]]
    p1.inter=[req["inter"],req["12pass"],req["12score"]]
    p1.btech=[req["btech"],req["btechpass"],req["btechscore"]]
    k=p1.project.split("\n")
    if k!=[""]:
        for i in range(len(k)):
            k[i]=k[i].split("-")
        p1.project=k
    else:
        p1.project=""
    p1.exp=p1.exp.strip()
    if p1.exp!="":
        p1.exp=p1.exp.split("\n")
    s=req["skills"].split("\n")
    p1.skills=[]
    t=[]
    for i in s:
        t.append(i)
        if len(t)==2:
            p1.skills.append(t)
            t=[]
    if len(t)==1:
        p1.skills.append(t+[" "])
    return render(request, "BuildResume/design.html")
