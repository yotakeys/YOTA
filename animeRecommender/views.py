from django.shortcuts import render
import requests

# Create your views here.
def animeRecommender(request):
    
    data = []
    amount = 1
    description = ""
    
    if request.method == 'POST':
        
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        
        response = requests.post("https://yotakey-anime-recommendation-based-descr-a345a91.hf.space/run/predict", json={
        "data": [
            description,
            amount,
            ]
        }).json()

        data = response["data"][0].split(",\n")[:-1]
    
    return render(request, 'animeRecommender/index.html', context={'datas':data, 'amount':amount, 'description' : description})