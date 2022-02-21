from django.shortcuts import render
from django.http import HttpResponse
import sklearn.externals
import joblib
import pandas as pd
import numpy as np

import pickle


with open('model/model','rb') as f:
    reloadmodel=pickle.load(f)
# Create your views here.


def index(request):
    return render(request,'form.html')

def predict(request):
    if request.method=="POST":
        temp={}
        temp["Present_Price"]=request.POST.get('Present_Price') #13.09
        temp["Kms_Driven"] = request.POST.get('Kms_Driven') #60079
        temp["Owner"] = request.POST.get('Owner') #0
        temp["no_year"] = request.POST.get('no_year') #6
        temp["Fuel_Type_Diesel"] = request.POST.get('Fuel_Type') #1
        temp["Fuel_Type_Petrol"] =0
        temp["Seller_Type_Individual"] = request.POST.get('Seller_Type') #0
        temp["Transmission_Manual"]=request.POST.get('Transmission') #1
        print(temp)
        #td = pd.DataFrame({"x": temp}).transpose()
        td=[list(temp.values())]

        # td=np.array(temp.values())
        print(td)

        scoreval=reloadmodel.predict(td)
        print(scoreval)
        context={"scoreval":scoreval}
        print(scoreval)
        return render(request,'form.html',context)
    else:
        return render(request,'form.html')