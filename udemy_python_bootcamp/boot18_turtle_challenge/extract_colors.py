import colorgram as cg

my_image = "boot18_TurtleChallenge\hirst.png"

color_list = cg.extract(my_image, 30)

color_palette = []

for color in color_list:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,b,g)
    color_palette.append(new_color)

print(color_palette)