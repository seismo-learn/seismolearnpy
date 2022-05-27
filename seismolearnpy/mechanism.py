import numpy as np


def fault2uv(strike, dip, rake):
    """
    Determine the slip vector **u** and fault normal vector **v** from fault orientation.

    See Figure 4.20 and Equation 4.83 in Aki & Richards, 1980 for the definitions.

    Parameters
    ----------
    strike : float
        Strike direction of the fault, measured clockwise from North.
        Valid range is [0, 360) in degrees.
    dip : float
        Dip angle of the fault, measured down from the horizontal.
        Valid range is [0, 90] in degrees.
    rake : float
        Angle between the strike direction and slip.
        Valid range is (-180, 180] in degrees.

    Returns
    -------
    u : numpy.ndarray
        Slip direction vector.
    v : numpy.ndarray
        Fault normal vector.

    Examples
    --------
    >>> u, v = fault2uv(20, 30, 40)
    >>> u
    array([ 0.9102388 , -0.26109644, -0.3213938 ])
    >>> v
    array([-0.17101007,  0.46984631, -0.8660254 ])
    """
    # convert angles from degrees to radians
    strike, dip, rake = map(np.radians, (strike, dip, rake))

    sstr, sdip, srak = map(np.sin, (strike, dip, rake))
    cstr, cdip, crak = map(np.cos, (strike, dip, rake))
    # slip direction vector
    u = np.array(
        [
            crak * cstr + srak * cdip * sstr,
            crak * sstr - srak * cdip * cstr,
            -srak * sdip,
        ]
    )
    # fault normal vector
    v = np.array([-sdip * sstr, sdip * cstr, -cdip])
    return u, v
