from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    # return 2 digit country code

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

# print(get_country_code("Andorra"))
# print(get_country_code("United Arab Emirates"))