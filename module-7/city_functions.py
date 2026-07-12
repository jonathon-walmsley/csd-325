# Jonathon Walmsley
# 07/12/2026
# Module 7.2
# Purpose: Demonstrate usage of unit tests

#def city_country(city, country):
    #"""Return a string of the form 'City, Country'."""
    #return f"{city}, {country}"

def city_country(city, country, population = 'None', language = 'None'):
    """Return a string of the form 'City, Country - population xxx'."""
    if population == 'None':
        return f"{city}, {country}"
    elif language == 'None':
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country} - population {population}, {language}"

if __name__ == '__main__':
    print(city_country("Santiago", "Chile"))
    print(city_country("Santiago", "Chile", "5000000"))
    print(city_country("Santiago", "Chile", "5000000", "Spanish"))