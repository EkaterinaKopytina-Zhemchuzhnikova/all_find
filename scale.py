def selection_of_scale(json):
    toponym = json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    toponym_l_c = toponym['boundedBy']['Envelope']['lowerCorner']
    toponym_r_c = toponym['boundedBy']['Envelope']['upperCorner']
    l_toponym_longitude, l_toponym_lattitude = map(float, toponym_l_c.split(" "))
    r_toponym_longitude, r_toponym_lattitude = map(float, toponym_r_c.split(" "))
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": f"{r_toponym_longitude - l_toponym_longitude},{r_toponym_lattitude - l_toponym_lattitude}",
        "l": "map",
        "pt": ",".join([toponym_longitude, toponym_lattitude]) + ",pm2rdm"}
    return map_params
