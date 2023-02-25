# color_values.py
# Wilson Portugal, Lisboa, Portugal
# 25 February 2023
# 
#     this will return an array of RGB values
#     in base 10 decimal form for 139 standard
#     HTML color names
#     
#     HTML colors covered:
#         1. lightsalmon
#         2. salmon
#         3. darksalmon
#         4. lightcoral
#         5. indianred
#         6. crimson
#         7. firebrick
#         8. red
#         9. darkred
#         10. coral
#         11. tomato
#         12. orangered
#         13. gold
#         14. orange
#         15. darkorange
#         16. lightyellow
#         17. lemonchiffon
#         18. lightgoldenrodyellow
#         19. papayawhip
#         20. moccasin
#         21. peachpuff
#         22. palegoldenrod
#         23. khaki
#         24. darkkhaki
#         25. yellow
#         26. lawngreen
#         27. chartreuse
#         28. limegreen
#         29. lime
#         30. forestgreen
#         31. green
#         32. darkgreen
#         33. greenyellow
#         34. yellowgreen
#         35. springgreen
#         36. mediumspringgreen
#         37. lightgreen
#         38. palegreen
#         39. darkseagreen
#         40. mediumseagreen
#         41. seagreen
#         42. olive
#         43. darkolivegreen
#         44. olivedrab
#         45. lightcyan
#         46. cyan
#         47. aqua
#         48. aquamarine
#         49. mediumaquamarine
#         50. paleturquoise
#         51. turquoise
#         52. mediumturquoise
#         53. darkturquoise
#         54. lightseagreen
#         55. cadetblue
#         56. darkcyan
#         57. teal
#         58. powderblue
#         59. lightblue
#         60. lightskyblue
#         61. skyblue
#         62. deepskyblue
#         63. lightsteelblue
#         64. dodgerblue
#         65. cornflowerblue
#         66. steelblue
#         67. royalblue
#         68. blue
#         69. mediumblue
#         70. darkblue
#         71. navy
#         72. midnightblue
#         73. mediumslateblue
#         74. slateblue
#         75. darkslateblue
#         76. lavender
#         77. thistle
#         78. plum
#         79. violet
#         80. orchid
#         81. fuchsia
#         82. magenta
#         83. mediumorchid
#         84. mediumpurple
#         85. blueviolet
#         86. darkviolet
#         87. darkorchid
#         88. darkmagenta
#         89. purple
#         90. indigo
#         91. pink
#         92. lightpink
#         93. hotpink
#         94. deeppink
#         95. palevioletred
#         96. mediumvioletred
#         97. white
#         98. snow
#         99. honeydew
#         100. mintcream
#         101. azure
#         102. aliceblue
#         103. ghostwhite
#         104. whitesmoke
#         105. seashell
#         106. beige
#         107. oldlace
#         108. floralwhite
#         109. ivory
#         110. antiquewhite
#         111. linen
#         112. lavenderblush
#         113. mistyrose
#         114. gainsboro
#         115. lightgray
#         116. silver
#         117. darkgray
#         118. gray
#         119. dimgray
#         120. lightslategray
#         121. slategray
#         122. darkslategray
#         123. black
#         124. cornsilk
#         125. blanchedalmond
#         126. bisque
#         127. navajowhite
#         128. wheat
#         129. burlywood
#         130. tan
#         131. rosybrown
#         132. sandybrown
#         133. goldenrod
#         134. peru
#         135. chocolate
#         136. saddlebrown
#         137. sienna
#         138. brown
#         139. maroon
# 
#     Data sourced from https://www.rapidtables.com/web/color/RGB_Color.html

def get_color_value(color_name):
    color_values = (0,0,0) # default return value - black
    if color_name.lower() == 'lightsalmon':
        color_values = (255,160,122)
    if color_name.lower() == 'salmon':
        color_values = (250,128,114)
    if color_name.lower() == 'darksalmon':
        color_values = (233,150,122)
    if color_name.lower() == 'lightcoral':
        color_values = (240,128,128)
    if color_name.lower() == 'indianred':
        color_values = (205,92,92)
    if color_name.lower() == 'crimson':
        color_values = (220,20,60)
    if color_name.lower() == 'firebrick':
        color_values = (178,34,34)
    if color_name.lower() == 'red':
        color_values = (255,0,0)
    if color_name.lower() == 'darkred':
        color_values = (139,0,0)
    if color_name.lower() == 'coral':
        color_values = (255,127,80)
    if color_name.lower() == 'tomato':
        color_values = (255,99,71)
    if color_name.lower() == 'orangered':
        color_values = (255,69,0)
    if color_name.lower() == 'gold':
        color_values = (255,215,0)
    if color_name.lower() == 'orange':
        color_values = (255,165,0)
    if color_name.lower() == 'darkorange':
        color_values = (255,140,0)
    if color_name.lower() == 'lightyellow':
        color_values = (255,255,224)
    if color_name.lower() == 'lemonchiffon':
        color_values = (255,250,205)
    if color_name.lower() == 'lightgoldenrodyellow':
        color_values = (250,250,210)
    if color_name.lower() == 'papayawhip':
        color_values = (255,239,213)
    if color_name.lower() == 'moccasin':
        color_values = (255,228,181)
    if color_name.lower() == 'peachpuff':
        color_values = (255,218,185)
    if color_name.lower() == 'palegoldenrod':
        color_values = (238,232,170)
    if color_name.lower() == 'khaki':
        color_values = (240,230,140)
    if color_name.lower() == 'darkkhaki':
        color_values = (189,183,107)
    if color_name.lower() == 'yellow':
        color_values = (255,255,0)
    if color_name.lower() == 'lawngreen':
        color_values = (124,252,0)
    if color_name.lower() == 'chartreuse':
        color_values = (127,255,0)
    if color_name.lower() == 'limegreen':
        color_values = (50,205,50)
    if color_name.lower() == 'lime':
        color_values = (0,255,0)
    if color_name.lower() == 'forestgreen':
        color_values = (34,139,34)
    if color_name.lower() == 'green':
        color_values = (0,128,0)
    if color_name.lower() == 'darkgreen':
        color_values = (0,100,0)
    if color_name.lower() == 'greenyellow':
        color_values = (173,255,47)
    if color_name.lower() == 'yellowgreen':
        color_values = (154,205,50)
    if color_name.lower() == 'springgreen':
        color_values = (0,255,127)
    if color_name.lower() == 'mediumspringgreen':
        color_values = (0,250,154)
    if color_name.lower() == 'lightgreen':
        color_values = (144,238,144)
    if color_name.lower() == 'palegreen':
        color_values = (152,251,152)
    if color_name.lower() == 'darkseagreen':
        color_values = (143,188,143)
    if color_name.lower() == 'mediumseagreen':
        color_values = (60,179,113)
    if color_name.lower() == 'seagreen':
        color_values = (46,139,87)
    if color_name.lower() == 'olive':
        color_values = (128,128,0)
    if color_name.lower() == 'darkolivegreen':
        color_values = (85,107,47)
    if color_name.lower() == 'olivedrab':
        color_values = (107,142,35)
    if color_name.lower() == 'lightcyan':
        color_values = (224,255,255)
    if color_name.lower() == 'cyan':
        color_values = (0,255,255)
    if color_name.lower() == 'aqua':
        color_values = (0,255,255)
    if color_name.lower() == 'aquamarine':
        color_values = (127,255,212)
    if color_name.lower() == 'mediumaquamarine':
        color_values = (102,205,170)
    if color_name.lower() == 'paleturquoise':
        color_values = (175,238,238)
    if color_name.lower() == 'turquoise':
        color_values = (64,224,208)
    if color_name.lower() == 'mediumturquoise':
        color_values = (72,209,204)
    if color_name.lower() == 'darkturquoise':
        color_values = (0,206,209)
    if color_name.lower() == 'lightseagreen':
        color_values = (32,178,170)
    if color_name.lower() == 'cadetblue':
        color_values = (95,158,160)
    if color_name.lower() == 'darkcyan':
        color_values = (0,139,139)
    if color_name.lower() == 'teal':
        color_values = (0,128,128)
    if color_name.lower() == 'powderblue':
        color_values = (176,224,230)
    if color_name.lower() == 'lightblue':
        color_values = (173,216,230)
    if color_name.lower() == 'lightskyblue':
        color_values = (135,206,250)
    if color_name.lower() == 'skyblue':
        color_values = (135,206,235)
    if color_name.lower() == 'deepskyblue':
        color_values = (0,191,255)
    if color_name.lower() == 'lightsteelblue':
        color_values = (176,196,222)
    if color_name.lower() == 'dodgerblue':
        color_values = (30,144,255)
    if color_name.lower() == 'cornflowerblue':
        color_values = (100,149,237)
    if color_name.lower() == 'steelblue':
        color_values = (70,130,180)
    if color_name.lower() == 'royalblue':
        color_values = (65,105,225)
    if color_name.lower() == 'blue':
        color_values = (0,0,255)
    if color_name.lower() == 'mediumblue':
        color_values = (0,0,205)
    if color_name.lower() == 'darkblue':
        color_values = (0,0,139)
    if color_name.lower() == 'navy':
        color_values = (0,0,128)
    if color_name.lower() == 'midnightblue':
        color_values = (25,25,112)
    if color_name.lower() == 'mediumslateblue':
        color_values = (123,104,238)
    if color_name.lower() == 'slateblue':
        color_values = (106,90,205)
    if color_name.lower() == 'darkslateblue':
        color_values = (72,61,139)
    if color_name.lower() == 'lavender':
        color_values = (230,230,250)
    if color_name.lower() == 'thistle':
        color_values = (216,191,216)
    if color_name.lower() == 'plum':
        color_values = (221,160,221)
    if color_name.lower() == 'violet':
        color_values = (238,130,238)
    if color_name.lower() == 'orchid':
        color_values = (218,112,214)
    if color_name.lower() == 'fuchsia':
        color_values = (255,0,255)
    if color_name.lower() == 'magenta':
        color_values = (255,0,255)
    if color_name.lower() == 'mediumorchid':
        color_values = (186,85,211)
    if color_name.lower() == 'mediumpurple':
        color_values = (147,112,219)
    if color_name.lower() == 'blueviolet':
        color_values = (138,43,226)
    if color_name.lower() == 'darkviolet':
        color_values = (148,0,211)
    if color_name.lower() == 'darkorchid':
        color_values = (153,50,204)
    if color_name.lower() == 'darkmagenta':
        color_values = (139,0,139)
    if color_name.lower() == 'purple':
        color_values = (128,0,128)
    if color_name.lower() == 'indigo':
        color_values = (75,0,130)
    if color_name.lower() == 'pink':
        color_values = (255,192,203)
    if color_name.lower() == 'lightpink':
        color_values = (255,182,193)
    if color_name.lower() == 'hotpink':
        color_values = (255,105,180)
    if color_name.lower() == 'deeppink':
        color_values = (255,20,147)
    if color_name.lower() == 'palevioletred':
        color_values = (219,112,147)
    if color_name.lower() == 'mediumvioletred':
        color_values = (199,21,133)
    if color_name.lower() == 'white':
        color_values = (255,255,255)
    if color_name.lower() == 'snow':
        color_values = (255,250,250)
    if color_name.lower() == 'honeydew':
        color_values = (240,255,240)
    if color_name.lower() == 'mintcream':
        color_values = (245,255,250)
    if color_name.lower() == 'azure':
        color_values = (240,255,255)
    if color_name.lower() == 'aliceblue':
        color_values = (240,248,255)
    if color_name.lower() == 'ghostwhite':
        color_values = (248,248,255)
    if color_name.lower() == 'whitesmoke':
        color_values = (245,245,245)
    if color_name.lower() == 'seashell':
        color_values = (255,245,238)
    if color_name.lower() == 'beige':
        color_values = (245,245,220)
    if color_name.lower() == 'oldlace':
        color_values = (253,245,230)
    if color_name.lower() == 'floralwhite':
        color_values = (255,250,240)
    if color_name.lower() == 'ivory':
        color_values = (255,255,240)
    if color_name.lower() == 'antiquewhite':
        color_values = (250,235,215)
    if color_name.lower() == 'linen':
        color_values = (250,240,230)
    if color_name.lower() == 'lavenderblush':
        color_values = (255,240,245)
    if color_name.lower() == 'mistyrose':
        color_values = (255,228,225)
    if color_name.lower() == 'gainsboro':
        color_values = (220,220,220)
    if color_name.lower() == 'lightgray':
        color_values = (211,211,211)
    if color_name.lower() == 'silver':
        color_values = (192,192,192)
    if color_name.lower() == 'darkgray':
        color_values = (169,169,169)
    if color_name.lower() == 'gray':
        color_values = (128,128,128)
    if color_name.lower() == 'dimgray':
        color_values = (105,105,105)
    if color_name.lower() == 'lightslategray':
        color_values = (119,136,153)
    if color_name.lower() == 'slategray':
        color_values = (112,128,144)
    if color_name.lower() == 'darkslategray':
        color_values = (47,79,79)
    if color_name.lower() == 'black':
        color_values = (0,0,0)
    if color_name.lower() == 'cornsilk':
        color_values = (255,248,220)
    if color_name.lower() == 'blanchedalmond':
        color_values = (255,235,205)
    if color_name.lower() == 'bisque':
        color_values = (255,228,196)
    if color_name.lower() == 'navajowhite':
        color_values = (255,222,173)
    if color_name.lower() == 'wheat':
        color_values = (245,222,179)
    if color_name.lower() == 'burlywood':
        color_values = (222,184,135)
    if color_name.lower() == 'tan':
        color_values = (210,180,140)
    if color_name.lower() == 'rosybrown':
        color_values = (188,143,143)
    if color_name.lower() == 'sandybrown':
        color_values = (244,164,96)
    if color_name.lower() == 'goldenrod':
        color_values = (218,165,32)
    if color_name.lower() == 'peru':
        color_values = (205,133,63)
    if color_name.lower() == 'chocolate':
        color_values = (210,105,30)
    if color_name.lower() == 'saddlebrown':
        color_values = (139,69,19)
    if color_name.lower() == 'sienna':
        color_values = (160,82,45)
    if color_name.lower() == 'brown':
        color_values = (165,42,42)
    if color_name.lower() == 'maroon':
        color_values = (128,0,0)
    return color_values
