from faker import Faker

fake = Faker()

def sellerID_generator():
    generated_sellerID=fake.random_int(min=111111, max=999999)
    return generated_sellerID

def name_generator():
    generated_name=fake.random_element(['Ауди', 'Киа', 'Тойота', 'БМВ', 'Лада', 'Шкода'])
    return generated_name

def price_generator():
    generated_price = fake.random_int(min=111222, max=4333555)
    return generated_price

def likes_generator():
    generated_likes = fake.random_int(min=0, max=500)
    return generated_likes

def viewCount_generator():
    generated_viewCount = fake.random_int(min=0, max=10000)
    return generated_viewCount

def contacts_generator():
    generated_contacts = fake.random_int(min=0, max=200)
    return generated_contacts
