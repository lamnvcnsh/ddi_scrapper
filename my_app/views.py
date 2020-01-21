import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models

BASE_DRUG_URL = 'https://www.drugs.com/drug-interactions/{}-index.html?filter={}'


# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    search_list = '-'.join(search.split(" "))
    #models.Search.objects.create(search=search)

    check_connect = requests.get('https://www.drugs.com/drug-interactions/{}-index.html'.format(search))
    if not check_connect:
        msg = search + " No"
        stuff_for_frontend = {
            'search': msg,
            'ddi_contents': "",
            'num_drug': "",
        }
    else:


        drug_name = []
        num_drug = []
        ddi_content = []
        ddi_type = []
        ddi_link = []

        classes = [3]
        for filter in classes:
            url = BASE_DRUG_URL.format(search_list, filter)
            response = requests.get(url)
            data = response.text
            soup = BeautifulSoup(data, features="html.parser")
            drug_links = soup.find_all('li', {'class': 'int_%d' % filter})
            num_drug = drug_links[0]
            num_drug = num_drug.b.text
            drug_links = drug_links[1:]

            for drug in drug_links:
                drug_name.append(drug.text)
                base_url = 'https://www.drugs.com{}'
                if 'drug-interaction' in drug.a['href']:
                    ddi_url = base_url.format(drug.a['href']).lower()
                    ddi_response = requests.get(ddi_url)
                    if ddi_response:
                        final_url = ddi_response.url+"?professional=1"
                    ddi_link.append(final_url)
                    ddi_data = requests.get(final_url).text
                    ddi_soup = BeautifulSoup(ddi_data, features='html.parser')
                    text = ddi_soup.find_all('p')
                    ddi_content.append(text[3].text)
                    # print(text[3].text)

                    if filter == 3:
                        ddi_type.append("major")
                    elif filter == 2:
                        ddi_type.append("moderate")
                    else:
                        ddi_type.append("minor")

        ddi_contents = zip(drug_name, ddi_type, ddi_content, ddi_link)

        stuff_for_frontend = {
            'search': search,
            'ddi_contents': ddi_contents,
            'num_drug': num_drug,
        }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)

