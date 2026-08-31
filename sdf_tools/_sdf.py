import numpy as np
from scipy.ndimage import distance_transform_edt


def compute_sdf_and_gradient(occupancy_grid, resolution, origin=None):
    """Signed distance field + gradient from a binary occupancy grid.

    Parameters
    ----------
    occupancy_grid : array (nD)   nonzero = occupied, zero = free
    resolution     : float        world size of one cell (meters)
    origin         : ignored      accepted for API compatibility with sdf_tools

    Returns
    -------
    sdf          : float64 array, same shape as grid. > 0 in free space,
                   < 0 inside obstacles; magnitude in world units.
    sdf_gradient : float64 array, grid.shape + (ndim,).
    """
    occ = np.asarray(occupancy_grid) > 0

    # distance_transform_edt gives, per True cell, the distance (in cells) to the
    # nearest False cell. Free-space distance uses the inverted grid; interior
    # distance uses the grid itself. Their difference is the signed field.
    dist_free = distance_transform_edt(~occ)   # >0 in free space, 0 in obstacles
    dist_obs = distance_transform_edt(occ)     # >0 inside obstacles, 0 in free
    sdf = (dist_free - dist_obs).astype(np.float64) * float(resolution)

    # gradient in world units (spacing = resolution), one component per axis,
    # stacked on a trailing axis to match sdf_tools' (grid..., ndim) layout.
    grads = np.gradient(sdf, float(resolution))
    if sdf.ndim == 1:
        grads = [grads]
    sdf_gradient = np.stack(grads, axis=-1).astype(np.float64)

    return sdf, sdf_gradient
