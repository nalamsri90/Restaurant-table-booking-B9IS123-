from pymongo import MongoClient
import os

client = MongoClient('mongodb://localhost:27017/')
db = client['desi_dhaba']
menu_collection = db['menu']

def upload_item(category, name, description, price, image_path):
    with open(image_path, 'rb') as img_file:
        image_data = img_file.read()

    item = {
        'category': category,
        'name': name,
        'description': description,
        'price': price,
        'image': image_data
    }
    menu_collection.insert_one(item)
    

upload_item('starter', 'Chilli Paneer', 'Spicy and tangy Indo-Chinese appetizer made with paneer (Indian cottage cheese), bell peppers, and a flavorful sauce.', 6.99, 'static/starter1.jpg')
upload_item('starter', 'Veg Manchurian', 'Deep-fried vegetable balls tossed in a tangy and spicy soy-based sauce, popular in Indo-Chinese cuisine.', 7.99, 'static/starter2.jpg')
upload_item('starter', 'Chilli Chicken', 'A spicy and savory Indo-Chinese dish featuring marinated chicken pieces stir-fried with bell peppers, onions, and chilies.', 8.99, 'static/starter3.jpg')
upload_item('starter', 'Mutton Fry', 'A flavorful and spicy South Indian dish made with tender mutton pieces cooked with aromatic spices and herbs.', 10.99, 'static/starter4.jpg')
upload_item('starter', 'Prawn Fry (Royyala Vepudu)', 'A flavorful and spicy South Indian dish made with tender mutton pieces cooked with aromatic spices and herbs.', 9.99, 'static/starter4.jpg')
upload_item('main course', 'Paneer Butter Masala', 'A rich and creamy North Indian curry made with paneer cubes simmered in a buttery tomato sauce infused with aromatic spices.', 15.99, 'static/main1.jpg')
upload_item('main course', 'Gutti Vankaya Curry (Brinjal)', 'A traditional Andhra dish featuring stuffed eggplants cooked in a spicy and tangy gravy.', 15.99, 'static/main2.jpg')
upload_item('main course', 'Andhra Chicken', 'A fiery and flavorful South Indian chicken curry made with a blend of regional spices and a rich gravy.', 18.99, 'static/main3.jpg')
upload_item('main course', 'Gongura Lamb Curry', 'A tangy and spicy lamb curry from Andhra Pradesh, cooked with gongura (sorrel) leaves and a medley of spices.', 20.99, 'static/main4.jpg')
upload_item('main course', 'Andhra Lamb Curry', 'A robust and spicy lamb curry from Andhra Pradesh, known for its rich flavors and use of local spices.', 22.99, 'static/main5.jpg')
upload_item('dessert', 'Rasamalai', 'Soft paneer dumplings soaked in a creamy, cardamom-flavored milk syrup, often garnished with nuts.', 5.99, 'static/dessert1.jpg')
upload_item('dessert', 'Gulab Jamun (2pcs) & scoop of ice cream', 'Deep-fried dough balls soaked in a fragrant sugar syrup flavored with cardamom and rosewater.', 6.99, 'static/dessert2.jpg')
upload_item('dessert', 'Semiya Payasam', 'A sweet South Indian dessert made with vermicelli cooked in milk, flavored with cardamom, and garnished with nuts and raisins.', 4.99, 'static/dessert3.jpg')
upload_item('dessert', 'Jilebi', 'Crispy, spiral-shaped sweets made from fermented batter, deep-fried, and soaked in saffron-infused sugar syrup.', 4.99, 'static/dessert4.jpg')
upload_item('dessert', 'Mango Lassi', 'A refreshing and creamy yogurt-based drink blended with ripe mangoes, sugar, and a hint of cardamom.', 5.99, 'static/dessert5.jpg')