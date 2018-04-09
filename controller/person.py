import connexion
from db import base_db

def create_person(newPerson) -> str:
    return 'do some magic!'

def create_person_affiliation(personId, newAffiliation) -> str:
    return 'do some magic!'

def create_person_property(personId, newProperty) -> str:
    return 'do some magic!'

def delete_person(personId) -> str:
    return 'do some magic!'

def delete_person_affiliation(personId, affiliationId) -> str:
    return 'do some magic!'

def delete_person_property(personId, propertyId) -> str:
    return 'do some magic!'

def find_person_by_identity(identity) -> str:
    return 'do some magic!'

def get_person(personId) -> str:
    return 'do some magic!'

def get_person_affiliation(personId, affiliationId) -> str:
    return 'do some magic!'

def get_person_affiliations(personId) -> str:
    return 'do some magic!'

def get_person_projects(personId) -> str:
    return 'do some magic!'

def get_person_properties(personId) -> str:
    return 'do some magic!'

def get_person_property(personId, propertyId) -> str:
    return 'do some magic!'

def get_persons() -> str:
    print('hello martin')
    print(connexion.request.headers)
    return 'do some magic!'

def patch_person(personId, params) -> str:
    return 'do some magic!'

def patch_person_affiliation(personId, affiliationId, params) -> str:
    return 'do some magic!'

def patch_person_property(personId, propertyId, params) -> str:
    return 'do some magic!'

def update_person(personId, projectUpdate) -> str:
    return 'do some magic!'

def update_person_affiliation(personId, affiliationId, personAffiliationUpdate) -> str:
    return 'do some magic!'

def update_person_property(personId, propertyId, propertyUpdate) -> str:
    return 'do some magic!'

