from numpy import zeros, ones, pi, array

from ....Classes.Simu1 import Simu1
from ....Tests.Validation.Machine.CEFC_Lam import CEFC_Lam

from ....Classes.InputCurrent import InputCurrent
from ....Classes.ImportGenVectLin import ImportGenVectLin
from ....Classes.ImportMatrixVal import ImportMatrixVal
from ....Classes.MagFEMM import MagFEMM
from ....Classes.Output import Output
from ....Tests import save_validation_path as save_path
from os.path import join

import matplotlib.pyplot as plt
import json
import numpy as np
from ....Functions.FEMM import GROUP_SC


def test_CEFC_002():
    """Validation of the TOYOTA Prius 2004 interior magnet (V shape) with distributed winding
    50 kW peak, 400 Nm peak at 1500 rpm from publication

    from publication
    Z. Yang, M. Krishnamurthy and I. P. Brown,
    "Electromagnetic and vibrational characteristic of IPM over full torque-speed range,"
    Electric Machines & Drives Conference (IEMDC), 2013 IEEE International, Chicago, IL, 2013, pp. 295-302.
    """

    simu = Simu1(name="SM_CEFC_002_save_mag", machine=CEFC_Lam, struct=None)

    # Definition of the enforced output of the electrical module
    Nr = ImportMatrixVal(value=ones(1) * 3000)
    Is = ImportMatrixVal(value=array([[2.25353053e02, 2.25353053e02, 2.25353053e02]]))
    time = ImportGenVectLin(start=0, stop=1, num=1, endpoint=True)
    angle = ImportGenVectLin(start=0, stop=2 * pi, num=1024, endpoint=False)

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        Nr=Nr,
        angle_rotor=None,  # Will be computed
        time=time,
        angle=angle,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        is_stator_linear_BH=2,
        is_rotor_linear_BH=2,
        is_get_mesh=True,
        is_save_FEA=True,
        is_sliding_band=False,
    )

    out = Output(simu=simu)
    out.post.legend_name = "Slotless lamination"
    simu.run()

    out.plot_mesh(mesh=out.mag.meshsolution.mesh[0], title="FEA Mesh")

    # out.plot_mesh_field(meshsolution=out.mag.meshsolution, title="Permeability")
    out.plot_mesh_field(
        mesh=out.mag.meshsolution.mesh[0],
        title="Permeability",
        field=out.mag.meshsolution.solution[0].face["mu"],
    )
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_CEFC_002_save_mag"))

    # Test save with MeshSolution object in out
    out.save(save_path=save_path)

    load_path = join(save_path, "Output.json")
    # Test to load the Meshsolution object (inside the output):
    with open(load_path) as json_file:
        json_tmp = json.load(json_file)
        FEMM = Output(init_dict=json_tmp)

    # To test that the "mu" is still a ndarray after saving and loading
    out.plot_mesh_field(
        mesh=FEMM.mag.meshsolution.mesh[0],
        title="Permeability",
        field=FEMM.mag.meshsolution.solution[0].face["mu"],
    )
