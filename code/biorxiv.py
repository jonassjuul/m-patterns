from selenium import webdriver
from selenium.webdriver import Firefox

article_num = 1
from_date = '2010-01-01'
to_date = '2020-08-30'

destination = '../../data/jlj/'


import urllib.request, json 

max_runs = 200000
number_of_papers = 100
run = 0
while (run < max_runs and number_of_papers == 100) :
    url = "https://api.biorxiv.org/details/biorxiv/%s/%s/"%(from_date,to_date)+str(article_num)

    with urllib.request.urlopen(url) as url_link:
        data = json.loads(url_link.read().decode())
        #print(data)


        #for element in data['collection'] :
            #print(element)
            #del element['abstract']
    with open(destination+'biorxiv_FROM%s_TO%s.txt'%(from_date,to_date), 'a') as outfile:
        for element in data['collection'] :
            json.dump(element, outfile)
    article_num += 100
    run +=1
    number_of_papers = len(data['collection'])
    print(number_of_papers)
