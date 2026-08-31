"""
Minimal pure-Python drop-in replacement for UM-ARM-Lab `sdf_tools`.

flow_mpc only uses `utils_2d.compute_sdf_and_gradient` and
`utils_3d.compute_sdf_and_gradient` to turn a binary occupancy grid into a signed
distance field (and its gradient). The upstream package is a ROS/C++ project that
is painful to build; this replacement computes the same thing with scipy's
Euclidean distance transform, matching the API, output shapes, and sign
convention that flow_mpc depends on:

    sdf           : same shape as the grid; POSITIVE in free space,
                    NEGATIVE inside obstacles, magnitude in world units.
    sdf_gradient  : grid shape + (ndim,), one spatial-gradient component per axis.

No ROS or compilation required.
"""
