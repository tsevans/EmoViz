def hex_to_rgb(hex):
    rgb_vals = tuple(map(ord, hex[1:].decode('hex')))
    return 'rgb({0},{1},{2})'.format(*rgb_vals)
