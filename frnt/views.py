from django.shortcuts import render, redirect
import numpy as np
import pickle

# Create your views here.
def index(request):
    if request.method =='POST':
        age = int(request.POST.get("age"))
        gender = int(request.POST.get("gender"))
        occup = int(request.POST.get("occup"))
        sd = int(request.POST.get("sd"))
        qs = int(request.POST.get("qs"))
        pal = int(request.POST.get("pal"))
        sl = int(request.POST.get("sl"))
        bmi = int(request.POST.get("bmi"))
        hr = int(request.POST.get("hr"))
        steps = int(request.POST.get("steps"))
        mxbp = int(request.POST.get("mxbp"))
        minbp = int(request.POST.get("minbp"))
        form_values = [age, gender, occup, sd, qs, pal, sl, bmi, hr, steps, mxbp, minbp]
        inp = np.array(form_values).reshape(1,-1)

        model = pickle.load(open("D:/WEB/sleepDisorder/frnt/sleep_disorder.pkl","rb"))
        output = model.predict(inp)[0]
        print(output)
        context = {'out':outputs}
        return render(request,'index.html', {'out':output})
    return render(request,"index.html")