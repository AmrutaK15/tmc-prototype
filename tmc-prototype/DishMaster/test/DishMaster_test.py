#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the DishMaster project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.
"""Contain the tests for the DishMaster Simulator."""

# Path
import sys
import os
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.insert(0, os.path.abspath(path))

# Imports
from time import sleep
from mock import MagicMock
from PyTango import DevFailed, DevState
from devicetest import DeviceTestCase, main
from DishMaster import DishMaster

# Note:
#
# Since the device uses an inner thread, it is necessary to
# wait during the tests in order the let the device update itself.
# Hence, the sleep calls have to be secured enough not to produce
# any inconsistent behavior. However, the unittests need to run fast.
# Here, we use a factor 3 between the read period and the sleep calls.
#
# Look at devicetest examples for more advanced testing


# Device test case
class DishMasterDeviceTestCase(DeviceTestCase):
    """Test case for packet generation."""
    # PROTECTED REGION ID(DishMaster.test_additionnal_import) ENABLED START #
    # PROTECTED REGION END #    //  DishMaster.test_additionnal_import
    device = DishMaster
    properties = {'SkaLevel': '4', 'CentralLoggingTarget': '', 'ElementLoggingTarget': '', 'StorageLoggingTarget': 'localhost', 'MetricList': 'healthState', 'GroupDefinitions': '', 'NrSubarrays': '16', 'CapabilityTypes': '', 'MaxCapabilities': '', 'ReceptorNumber': '', 
                  }
    empty = None  # Should be []

    @classmethod
    def mocking(cls):
        """Mock external libraries."""
        # Example : Mock numpy
        # cls.numpy = DishMaster.numpy = MagicMock()
        # PROTECTED REGION ID(DishMaster.test_mocking) ENABLED START #
        # PROTECTED REGION END #    //  DishMaster.test_mocking

    def test_properties(self):
        # test the properties
        # PROTECTED REGION ID(DishMaster.test_properties) ENABLED START #
        # PROTECTED REGION END #    //  DishMaster.test_properties
        pass

    def test_State(self):
        """Test for State"""
        # PROTECTED REGION ID(DishMaster.test_State) ENABLED START #
        self.device.State()
        # PROTECTED REGION END #    //  DishMaster.test_State

    def test_Status(self):
        """Test for Status"""
        # PROTECTED REGION ID(DishMaster.test_Status) ENABLED START #
        self.device.Status()
        # PROTECTED REGION END #    //  DishMaster.test_Status

    def test_GetMetrics(self):
        """Test for GetMetrics"""
        # PROTECTED REGION ID(DishMaster.test_GetMetrics) ENABLED START #
        self.device.GetMetrics()
        # PROTECTED REGION END #    //  DishMaster.test_GetMetrics

    def test_ToJson(self):
        """Test for ToJson"""
        # PROTECTED REGION ID(DishMaster.test_ToJson) ENABLED START #
        self.device.ToJson("")
        # PROTECTED REGION END #    //  DishMaster.test_ToJson

    def test_GetVersionInfo(self):
        """Test for GetVersionInfo"""
        # PROTECTED REGION ID(DishMaster.test_GetVersionInfo) ENABLED START #
        self.device.GetVersionInfo()
        # PROTECTED REGION END #    //  DishMaster.test_GetVersionInfo

    def test_isCapabilityAchievable(self):
        """Test for isCapabilityAchievable"""
        # PROTECTED REGION ID(DishMaster.test_isCapabilityAchievable) ENABLED START #
        self.device.isCapabilityAchievable([[0], [""]])
        # PROTECTED REGION END #    //  DishMaster.test_isCapabilityAchievable

    def test_Reset(self):
        """Test for Reset"""
        # PROTECTED REGION ID(DishMaster.test_Reset) ENABLED START #
        self.device.Reset()
        # PROTECTED REGION END #    //  DishMaster.test_Reset

    def test_SetStowMode(self):
        """Test for SetStowMode"""
        # PROTECTED REGION ID(DishMaster.test_SetStowMode) ENABLED START #
        self.device.SetStowMode()
        # PROTECTED REGION END #    //  DishMaster.test_SetStowMode

    def test_SetStandbyLPMode(self):
        """Test for SetStandbyLPMode"""
        # PROTECTED REGION ID(DishMaster.test_SetStandbyLPMode) ENABLED START #
        self.device.SetStandbyLPMode()
        # PROTECTED REGION END #    //  DishMaster.test_SetStandbyLPMode

    def test_SetMaintenanceMode(self):
        """Test for SetMaintenanceMode"""
        # PROTECTED REGION ID(DishMaster.test_SetMaintenanceMode) ENABLED START #
        self.device.SetMaintenanceMode()
        # PROTECTED REGION END #    //  DishMaster.test_SetMaintenanceMode

    def test_SetOperateMode(self):
        """Test for SetOperateMode"""
        # PROTECTED REGION ID(DishMaster.test_SetOperateMode) ENABLED START #
        self.device.SetOperateMode()
        # PROTECTED REGION END #    //  DishMaster.test_SetOperateMode

    def test_Scan(self):
        """Test for Scan"""
        # PROTECTED REGION ID(DishMaster.test_Scan) ENABLED START #
        self.device.Scan("")
        # PROTECTED REGION END #    //  DishMaster.test_Scan

    def test_StartCapture(self):
        """Test for StartCapture"""
        # PROTECTED REGION ID(DishMaster.test_StartCapture) ENABLED START #
        self.device.StartCapture("")
        # PROTECTED REGION END #    //  DishMaster.test_StartCapture

    def test_StopCapture(self):
        """Test for StopCapture"""
        # PROTECTED REGION ID(DishMaster.test_StopCapture) ENABLED START #
        self.device.StopCapture("")
        # PROTECTED REGION END #    //  DishMaster.test_StopCapture

    def test_SetStandbyFPMode(self):
        """Test for SetStandbyFPMode"""
        # PROTECTED REGION ID(DishMaster.test_SetStandbyFPMode) ENABLED START #
        self.device.SetStandbyFPMode()
        # PROTECTED REGION END #    //  DishMaster.test_SetStandbyFPMode

    def test_elementLoggerAddress(self):
        """Test for elementLoggerAddress"""
        # PROTECTED REGION ID(DishMaster.test_elementLoggerAddress) ENABLED START #
        self.device.elementLoggerAddress
        # PROTECTED REGION END #    //  DishMaster.test_elementLoggerAddress

    def test_elementAlarmAddress(self):
        """Test for elementAlarmAddress"""
        # PROTECTED REGION ID(DishMaster.test_elementAlarmAddress) ENABLED START #
        self.device.elementAlarmAddress
        # PROTECTED REGION END #    //  DishMaster.test_elementAlarmAddress

    def test_elementTelStateAddress(self):
        """Test for elementTelStateAddress"""
        # PROTECTED REGION ID(DishMaster.test_elementTelStateAddress) ENABLED START #
        self.device.elementTelStateAddress
        # PROTECTED REGION END #    //  DishMaster.test_elementTelStateAddress

    def test_elementDatabaseAddress(self):
        """Test for elementDatabaseAddress"""
        # PROTECTED REGION ID(DishMaster.test_elementDatabaseAddress) ENABLED START #
        self.device.elementDatabaseAddress
        # PROTECTED REGION END #    //  DishMaster.test_elementDatabaseAddress

    def test_buildState(self):
        """Test for buildState"""
        # PROTECTED REGION ID(DishMaster.test_buildState) ENABLED START #
        self.device.buildState
        # PROTECTED REGION END #    //  DishMaster.test_buildState

    def test_versionId(self):
        """Test for versionId"""
        # PROTECTED REGION ID(DishMaster.test_versionId) ENABLED START #
        self.device.versionId
        # PROTECTED REGION END #    //  DishMaster.test_versionId

    def test_centralLoggingLevel(self):
        """Test for centralLoggingLevel"""
        # PROTECTED REGION ID(DishMaster.test_centralLoggingLevel) ENABLED START #
        self.device.centralLoggingLevel
        # PROTECTED REGION END #    //  DishMaster.test_centralLoggingLevel

    def test_elementLoggingLevel(self):
        """Test for elementLoggingLevel"""
        # PROTECTED REGION ID(DishMaster.test_elementLoggingLevel) ENABLED START #
        self.device.elementLoggingLevel
        # PROTECTED REGION END #    //  DishMaster.test_elementLoggingLevel

    def test_storageLoggingLevel(self):
        """Test for storageLoggingLevel"""
        # PROTECTED REGION ID(DishMaster.test_storageLoggingLevel) ENABLED START #
        self.device.storageLoggingLevel
        # PROTECTED REGION END #    //  DishMaster.test_storageLoggingLevel

    def test_healthState(self):
        """Test for healthState"""
        # PROTECTED REGION ID(DishMaster.test_healthState) ENABLED START #
        self.device.healthState
        # PROTECTED REGION END #    //  DishMaster.test_healthState

    def test_adminMode(self):
        """Test for adminMode"""
        # PROTECTED REGION ID(DishMaster.test_adminMode) ENABLED START #
        self.device.adminMode
        # PROTECTED REGION END #    //  DishMaster.test_adminMode

    def test_controlMode(self):
        """Test for controlMode"""
        # PROTECTED REGION ID(DishMaster.test_controlMode) ENABLED START #
        self.device.controlMode
        # PROTECTED REGION END #    //  DishMaster.test_controlMode

    def test_simulationMode(self):
        """Test for simulationMode"""
        # PROTECTED REGION ID(DishMaster.test_simulationMode) ENABLED START #
        self.device.simulationMode
        # PROTECTED REGION END #    //  DishMaster.test_simulationMode

    def test_testMode(self):
        """Test for testMode"""
        # PROTECTED REGION ID(DishMaster.test_testMode) ENABLED START #
        self.device.testMode
        # PROTECTED REGION END #    //  DishMaster.test_testMode

    def test_dishMode(self):
        """Test for dishMode"""
        # PROTECTED REGION ID(DishMaster.test_dishMode) ENABLED START #
        self.device.dishMode
        # PROTECTED REGION END #    //  DishMaster.test_dishMode

    def test_pointingState(self):
        """Test for pointingState"""
        # PROTECTED REGION ID(DishMaster.test_pointingState) ENABLED START #
        self.device.pointingState
        # PROTECTED REGION END #    //  DishMaster.test_pointingState

    def test_band1SamplerFrequency(self):
        """Test for band1SamplerFrequency"""
        # PROTECTED REGION ID(DishMaster.test_band1SamplerFrequency) ENABLED START #
        self.device.band1SamplerFrequency
        # PROTECTED REGION END #    //  DishMaster.test_band1SamplerFrequency

    def test_band2SamplerFrequency(self):
        """Test for band2SamplerFrequency"""
        # PROTECTED REGION ID(DishMaster.test_band2SamplerFrequency) ENABLED START #
        self.device.band2SamplerFrequency
        # PROTECTED REGION END #    //  DishMaster.test_band2SamplerFrequency

    def test_band3SamplerFrequency(self):
        """Test for band3SamplerFrequency"""
        # PROTECTED REGION ID(DishMaster.test_band3SamplerFrequency) ENABLED START #
        self.device.band3SamplerFrequency
        # PROTECTED REGION END #    //  DishMaster.test_band3SamplerFrequency

    def test_band4SamplerFrequency(self):
        """Test for band4SamplerFrequency"""
        # PROTECTED REGION ID(DishMaster.test_band4SamplerFrequency) ENABLED START #
        self.device.band4SamplerFrequency
        # PROTECTED REGION END #    //  DishMaster.test_band4SamplerFrequency

    def test_band5aSamplerFrequency(self):
        """Test for band5aSamplerFrequency"""
        # PROTECTED REGION ID(DishMaster.test_band5aSamplerFrequency) ENABLED START #
        self.device.band5aSamplerFrequency
        # PROTECTED REGION END #    //  DishMaster.test_band5aSamplerFrequency

    def test_band5bSamplerFrequency(self):
        """Test for band5bSamplerFrequency"""
        # PROTECTED REGION ID(DishMaster.test_band5bSamplerFrequency) ENABLED START #
        self.device.band5bSamplerFrequency
        # PROTECTED REGION END #    //  DishMaster.test_band5bSamplerFrequency

    def test_capturing(self):
        """Test for capturing"""
        # PROTECTED REGION ID(DishMaster.test_capturing) ENABLED START #
        self.device.capturing
        # PROTECTED REGION END #    //  DishMaster.test_capturing

    def test_maxCapabilities(self):
        """Test for maxCapabilities"""
        # PROTECTED REGION ID(DishMaster.test_maxCapabilities) ENABLED START #
        self.device.maxCapabilities
        # PROTECTED REGION END #    //  DishMaster.test_maxCapabilities

    def test_availableCapabilities(self):
        """Test for availableCapabilities"""
        # PROTECTED REGION ID(DishMaster.test_availableCapabilities) ENABLED START #
        self.device.availableCapabilities
        # PROTECTED REGION END #    //  DishMaster.test_availableCapabilities

    def test_desiredPointing(self):
        """Test for desiredPointing"""
        # PROTECTED REGION ID(DishMaster.test_desiredPointing) ENABLED START #
        self.device.desiredPointing
        # PROTECTED REGION END #    //  DishMaster.test_desiredPointing

    def test_achievedPointing(self):
        """Test for achievedPointing"""
        # PROTECTED REGION ID(DishMaster.test_achievedPointing) ENABLED START #
        self.device.achievedPointing
        # PROTECTED REGION END #    //  DishMaster.test_achievedPointing


# Main execution
if __name__ == "__main__":
    main()
