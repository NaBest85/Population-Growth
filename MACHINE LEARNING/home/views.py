from django.shortcuts import render
from django.shortcuts import redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from datetime import datetime
from home.models import Contact
from django.contrib import messages
import os
import Main.settings as settings
from django.http import FileResponse
import openai
import os
import csv
import openai
from django.http import JsonResponse
import speech_recognition as sr
from pydub.utils import mediainfo
import plotly.express as px
import matplotlib.pyplot as plt
from django.shortcuts import render, redirect
import plotly.express as px
from io import BytesIO
import base64
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
import numpy as np
import warnings
import json
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
file_path = 'ALL DATA NORMALIZATION SCORES.xlsx'


def process_selected_items(request):
    pass



def home(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            selected_items = data.get('selectedItems', [])
            sheet_names = [
                    'MALE UNEMPLOYMENT RATE',
                    'FEMALE UNEMPLOYMENT RATE',
                    'COMBINED HOUSEHOLD INCOME',
                    'EMPLOYMENT AVERAGE SALARY', 
                    'ONE-YEAR HOME APPRECIATION',
                    'STATE GDP', 
                    'POVERTY ESTIMATE', 
                    'SMALL BUSINESS',
                    'POPULATION (0-19)',
                    'POPULATION (20-34)',
                    'POPULATION (35-49)',
                    'POPULATION (50-69)',
                    'POPULATION (70 & OVER)',
                    'MALE POPULATION',
                    'FEMALE POPULATION', 
                    'BIRTH RATE',
                    'DEATH RATE'

                ]
            data = {
                    # List of U.S. state names
                    'State' : [
                    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
                    'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
                    'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
                    'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
                    'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
                    'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
                    'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming','Nan']
                    
                }
            for sheet_name in sheet_names:
                df = pd.read_excel(file_path, sheet_name=sheet_name)
                df.fillna(0, inplace=True)
                data[f'{sheet_name}']=df['WEIGHTED']

            # Process the selected items as needed
            df = pd.DataFrame(data)
            df = df.iloc[:-1]
            # Select factors and weights based on your requirements
            percentages = [7, 7, 13, 12, 6, 19, 7, 7, 2, 2, 8, 10, 10, 2, 3, 3, 1, 1]
            names = [
                "Unemployment Rate Men",
                "Unemployment Rate Women",
                "Combined Household Income",
                "Employment Average Salary",
                "One-Year Home Appreciation",
                "State GDP",
                "Poverty Rate",
                "Small Business with Less Than 5 Employees",
                "Violent Crime Rate",
                "Population 0-19",
                "Population 20-34",
                "Population 35-49",
                "Population 50-69",
                "Population 70 and Over",
                "Total State Population (Male)",
                "Total State Population (Female)",
                "Total Birth Rate",
                "Total Death Rate",
            ]
            
            data = []
            data=[]
            for item in selected_items:
                for item1,item2 in zip(names,percentages):
                
                    if item==item1:
                        data.append(item2)
            
            selected_factors = ['MALE UNEMPLOYMENT RATE','FEMALE UNEMPLOYMENT RATE','COMBINED HOUSEHOLD INCOME']
            weights = [0.07, 0.07, 0.13]
            # Calculate weighted average for each state
            df['WeightedAverage'] = df[selected_factors].mul(weights).sum(axis=1)
            # Rank the states based on the weighted average
            df['Rank'] = df['WeightedAverage'].rank(ascending=False)
            # Sort the DataFrame by rank
            df = df.sort_values(by='Rank')
            # Display the result
            # print('Selected Items:', df[['State', 'WeightedAverage', 'Rank']])
            context = {
            'State': df['State'].tolist(),
            'WeightedAverage': df['WeightedAverage'].tolist(),
            'Rank': df['Rank'].tolist(),
            }
            csv_file = 'states_data.csv'

            # Write the dictionary to the CSV file
            # with open(csv_file, 'w', newline='') as file:
            #     writer = csv.writer(file)

            #     # Write header
            #     writer.writerow(['State', 'WeightedAverage','Rank'])

            #     for State,WeightedAverage,Rank in context.items():
            #         writer.writerow([State,WeightedAverage,Rank])

            
        
                # return JsonResponse(context)  # Use JsonResponse to send JSON response

            # Pass the serialized context to the template
            print(context)
            return JsonResponse(context)  # Use JsonResponse to send JSON response
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in request body'}, status=400)
    else:
        return render(request, 'home.html')


def logoutuser(coming):
    logout(coming)
    return redirect("/login")
def about(coming):
    if coming.user.is_anonymous:
        return redirect("/login") 
    else:
        return render(coming,'about.html')
def index(coming):
    if coming.user.is_anonymous:
        return redirect("/login") 
    else:
        return render(coming,'home.html')
def loginuser(coming):
    if coming.method == "POST":
        Identtiy = coming.POST.get('username')
        seckey = coming.POST.get('password')
        user = authenticate(username=Identtiy, password=seckey)
        if user is not None:
            login(coming, user)
            return redirect("/")
    else:
        return render(coming, 'login.html')



    return render(coming,'login.html')
def contact(coming):
    if coming.user.is_anonymous:
        return redirect("/login")
    
    elif coming.method == "POST":
        unclename = coming.POST.get('name')
        Gmailid = coming.POST.get('email')
        numbertocontact = coming.POST.get('phone')
        problem = coming.POST.get('desc')
        contact = Contact(name=unclename, email=Gmailid, phone=numbertocontact, desc=problem, date = datetime.today())
        contact.save()
    else:
        return render(coming, 'contact.html')
    
def contactus(coming):
    if coming.user.is_anonymous:
        return redirect("/login")
    
    elif coming.method == "POST":
        unclename = coming.POST.get('name')
        Gmailid = coming.POST.get('email')
        numbertocontact = coming.POST.get('phone')
        problem = coming.POST.get('desc')
        contact = Contact(name=unclename, email=Gmailid, phone=numbertocontact, desc=problem, date = datetime.today())
        contact.save()
    else:
        return render(coming, 'contact.html')
def signup(coming):
    return render(coming,'signup.html')
def about(coming):
    return render(coming,'about.html')
def search(coming):
  
    return render(coming,'search.html')

def signup(coming):
    if coming.method=="POST":
        username=coming.POST['username']
        email=coming.POST['email']
        fname=coming.POST['fname']
        lname=coming.POST['lname']
        password=coming.POST['password']
        password2=coming.POST['password2']
        cominguser = User.objects.create_user(username, email, password)
        cominguser.first_name= fname
        cominguser.last_name= lname
        cominguser.save()
        return redirect('/home')
    return render(coming,'signup.html')

from django.core.mail import EmailMessage

def send_email_with_pdf(request):
    if request.method == "POST":
        df=pd.read_csv('states_data.csv')
        state1 = request.POST.get('targetLanguageSelect1')
        state2 = request.POST.get('targetLanguageSelect2')
        state3 = request.POST.get('targetLanguageSelect3')
        d1=df[df['State'] == state1]
        d2=df[df['State'] == state2]
        d3=df[df['State'] == state3]
        context={"State":[d1['State'],d2['State'],d3['State3']],
                 "Weigth":[d1['WeightedAverage'],d2['WeightedAverage'],d3['WeightedAverage']]
                 }

    return JsonResponse(context)