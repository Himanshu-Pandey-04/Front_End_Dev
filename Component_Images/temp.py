Str = """OS	::: ‎Android
RAM	::: ‎2 GB
Product Dimensions ::: 	‎16.49 x 0.9 x 7.71 cm; 194 Grams
Batteries ::: 	‎1 Lithium Polymer batteries required. (included)
Item model number	 ::: ‎Redmi 9A (2GB+32GB)
Wireless communication technologies ::: 	‎Bluetooth, Wi-Fi
Connectivity technologies ::: 	‎Wifi; 802.11 a/b/g/n Bluetooth v5.0 wireless technology;USB 2.0;GPS, GLONASS, BeiDou
Special features ::: 	‎Dual SIM, E-mail, Accelerometer, GPS, Ambient Light sensor, Video Player, Music Player, Proximity sensor
Display technology ::: 	‎HD+
Other display features	 ::: ‎Wireless
Device interface - primary ::: 	‎Touchscreen
Other camera features	 ::: ‎5
Audio Jack ::: 	‎3.5 mm
Form factor ::: ‎Smartphone
Colour ::: 	‎Midnight Black
Battery Power Rating ::: 	‎5000
Phone Talk Time	 ::: ‎27 Hours
Phone Standby Time (with data) ::: 	‎915 Hours
Whats in the box ::: 	‎Handset, Power Adapter, USB Cable, Sim Eject Tool, Warranty Card and User Guide
Manufacturer ::: 	‎Redmi
Country of Origin	 ::: ‎India
Item Weight	 ::: ‎194 g"""

Str2 = """Package Dimensions ‏ : ‎ 31.2 x 21.6 x 11.4 cm; 760 Grams
Date First Available ‏ : ‎ 17 December 2018
Manufacturer ‏ : ‎ Zee Footwears Pvt Ltd - Bourge
ASIN ‏ : ‎ B07LFD7FDN
Item model number ‏ : ‎ Loire-1-Grey-08
Country of Origin ‏ : ‎ India
Department ‏ : ‎ Mens
Manufacturer ‏ : ‎ Zee Footwears Pvt Ltd - Bourge, Zee Footwears Pvt Ltd - Bourge
Item Weight ‏ : ‎ 760 g
Net Quantity ‏ : ‎ 2 N
Generic Name ‏ : ‎ Running Shoes
Best Sellers Rank: #26 in Shoes & Handbags"""

def Clean(Str, delimiter = ":"):
    Features = {}
    for s in Str.split('\n'):
        def Cleaner(ele):
            ele = s.translate(s.maketrans({"\u200e":"", "\t":""}))
            return ele
        s = Cleaner(s)
        k, v = map(lambda x: x.strip(), s.split(delimiter))
        Features[k] = v
    return Features

table = Clean(Str2)

Str = ""
for fea, val in table.items():
    Str += f"\n<tr>\n<td>{fea}</td>\n<td>{val}</td>\n</tr>"
print(Str)

