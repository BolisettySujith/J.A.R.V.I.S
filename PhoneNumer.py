import os

def Phonenumber_location_tracker():
    current_path = os.getcwd()
    #modules used
    import datetime
    import phonenumbers
    from phonenumbers import geocoder
    import folium
    from phonenumbers import carrier
    from opencage.geocoder import OpenCageGeocode

    num = input("Enter a number: ")
    time_ = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    #API key
    API_key = "_OPEN_CAGE_GEOCODE_API_KEY_"
    sanNummber = phonenumbers.parse(num)
    #country Location finder
    location = geocoder.description_for_number(sanNummber,"en")
    #Service provider finder
    sea_pro = phonenumbers.parse(num)
    servise_prover=carrier.name_for_number(sea_pro,'en')
    #Finding the latitude and longitude
    geocoder = OpenCageGeocode(API_key)
    quesry = str(location)
    resltt = geocoder.geocode(quesry)
    lat = resltt[0]['geometry']['lat']
    lng = resltt[0]['geometry']['lng']
    #creating a map with the phone number location as pointer
    mymap = folium.Map(location=[lat,lng],zoom_start=9)
    folium.Marker([lat,lng],popup=location).add_to(mymap)
    mymap.save(rf"{current_path}/Maps/{num+str('-')+str(time_)}.html")

    return location,servise_prover,lat,lng