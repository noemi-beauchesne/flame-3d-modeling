"""
Spatial interpolation helpers (nearest, trilinear, RBF placeholder).
Keep signatures simple so we can swap later.
"""

def nearest_neighbor(samples, query_xyz):
    """
    samples: list of (x,y,z,value). returns value at nearest point.
    """
    bx,by,bz,bv = None,None,None,None
    best = 1e99
    qx,qy,qz = query_xyz
    for x,y,z,v in samples:
        d = (x-qx)**2 + (y-qy)**2 + (z-qz)**2
        if d < best:
            best = d; bx,by,bz,bv = x,y,z,v
    return bv