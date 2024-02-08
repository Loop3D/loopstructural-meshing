from LoopStructural.utils import BoundingBox
from LoopStructural.interpolators import UnStructuredTetMesh, P2UnstructuredTetMesh
import numpy as np
import meshpy.tet
from typing import Optional


class MeshFactory:
    @staticmethod
    def create_mesh(
        bounding_box: BoundingBox,
        max_volume: Optional[float] = None,
        n_elements: Optional[int] = None,
        order: int = 1,
        options: Optional[str] = None,
    ):
        """
        Create a mesh from a bounding box

        Parameters
        ----------
        bounding_box - BoundingBox
            bounding box to create mesh from
        max_volume - float
            maximum volume of tetrahedra
        n_elements - int
            number of elements to create

        Returns
        -------
        mesh - UnStructuredTetMesh
            mesh object
        """
        nodes, elements, neighbours = MeshFactory.get_mesh_components(
            bounding_box=bounding_box,
            max_volume=max_volume,
            n_elements=n_elements,
            order=order,
            options=options,
        )
        if order == 2:
            return P2UnstructuredTetMesh(nodes, elements, neighbours)
        else:
            return UnStructuredTetMesh(nodes, elements, neighbours)

    @staticmethod
    def get_mesh_components(
        bounding_box: BoundingBox,
        max_volume: Optional[float] = None,
        n_elements: Optional[int] = None,
        order: int = 1,
        options: Optional[str] = None,
    ):
        if max_volume is None and n_elements is None:
            raise ValueError("Either max_volume or n_elements must be specified")
        if max_volume is not None and n_elements is not None:
            raise ValueError("Either max_volume or n_elements must be specified")
        # convert nelements to max volume
        info = meshpy.tet.MeshInfo()
        info.set_points(bounding_box.corners)
        if max_volume is None:
            max_volume = bounding_box.volume / n_elements
        # specify the faces of the bounding box
        info.set_facets(
            [
                [0, 1, 2, 3],
                [4, 5, 6, 7],
                [0, 4, 5, 1],
                [1, 5, 6, 2],
                [2, 6, 7, 3],
                [3, 7, 4, 0],
            ]
        )

        meshpy_mesh = meshpy.tet.build(
            info,
            max_volume=max_volume,
            options=meshpy.tet.Options("pqnf", order=order),
        )
        nodes = np.array(meshpy_mesh.points)
        elements = np.array(meshpy_mesh.elements)
        neighbours = np.array(meshpy_mesh.neighbors)
        return nodes, elements, neighbours
