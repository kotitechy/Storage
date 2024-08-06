import pywhatkit

pywhatkit.sendwhatmsg_to_group_instantly('TIMEPASS', 'HEllo every one this is an simple automated msg from python i will say jokes')
indian_dishes = [
    "Biryani",
    "Tandoori Chicken",
    "Butter Chicken (Murgh Makhani)",
    "Masala Dosa",
    "Palak Paneer",
    "Chole (Chickpea Curry)",
    "Aloo Gobi",
    "Samosa",
    "Rogan Josh",
    "Paneer Tikka",
    "Dhokla",
    "Pani Puri/Golgappa",
    "Chaat",
    "Raita",
    "Idli"
]

for i in indian_dishes:
    pywhatkit.sendwhatmsg_to_group_instantly('TIMEPASS', i)
