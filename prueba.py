import urllib.parse
import requests
import json

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "92YK1BDpVqeJ5NDGUYwRQsIJCrWN8jZG"

while True:
    orig = input("ingrese la ciudad de origen: ")
    orig_lower= orig.lower()
    if(orig_lower=="s" or orig_lower=="salida"):
        print("ha salido del sistema exitosamente.")
        break
    dest = input("ingrese la ciudad de destino: ")
    dest_lower= dest.lower()
    if(dest_lower=="s" or dest_lower=="salida"):
        print("ha salido del bucle exitosamente")
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    
    if json_data['info']['statuscode'] != 0:
        print("Ha ocurrido un error en la consulta. Verifique las ciudades ingresadas.")
        continue
    print("\n")
    print("Para mas detalles visite:",url,"\n")
    distancia = json_data['route']['legs'][0]['distance']
    km = round(distancia*1.609344, 1)
    print("la distancia entre las ciudades es:",km,"km")
    tiempoTotal = json_data['route']['legs'][0]['formattedTime']
    print('el tiempo necesario para llegar es :',tiempoTotal+"\n"+"\n")
    for maneuver in json_data['route']['legs'][0]['maneuvers']:
        indicaciones = maneuver['narrative'].replace('[0]', 'reemplazo')
        print(indicaciones+"\n")
    print("\n")
    print("\n")