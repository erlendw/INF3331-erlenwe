
import colorsys


import numpy as np
import colorsys

def _get_colors(num_colors):
    colors=[]
    for i in np.arange(0., 360., 360. / num_colors):
        hue = i/360 * 255.
        lightness = (50 + np.random.rand() * 10)/100 * 255.
        saturation = (90 + np.random.rand() * 10)/100 *255.
        colors.append(colorsys.hls_to_rgb(hue, lightness, saturation))
    return colors