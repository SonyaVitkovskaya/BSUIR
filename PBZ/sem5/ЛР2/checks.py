from requests import take_rows, count
import datetime
ALFABET = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0', '-']

def date_check(date):
    try: datetime.datetime.strptime(date, '%Y-%m-%d')
    except Exception: date = ""           
    finally: return date

def id_check(officer_id):
    ids = take_rows('traffic_police_officer', "id")
    try: 
        if (int(officer_id),) in ids: return officer_id
        else: return 0
    except Exception: return 0

def lisence_number_check(license_number):
    result = license_number[0] if license_number[0] in ALFABET[26:] else ""
    if len(license_number) == 9:
        for elem in license_number[1:3]:
            if elem in ALFABET[0:26] and license_number[0] in ALFABET[26:]: result+= elem
        for elem in license_number[3:]:
            if elem in ALFABET[26:]: result+= elem
        if len(result) < 9: result = ''
    else: result = ''
    license_numbers = take_rows('owner', "license_number")
    if (result,) in license_numbers: result = ""
    return result

def reg_license_plate_number(license_plate_number):
    license_plate_numbers = take_rows('auto', "license_plate_number")
    if (license_plate_number,) in license_plate_numbers: return license_plate_number
    return ""    

def reg_owner_license(owner_license):
    owner_licenses = take_rows('owner', "license_number")
    if (owner_license,) in owner_licenses: return owner_license
    return ""

def lisence_plate_number_check(lisence_plate_number):
    result = ''
    if len(lisence_plate_number) == 8:
        for elem in lisence_plate_number:
            if elem in ALFABET: result+= elem
        if len(result) < 8: result = ''
    else: result = ''
    return result

def reg_engine_number(engine_number):
    engine_numbers = take_rows('auto', "engine_number")
    if (engine_number,) in engine_numbers: return ""
    return engine_number

def not_reg_engine_number(engine_number):
    engine_numbers = take_rows('auto', "engine_number")
    if (engine_number,) in engine_numbers: return engine_number
    return ""

def passport_number_check(passport_number):
    result = ''
    if len(passport_number) == 9:
        for elem in passport_number[0:3]:
            if elem in ALFABET[0:26]: result+= elem
        for elem in passport_number[3:]:
            if elem in ALFABET[26:]: result+= elem
        if len(result) < 8: result = ''
    else: result = ''
    passport_numbers = take_rows('auto', "passport_number")
    if (result,) in passport_numbers: result = ''
    return result

def check_off_work(id, date):
    if count("inspection_history", f'date = {date} and officer_id = {id}') < 10: return 1
    return 0 