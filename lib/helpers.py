from db.apartment import Apartment
from db.owner import Owner
from db.tenant import Tenant
from db.payment import Payment

def exit_program():
    print("Bye! Thank you for using our system")
    exit()

def list_apartments():
    apartments = Apartment.get_all()
    for apartment in apartments:
        print(apartment)

def find_apartment_by_name():
     name = input("Enter the apartment's name: ")
     apartment = Apartment.find_by_name(name)
     print(apartment) if apartment else print(
        f'Apartment {name} not found')

def find_apartment_by_id():
    apartment_id = input("Enter the apartment id: ")
    apartment = Apartment.find_by_id(apartment_id)
    print(apartment) if apartment else print(f'Apartment {apartment_id} not found')

def add_apartment():
    name = input("Enter the apartment's name: ")
    location = input("Enter the apartment's location: ")
    owner_id = input("Enter the apartment's owner id: ")
    tenant_id = input("Enter the apartment's tenant id: ")
    try:
        apartment = Apartment.create(name, location, owner_id, tenant_id)
        print(f'Success: {apartment}')
    except Exception as exc:
        print("Error Adding new apartment: ", exc)

def update_apartment():
    apartment_id = input("Enter the apartment's id: ")
    if apartment := Apartment.find_by_id(apartment_id):
        try:
            name = input("Enter the apartments's new name: ")
            apartment.name = name
            location = input("Enter the apartment's new location: ")
            apartment.location = location
            owner_id = input("Enter the apartment's new owner id: ")
            apartment.owner_id = owner_id
            tenant_id = input("Enter the apartment's new tenant id: ")
            apartment.tenant_id = tenant_id

            apartment.update()
            print(f'Success: {apartment}')
        except Exception as exc:
            print("Error updating apartment: ", exc)
    else:
        print(f'Apartment {apartment_id} not found')

def delete_apartment():
    id_ = input("Enter the apartment's id: ")
    if apartment := Apartment.find_by_id(id_):
        apartment.delete()
        print(f'Apartment {id_} deleted')
    else:
        print(f'Apartment {id_} not found')