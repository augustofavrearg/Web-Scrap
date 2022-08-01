from tkinter import PAGES
from selenium.webdriver import ChromeOptions, Chrome
from time import sleep

from selenium import webdriver

import pandas as pd

#importar para poder seleccionar listas desplegables
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By



from selenium import webdriver
import time

path="C:/Users/alnac/Desktop/PROGRAMACION/webscrap/chromedriver"

list=[
    "https://autos.mercadolibre.com.ar/_VEHICLE*BODY*TYPE_452748#applied_filter_id%3DVEHICLE_BODY_TYPE%26applied_filter_name%3DTipo+de+carrocer%C3%ADa%26applied_filter_order%3D14%26applied_value_id%3D452748%26applied_value_name%3DCabriolet%26applied_value_order%3D1%26applied_value_results%3D275%26is_custom%3Dfalse%26view_more_flag%3Dtrue#VEHICLE_BODY_TYPE",
    "https://autos.mercadolibre.com.ar/_VEHICLE*BODY*TYPE_452749#applied_filter_id%3DVEHICLE_BODY_TYPE%26applied_filter_name%3DTipo+de+carrocer%C3%ADa%26applied_filter_order%3D14%26applied_value_id%3D452749%26applied_value_name%3DCoup%C3%A9%26applied_value_order%3D2%26applied_value_results%3D1450%26is_custom%3Dfalse%26view_more_flag%3Dtrue#VEHICLE_BODY_TYPE",
    "https://autos.mercadolibre.com.ar/_VEHICLE*BODY*TYPE_452761#applied_filter_id%3DVEHICLE_BODY_TYPE%26applied_filter_name%3DTipo+de+carrocer%C3%ADa%26applied_filter_order%3D14%26applied_value_id%3D452761%26applied_value_name%3DCrossover%26applied_value_order%3D3%26applied_value_results%3D75%26is_custom%3Dfalse%26view_more_flag%3Dtrue#VEHICLE_BODY_TYPE",
    "https://autos.mercadolibre.com.ar/_VEHICLE*BODY*TYPE_452750#applied_filter_id%3DVEHICLE_BODY_TYPE%26applied_filter_name%3DTipo+de+carrocer%C3%ADa%26applied_filter_order%3D14%26applied_value_id%3D452750%26applied_value_name%3DFurg%C3%B3n%26applied_value_order%3D3%26applied_value_results%3D5300%26is_custom%3Dfalse#VEHICLE_BODY_TYPE",
    "https://autos.mercadolibre.com.ar/_VEHICLE*BODY*TYPE_479344#applied_filter_id%3DVEHICLE_BODY_TYPE%26applied_filter_name%3DTipo+de+carrocer%C3%ADa%26applied_filter_order%3D14%26applied_value_id%3D479344%26applied_value_name%3DHatchback%26applied_value_order%3D4%26applied_value_results%3D35275%26is_custom%3Dfalse#VEHICLE_BODY_TYPE",
    "https://autos.mercadolibre.com.ar/_VEHICLE*BODY*TYPE_452751#applied_filter_id%3DVEHICLE_BODY_TYPE%26applied_filter_name%3DTipo+de+carrocer%C3%ADa%26applied_filter_order%3D14%26applied_value_id%3D452751%26applied_value_name%3DLight+Truck%26applied_value_order%3D6%26applied_value_results%3D125%26is_custom%3Dfalse%26view_more_flag%3Dtrue#VEHICLE_BODY_TYPE",
    "https://autos.mercadolibre.com.ar/_VEHICLE*BODY*TYPE_452753#applied_filter_id%3DVEHICLE_BODY_TYPE%26applied_filter_name%3DTipo+de+carrocer%C3%ADa%26applied_filter_order%3D14%26applied_value_id%3D452753%26applied_value_name%3DMinivan%26applied_value_order%3D6%26applied_value_results%3D350%26is_custom%3Dfalse%26view_more_flag%3Dtrue#VEHICLE_BODY_TYPE",
    "https://autos.mercadolibre.com.ar/_VEHICLE*BODY*TYPE_452752#applied_filter_id%3DVEHICLE_BODY_TYPE%26applied_filter_name%3DTipo+de+carrocer%C3%ADa%26applied_filter_order%3D14%26applied_value_id%3D452752%26applied_value_name%3DMonovolumen%26applied_value_order%3D8%26applied_value_results%3D5475%26is_custom%3Dfalse%26view_more_flag%3Dtrue#VEHICLE_BODY_TYPE",
    "https://autos.mercadolibre.com.ar/_VEHICLE*BODY*TYPE_452754#applied_filter_id%3DVEHICLE_BODY_TYPE%26applied_filter_name%3DTipo+de+carrocer%C3%ADa%26applied_filter_order%3D14%26applied_value_id%3D452754%26applied_value_name%3DOff-Road%26applied_value_order%3D8%26applied_value_results%3D200%26is_custom%3Dfalse%26view_more_flag%3Dtrue#VEHICLE_BODY_TYPE",
    "https://autos.mercadolibre.com.ar/_VEHICLE*BODY*TYPE_452756#applied_filter_id%3DVEHICLE_BODY_TYPE%26applied_filter_name%3DTipo+de+carrocer%C3%ADa%26applied_filter_order%3D14%26applied_value_id%3D452756%26applied_value_name%3DPick-Up%26applied_value_order%3D9%26applied_value_results%3D19425%26is_custom%3Dfalse#VEHICLE_BODY_TYPE",
    "https://autos.mercadolibre.com.ar/_VEHICLE*BODY*TYPE_452760#applied_filter_id%3DVEHICLE_BODY_TYPE%26applied_filter_name%3DTipo+de+carrocer%C3%ADa%26applied_filter_order%3D14%26applied_value_id%3D452760%26applied_value_name%3DRural%26applied_value_order%3D11%26applied_value_results%3D900%26is_custom%3Dfalse%26view_more_flag%3Dtrue#VEHICLE_BODY_TYPE",
    "https://autos.mercadolibre.com.ar/_NoIndex_True_VEHICLE*BODY*TYPE_452759#applied_filter_id%3DVEHICLE_BODY_TYPE%26applied_filter_name%3DTipo+de+carrocer%C3%ADa%26applied_filter_order%3D14%26applied_value_id%3D452759%26applied_value_name%3DSUV%26applied_value_order%3D13%26applied_value_results%3D22475%26is_custom%3Dfalse#VEHICLE_BODY_TYPE",
    "https://autos.mercadolibre.com.ar/autos_NoIndex_True_VEHICLE*BODY*TYPE_452758?internal_referrer=true#applied_filter_id%3DVEHICLE_BODY_TYPE%26applied_filter_name%3DTipo+de+carrocer%C3%ADa%26applied_filter_order%3D14%26applied_value_id%3D452758%26applied_value_name%3DSed%C3%A1n%26applied_value_order%3D11%26applied_value_results%3D23920%26is_custom%3Dfalse#VEHICLE_BODY_TYPE"

]
 
driver = webdriver.Chrome(path)
time.sleep(5)

autosTotal=[]
def cabriolet():
   
    
    driver.get(list[0])
    time.sleep(5)
    totalPaginas=driver.find_element(by=By.XPATH, value='//*[@id="root-app"]/div/div/section/div[5]/ul/li[2]')

    numeroPaginas=[]
    separador=" "
    numeroPaginas.append(totalPaginas.text.split(separador))

    print(numeroPaginas)

    i=0
    a = numeroPaginas[0][1]
    a=int(a)
    
    while i < (a-1):
    
        element=driver.find_element(by=By.XPATH, value='//*[@title="Siguiente"]')

        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

        cars= driver.find_elements_by_class_name('ui-search-result__content-wrapper')
        for car in cars:
            separador="\n"
            autosTotal.append(car.text.split(separador))
        df = pd.DataFrame({"autosTotal":autosTotal})
        print(df)
        df.to_csv("autosTotal.csv", index=False)
        i+=1
        

cabriolet()

driver.execute_script("window.open('');")
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)

def coupe():
   
    #entrar al sitio web
    driver.get(list[1])
    time.sleep(5)
    #tomar numero de paginas
    totalPaginas=driver.find_element(by=By.XPATH, value='//*[@id="root-app"]/div/div/section/div[6]/ul/li[2]')
    numeroPaginas=[]
    separador=" "
    numeroPaginas.append(totalPaginas.text.split(separador))

    print(numeroPaginas)

    
    i=0
    a = numeroPaginas[0][1]
    a=int(a)
    
    #obtener todos los autos de todas las paginas del tipo de auto
    while i < (a-1):
    
        element=driver.find_element(by=By.XPATH, value='//*[@title="Siguiente"]')

        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

        cars= driver.find_elements_by_class_name('ui-search-result__content-wrapper')
        for car in cars:
            separador="\n"
            autosTotal.append(car.text.split(separador))
        df = pd.DataFrame({"autosTotal":autosTotal})
        print(df)
        df.to_csv("autosTotal.csv", index=False)
        i+=1
        
coupe()

time.sleep(10)

def cross():
    
    driver.get(list[2])
    time.sleep(10)
    totalPaginas=driver.find_element(by=By.XPATH, value='//*[@id="root-app"]/div/div/section/div[5]/ul/li[2]')

    numeroPaginas=[]
    separador=" "
    numeroPaginas.append(totalPaginas.text.split(separador))

    print(numeroPaginas)

    i=0
    a = numeroPaginas[0][1]
    a=int(a)
    
    while i < (a-1):
    
        element=driver.find_element(by=By.XPATH, value='//*[@title="Siguiente"]')

        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

        cars= driver.find_elements_by_class_name('ui-search-result__content-wrapper')
        for car in cars:
            separador="\n"
            autosTotal.append(car.text.split(separador))
        df = pd.DataFrame({"autosTotal":autosTotal})
        print(df)
        df.to_csv("autosTotal.csv", index=False)
        i+=1

cross()

time.sleep(10)

def furgon():
    
    driver.get(list[3])
    time.sleep(15)
    totalPaginas=driver.find_element(by=By.XPATH, value='//*[@id="root-app"]/div/div/section/div[6]/ul/li[2]')

    numeroPaginas=[]
    separador=" "
    numeroPaginas.append(totalPaginas.text.split(separador))

    print(numeroPaginas)

    i=0
    a = numeroPaginas[0][1]
    a=int(a)
    
    while i < (a-1):
    
        element=driver.find_element(by=By.XPATH, value='//*[@title="Siguiente"]')

        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

        cars= driver.find_elements_by_class_name('ui-search-result__content-wrapper')
        for car in cars:
            separador="\n"
            autosTotal.append(car.text.split(separador))
        df = pd.DataFrame({"autosTotal":autosTotal})
        print(df)
        df.to_csv("autosTotal.csv", index=False)
        i+=1

furgon()

time.sleep(10)

def hatchback():
    
    driver.get(list[4])
    time.sleep(15)
    totalPaginas=driver.find_element(by=By.XPATH, value='//*[@id="root-app"]/div/div/section/div[6]/ul/li[2]')

    numeroPaginas=[]
    separador=" "
    numeroPaginas.append(totalPaginas.text.split(separador))

    print(numeroPaginas)

    i=0
    a = numeroPaginas[0][1]
    a=int(a)
    
    while i < (a-1):
    
        element=driver.find_element(by=By.XPATH, value='//*[@title="Siguiente"]')

        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

        cars= driver.find_elements_by_class_name('ui-search-result__content-wrapper')
        for car in cars:
            separador="\n"
            autosTotal.append(car.text.split(separador))
        df = pd.DataFrame({"autosTotal":autosTotal})
        print(df)
        df.to_csv("autosTotal.csv", index=False)
        i+=1



hatchback()

time.sleep(10)


def light():
    
    driver.get(list[5])
    time.sleep(15)
    totalPaginas=driver.find_element(by=By.XPATH, value='//*[@id="root-app"]/div/div/section/div[5]/ul/li[2]')

    numeroPaginas=[]
    separador=" "
    numeroPaginas.append(totalPaginas.text.split(separador))

    print(numeroPaginas)

    i=0
    a = numeroPaginas[0][1]
    a=int(a)
    
    while i < (a-1):
    
        element=driver.find_element(by=By.XPATH, value='//*[@title="Siguiente"]')

        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

        cars= driver.find_elements_by_class_name('ui-search-result__content-wrapper')
        for car in cars:
            separador="\n"
            autosTotal.append(car.text.split(separador))
        df = pd.DataFrame({"autosTotal":autosTotal})
        print(df)
        df.to_csv("autosTotal.csv", index=False)
        i+=1



light()

time.sleep(10)


def minivan():
    
    driver.get(list[6])
    time.sleep(15)
    totalPaginas=driver.find_element(by=By.XPATH, value='//*[@id="root-app"]/div/div/section/div[6]/ul/li[2]')

    numeroPaginas=[]
    separador=" "
    numeroPaginas.append(totalPaginas.text.split(separador))

    print(numeroPaginas)

    i=0
    a = numeroPaginas[0][1]
    a=int(a)
    
    while i < (a-1):
    
        element=driver.find_element(by=By.XPATH, value='//*[@title="Siguiente"]')

        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

        cars= driver.find_elements_by_class_name('ui-search-result__content-wrapper')
        for car in cars:
            separador="\n"
            autosTotal.append(car.text.split(separador))
        df = pd.DataFrame({"autosTotal":autosTotal})
        print(df)
        df.to_csv("autosTotal.csv", index=False)
        i+=1



minivan()

time.sleep(10)


def mono():
    
    driver.get(list[7])
    time.sleep(15)
    totalPaginas=driver.find_element(by=By.XPATH, value='//*[@id="root-app"]/div/div/section/div[6]/ul/li[2]')

    numeroPaginas=[]
    separador=" "
    numeroPaginas.append(totalPaginas.text.split(separador))

    print(numeroPaginas)

    i=0
    a = numeroPaginas[0][1]
    a=int(a)
    
    while i < (a-1):
    
        element=driver.find_element(by=By.XPATH, value='//*[@title="Siguiente"]')

        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

        cars= driver.find_elements_by_class_name('ui-search-result__content-wrapper')
        for car in cars:
            separador="\n"
            autosTotal.append(car.text.split(separador))
        df = pd.DataFrame({"autosTotal":autosTotal})
        print(df)
        df.to_csv("autosTotal.csv", index=False)
        i+=1



mono()

time.sleep(10)


def off():
    
    driver.get(list[8])
    time.sleep(15)
    totalPaginas=driver.find_element(by=By.XPATH, value='//*[@id="root-app"]/div/div/section/div[6]/ul/li[2]')

    numeroPaginas=[]
    separador=" "
    numeroPaginas.append(totalPaginas.text.split(separador))

    print(numeroPaginas)

    i=0
    a = numeroPaginas[0][1]
    a=int(a)
    
    while i < (a-1):
    
        element=driver.find_element(by=By.XPATH, value='//*[@title="Siguiente"]')

        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

        cars= driver.find_elements_by_class_name('ui-search-result__content-wrapper')
        for car in cars:
            separador="\n"
            autosTotal.append(car.text.split(separador))
        df = pd.DataFrame({"autosTotal":autosTotal})
        print(df)
        df.to_csv("autosTotal.csv", index=False)
        i+=1



off()

time.sleep(10)


def pick():
    
    driver.get(list[9])
    time.sleep(15)
    totalPaginas=driver.find_element(by=By.XPATH, value='//*[@id="root-app"]/div/div/section/div[6]/ul/li[2]')

    numeroPaginas=[]
    separador=" "
    numeroPaginas.append(totalPaginas.text.split(separador))

    print(numeroPaginas)

    i=0
    a = numeroPaginas[0][1]
    a=int(a)
    
    while i < (a-1):
    
        element=driver.find_element(by=By.XPATH, value='//*[@title="Siguiente"]')

        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

        cars= driver.find_elements_by_class_name('ui-search-result__content-wrapper')
        for car in cars:
            separador="\n"
            autosTotal.append(car.text.split(separador))
        df = pd.DataFrame({"autosTotal":autosTotal})
        print(df)
        df.to_csv("autosTotal.csv", index=False)
        i+=1



pick()

time.sleep(10)


def rural():
    
    driver.get(list[10])
    time.sleep(15)
    totalPaginas=driver.find_element(by=By.XPATH, value='//*[@id="root-app"]/div/div/section/div[5]/ul/li[2]')

    numeroPaginas=[]
    separador=" "
    numeroPaginas.append(totalPaginas.text.split(separador))

    print(numeroPaginas)

    i=0
    a = numeroPaginas[0][1]
    a=int(a)
    
    while i < (a-1):
    
        element=driver.find_element(by=By.XPATH, value='//*[@title="Siguiente"]')

        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

        cars= driver.find_elements_by_class_name('ui-search-result__content-wrapper')
        for car in cars:
            separador="\n"
            autosTotal.append(car.text.split(separador))
        df = pd.DataFrame({"autosTotal":autosTotal})
        print(df)
        df.to_csv("autosTotal.csv", index=False)
        i+=1



rural()

time.sleep(10)


def suv():
    
    driver.get(list[11])
    time.sleep(15)
    totalPaginas=driver.find_element(by=By.XPATH, value='//*[@id="root-app"]/div/div/section/div[6]/ul/li[2]')

    numeroPaginas=[]
    separador=" "
    numeroPaginas.append(totalPaginas.text.split(separador))

    print(numeroPaginas)

    i=0
    a = numeroPaginas[0][1]
    a=int(a)
    
    while i < (a-1):
    
        element=driver.find_element(by=By.XPATH, value='//*[@title="Siguiente"]')

        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

        cars= driver.find_elements_by_class_name('ui-search-result__content-wrapper')
        for car in cars:
            separador="\n"
            autosTotal.append(car.text.split(separador))
        df = pd.DataFrame({"autosTotal":autosTotal})
        print(df)
        df.to_csv("autosTotal.csv", index=False)
        i+=1



suv()

time.sleep(10)


def sedan():
    
    driver.get(list[12])
    time.sleep(15)
    totalPaginas=driver.find_element(by=By.XPATH, value='//*[@id="root-app"]/div/div/section/div[6]/ul/li[2]')

    numeroPaginas=[]
    separador=" "
    numeroPaginas.append(totalPaginas.text.split(separador))

    print(numeroPaginas)

    i=0
    a = numeroPaginas[0][1]
    a=int(a)
    
    while i < (a-1):
    
        element=driver.find_element(by=By.XPATH, value='//*[@title="Siguiente"]')

        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

        cars= driver.find_elements_by_class_name('ui-search-result__content-wrapper')
        for car in cars:
            separador="\n"
            autosTotal.append(car.text.split(separador))
        df = pd.DataFrame({"autosTotal":autosTotal})
        print(df)
        df.to_csv("autosTotal.csv", index=False)
        i+=1



sedan()