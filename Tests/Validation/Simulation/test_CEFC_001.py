from numpy import ones, pi, array

from ....Classes.Simu1 import Simu1
from ....Tests.Validation.Machine.CEFC_Lam import CEFC_Lam

from ....Classes.InputCurrent import InputCurrent
from ....Classes.ImportGenVectLin import ImportGenVectLin
from ....Classes.ImportMatrixVal import ImportMatrixVal

from ....Classes.MagFEMM import MagFEMM
from ....Classes.Output import Output


def test_CEFC_001():
    """Test compute the Flux in FEMM without slots and without sliding band.
    """
    simu = Simu1(name="SM_CEFC_001", machine=CEFC_Lam, struct=None)

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
        is_stator_linear_BH=2, is_rotor_linear_BH=0, is_sliding_band=False
    )

    out = Output(simu=simu)
    out.post.legend_name = "Slotless lamination"
    simu.run()
