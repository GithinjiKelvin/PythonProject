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

        # tenants
def list_tenants():
    tenants = Tenant.get_all()
    for tenant in tenants:
        print(tenant)

def find_tenant_by_name():
     name = input("Enter the tenant's name: ")
     tenant = Tenant.find_by_name(name)
     print(tenant) if tenant else print(
        f'Tenant {name} not found')

def find_tenant_by_id():
    tenant_id = input("Enter the tenant id: ")
    tenant = Tenant.find_by_id(tenant_id)
    print(tenant) if tenant else print(f'Tenant {tenant_id} not found')

def add_tenant():
    name = input("Enter the tenant's name: ")
    age = input("Enter the tenants's age: ")
    phone_num = input("Enter the tenants's phone_num: ")
    
    try:
        tenant = Tenant.create(name, age, phone_num)
        print(f'Success: {tenant}')
    except Exception as exc:
        print("Error Adding new tenant: ", exc)

def update_tenant():
    tenant_id = input("Enter the tenant's id: ")
    if tenant := Tenant.find_by_id(tenant_id):
        try:
            name = input("Enter the tenants's new name: ")
            tenant.name = name
            age = input("Enter the tenants's new age: ")
            tenant.age = age
            phone_num = input("Enter the tenants's new phone number: ")
            tenant.phone_num = phone_num
            
            tenant.update()
            print(f'Success: {tenant}')
        except Exception as exc:
            print("Error updating tenants info: ", exc)
    else:
        print(f'Tenant {tenant_id} not found')

def delete_tenant():
    id_ = input("Enter the tenant's id: ")
    if tenant := Tenant.find_by_id(id_):
        tenant.delete()
        print(f'Tenant {id_} deleted')
    else:
        print(f'Tenant {id_} not found')