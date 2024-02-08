from LoopStructural.interpolators.supports import UnStructuredTetMesh
from LoopStructural.interpolators.supports import P2UnstructuredTetMesh
from LoopStructural.utils import BoundingBox
import numpy as np
from . import MeshFactory

# class TetGenWrapper:


class TetGenP1(UnStructuredTetMesh):
    def __init__(self, origin=np.zeros(3), nsteps=np.ones(3) * 10, step_vector=np.ones(3)):
        self.origin = origin
        self.nsteps = nsteps
        self.step_vector = step_vector
        nelements = np.prod(nsteps) * 5
        self.bb = BoundingBox(origin=origin, nsteps=nsteps, step_vector=step_vector)
        nodes, elements, neighbours = MeshFactory.get_mesh_components(
            self.bb, n_elements=nelements, order=1
        )
        super().__init__(nodes, elements, neighbours)


class TetGenP2(P2UnstructuredTetMesh):
    def __init__(self, origin=np.zeros(3), nsteps=np.ones(3) * 10, step_vector=np.ones(3)):
        self.origin = origin
        self.nsteps = nsteps
        self.step_vector = step_vector
        nelements = np.prod(nsteps) * 5
        self.bb = BoundingBox(origin=origin, nsteps=nsteps, step_vector=step_vector)
        nodes, elements, neighbours = MeshFactory.get_mesh_components(
            self.bb, n_elements=nelements, order=2
        )
        super().__init__(nodes, elements, neighbours)


import LoopStructural
from LoopStructural.interpolators import InterpolatorType

LoopStructural.interpolators.supports.support_map[
    LoopStructural.interpolators.support_interpolator_map[InterpolatorType.PIECEWISE_QUADRATIC]
] = TetGenP2

LoopStructural.interpolators.supports.support_map[
    LoopStructural.interpolators.support_interpolator_map[InterpolatorType.PIECEWISE_LINEAR]
] = TetGenP1
