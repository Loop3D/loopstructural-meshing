from LoopStructural import GeologicalModel
from LoopStructural.datasets import load_claudius  # , load_intrusion
from loopstructuralmeshing import MeshFactory

data, bb = load_claudius()

model = GeologicalModel(bb[0, :], bb[1, :])
model.data = data
model.create_and_add_foliation("strati", interpolator="PLI", nelements=1e4)


mesh = MeshFactory.create_mesh(model.bounding_box, order=2, n_elements=1e4)
