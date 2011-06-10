_delta2vi_map = {
     -1: 'h',
    -81: 'y',
    -80: 'k',
    -79: 'u',
      1: 'l',
     81: 'n',
     80: 'j',
     79: 'b'
}
def delta2vi(delta):
    global _delta2vi_map
    return _delta2vi_map[delta]

def farlook(x1, y1, x2, y2):
    """
    Generate the sequence of hjkl moves needed to go from (x1,y1) to (x2,y2)
    """

    if x1 == x2 and y1 == y2:
        return ''

    xdir = cmp(x2, x1)
    ydir = cmp(y2, y1)
    xfar = abs(x1 - x2) >= 8
    yfar = abs(y1 - y2) >= 8
    xdelta = delta2vi(xdir) if xdir else 0
    ydelta = delta2vi(80 * ydir) if ydir else 0
    xydelta = delta2vi(xdir + 80 * ydir)

    if xfar and yfar:
        return xydelta.upper() + farlook(x1 + 8 * xdir, y1 + 8 * ydir, x2, y2)
    if xfar:
        return xdelta.upper() + farlook(x1 + 8 * xdir, y1, x2, y2)
    if yfar:
        return ydelta.upper() + farlook(x1, y1 + 8 * ydir, x2, y2)

    if xdir and ydir:
        return xydelta + farlook(x1 + xdir, y1 + ydir, x2, y2)
    if xdir:
        return xdelta + farlook(x1 + xdir, y1, x2, y2)
    if ydir:
        return ydelta + farlook(x1, y1 + ydir, x2, y2)

    assert False
