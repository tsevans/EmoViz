def hex_to_rgb(hex_color):
    """
    Convert hex string to rgb format.
    :param hex_color:
    :return:
    """
    rgb_vals = tuple(map(ord, hex_color[1:].decode('hex')))
    return 'rgb({0},{1},{2})'.format(*rgb_vals)
