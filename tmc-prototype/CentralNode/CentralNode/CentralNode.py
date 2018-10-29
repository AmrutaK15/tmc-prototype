# -*- coding: utf-8 -*-
#
# This file is part of the CentralNode project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" CentralNode

Central Node is a coordinator of the complete M&C system.
"""

# PyTango imports
import PyTango
from PyTango import DebugIt
from PyTango.server import run
from PyTango.server import Device, DeviceMeta
from PyTango.server import attribute, command
from PyTango.server import device_property
from PyTango import AttrQuality, DispLevel, DevState
from PyTango import AttrWriteType, PipeWriteType
from SKABaseDevice import SKABaseDevice
# Additional import
# PROTECTED REGION ID(CentralNode.additionnal_import) ENABLED START #
# PROTECTED REGION END #    //  CentralNode.additionnal_import

__all__ = ["CentralNode", "main"]


class CentralNode(SKABaseDevice):
    """
    Central Node is a coordinator of the complete M&C system.
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(CentralNode.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  CentralNode.class_variable

    # -----------------
    # Device Properties
    # -----------------







    CentralAlarmHandler = device_property(
        dtype='str',
    )

    TMAlarmHandler = device_property(
        dtype='str',
    )

    TMMidSubarrayNodes = device_property(
        dtype=('str',),
    )

    NumDishes = device_property(
        dtype='uint',
    )

    DishLeafNodePrefix = device_property(
        dtype='str', default_value="ska_mid/tm_leaf_node/d"
    )

    # ----------
    # Attributes
    # ----------











    telescopeHealthState = attribute(
        dtype='DevEnum',
        enum_labels=["OK", "DEGRADED", "FAILED", "UNKNOWN", ],
    )

    subarray1HealthState = attribute(
        dtype='DevEnum',
        enum_labels=["OK", "DEGRADED", "FAILED", "UNKNOWN", ],
    )

    subarray2HealthState = attribute(
        dtype='DevEnum',
        enum_labels=["OK", "DEGRADED", "FAILED", "UNKNOWN", ],
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        SKABaseDevice.init_device(self)
        # PROTECTED REGION ID(CentralNode.init_device) ENABLED START #
        self.set_state(PyTango.DevState.ON)
        # Initialise Properties
        self.SkaLevel = 1

        # Initialise Attributes
        self._health_state = 0
        self._admin_mode = 0
        self._telescope_health = 0
        self._subarray1_health_state = 0
        self._subarray2_health_state = 0
        # PROTECTED REGION END #    //  CentralNode.init_device

        #  Get Dish Leaf Node devices List
        self.db = PyTango.Database()
        self.dev_DbDatum = self.db.get_device_exported("mid_d000*/elt/master")
        self._dish_leaf_node_devices = self.dev_DbDatum.value_string

    def always_executed_hook(self):
        # PROTECTED REGION ID(CentralNode.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  CentralNode.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(CentralNode.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  CentralNode.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_telescopeHealthState(self):
        # PROTECTED REGION ID(CentralNode.telescopeHealthState_read) ENABLED START #
        if ((self._subarray1_health_state == 0) & (self._subarray2_health_state == 0)):
            self._telescope_health = 0
        elif ((self._subarray1_health_state == 2) & (self._subarray2_health_state == 2)):
            self._telescope_health = 2
        elif ((self._subarray1_health_state == 1) | (self._subarray2_health_state == 1)):
            self._telescope_health = 1
        else:
            self._telescope_health = 3

        return self._telescope_health
        # PROTECTED REGION END #    //  CentralNode.telescopeHealthState_read

    def read_subarray1HealthState(self):
        # PROTECTED REGION ID(CentralNode.subarray1HealthState_read) ENABLED START #
        #self._subarray1_proxy = PyTango.DeviceProxy("")
        #self._subarray1_health_state = self._subarray1_proxy._health_state
        return self._subarray1_health_state
        # PROTECTED REGION END #    //  CentralNode.subarray1HealthState_read

    def read_subarray2HealthState(self):
        # PROTECTED REGION ID(CentralNode.subarray2HealthState_read) ENABLED START #
        # self._subarray2_proxy = PyTango.DeviceProxy("")
        # self._subarray2_health_state = self._subarray1_proxy._health_state
        return self._subarray2_health_state
        # PROTECTED REGION END #    //  CentralNode.subarray2HealthState_read


    # --------
    # Commands
    # --------

    @command(
    dtype_in=('str',), 
    doc_in="List of Receptors to be stowed", 
    )
    @DebugIt()
    def StowAntennas(self, argin):
        # PROTECTED REGION ID(CentralNode.StowAntennas) ENABLED START #
        for name in range (0,len(self._dish_leaf_node_devices)):
            device_proxy = PyTango.DeviceProxy(self._dish_leaf_node_devices[name])
            device_proxy.command_inout("SetStowMode")
        pass
        # PROTECTED REGION END #    //  CentralNode.StowAntennas

    @command(
    )
    @DebugIt()
    def StandByTelescope(self):
        # PROTECTED REGION ID(CentralNode.StandByTelescope) ENABLED START #
        for name in range (0,len(self._dish_leaf_node_devices)):
            device_proxy = PyTango.DeviceProxy(self._dish_leaf_node_devices[name])
            device_proxy.command_inout("SetStandbyLPMode")
        pass
        # PROTECTED REGION END #    //  CentralNode.StandByTelescope

    @command(
    )
    @DebugIt()
    def StartUpTelescope(self):
        # PROTECTED REGION ID(CentralNode.StartUpTelescope) ENABLED START #
        for name in range (0,len(self._dish_leaf_node_devices)):
            device_proxy = PyTango.DeviceProxy(self._dish_leaf_node_devices[name])
            device_proxy.command_inout("SetOperateMode")

        pass
        # PROTECTED REGION END #    //  CentralNode.StartUpTelescope

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(CentralNode.main) ENABLED START #
    return run((CentralNode,), args=args, **kwargs)
    # PROTECTED REGION END #    //  CentralNode.main

if __name__ == '__main__':
    main()
