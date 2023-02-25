# color_pixels_waveshare_rp2040_zero.py
# william martin - lisboa, portugal - 25 february 2023
# 
# This program I wrote for a waveshare rp2040

from neopixel_value import neo_pixel
from color_values import get_color_value
from utime import sleep

def display_color(color_name):
    print(color_name)
    neo_pixel(get_color_value(color_name))
    sleep(1)

display_color('lightsalmon')
display_color('salmon')
display_color('darksalmon')
display_color('lightcoral')
display_color('indianred')
display_color('crimson')
display_color('firebrick')
display_color('red')
display_color('darkred')
display_color('coral')
display_color('tomato')
display_color('orangered')
display_color('gold')
display_color('orange')
display_color('darkorange')
display_color('lightyellow')
display_color('lemonchiffon')
display_color('lightgoldenrodyellow')
display_color('papayawhip')
display_color('moccasin')
display_color('peachpuff')
display_color('palegoldenrod')
display_color('khaki')
display_color('darkkhaki')
display_color('yellow')
display_color('lawngreen')
display_color('chartreuse')
display_color('limegreen')
display_color('lime')
display_color('forestgreen')
display_color('green')
display_color('darkgreen')
display_color('greenyellow')
display_color('yellowgreen')
display_color('springgreen')
display_color('mediumspringgreen')
display_color('lightgreen')
display_color('palegreen')
display_color('darkseagreen')
display_color('mediumseagreen')
display_color('seagreen')
display_color('olive')
display_color('darkolivegreen')
display_color('olivedrab')
display_color('lightcyan')
display_color('cyan')
display_color('aqua')
display_color('aquamarine')
display_color('mediumaquamarine')
display_color('paleturquoise')
display_color('turquoise')
display_color('mediumturquoise')
display_color('darkturquoise')
display_color('lightseagreen')
display_color('cadetblue')
display_color('darkcyan')
display_color('teal')
display_color('powderblue')
display_color('lightblue')
display_color('lightskyblue')
display_color('skyblue')
display_color('deepskyblue')
display_color('lightsteelblue')
display_color('dodgerblue')
display_color('cornflowerblue')
display_color('steelblue')
display_color('royalblue')
display_color('blue')
display_color('mediumblue')
display_color('darkblue')
display_color('navy')
display_color('midnightblue')
display_color('mediumslateblue')
display_color('slateblue')
display_color('darkslateblue')
display_color('lavender')
display_color('thistle')
display_color('plum')
display_color('violet')
display_color('orchid')
display_color('fuchsia')
display_color('magenta')
display_color('mediumorchid')
display_color('mediumpurple')
display_color('blueviolet')
display_color('darkviolet')
display_color('darkorchid')
display_color('darkmagenta')
display_color('purple')
display_color('indigo')
display_color('pink')
display_color('lightpink')
display_color('hotpink')
display_color('deeppink')
display_color('palevioletred')
display_color('mediumvioletred')
display_color('white')
display_color('snow')
display_color('honeydew')
display_color('mintcream')
display_color('azure')
display_color('aliceblue')
display_color('ghostwhite')
display_color('whitesmoke')
display_color('seashell')
display_color('beige')
display_color('oldlace')
display_color('floralwhite')
display_color('ivory')
display_color('antiquewhite')
display_color('linen')
display_color('lavenderblush')
display_color('mistyrose')
display_color('gainsboro')
display_color('lightgray')
display_color('silver')
display_color('darkgray')
display_color('gray')
display_color('dimgray')
display_color('lightslategray')
display_color('slategray')
display_color('darkslategray')
display_color('black')
display_color('cornsilk')
display_color('blanchedalmond')
display_color('bisque')
display_color('navajowhite')
display_color('wheat')
display_color('burlywood')
display_color('tan')
display_color('rosybrown')
display_color('sandybrown')
display_color('goldenrod')
display_color('peru')
display_color('chocolate')
display_color('saddlebrown')
display_color('sienna')
display_color('brown')
display_color('maroon')

neo_pixel(0)
