from twilio.rest import Client

import bs4, requests

getPage = requests.get('https://www.armadillosicecreamshoppe.com/?fbclid=IwAR01ABR1pPN2_eqewG21RlT5NDyanhv__l_RBl5W-yy6quZO-jFBy0SXnnE')

getPage.raise_for_status()

page = bs4.BeautifulSoup(getPage.text, 'html.parser')
flavorOfTheDay = page.select('.simcal-event-details')

print(flavorOfTheDay)


client = Client("AC751adb6bd06c573d223cb4ce65819c2c","40b363d260fc691490ab59ddde4c8057")

client.messages.create(to="+15075129194", 
                       from_="+12057821700", 
                       body="Hello from Python!")
