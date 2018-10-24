# -*- coding: utf-8 -*-
#
# This file is part of the DishMaster project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" DishMaster Simulator

A TANGO device server to simulate the SKA Dish Master.
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
from SKAMaster import SKAMaster
# Additional import
# PROTECTED REGION ID(DishMaster.additionnal_import) ENABLED START #
import time
#from datetime import datetime
from threading import Timer
import threading
# PROTECTED REGION END #    //  DishMaster.additionnal_import

__all__ = ["DishMaster", "main"]


class DishMaster(SKAMaster):
    """
    A TANGO device server to simulate the SKA Dish Master.
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(DishMaster.class_variable) ENABLED START #

    # Logic to implement pointing behavior - in progress
    def point(self):
        print('Point function invoked at :-> ', time.time())
        self._achieved_pointing = self._desired_pointing
        self._pointing_state = 0

    '''    
        #self.pointThread = threading.Thread(None, self.test(), 'DishMaster')
        
        if ((self._achieved_pointing[1] != self._desired_pointing[1]) & (self._achieved_pointing[2] != self._desired_pointing[2])):
            print time.time()
            self._pointing_state = 0
            self._achieved_pointing = self._desired_pointing
            print "pointing is successful"


    def test(self):
        self._achieved_pointing[0] = time.time()
    '''
    # PROTECTED REGION END #    //  DishMaster.class_variable

    # -----------------
    # Device Properties
    # -----------------










    ReceptorNumber = device_property(
        dtype='uint',
        mandatory=True
    )

    # ----------
    # Attributes
    # ----------















    dishMode = attribute(
        dtype='DevEnum',
        enum_labels=["OFF", "STARTUP", "SHUTDOWN", "STANDBY-LP", "STANDBY-FP", "MAINTENANCE", "STOW", "CONFIG", "OPERATE", ],
    )

    pointingState = attribute(
        dtype='DevEnum',
        enum_labels=["READY", "SLEW", "TRACK", "SCAN", ],
    )

    band1SamplerFrequency = attribute(
        dtype='double',
        access=AttrWriteType.WRITE,
    )

    band2SamplerFrequency = attribute(
        dtype='double',
        access=AttrWriteType.WRITE,
    )

    band3SamplerFrequency = attribute(
        dtype='double',
        access=AttrWriteType.WRITE,
    )

    band4SamplerFrequency = attribute(
        dtype='double',
        access=AttrWriteType.WRITE,
    )

    band5aSamplerFrequency = attribute(
        dtype='double',
        access=AttrWriteType.WRITE,
    )

    band5bSamplerFrequency = attribute(
        dtype='double',
        access=AttrWriteType.WRITE,
    )

    capturing = attribute(
        dtype='bool',
    )



    desiredPointing = attribute(
        dtype=('double',),
        access=AttrWriteType.READ_WRITE,
        max_dim_x=7,
    )

    achievedPointing = attribute(
        dtype=('double',),
        max_dim_x=7,
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        SKAMaster.init_device(self)
        # PROTECTED REGION ID(DishMaster.init_device) ENABLED START #
        self._dish_mode = 3
        self._pointing_state = 1
        self._band1_sampler_frequency = 0
        self._band2_sampler_frequency = 0
        self._band3_sampler_frequency = 0
        self._band4_sampler_frequency = 0
        self._band5a_sampler_frequency = 0
        self._band5b_sampler_frequency = 0
        self._capturing = False
        self._desired_pointing = [10.0,20.0,40.0]
        self._achieved_pointing = [0.0,0.0,0.0]
        self.set_state(PyTango.DevState.STANDBY)

        #Scan command
        self._current_time = 0
        self._execution_time = 0
        self._delta_t = 0
        self._secs = 0
        # PROTECTED REGION END #    //  DishMaster.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(DishMaster.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  DishMaster.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(DishMaster.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  DishMaster.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_dishMode(self):
        # PROTECTED REGION ID(DishMaster.dishMode_read) ENABLED START #
        return self._dish_mode
        # PROTECTED REGION END #    //  DishMaster.dishMode_read

    def read_pointingState(self):
        # PROTECTED REGION ID(DishMaster.pointingState_read) ENABLED START #
        return self._pointing_state
        # PROTECTED REGION END #    //  DishMaster.pointingState_read

    def write_band1SamplerFrequency(self, value):
        # PROTECTED REGION ID(DishMaster.band1SamplerFrequency_write) ENABLED START #
        self._band1_sampler_frequency = value
        pass
        # PROTECTED REGION END #    //  DishMaster.band1SamplerFrequency_write

    def write_band2SamplerFrequency(self, value):
        # PROTECTED REGION ID(DishMaster.band2SamplerFrequency_write) ENABLED START #
        self._band2_sampler_frequency = value
        pass
        # PROTECTED REGION END #    //  DishMaster.band2SamplerFrequency_write

    def write_band3SamplerFrequency(self, value):
        # PROTECTED REGION ID(DishMaster.band3SamplerFrequency_write) ENABLED START #
        self._band3_sampler_frequency = value
        pass
        # PROTECTED REGION END #    //  DishMaster.band3SamplerFrequency_write

    def write_band4SamplerFrequency(self, value):
        # PROTECTED REGION ID(DishMaster.band4SamplerFrequency_write) ENABLED START #
        self._band4_sampler_frequency = value
        pass
        # PROTECTED REGION END #    //  DishMaster.band4SamplerFrequency_write

    def write_band5aSamplerFrequency(self, value):
        # PROTECTED REGION ID(DishMaster.band5aSamplerFrequency_write) ENABLED START #
        self._band5a_sampler_frequency = value
        pass
        # PROTECTED REGION END #    //  DishMaster.band5aSamplerFrequency_write

    def write_band5bSamplerFrequency(self, value):
        # PROTECTED REGION ID(DishMaster.band5bSamplerFrequency_write) ENABLED START #
        self._band5b_sampler_frequency = value
        pass
        # PROTECTED REGION END #    //  DishMaster.band5bSamplerFrequency_write

    def read_capturing(self):
        # PROTECTED REGION ID(DishMaster.capturing_read) ENABLED START #
        return self._capturing
        # PROTECTED REGION END #    //  DishMaster.capturing_read

    def read_desiredPointing(self):
        # PROTECTED REGION ID(DishMaster.desiredPointing_read) ENABLED START #
        return self._desired_pointing
        # PROTECTED REGION END #    //  DishMaster.desiredPointing_read

    def write_desiredPointing(self, value):
        # PROTECTED REGION ID(DishMaster.desiredPointing_write) ENABLED START #
        self._desired_pointing = value

        '''
        # Execute POINT command at given timestamp
        self._current_time = time.time()
        print self._current_time
        # self.y = self.x.replace(day= self.x.day + 0, hour=0, minute=1, second=0, microsecond=0)
        self._execution_time = self._desired_pointing[0]
        print self._execution_time
        self.delta_t = self._execution_time - self._current_time
        print self._delta_t
        # self.secs = self.delta_t.seconds + 1
        t = Timer(self._delta_t, self.point())
        print "started timer to execute command"
        t.start()
        print "command is executed"
        pass
        '''
        # PROTECTED REGION END #    //  DishMaster.desiredPointing_write

    def read_achievedPointing(self):
        # PROTECTED REGION ID(DishMaster.achievedPointing_read) ENABLED START #
        return self._achieved_pointing
        # PROTECTED REGION END #    //  DishMaster.achievedPointing_read


    # --------
    # Commands
    # --------

    @command(
    )
    @DebugIt()
    def SetStowMode(self):
        # PROTECTED REGION ID(DishMaster.SetStowMode) ENABLED START #
        self._admin_mode = 1
        self.set_state(PyTango.DevState.DISABLE)
        self._health_state = 0
        # set dishMode to STOW
        self._dish_mode = 6
        pass
        # PROTECTED REGION END #    //  DishMaster.SetStowMode

    def is_SetStowMode_allowed(self):
        # PROTECTED REGION ID(DishMaster.is_SetStowMode_allowed) ENABLED START #
        return self.get_state() not in [DevState.ON,DevState.ALARM]
        # PROTECTED REGION END #    //  DishMaster.is_SetStowMode_allowed

    @command(
    )
    @DebugIt()
    def SetStandbyLPMode(self):
        # PROTECTED REGION ID(DishMaster.SetStandbyLPMode) ENABLED START #
        self.set_state(PyTango.DevState.STANDBY)
        # set dishMode to STANDBYLP
        self._dish_mode = 3
        pass
        # PROTECTED REGION END #    //  DishMaster.SetStandbyLPMode

    @command(
    )
    @DebugIt()
    def SetMaintenanceMode(self):
        # PROTECTED REGION ID(DishMaster.SetMaintenanceMode) ENABLED START #
        self._admin_mode = 2
        self.set_state(PyTango.DevState.DISABLE)
        # set dishMode to maintenance
        self._dish_mode = 5
        pass
        # PROTECTED REGION END #    //  DishMaster.SetMaintenanceMode

    def is_SetMaintenanceMode_allowed(self):
        # PROTECTED REGION ID(DishMaster.is_SetMaintenanceMode_allowed) ENABLED START #
        return self.get_state() not in [DevState.ON,DevState.ALARM,DevState.DISABLE]
        # PROTECTED REGION END #    //  DishMaster.is_SetMaintenanceMode_allowed

    @command(
    )
    @DebugIt()
    def SetOperateMode(self):
        # PROTECTED REGION ID(DishMaster.SetOperateMode) ENABLED START #
        self._admin_mode = 0
        self.set_state(PyTango.DevState.ON)
        # set dishMode to OPERATE
        self._dish_mode = 8
        pass
        # PROTECTED REGION END #    //  DishMaster.SetOperateMode

    def is_SetOperateMode_allowed(self):
        # PROTECTED REGION ID(DishMaster.is_SetOperateMode_allowed) ENABLED START #
        return self.get_state() not in [DevState.ON,DevState.OFF,DevState.FAULT,DevState.ALARM,DevState.UNKNOWN,DevState.DISABLE]
        # PROTECTED REGION END #    //  DishMaster.is_SetOperateMode_allowed

    @command(
    dtype_in='str', 
    doc_in="The timestamp indicates the time, in UTC, at which command execution should start.", 
    )
    @DebugIt()
    def Scan(self, argin):
        # PROTECTED REGION ID(DishMaster.Scan) ENABLED START #
        print argin
        self._current_time = time.time()
        print self._current_time
        # self.y = self.x.replace(day= self.x.day + 0, hour=0, minute=1, second=0, microsecond=0)
        self._execution_time = float(argin)
        print self._execution_time
        self._delta_t = self._execution_time - self._current_time
        print self._delta_t
        # self.secs = self.delta_t.seconds + 1
        t = Timer(self._delta_t, self.point)
        print "started timer to execute command"
        t.start()
        print "command is executed"
        pass
        # PROTECTED REGION END #    //  DishMaster.Scan

    def is_Scan_allowed(self):
        # PROTECTED REGION ID(DishMaster.is_Scan_allowed) ENABLED START #
        return self.get_state() not in [DevState.OFF,DevState.FAULT,DevState.INIT,DevState.UNKNOWN,DevState.STANDBY,DevState.DISABLE]
        # PROTECTED REGION END #    //  DishMaster.is_Scan_allowed

    @command(
    dtype_in='str', 
    doc_in="The timestamp indicates the time, in UTC, at which command execution should start.", 
    )
    @DebugIt()
    def StartCapture(self, argin):
        # PROTECTED REGION ID(DishMaster.StartCapture) ENABLED START #
        self._capturing = True
        pass
        # PROTECTED REGION END #    //  DishMaster.StartCapture

    def is_StartCapture_allowed(self):
        # PROTECTED REGION ID(DishMaster.is_StartCapture_allowed) ENABLED START #
        return self.get_state() not in [DevState.OFF,DevState.FAULT,DevState.INIT,DevState.UNKNOWN,DevState.STANDBY,DevState.DISABLE]
        # PROTECTED REGION END #    //  DishMaster.is_StartCapture_allowed

    @command(
    dtype_in='str', 
    doc_in="The timestamp indicates the time, in UTC, at which command execution should start.", 
    )
    @DebugIt()
    def StopCapture(self, argin):
        # PROTECTED REGION ID(DishMaster.StopCapture) ENABLED START #
        self._capturing = False
        pass
        # PROTECTED REGION END #    //  DishMaster.StopCapture

    def is_StopCapture_allowed(self):
        # PROTECTED REGION ID(DishMaster.is_StopCapture_allowed) ENABLED START #
        return self.get_state() not in [DevState.OFF,DevState.FAULT,DevState.INIT,DevState.UNKNOWN,DevState.STANDBY,DevState.DISABLE]
        # PROTECTED REGION END #    //  DishMaster.is_StopCapture_allowed

    @command(
    )
    @DebugIt()
    def SetStandbyFPMode(self):
        # PROTECTED REGION ID(DishMaster.SetStandbyFPMode) ENABLED START #
        self.set_state(PyTango.DevState.STANDBY)
        # set dishMode to STANDBYFP
        self._dish_mode = 4
        pass
        # PROTECTED REGION END #    //  DishMaster.SetStandbyFPMode

    def is_SetStandbyFPMode_allowed(self):
        # PROTECTED REGION ID(DishMaster.is_SetStandbyFPMode_allowed) ENABLED START #
        return self.get_state() not in [DevState.UNKNOWN,DevState.DISABLE]
        # PROTECTED REGION END #    //  DishMaster.is_SetStandbyFPMode_allowed

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(DishMaster.main) ENABLED START #
    return run((DishMaster,), args=args, **kwargs)
    # PROTECTED REGION END #    //  DishMaster.main

if __name__ == '__main__':
    main()
