import colorgram

colors = colorgram.extract("image.jpg", 10) # extract the colors of the image

def rgb_tuple_list(list_colors: list):
    rgb_list = [] # list of rgb

    for i in range(len(list_colors)):

        i_color = colors[i]
        rgb = i_color.rgb

        rgb_tuple = (rgb.r, rgb.g, rgb.b)

        rgb_list.append(rgb_tuple)

    return rgb_list

colors_tuple = rgb_tuple_list(colors)

print(colors_tuple)

color_list = [(243, 243, 245), (244, 241, 233), (48, 95, 140), (215, 154, 104), (163, 80, 44), (234, 242, 238)]