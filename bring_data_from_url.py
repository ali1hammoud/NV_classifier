#We use requests module to connect to the internet and request the articles url
#We use BeautifulSoup to read the data which come back from the request in html format
#We use pandas to orgnize the informations and to save them to CSV file
from bs4 import BeautifulSoup
import requests
import pandas as pd
from clear_data_fun import clear_data

def bring_data():
    #cat list has the category and two list contain the urls for every category, We can add any number of url
    cat = ['Art', 'Science']
    #urls of arts
    url_cat1= [ 'https://en.wikipedia.org/wiki/Art',
                'https://en.wikipedia.org/wiki/The_arts',
                'https://en.wikipedia.org/wiki/Drawing',
                'https://en.wikipedia.org/wiki/Graphic_design',
                'https://en.wikipedia.org/wiki/Paint',
                'https://en.wikipedia.org/wiki/Song',
                'https://en.wikipedia.org/wiki/Singing',
                'https://en.wikipedia.org/wiki/Music',
                'https://en.wikipedia.org/wiki/Rhythm',
                'https://en.wikipedia.org/wiki/Artist',
                'https://en.wikipedia.org/wiki/Disco',
                'https://en.wikipedia.org/wiki/Hip-hop_dance',
                'https://en.wikipedia.org/wiki/Art_museum',
                'https://en.wikipedia.org/wiki/Moscow_Museum_of_Modern_Art',
                'https://en.wikipedia.org/wiki/Hand-colouring_of_photographs',
                'https://en.wikipedia.org/wiki/Performance_art',
                'https://en.wikipedia.org/wiki/Magic_(illusion)',
                'https://en.wikipedia.org/wiki/Poetry_reading',
                'https://en.wikipedia.org/wiki/Casting_(performing_arts)',
                'https://en.wikipedia.org/wiki/Writing']
    #urls of science
    url_cat2= [ 'https://en.wikipedia.org/wiki/Science',
                'https://en.wikipedia.org/wiki/Mathematics',
                'https://en.wikipedia.org/wiki/Computer_program',
                'https://en.wikipedia.org/wiki/Programmer',
                'https://en.wikipedia.org/wiki/Engineering',
                'https://en.wikipedia.org/wiki/Mechatronics',
                'https://en.wikipedia.org/wiki/Robotics',
                'https://en.wikipedia.org/wiki/Physics',
                'https://en.wikipedia.org/wiki/Algorithm',
                'https://en.wikipedia.org/wiki/Computer_science',
                'https://en.wikipedia.org/wiki/Engineer',
                'https://en.wikipedia.org/wiki/Robot',
                'https://en.wikipedia.org/wiki/Motion_planning',
                'https://en.wikipedia.org/wiki/Mechanical_engineering',
                'https://en.wikipedia.org/wiki/Statistics',
                'https://en.wikipedia.org/wiki/Data_science',
                'https://en.wikipedia.org/wiki/Machine',
                'https://en.wikipedia.org/wiki/Electricity',
                'https://en.wikipedia.org/wiki/Engine',
                'https://en.wikipedia.org/wiki/Applied_mathematics']
    data_pd=[]
    for url in url_cat1 :
        #request the url
        text_html = requests.get( url, timeout=5).text 
        #save the data as html code and we take just the data in <div> with 'id'='bodyContent'     
        soup = BeautifulSoup(text_html,"html5lib").find("div", {"id": "bodyContent"})
        #extract the text from the data
        data = soup.get_text().lower()
        #apply NLP to the text for preparing it to classification
        data_ready = clear_data(data)
        #add the text and his category to the data list
        data_pd.append([data_ready, cat[0]])

    for url in url_cat2 :
        text_html = requests.get( url, timeout=5).text      
        soup = BeautifulSoup(text_html,"html5lib").find("div", {"id": "bodyContent"})
        data = soup.get_text().lower()
        data_ready = clear_data(data)
        data_pd.append([data_ready, cat[1]])

    # Create the pandas DataFrame 
    df = pd.DataFrame(data_pd, columns = ['the_article', 'Class'])
    # set a numerical label for the category
    df['label'] = df['Class'].apply(lambda x: 0 if x=='Art' else 1)
    #Save the data to CSV file
    df.to_csv('DATA.csv')
