"""Check for places within the LatLong range"""
import requests


# class Location:
#     '''check for location'''


def check_location(location, lat, long):
    """
    Input location with lat long for results
    1 for true
    0 for false
    """
    api_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    api_params = {'address': location, 'key': '[API_KEY]}
    json_data = requests.get(url=api_url, params=api_params)
    new_data = json_data.json()
    bounds = new_data['results'][0]['geometry']['bounds']
    north_east_lat = bounds['northeast']['lat']
    north_east_lon = bounds['northeast']['lng']
    south_west_lat = bounds['southwest']['lat']
    south_west_lon = bounds['southwest']['lng']
    ex_lat = lat
    ex_long = long

    lat_range_end = float(north_east_lat) if north_east_lat > south_west_lat else south_west_lat
    lat_range_start, lat_range_end = sorted([north_east_lat, south_west_lat])

    if north_east_lon > south_west_lon:
        lon_range_start = south_west_lon
        lon_range_end = north_east_lon
    else:
        lon_range_start = north_east_lon
        lon_range_end = south_west_lon

    if north_east_lat > south_west_lat:
        lat_range_start = south_west_lat
        lat_range_end = north_east_lat
    else:
        lat_range_start = north_east_lat
        lat_range_end = south_west_lat

    flag = 0
    if lat_range_start <= ex_lat <= lat_range_end and \
            lon_range_start <= ex_long <= lon_range_end:
        flag = 1
    return flag
