import folium, webbrowser

def create_map(metadata):
    gps_info = metadata.get('GPSInfo')
    if gps_info is None:
        print("GPS coordinates missing, cannot create map.")
        return None
    
    # Extract latitude and longitude from the GPSInfo dictionary
    latitude = gps_info.get(2)
    longitude = gps_info.get(4)
    lat_ref = gps_info.get(1)
    lon_ref = gps_info.get(3)
    
    if latitude is None or longitude is None or lat_ref is None or lon_ref is None:
        print("GPS coordinates missing or invalid, cannot create map.")
        return None
    
    # Convert degrees, minutes, seconds to decimal degrees
    lat = (latitude[0] + latitude[1] / 60 + latitude[2] / 3600) * (-1 if lat_ref == 'S' else 1)
    lon = (longitude[0] + longitude[1] / 60 + longitude[2] / 3600) * (-1 if lon_ref == 'W' else 1)
    
    print(f"\tLatitude:", lat)
    print(f"\tLongitude:", lon)
    
    # Create Folium map
    m = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker(location=[lat, lon], popup="Location: {lat}, {lon}".format(lat=lat, lon=lon), icon=folium.Icon(color='green')).add_to(m)
    m.save('map.html')
    webbrowser.open("map.html")
    return m