# -*- coding: utf-8 -*-
#
# This file is part of the DishLeafNode project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" 

A Leaf control node for DishMaster.
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
# PROTECTED REGION ID(DishLeafNode.additionnal_import) ENABLED START #
from tango import DeviceProxy, DevState, EventType, utils, DeviceData

# PROTECTED REGION END #    //  DishLeafNode.additionnal_import

__all__ = ["DishLeafNode", "main"]


class DishLeafNode(SKABaseDevice):
    """
    A Leaf control node for DishMaster.
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(DishLeafNode.class_variable) ENABLED START #
    #_dish_proxy = device_property("DishMasterFQDN")

    class DishModeCallback (utils.EventCallback):
        def push_event(self, evt):

            if (evt.err==False):
                try:
                    self._dish_mode = evt.attr_value.value
                    if(self._dish_mode == 0):
                        print "Dish Mode :-> OFF"
                    elif (self._dish_mode == 1):
                        print "Dish Mode :-> STARTUP"
                    elif (self._dish_mode == 2):
                        print "Dish Mode :->  SHUTDOWN"
                    elif (self._dish_mode == 3):
                        print "Dish Mode :->  STANDBY-LP"
                    elif (self._dish_mode == 4):
                        print "Dish Mode :-> STANDBY-FP"
                    elif (self._dish_mode == 5):
                        print "Dish Mode :-> MAINTENANCE"
                    elif (self._dish_mode == 6):
                        print "Dish Mode :-> STOW"
                    elif (self._dish_mode == 7):
                        print "Dish Mode :-> CONFIG"
                    elif (self._dish_mode == 8):
                        print "Dish Mode :-> OPERATE"
                    else:
                        print "Dish Mode :-> UNKNOWN!\n", evt
                except Exception as e:
                    print "Unexpected error in DishModeCallback!\n", e.message
            else:
                print "Error event on subscribing DishMode attribute!\n", evt.errors

    class DishPointingStateCallback (utils.EventCallback):
        def push_event(self, evt):

            if (evt.err==False):
                try:
                    self._pointing_state = evt.attr_value.value
                    if(self._pointing_state == 0):
                        print "Dish Pointing State :-> READY"
                    elif (self._pointing_state == 1):
                        print "Dish Pointing State :-> SLEWING"
                    elif (self._pointing_state == 2):
                        print "Dish Pointing State :-> TRACKING"
                    elif (self._pointing_state == 3):
                        print "Dish Pointing State :-> SCANNING"
                    else:
                        print "Dish is in UNKNOWN pointing state!\n", evt
                except Exception as e:
                    print "Unexpected error in DishPointingStateCallback!\n", e.message
            else:
                print "Error event on subscribing PointingState attribute!\n", evt.errors


    class DishHealthStateCallback (utils.EventCallback):
        def push_event(self, evt):

            if (evt.err==False):
                try:
                    self._dish_health_state = evt.attr_value.value
                    if(self._dish_health_state == 0):
                        print "Dish Health state :-> ON-LINE"
                    elif (self._dish_health_state == 1):
                        print "Dish Health state :-> OFF-LINE"
                    elif (self._dish_health_state == 2):
                        print "Dish Health state :-> MAINTENANCE"
                    elif (self._dish_health_state == 3):
                        print "Dish Health state :-> NOT-FITTED"
                    elif (self._dish_health_state == 4):
                        print "Dish Health state :-> RESERVED"
                    else:
                        print "Dish Health state :-> UNKNOWN!\n", evt
                except Exception as e:
                    print "Unexpected error in DishHealthStateCallback!\n", e.message
            else:
                print "Error event on subscribing HealthState attribute!\n", evt.errors

    class DishCapturingCallback (utils.EventCallback):
        def push_event(self, evt):

            if (evt.err==False):
                try:
                    self._dish_capturing = evt.attr_value.value
                    if(self._dish_capturing == True):
                        print "Dish data capturing :-> TRUE"
                    elif (self._dish_capturing == False):
                        print "Dish data capturing :-> FALSE"
                    else:
                        print "Dish date capturing :-> UNKNOWN!\n", evt
                except Exception as e:
                    print "Unexpected error in DishCapturingCallback!\n", e.message
            else:
                print "Error event on subscribing Capturing attribute!\n", evt.errors

    # PROTECTED REGION END #    //  DishLeafNode.class_variable

    # -----------------
    # Device Properties
    # -----------------







    DishMasterFQDN = device_property(
        dtype='str',
        mandatory=True
    )

    # ----------
    # Attributes
    # ----------











    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        SKABaseDevice.init_device(self)
        # PROTECTED REGION ID(DishLeafNode.init_device) ENABLED START #
        print "Initializing Leaf Node..."
        self.SkaLevel=3
        self._dish_proxy = DeviceProxy(self.DishMasterFQDN)     #Creating proxy to the DishMaster
        self._admin_mode = 0                                    #Setting adminMode to "ONLINE"
        self._health_state = 0                                  #Setting healthState to "OK"
        self._simulation_mode = False                            #Enabling the simulation mode

        self.set_state(DevState.ON)

        #Subscribing to DishMaster Attributes

        dishModeCallback = self.DishModeCallback()
        dishPointingStateCallback = self.DishPointingStateCallback()
        dishHealthStateCallback = self.DishHealthStateCallback()
        dishCapturingCallback = self.DishCapturingCallback()


        try:
            self._dish_proxy.subscribe_event("dishMode", EventType.CHANGE_EVENT, dishModeCallback, stateless=True)
            self._dish_proxy.subscribe_event("pointingState", EventType.CHANGE_EVENT, dishPointingStateCallback, stateless=True)
            self._dish_proxy.subscribe_event("healthState",EventType.CHANGE_EVENT, dishHealthStateCallback, stateless=True)
            self._dish_proxy.subscribe_event("capturing",EventType.CHANGE_EVENT, dishCapturingCallback, stateless=True)
            self.set_status("Dish Leaf Node initialized successfully. Ready to accept commands!")

        except Exception as e:
            print "Exception occurred while subscribing to Dish attributes", e.message
            self.set_state(DevState.FAULT)
            self.set_status("Error occured in Dish Leaf Node initialization!")



        # PROTECTED REGION END #    //  DishLeafNode.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(DishLeafNode.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  DishLeafNode.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(DishLeafNode.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  DishLeafNode.delete_device

    # ------------------
    # Attributes methods
    # ------------------


    # --------
    # Commands
    # --------

    @command(
    )
    @DebugIt()
    def SetStowMode(self):
        # PROTECTED REGION ID(DishLeafNode.SetStowMode) ENABLED START #
        self._dish_proxy.command_inout_asynch("SetStowMode")
        pass
        # PROTECTED REGION END #    //  DishLeafNode.SetStowMode

    @command(
    )
    @DebugIt()
    def SetStandByLPMode(self):
        # PROTECTED REGION ID(DishLeafNode.SetStandByLPMode) ENABLED START #
        self._dish_proxy.command_inout_asynch("SetStandByLPMode")
        pass
        # PROTECTED REGION END #    //  DishLeafNode.SetStandByLPMode

    @command(
    )
    @DebugIt()
    def SetOperateMode(self):
        # PROTECTED REGION ID(DishLeafNode.SetOperateMode) ENABLED START #
        self._dish_proxy.command_inout_asynch("SetOperateMode")
        pass
        # PROTECTED REGION END #    //  DishLeafNode.SetOperateMode

    @command(
    dtype_in='str', 
    doc_in="Timestamp", 
    )
    @DebugIt()
    def Scan(self, argin):
        # PROTECTED REGION ID(DishLeafNode.Scan) ENABLED START #
        self._dish_proxy.command_inout_asynch("Scan", argin)
        pass
        # PROTECTED REGION END #    //  DishLeafNode.Scan

    @command(
    dtype_in='str', 
    doc_in="Timestamp", 
    )
    @DebugIt()
    def EndScan(self, argin):
        # PROTECTED REGION ID(DishLeafNode.EndScan) ENABLED START #
        print type(argin)
        self._dish_proxy.command_inout_asynch("StopCapture", argin)
        pass
        # PROTECTED REGION END #    //  DishLeafNode.EndScan

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(DishLeafNode.main) ENABLED START #
    return run((DishLeafNode,), args=args, **kwargs)
    # PROTECTED REGION END #    //  DishLeafNode.main

if __name__ == '__main__':
    main()
