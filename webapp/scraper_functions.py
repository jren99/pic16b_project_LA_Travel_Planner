def visit_hotel(df, want_to_go_name):
    each_name = want_to_go_name.split(".")
    
    for name in each_name:
        if name == each_name[0]:
            visit_html = df[["Hotel Name", "Site Link"]][df["Hotel Name"] == name]
        else:
            visit_html = visit_html.append(df[["Hotel Name", "Site Link"]][df["Hotel Name"] == name])
    
    return visit_html

def find_location_hotel(visit_html):
    
    location = []
    
    for link in visit_html["Site Link"]:
        html = requests.get(link)
        bsobj = soup(html.content, "lxml")
    
        for loc in bsobj.find_all("script", type = "application/ld+json"):
            if "streetAddress" in loc.string:
                find_part_html = loc.string.split("{")
                for street in find_part_html:
                    if "streetAddress" in street:
                        for value in street.split(","):
                            if "streetAddress" in value:
                                street_name = value.split(":")[1][1:][:-1] + ", "
                                   
                            if "addressLocality" in value:
                                city_name = value.split(":")[1][1:][:-1] + ", "
                                 
                            if "postalCode" in value:
                                zipcode = "CA " + value.split(":")[1][1:][:-1]
                            
        location_info = street_name + city_name + zipcode
        location.append(location_info)
    
    return location

def visit_tourist(df, want_to_go_name):
    each_name = want_to_go_name.split(".")
    
    for name in each_name:
        if name == each_name[0]:
            visit_html = df[["Tourist Site Name", "Site Link"]][df["Tourist Site Name"] == name]
        else:
            visit_html = visit_html.append(df[["Tourist Site Name", "Site Link"]][df["Tourist Site Name"] == name])
    
    return visit_html

def find_location_site(visit_html):
    
    location = []
    
    for link in visit_html["Site Link"]:
        html = requests.get(link)
        bsobj = soup(html.content, "lxml")
    
        for loc in bsobj.find_all("script", type = "application/ld+json"):
            if "streetAddress" in loc.string:
                find_part_html = loc.string.split("{")
                for street in find_part_html:
                    if "streetAddress" in street:
                        for value in street.split(","):
                            if "streetAddress" in value:
                                street_name = value.split(":")[1][1:][:-1] + ", "
                                   
                            if "addressLocality" in value:
                                city_name = value.split(":")[1][1:][:-1] + ", "
                                 
                            if "postalCode" in value:
                                zipcode = "CA " + value.split(":")[1][1:][:-1]
                            
        location_info = street_name + city_name + zipcode
        location.append(location_info)
    
    return location