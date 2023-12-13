from LoopStructural import GeologicalModel
from LoopStructural.datasets import load_claudius  # , load_intrusion
from loopstructuralmeshing import MeshFactory

data, bb = load_claudius()

model = GeologicalModel(bb[0, :], bb[1, :])

mesh = MeshFactory.create_mesh(model.bounding_box, order=1, n_elements=1e4)

mesh.