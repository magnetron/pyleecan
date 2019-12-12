# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot26.Ui_PWSlot26 import Ui_PWSlot26


class Gen_PWSlot26(Ui_PWSlot26):
    def setupUi(self, PWSlot26):
        Ui_PWSlot26.setupUi(self, PWSlot26)
        # Setup of in_W0
        txt = self.tr(u"""Slot isthmus width.""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr(u"""Slot isthmus width.""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr(u"""Slot isthmus height.""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr(u"""Slot isthmus height.""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)

        # Setup of in_H1
        txt = self.tr(u"""Slot depth """)
        self.in_H1.setWhatsThis(txt)
        self.in_H1.setToolTip(txt)

        # Setup of lf_H1
        self.lf_H1.validator().setBottom(0)
        txt = self.tr(u"""Slot depth """)
        self.lf_H1.setWhatsThis(txt)
        self.lf_H1.setToolTip(txt)

        # Setup of in_R1
        txt = self.tr(u"""Slot edge radius""")
        self.in_R1.setWhatsThis(txt)
        self.in_R1.setToolTip(txt)

        # Setup of lf_R1
        self.lf_R1.validator().setBottom(0)
        txt = self.tr(u"""Slot edge radius""")
        self.lf_R1.setWhatsThis(txt)
        self.lf_R1.setToolTip(txt)

        # Setup of in_R2
        txt = self.tr(u"""Slot top radius""")
        self.in_R2.setWhatsThis(txt)
        self.in_R2.setToolTip(txt)

        # Setup of lf_R2
        self.lf_R2.validator().setBottom(0)
        txt = self.tr(u"""Slot top radius""")
        self.lf_R2.setWhatsThis(txt)
        self.lf_R2.setToolTip(txt)
