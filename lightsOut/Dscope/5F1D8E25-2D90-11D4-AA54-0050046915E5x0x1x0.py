# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
# From type library 'DScope.exe'
# On Thu Mar  8 16:23:30 2018
'dScope Series III'
makepy_version = '0.5.01'
python_version = 0x30604f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{5F1D8E25-2D90-11D4-AA54-0050046915E5}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IAnalogueInputs(DispatchBaseClass):
	CLSID = IID('{E302BAC9-E4DC-11D1-91DD-70AB00C10000}')
	coclass_clsid = IID('{E302BACB-E4DC-11D1-91DD-70AB00C10000}')

	_prop_map_get_ = {
		"AI_ActualSampleRate": (13, 2, (5, 0), (), "AI_ActualSampleRate", None),
		"AI_AutoAdjustRanges": (28, 2, (11, 0), (), "AI_AutoAdjustRanges", None),
		"AI_AutoRange": (20, 2, (11, 0), (), "AI_AutoRange", None),
		"AI_IMPEDANCE_100K": (16, 2, (2, 0), (), "AI_IMPEDANCE_100K", None),
		"AI_IMPEDANCE_150R": (17, 2, (2, 0), (), "AI_IMPEDANCE_150R", None),
		"AI_IMPEDANCE_200R": (18, 2, (2, 0), (), "AI_IMPEDANCE_200R", None),
		"AI_IMPEDANCE_600R": (19, 2, (2, 0), (), "AI_IMPEDANCE_600R", None),
		"AI_Impedance": (15, 2, (2, 0), (), "AI_Impedance", None),
		"AI_OverrideManualRange": (27, 2, (11, 0), (), "AI_OverrideManualRange", None),
		"AI_RANGESTEPSIZE_COARSE": (32, 2, (2, 0), (), "AI_RANGESTEPSIZE_COARSE", None),
		"AI_RANGESTEPSIZE_FINE": (30, 2, (2, 0), (), "AI_RANGESTEPSIZE_FINE", None),
		"AI_RANGESTEPSIZE_MEDIUM": (31, 2, (2, 0), (), "AI_RANGESTEPSIZE_MEDIUM", None),
		"AI_Range": (21, 2, (5, 0), (), "AI_Range", None),
		"AI_RangeChA": (22, 2, (5, 0), (), "AI_RangeChA", None),
		"AI_RangeChB": (23, 2, (5, 0), (), "AI_RangeChB", None),
		"AI_RangeOverriddenChA": (24, 2, (11, 0), (), "AI_RangeOverriddenChA", None),
		"AI_RangeOverriddenChB": (25, 2, (11, 0), (), "AI_RangeOverriddenChB", None),
		"AI_RangeStepSize": (29, 2, (2, 0), (), "AI_RangeStepSize", None),
		"AI_RangesTied": (26, 2, (11, 0), (), "AI_RangesTied", None),
		"AI_SAMPLERATE_192": (12, 2, (3, 0), (), "AI_SAMPLERATE_192", None),
		"AI_SAMPLERATE_48": (10, 2, (3, 0), (), "AI_SAMPLERATE_48", None),
		"AI_SAMPLERATE_96": (11, 2, (3, 0), (), "AI_SAMPLERATE_96", None),
		"AI_SOURCE_BAL_UNBAL": (2, 2, (2, 0), (), "AI_SOURCE_BAL_UNBAL", None),
		"AI_SOURCE_CHA": (6, 2, (2, 0), (), "AI_SOURCE_CHA", None),
		"AI_SOURCE_CHB": (7, 2, (2, 0), (), "AI_SOURCE_CHB", None),
		"AI_SOURCE_COMMONMODE": (8, 2, (2, 0), (), "AI_SOURCE_COMMONMODE", None),
		"AI_SOURCE_GENOUTPUT": (5, 2, (2, 0), (), "AI_SOURCE_GENOUTPUT", None),
		"AI_SOURCE_JITTERDEMOD_DATA": (4, 2, (2, 0), (), "AI_SOURCE_JITTERDEMOD_DATA", None),
		"AI_SOURCE_JITTERDEMOD_FS": (3, 2, (2, 0), (), "AI_SOURCE_JITTERDEMOD_FS", None),
		"AI_SampleRate": (9, 2, (3, 0), (), "AI_SampleRate", None),
		"AI_SampleRatesTied": (14, 2, (11, 0), (), "AI_SampleRatesTied", None),
		"AI_Source": (1, 2, (2, 0), (), "AI_Source", None),
	}
	_prop_map_put_ = {
		"AI_ActualSampleRate" : ((13, LCID, 4, 0),()),
		"AI_AutoAdjustRanges" : ((28, LCID, 4, 0),()),
		"AI_AutoRange" : ((20, LCID, 4, 0),()),
		"AI_IMPEDANCE_100K" : ((16, LCID, 4, 0),()),
		"AI_IMPEDANCE_150R" : ((17, LCID, 4, 0),()),
		"AI_IMPEDANCE_200R" : ((18, LCID, 4, 0),()),
		"AI_IMPEDANCE_600R" : ((19, LCID, 4, 0),()),
		"AI_Impedance" : ((15, LCID, 4, 0),()),
		"AI_OverrideManualRange" : ((27, LCID, 4, 0),()),
		"AI_RANGESTEPSIZE_COARSE" : ((32, LCID, 4, 0),()),
		"AI_RANGESTEPSIZE_FINE" : ((30, LCID, 4, 0),()),
		"AI_RANGESTEPSIZE_MEDIUM" : ((31, LCID, 4, 0),()),
		"AI_Range" : ((21, LCID, 4, 0),()),
		"AI_RangeChA" : ((22, LCID, 4, 0),()),
		"AI_RangeChB" : ((23, LCID, 4, 0),()),
		"AI_RangeOverriddenChA" : ((24, LCID, 4, 0),()),
		"AI_RangeOverriddenChB" : ((25, LCID, 4, 0),()),
		"AI_RangeStepSize" : ((29, LCID, 4, 0),()),
		"AI_RangesTied" : ((26, LCID, 4, 0),()),
		"AI_SAMPLERATE_192" : ((12, LCID, 4, 0),()),
		"AI_SAMPLERATE_48" : ((10, LCID, 4, 0),()),
		"AI_SAMPLERATE_96" : ((11, LCID, 4, 0),()),
		"AI_SOURCE_BAL_UNBAL" : ((2, LCID, 4, 0),()),
		"AI_SOURCE_CHA" : ((6, LCID, 4, 0),()),
		"AI_SOURCE_CHB" : ((7, LCID, 4, 0),()),
		"AI_SOURCE_COMMONMODE" : ((8, LCID, 4, 0),()),
		"AI_SOURCE_GENOUTPUT" : ((5, LCID, 4, 0),()),
		"AI_SOURCE_JITTERDEMOD_DATA" : ((4, LCID, 4, 0),()),
		"AI_SOURCE_JITTERDEMOD_FS" : ((3, LCID, 4, 0),()),
		"AI_SampleRate" : ((9, LCID, 4, 0),()),
		"AI_SampleRatesTied" : ((14, LCID, 4, 0),()),
		"AI_Source" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IAnalogueOutputs(DispatchBaseClass):
	CLSID = IID('{C8EA98A3-E3F7-11D1-91DD-70AB00C10000}')
	coclass_clsid = IID('{C8EA98A5-E3F7-11D1-91DD-70AB00C10000}')

	_prop_map_get_ = {
		"AO_ActualSampleRate": (12, 2, (5, 0), (), "AO_ActualSampleRate", None),
		"AO_GROUNDING_CHASSIS": (26, 2, (2, 0), (), "AO_GROUNDING_CHASSIS", None),
		"AO_GROUNDING_FLOATING": (25, 2, (2, 0), (), "AO_GROUNDING_FLOATING", None),
		"AO_Grounding": (24, 2, (2, 0), (), "AO_Grounding", None),
		"AO_IMPEDANCE_BAL_150R": (20, 2, (2, 0), (), "AO_IMPEDANCE_BAL_150R", None),
		"AO_IMPEDANCE_BAL_200R": (21, 2, (2, 0), (), "AO_IMPEDANCE_BAL_200R", None),
		"AO_IMPEDANCE_BAL_50R": (19, 2, (2, 0), (), "AO_IMPEDANCE_BAL_50R", None),
		"AO_IMPEDANCE_BAL_600R": (22, 2, (2, 0), (), "AO_IMPEDANCE_BAL_600R", None),
		"AO_IMPEDANCE_BAL_ASYMMETRIC": (23, 2, (2, 0), (), "AO_IMPEDANCE_BAL_ASYMMETRIC", None),
		"AO_IMPEDANCE_BAL_MIN": (18, 2, (2, 0), (), "AO_IMPEDANCE_BAL_MIN", None),
		"AO_IMPEDANCE_UNBAL_25R": (16, 2, (2, 0), (), "AO_IMPEDANCE_UNBAL_25R", None),
		"AO_IMPEDANCE_UNBAL_600R": (17, 2, (2, 0), (), "AO_IMPEDANCE_UNBAL_600R", None),
		"AO_IMPEDANCE_UNBAL_MIN": (15, 2, (2, 0), (), "AO_IMPEDANCE_UNBAL_MIN", None),
		"AO_Impedance": (14, 2, (2, 0), (), "AO_Impedance", None),
		"AO_Mute": (1, 2, (11, 0), (), "AO_Mute", None),
		"AO_MuteChA": (2, 2, (11, 0), (), "AO_MuteChA", None),
		"AO_MuteChB": (3, 2, (11, 0), (), "AO_MuteChB", None),
		"AO_OUTPUT_BALCOMMONMODE": (6, 2, (2, 0), (), "AO_OUTPUT_BALCOMMONMODE", None),
		"AO_OUTPUT_BALNORMAL": (5, 2, (2, 0), (), "AO_OUTPUT_BALNORMAL", None),
		"AO_OUTPUT_UNBAL": (7, 2, (2, 0), (), "AO_OUTPUT_UNBAL", None),
		"AO_Output": (4, 2, (2, 0), (), "AO_Output", None),
		"AO_SAMPLERATE_192": (11, 2, (3, 0), (), "AO_SAMPLERATE_192", None),
		"AO_SAMPLERATE_48": (9, 2, (3, 0), (), "AO_SAMPLERATE_48", None),
		"AO_SAMPLERATE_96": (10, 2, (3, 0), (), "AO_SAMPLERATE_96", None),
		"AO_SampleRate": (8, 2, (3, 0), (), "AO_SampleRate", None),
		"AO_SampleRatesTied": (13, 2, (11, 0), (), "AO_SampleRatesTied", None),
	}
	_prop_map_put_ = {
		"AO_ActualSampleRate" : ((12, LCID, 4, 0),()),
		"AO_GROUNDING_CHASSIS" : ((26, LCID, 4, 0),()),
		"AO_GROUNDING_FLOATING" : ((25, LCID, 4, 0),()),
		"AO_Grounding" : ((24, LCID, 4, 0),()),
		"AO_IMPEDANCE_BAL_150R" : ((20, LCID, 4, 0),()),
		"AO_IMPEDANCE_BAL_200R" : ((21, LCID, 4, 0),()),
		"AO_IMPEDANCE_BAL_50R" : ((19, LCID, 4, 0),()),
		"AO_IMPEDANCE_BAL_600R" : ((22, LCID, 4, 0),()),
		"AO_IMPEDANCE_BAL_ASYMMETRIC" : ((23, LCID, 4, 0),()),
		"AO_IMPEDANCE_BAL_MIN" : ((18, LCID, 4, 0),()),
		"AO_IMPEDANCE_UNBAL_25R" : ((16, LCID, 4, 0),()),
		"AO_IMPEDANCE_UNBAL_600R" : ((17, LCID, 4, 0),()),
		"AO_IMPEDANCE_UNBAL_MIN" : ((15, LCID, 4, 0),()),
		"AO_Impedance" : ((14, LCID, 4, 0),()),
		"AO_Mute" : ((1, LCID, 4, 0),()),
		"AO_MuteChA" : ((2, LCID, 4, 0),()),
		"AO_MuteChB" : ((3, LCID, 4, 0),()),
		"AO_OUTPUT_BALCOMMONMODE" : ((6, LCID, 4, 0),()),
		"AO_OUTPUT_BALNORMAL" : ((5, LCID, 4, 0),()),
		"AO_OUTPUT_UNBAL" : ((7, LCID, 4, 0),()),
		"AO_Output" : ((4, LCID, 4, 0),()),
		"AO_SAMPLERATE_192" : ((11, LCID, 4, 0),()),
		"AO_SAMPLERATE_48" : ((9, LCID, 4, 0),()),
		"AO_SAMPLERATE_96" : ((10, LCID, 4, 0),()),
		"AO_SampleRate" : ((8, LCID, 4, 0),()),
		"AO_SampleRatesTied" : ((13, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IAnalyzer(DispatchBaseClass):
	CLSID = IID('{8E6A399F-C230-11D1-91DD-70AB00C10000}')
	coclass_clsid = IID('{8E6A39A1-C230-11D1-91DD-70AB00C10000}')

	def CreateFFTDetector(self):
		'CreateFFTDetector'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (2, 0), (),)

	def RemoveFFTDetector(self, sDetectorID=defaultNamedNotOptArg):
		'RemoveFFTDetector'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((2, 0),),sDetectorID
			)

	def SetFFTDetector(self, sDetectorID=defaultNamedNotOptArg):
		'SetFFTDetector'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((2, 0),),sDetectorID
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IAutomation(DispatchBaseClass):
	CLSID = IID('{D0309162-171D-11D2-91DE-70AB00C10000}')
	coclass_clsid = IID('{21973E01-D1B6-11D4-AA54-0050046915E5}')

	def AUT_RunScript(self, lpszScript=defaultNamedNotOptArg):
		'AUT_RunScript'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 0),),lpszScript
			)

	def AUT_StopScript(self):
		'AUT_StopScript'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

	def SCR_RunScript(self, lpszScript=defaultNamedNotOptArg):
		'AUT_RunScript'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((8, 0),),lpszScript
			)

	def SCR_StopScript(self):
		'AUT_StopScript'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ICTDetector(DispatchBaseClass):
	CLSID = IID('{E76688E1-1596-11D2-91DE-70AB00C10000}')
	coclass_clsid = IID('{E76688E3-1596-11D2-91DE-70AB00C10000}')

	_prop_map_get_ = {
		"CTD_BPBRBANDWIDTH_12": (13, 2, (2, 0), (), "CTD_BPBRBANDWIDTH_12", None),
		"CTD_BPBRBANDWIDTH_24": (14, 2, (2, 0), (), "CTD_BPBRBANDWIDTH_24", None),
		"CTD_BPBRBANDWIDTH_3": (11, 2, (2, 0), (), "CTD_BPBRBANDWIDTH_3", None),
		"CTD_BPBRBANDWIDTH_6": (12, 2, (2, 0), (), "CTD_BPBRBANDWIDTH_6", None),
		"CTD_BPBRBandwidth": (10, 2, (2, 0), (), "CTD_BPBRBandwidth", None),
		"CTD_BPBRFREQMODE_FIXED": (19, 2, (2, 0), (), "CTD_BPBRFREQMODE_FIXED", None),
		"CTD_BPBRFREQMODE_GEN": (17, 2, (2, 0), (), "CTD_BPBRFREQMODE_GEN", None),
		"CTD_BPBRFREQMODE_GENOTHER": (18, 2, (2, 0), (), "CTD_BPBRFREQMODE_GENOTHER", None),
		"CTD_BPBRFREQMODE_IMDDIFF": (20, 2, (2, 0), (), "CTD_BPBRFREQMODE_IMDDIFF", None),
		"CTD_BPBRFREQMODE_INPUT": (16, 2, (2, 0), (), "CTD_BPBRFREQMODE_INPUT", None),
		"CTD_BPBRFreq": (21, 2, (5, 0), (), "CTD_BPBRFreq", None),
		"CTD_BPBRFreqMode": (15, 2, (2, 0), (), "CTD_BPBRFreqMode", None),
		"CTD_BPBRMODE_BP": (7, 2, (2, 0), (), "CTD_BPBRMODE_BP", None),
		"CTD_BPBRMODE_BR": (8, 2, (2, 0), (), "CTD_BPBRMODE_BR", None),
		"CTD_BPBRMODE_IMD": (9, 2, (2, 0), (), "CTD_BPBRMODE_IMD", None),
		"CTD_BPBRMODE_OFF": (6, 2, (2, 0), (), "CTD_BPBRMODE_OFF", None),
		"CTD_BPBRMode": (5, 2, (2, 0), (), "CTD_BPBRMode", None),
		"CTD_ChA": (2, 2, (5, 0), (), "CTD_ChA", None),
		"CTD_ChB": (3, 2, (5, 0), (), "CTD_ChB", None),
		"CTD_Function": (1, 2, (8, 0), (), "CTD_Function", None),
		"CTD_HPFilter": (22, 2, (2, 0), (), "CTD_HPFilter", None),
		"CTD_HPFilterFreq": (23, 2, (3, 0), (), "CTD_HPFilterFreq", None),
		"CTD_HP_100HZ": (28, 2, (2, 0), (), "CTD_HP_100HZ", None),
		"CTD_HP_10HZ": (26, 2, (2, 0), (), "CTD_HP_10HZ", None),
		"CTD_HP_22HZ": (27, 2, (2, 0), (), "CTD_HP_22HZ", None),
		"CTD_HP_400HZ": (29, 2, (2, 0), (), "CTD_HP_400HZ", None),
		"CTD_HP_DCB": (25, 2, (2, 0), (), "CTD_HP_DCB", None),
		"CTD_HP_DEFAULT": (30, 2, (2, 0), (), "CTD_HP_DEFAULT", None),
		"CTD_HP_OFF": (24, 2, (2, 0), (), "CTD_HP_OFF", None),
		"CTD_LPFilter": (31, 2, (2, 0), (), "CTD_LPFilter", None),
		"CTD_LPFilterFreq": (32, 2, (3, 0), (), "CTD_LPFilterFreq", None),
		"CTD_LP_20KHZ_AES17": (38, 2, (2, 0), (), "CTD_LP_20KHZ_AES17", None),
		"CTD_LP_22KHZ": (34, 2, (2, 0), (), "CTD_LP_22KHZ", None),
		"CTD_LP_30KHZ": (35, 2, (2, 0), (), "CTD_LP_30KHZ", None),
		"CTD_LP_40KHZ": (36, 2, (2, 0), (), "CTD_LP_40KHZ", None),
		"CTD_LP_80KHZ": (37, 2, (2, 0), (), "CTD_LP_80KHZ", None),
		"CTD_LP_DEFAULT": (39, 2, (2, 0), (), "CTD_LP_DEFAULT", None),
		"CTD_LP_OFF": (33, 2, (2, 0), (), "CTD_LP_OFF", None),
		"CTD_RELATIVITY_ABS": (53, 2, (2, 0), (), "CTD_RELATIVITY_ABS", None),
		"CTD_RELATIVITY_CHANNEL": (56, 2, (2, 0), (), "CTD_RELATIVITY_CHANNEL", None),
		"CTD_RELATIVITY_GEN": (55, 2, (2, 0), (), "CTD_RELATIVITY_GEN", None),
		"CTD_RELATIVITY_SELF": (54, 2, (2, 0), (), "CTD_RELATIVITY_SELF", None),
		"CTD_RESPONSE_PEAK": (49, 2, (2, 0), (), "CTD_RESPONSE_PEAK", None),
		"CTD_RESPONSE_PEAKSAMPLE": (50, 2, (2, 0), (), "CTD_RESPONSE_PEAKSAMPLE", None),
		"CTD_RESPONSE_QPEAK": (51, 2, (2, 0), (), "CTD_RESPONSE_QPEAK", None),
		"CTD_RESPONSE_RMS": (48, 2, (2, 0), (), "CTD_RESPONSE_RMS", None),
		"CTD_Relativity": (52, 2, (2, 0), (), "CTD_Relativity", None),
		"CTD_Response": (47, 2, (2, 0), (), "CTD_Response", None),
		"CTD_Unit": (4, 2, (2, 0), (), "CTD_Unit", None),
		"CTD_WEIGHTING_AWEIGHTING": (42, 2, (2, 0), (), "CTD_WEIGHTING_AWEIGHTING", None),
		"CTD_WEIGHTING_CCIR468_1K": (44, 2, (2, 0), (), "CTD_WEIGHTING_CCIR468_1K", None),
		"CTD_WEIGHTING_CCIR468_2K": (45, 2, (2, 0), (), "CTD_WEIGHTING_CCIR468_2K", None),
		"CTD_WEIGHTING_CWEIGHTING": (43, 2, (2, 0), (), "CTD_WEIGHTING_CWEIGHTING", None),
		"CTD_WEIGHTING_DEFAULT": (46, 2, (2, 0), (), "CTD_WEIGHTING_DEFAULT", None),
		"CTD_WEIGHTING_NONE": (41, 2, (2, 0), (), "CTD_WEIGHTING_NONE", None),
		"CTD_WeightingFilter": (40, 2, (2, 0), (), "CTD_WeightingFilter", None),
	}
	_prop_map_put_ = {
		"CTD_BPBRBANDWIDTH_12" : ((13, LCID, 4, 0),()),
		"CTD_BPBRBANDWIDTH_24" : ((14, LCID, 4, 0),()),
		"CTD_BPBRBANDWIDTH_3" : ((11, LCID, 4, 0),()),
		"CTD_BPBRBANDWIDTH_6" : ((12, LCID, 4, 0),()),
		"CTD_BPBRBandwidth" : ((10, LCID, 4, 0),()),
		"CTD_BPBRFREQMODE_FIXED" : ((19, LCID, 4, 0),()),
		"CTD_BPBRFREQMODE_GEN" : ((17, LCID, 4, 0),()),
		"CTD_BPBRFREQMODE_GENOTHER" : ((18, LCID, 4, 0),()),
		"CTD_BPBRFREQMODE_IMDDIFF" : ((20, LCID, 4, 0),()),
		"CTD_BPBRFREQMODE_INPUT" : ((16, LCID, 4, 0),()),
		"CTD_BPBRFreq" : ((21, LCID, 4, 0),()),
		"CTD_BPBRFreqMode" : ((15, LCID, 4, 0),()),
		"CTD_BPBRMODE_BP" : ((7, LCID, 4, 0),()),
		"CTD_BPBRMODE_BR" : ((8, LCID, 4, 0),()),
		"CTD_BPBRMODE_IMD" : ((9, LCID, 4, 0),()),
		"CTD_BPBRMODE_OFF" : ((6, LCID, 4, 0),()),
		"CTD_BPBRMode" : ((5, LCID, 4, 0),()),
		"CTD_ChA" : ((2, LCID, 4, 0),()),
		"CTD_ChB" : ((3, LCID, 4, 0),()),
		"CTD_Function" : ((1, LCID, 4, 0),()),
		"CTD_HPFilter" : ((22, LCID, 4, 0),()),
		"CTD_HPFilterFreq" : ((23, LCID, 4, 0),()),
		"CTD_HP_100HZ" : ((28, LCID, 4, 0),()),
		"CTD_HP_10HZ" : ((26, LCID, 4, 0),()),
		"CTD_HP_22HZ" : ((27, LCID, 4, 0),()),
		"CTD_HP_400HZ" : ((29, LCID, 4, 0),()),
		"CTD_HP_DCB" : ((25, LCID, 4, 0),()),
		"CTD_HP_DEFAULT" : ((30, LCID, 4, 0),()),
		"CTD_HP_OFF" : ((24, LCID, 4, 0),()),
		"CTD_LPFilter" : ((31, LCID, 4, 0),()),
		"CTD_LPFilterFreq" : ((32, LCID, 4, 0),()),
		"CTD_LP_20KHZ_AES17" : ((38, LCID, 4, 0),()),
		"CTD_LP_22KHZ" : ((34, LCID, 4, 0),()),
		"CTD_LP_30KHZ" : ((35, LCID, 4, 0),()),
		"CTD_LP_40KHZ" : ((36, LCID, 4, 0),()),
		"CTD_LP_80KHZ" : ((37, LCID, 4, 0),()),
		"CTD_LP_DEFAULT" : ((39, LCID, 4, 0),()),
		"CTD_LP_OFF" : ((33, LCID, 4, 0),()),
		"CTD_RELATIVITY_ABS" : ((53, LCID, 4, 0),()),
		"CTD_RELATIVITY_CHANNEL" : ((56, LCID, 4, 0),()),
		"CTD_RELATIVITY_GEN" : ((55, LCID, 4, 0),()),
		"CTD_RELATIVITY_SELF" : ((54, LCID, 4, 0),()),
		"CTD_RESPONSE_PEAK" : ((49, LCID, 4, 0),()),
		"CTD_RESPONSE_PEAKSAMPLE" : ((50, LCID, 4, 0),()),
		"CTD_RESPONSE_QPEAK" : ((51, LCID, 4, 0),()),
		"CTD_RESPONSE_RMS" : ((48, LCID, 4, 0),()),
		"CTD_Relativity" : ((52, LCID, 4, 0),()),
		"CTD_Response" : ((47, LCID, 4, 0),()),
		"CTD_Unit" : ((4, LCID, 4, 0),()),
		"CTD_WEIGHTING_AWEIGHTING" : ((42, LCID, 4, 0),()),
		"CTD_WEIGHTING_CCIR468_1K" : ((44, LCID, 4, 0),()),
		"CTD_WEIGHTING_CCIR468_2K" : ((45, LCID, 4, 0),()),
		"CTD_WEIGHTING_CWEIGHTING" : ((43, LCID, 4, 0),()),
		"CTD_WEIGHTING_DEFAULT" : ((46, LCID, 4, 0),()),
		"CTD_WEIGHTING_NONE" : ((41, LCID, 4, 0),()),
		"CTD_WeightingFilter" : ((40, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ICarrierDisplay(DispatchBaseClass):
	CLSID = IID('{BA01E3C1-6CDB-11D3-B0E8-00AA0011AF6D}')
	coclass_clsid = IID('{BA01E3C3-6CDB-11D3-B0E8-00AA0011AF6D}')

	def CD_GetXRange(self, dMinValue=defaultNamedNotOptArg, dMaxValue=defaultNamedNotOptArg):
		'CD_GetXRange'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((16396, 0), (16396, 0)),dMinValue
			, dMaxValue)

	def CD_GetYRange(self, dMinValue=defaultNamedNotOptArg, dMaxValue=defaultNamedNotOptArg):
		'CD_GetYRange'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((16396, 0), (16396, 0)),dMinValue
			, dMaxValue)

	def CD_Restart(self):
		'CD_Restart'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), (),)

	def CD_SetXRange(self, dMinValue=defaultNamedNotOptArg, dMaxValue=defaultNamedNotOptArg):
		'CD_SetXRange'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((5, 0), (5, 0)),dMinValue
			, dMaxValue)

	def CD_SetYRange(self, dMinValue=defaultNamedNotOptArg, dMaxValue=defaultNamedNotOptArg):
		'CD_SetYRange'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((5, 0), (5, 0)),dMinValue
			, dMaxValue)

	_prop_map_get_ = {
		"CD_GateTime": (4, 2, (2, 0), (), "CD_GateTime", None),
		"CD_IncreaseRes": (5, 2, (11, 0), (), "CD_IncreaseRes", None),
		"CD_Interpolate": (3, 2, (11, 0), (), "CD_Interpolate", None),
		"CD_Resolution": (6, 2, (2, 0), (), "CD_Resolution", None),
		"CD_ShowAESDetails": (2, 2, (11, 0), (), "CD_ShowAESDetails", None),
		"CD_XUnit": (1, 2, (2, 0), (), "CD_XUnit", None),
	}
	_prop_map_put_ = {
		"CD_GateTime" : ((4, LCID, 4, 0),()),
		"CD_IncreaseRes" : ((5, LCID, 4, 0),()),
		"CD_Interpolate" : ((3, LCID, 4, 0),()),
		"CD_Resolution" : ((6, LCID, 4, 0),()),
		"CD_ShowAESDetails" : ((2, LCID, 4, 0),()),
		"CD_XUnit" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChannelStatus(DispatchBaseClass):
	CLSID = IID('{C2433361-FA1B-11D1-91DD-70AB00C10000}')
	coclass_clsid = IID('{C2433363-FA1B-11D1-91DD-70AB00C10000}')

	def CS_SampleTimeGetCurrent(self):
		'CS_SampleTimeGetCurrent'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def CS_TimeOfDayGetCurrent(self):
		'CS_TimeOfDayGetCurrent'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	# Result is of type IChannelStatusStream
	def ChAInput(self):
		'ChAInput'
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChAInput', '{EF2310A4-0B44-11D2-91DD-70AB00C10000}')
		return ret

	# Result is of type IChannelStatusStream
	def ChAOutput(self):
		'ChAOutput'
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChAOutput', '{EF2310A4-0B44-11D2-91DD-70AB00C10000}')
		return ret

	# Result is of type IChannelStatusStream
	def ChBInput(self):
		'ChBInput'
		ret = self._oleobj_.InvokeTypes(21, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChBInput', '{EF2310A4-0B44-11D2-91DD-70AB00C10000}')
		return ret

	# Result is of type IChannelStatusStream
	def ChBOutput(self):
		'ChBOutput'
		ret = self._oleobj_.InvokeTypes(19, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChBOutput', '{EF2310A4-0B44-11D2-91DD-70AB00C10000}')
		return ret

	_prop_map_get_ = {
		"CS_CRC_CORRECT": (14, 2, (2, 0), (), "CS_CRC_CORRECT", None),
		"CS_CRC_INCORRECT": (15, 2, (2, 0), (), "CS_CRC_INCORRECT", None),
		"CS_CRC_STATIC": (17, 2, (2, 0), (), "CS_CRC_STATIC", None),
		"CS_CRC_ZERO": (16, 2, (2, 0), (), "CS_CRC_ZERO", None),
		"CS_ConsSampleRateAuto": (2, 2, (11, 0), (), "CS_ConsSampleRateAuto", None),
		"CS_ConsWordLengthAuto": (3, 2, (11, 0), (), "CS_ConsWordLengthAuto", None),
		"CS_ProfChannelModeAuto": (6, 2, (11, 0), (), "CS_ProfChannelModeAuto", None),
		"CS_ProfFreqLockingAuto": (4, 2, (11, 0), (), "CS_ProfFreqLockingAuto", None),
		"CS_ProfSampleRateAuto": (5, 2, (11, 0), (), "CS_ProfSampleRateAuto", None),
		"CS_ProfWordLengthAuto": (7, 2, (11, 0), (), "CS_ProfWordLengthAuto", None),
		"CS_SampleTimeInputShowHex": (9, 2, (11, 0), (), "CS_SampleTimeInputShowHex", None),
		"CS_SampleTimeOutputShowHex": (8, 2, (11, 0), (), "CS_SampleTimeOutputShowHex", None),
		"CS_SampleTimeSendBCD": (10, 2, (11, 0), (), "CS_SampleTimeSendBCD", None),
		"CS_Tied": (1, 2, (11, 0), (), "CS_Tied", None),
		"CS_TimeOfDayInputShowHex": (12, 2, (11, 0), (), "CS_TimeOfDayInputShowHex", None),
		"CS_TimeOfDayOutputShowHex": (11, 2, (11, 0), (), "CS_TimeOfDayOutputShowHex", None),
		"CS_TimeOfDaySendBCD": (13, 2, (11, 0), (), "CS_TimeOfDaySendBCD", None),
	}
	_prop_map_put_ = {
		"CS_CRC_CORRECT" : ((14, LCID, 4, 0),()),
		"CS_CRC_INCORRECT" : ((15, LCID, 4, 0),()),
		"CS_CRC_STATIC" : ((17, LCID, 4, 0),()),
		"CS_CRC_ZERO" : ((16, LCID, 4, 0),()),
		"CS_ConsSampleRateAuto" : ((2, LCID, 4, 0),()),
		"CS_ConsWordLengthAuto" : ((3, LCID, 4, 0),()),
		"CS_ProfChannelModeAuto" : ((6, LCID, 4, 0),()),
		"CS_ProfFreqLockingAuto" : ((4, LCID, 4, 0),()),
		"CS_ProfSampleRateAuto" : ((5, LCID, 4, 0),()),
		"CS_ProfWordLengthAuto" : ((7, LCID, 4, 0),()),
		"CS_SampleTimeInputShowHex" : ((9, LCID, 4, 0),()),
		"CS_SampleTimeOutputShowHex" : ((8, LCID, 4, 0),()),
		"CS_SampleTimeSendBCD" : ((10, LCID, 4, 0),()),
		"CS_Tied" : ((1, LCID, 4, 0),()),
		"CS_TimeOfDayInputShowHex" : ((12, LCID, 4, 0),()),
		"CS_TimeOfDayOutputShowHex" : ((11, LCID, 4, 0),()),
		"CS_TimeOfDaySendBCD" : ((13, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChannelStatusStream(DispatchBaseClass):
	CLSID = IID('{EF2310A4-0B44-11D2-91DD-70AB00C10000}')
	coclass_clsid = IID('{EF2310A6-0B44-11D2-91DD-70AB00C10000}')

	def CS_SetDefault(self):
		'CS_SetDefault'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"CS_Byte0": (1, 2, (2, 0), (), "CS_Byte0", None),
		"CS_Byte1": (2, 2, (2, 0), (), "CS_Byte1", None),
		"CS_Byte10": (11, 2, (2, 0), (), "CS_Byte10", None),
		"CS_Byte11": (12, 2, (2, 0), (), "CS_Byte11", None),
		"CS_Byte12": (13, 2, (2, 0), (), "CS_Byte12", None),
		"CS_Byte13": (14, 2, (2, 0), (), "CS_Byte13", None),
		"CS_Byte14": (15, 2, (2, 0), (), "CS_Byte14", None),
		"CS_Byte15": (16, 2, (2, 0), (), "CS_Byte15", None),
		"CS_Byte16": (17, 2, (2, 0), (), "CS_Byte16", None),
		"CS_Byte17": (18, 2, (2, 0), (), "CS_Byte17", None),
		"CS_Byte18": (19, 2, (2, 0), (), "CS_Byte18", None),
		"CS_Byte19": (20, 2, (2, 0), (), "CS_Byte19", None),
		"CS_Byte2": (3, 2, (2, 0), (), "CS_Byte2", None),
		"CS_Byte20": (21, 2, (2, 0), (), "CS_Byte20", None),
		"CS_Byte21": (22, 2, (2, 0), (), "CS_Byte21", None),
		"CS_Byte22": (23, 2, (2, 0), (), "CS_Byte22", None),
		"CS_Byte23": (24, 2, (2, 0), (), "CS_Byte23", None),
		"CS_Byte3": (4, 2, (2, 0), (), "CS_Byte3", None),
		"CS_Byte4": (5, 2, (2, 0), (), "CS_Byte4", None),
		"CS_Byte5": (6, 2, (2, 0), (), "CS_Byte5", None),
		"CS_Byte6": (7, 2, (2, 0), (), "CS_Byte6", None),
		"CS_Byte7": (8, 2, (2, 0), (), "CS_Byte7", None),
		"CS_Byte8": (9, 2, (2, 0), (), "CS_Byte8", None),
		"CS_Byte9": (10, 2, (2, 0), (), "CS_Byte9", None),
		"CS_CRCMode": (25, 2, (2, 0), (), "CS_CRCMode", None),
	}
	_prop_map_put_ = {
		"CS_Byte0" : ((1, LCID, 4, 0),()),
		"CS_Byte1" : ((2, LCID, 4, 0),()),
		"CS_Byte10" : ((11, LCID, 4, 0),()),
		"CS_Byte11" : ((12, LCID, 4, 0),()),
		"CS_Byte12" : ((13, LCID, 4, 0),()),
		"CS_Byte13" : ((14, LCID, 4, 0),()),
		"CS_Byte14" : ((15, LCID, 4, 0),()),
		"CS_Byte15" : ((16, LCID, 4, 0),()),
		"CS_Byte16" : ((17, LCID, 4, 0),()),
		"CS_Byte17" : ((18, LCID, 4, 0),()),
		"CS_Byte18" : ((19, LCID, 4, 0),()),
		"CS_Byte19" : ((20, LCID, 4, 0),()),
		"CS_Byte2" : ((3, LCID, 4, 0),()),
		"CS_Byte20" : ((21, LCID, 4, 0),()),
		"CS_Byte21" : ((22, LCID, 4, 0),()),
		"CS_Byte22" : ((23, LCID, 4, 0),()),
		"CS_Byte23" : ((24, LCID, 4, 0),()),
		"CS_Byte3" : ((4, LCID, 4, 0),()),
		"CS_Byte4" : ((5, LCID, 4, 0),()),
		"CS_Byte5" : ((6, LCID, 4, 0),()),
		"CS_Byte6" : ((7, LCID, 4, 0),()),
		"CS_Byte7" : ((8, LCID, 4, 0),()),
		"CS_Byte8" : ((9, LCID, 4, 0),()),
		"CS_Byte9" : ((10, LCID, 4, 0),()),
		"CS_CRCMode" : ((25, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDScope(DispatchBaseClass):
	CLSID = IID('{5F1D8E26-2D90-11D4-AA54-0050046915E5}')
	coclass_clsid = IID('{5F1D8E24-2D90-11D4-AA54-0050046915E5}')

	# Result is of type IAnalogueInputs
	def AnalogueInputs(self):
		'AnalogueInputs'
		ret = self._oleobj_.InvokeTypes(71, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AnalogueInputs', '{E302BAC9-E4DC-11D1-91DD-70AB00C10000}')
		return ret

	# Result is of type IAnalogueOutputs
	def AnalogueOutputs(self):
		'AnalogueOutputs'
		ret = self._oleobj_.InvokeTypes(65, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AnalogueOutputs', '{C8EA98A3-E3F7-11D1-91DD-70AB00C10000}')
		return ret

	# Result is of type IAnalyzer
	def Analyzer(self):
		'Analyzer'
		ret = self._oleobj_.InvokeTypes(73, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Analyzer', '{8E6A399F-C230-11D1-91DD-70AB00C10000}')
		return ret

	# Result is of type IAutomation
	def Automation(self):
		'Automation'
		ret = self._oleobj_.InvokeTypes(83, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Automation', '{D0309162-171D-11D2-91DE-70AB00C10000}')
		return ret

	# Result is of type ICTDetector
	def CTDetector(self):
		'CTDetector'
		ret = self._oleobj_.InvokeTypes(77, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CTDetector', '{E76688E1-1596-11D2-91DE-70AB00C10000}')
		return ret

	# Result is of type ICarrierDisplay
	def CarrierDisplay(self):
		'CarrierDisplay'
		ret = self._oleobj_.InvokeTypes(70, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CarrierDisplay', '{BA01E3C1-6CDB-11D3-B0E8-00AA0011AF6D}')
		return ret

	# Result is of type IdSNet
	def ChannelArray(self):
		'ChannelArray'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChannelArray', '{2DA438F9-47DC-4FA0-BC9E-29B479667BF5}')
		return ret

	# Result is of type IChannelStatus
	def ChannelStatus(self):
		'ChannelStatus'
		ret = self._oleobj_.InvokeTypes(80, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ChannelStatus', '{C2433361-FA1B-11D1-91DD-70AB00C10000}')
		return ret

	def CloseApplication(self):
		'CloseApplication'
		return self._oleobj_.InvokeTypes(109, LCID, 1, (24, 0), (),)

	def ConfigurationHasUnsupportedSettings(self):
		'ConfigurationHasUnsupportedSettings'
		return self._oleobj_.InvokeTypes(124, LCID, 1, (3, 0), (),)

	# Result is of type IDigitalInputCarrier
	def DigitalInputCarrier(self):
		'DigitalInputCarrier'
		ret = self._oleobj_.InvokeTypes(69, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DigitalInputCarrier', '{E302BAC4-E4DC-11D1-91DD-70AB00C10000}')
		return ret

	# Result is of type IDigitalInputs
	def DigitalInputs(self):
		'DigitalInputs'
		ret = self._oleobj_.InvokeTypes(68, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DigitalInputs', '{E302BAC1-E4DC-11D1-91DD-70AB00C10000}')
		return ret

	# Result is of type IDigitalOutputCarrier
	def DigitalOutputCarrier(self):
		'DigitalOutputCarrier'
		ret = self._oleobj_.InvokeTypes(64, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DigitalOutputCarrier', '{12E40661-E0F8-11D1-91DD-70AB00C10000}')
		return ret

	# Result is of type IDigitalOutputs
	def DigitalOutputs(self):
		'DigitalOutputs'
		ret = self._oleobj_.InvokeTypes(63, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DigitalOutputs', '{C8EA98A6-E3F7-11D1-91DD-70AB00C10000}')
		return ret

	def Display(self, sDisplay=defaultNamedNotOptArg):
		'Display'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((2, 0),),sDisplay
			)

	def EndTimer(self, iTimerID=defaultNamedNotOptArg):
		'EndTimer'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), ((3, 0),),iTimerID
			)

	# Result is of type IEventManager
	def EventManager(self):
		'EventManager'
		ret = self._oleobj_.InvokeTypes(87, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'EventManager', '{D59FA601-A542-11D2-91DE-70AB00C10000}')
		return ret

	# Result is of type IFFTDetector
	def FFTDetector(self):
		'FFTDetector'
		ret = self._oleobj_.InvokeTypes(78, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'FFTDetector', '{B9A66201-2AB2-11D2-91DE-70AB00C10000}')
		return ret

	# Result is of type IFFTParameters
	def FFTParameters(self):
		'FFTParameters'
		ret = self._oleobj_.InvokeTypes(75, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'FFTParameters', '{2CDD6201-17F8-11D2-91DE-70AB00C10000}')
		return ret

	def FireEvent(self, lParam=defaultNamedNotOptArg):
		'FireEvent'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), ((3, 0),),lParam
			)

	# Result is of type IFormatConverter
	def FormatConverter(self):
		'FormatConverter'
		ret = self._oleobj_.InvokeTypes(99, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'FormatConverter', '{2840227C-5408-4E53-B52B-0F6637199948}')
		return ret

	def GetConfiguration(self, bFullPath=defaultNamedNotOptArg):
		'GetConfiguration'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(108, LCID, 1, (8, 0), ((11, 0),),bFullPath
			)

	def GetFirstFFTDetReading(self, sResultID=defaultNamedNotOptArg, sDetectorID=defaultNamedNotOptArg):
		'GetFirstFFTDetReading'
		return self._oleobj_.InvokeTypes(119, LCID, 1, (11, 0), ((2, 0), (2, 0)),sResultID
			, sDetectorID)

	def GetFirstReadingForResult(self, sResultID=defaultNamedNotOptArg):
		'GetFirstReadingForResult'
		return self._oleobj_.InvokeTypes(117, LCID, 1, (11, 0), ((2, 0),),sResultID
			)

	def GetNextFFTDetReading(self, sResultID=defaultNamedNotOptArg, sDetectorID=defaultNamedNotOptArg):
		'GetNextFFTDetReading'
		return self._oleobj_.InvokeTypes(120, LCID, 1, (11, 0), ((2, 0), (2, 0)),sResultID
			, sDetectorID)

	def GetNextReadingForResult(self, sResultID=defaultNamedNotOptArg):
		'GetNextReadingForResult '
		return self._oleobj_.InvokeTypes(118, LCID, 1, (11, 0), ((2, 0),),sResultID
			)

	def GetSecurityLevel(self):
		'GetSecurityLevel'
		return self._oleobj_.InvokeTypes(111, LCID, 1, (2, 0), (),)

	def GetSoftwareVersion(self, ucMajor=defaultNamedNotOptArg, ucMinor=defaultNamedNotOptArg, ucLetter=defaultNamedNotOptArg):
		'GetSoftwareVersion'
		return self._oleobj_.InvokeTypes(112, LCID, 1, (24, 0), ((16396, 0), (16396, 0), (16396, 0)),ucMajor
			, ucMinor, ucLetter)

	# Result is of type IHardware
	def Hardware(self):
		'Hardware'
		ret = self._oleobj_.InvokeTypes(93, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Hardware', '{3A499641-CE6B-11D3-B0E8-00AA0011AF6D}')
		return ret

	# Result is of type IIOSwitcher
	def IOSwitcher(self):
		'IOSwitcher'
		ret = self._oleobj_.InvokeTypes(98, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'IOSwitcher', '{F0815F9F-99C1-4931-B018-2735C3F176A9}')
		return ret

	# Result is of type IImpulseResponse
	def ImpulseResponse(self):
		'ImpulseResponse'
		ret = self._oleobj_.InvokeTypes(76, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ImpulseResponse', '{1CD7F788-84E1-415F-8EE0-739E3121D0AF}')
		return ret

	def IsHardwareMissing(self):
		'IsHardwareMissing'
		return self._oleobj_.InvokeTypes(123, LCID, 1, (11, 0), (),)

	def IsInitialised(self):
		'IsInitialised'
		return self._oleobj_.InvokeTypes(113, LCID, 1, (11, 0), (),)

	def LastResultSettled(self):
		'LastResultSettled'
		return self._oleobj_.InvokeTypes(116, LCID, 1, (11, 0), (),)

	# Result is of type ILimitTable
	def LimitTable(self):
		'LimitTable'
		ret = self._oleobj_.InvokeTypes(89, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'LimitTable', '{64D4EDC2-F218-11D4-B9A2-0050046915E5}')
		return ret

	def LoadConfiguration(self, strFileName=defaultNamedNotOptArg):
		'LoadConfiguration'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (11, 0), ((8, 0),),strFileName
			)

	# Result is of type IMonitorOutputs
	def MonitorOutputs(self):
		'MonitorOutputs'
		ret = self._oleobj_.InvokeTypes(79, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MonitorOutputs', '{E302BACC-E4DC-11D1-91DD-70AB00C10000}')
		return ret

	def MsgBoxWithTimeOut(self, strMsg=defaultNamedNotOptArg, lTimeout=defaultNamedNotOptArg, sButtons=defaultNamedNotOptArg, strTitle=defaultNamedNotOptArg):
		'MsgBoxWithTimeOut'
		return self._oleobj_.InvokeTypes(114, LCID, 1, (2, 0), ((8, 0), (3, 0), (2, 0), (8, 0)),strMsg
			, lTimeout, sButtons, strTitle)

	# Result is of type IOptions
	def Options(self):
		'Options'
		ret = self._oleobj_.InvokeTypes(86, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Options', '{A3AB5423-CD5E-11D2-B0E8-00AA0011AF6D}')
		return ret

	# Result is of type IPorts
	def Ports(self):
		'Ports'
		ret = self._oleobj_.InvokeTypes(94, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Ports', '{0211EBA7-BFF6-4C67-9E59-58EA93952CCD}')
		return ret

	# Result is of type IReading
	def Reading(self):
		'Reading'
		ret = self._oleobj_.InvokeTypes(92, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Reading', '{BABA8F2B-2405-48C6-B991-337B5B00DBD8}')
		return ret

	# Result is of type IRegulation
	def Regulation(self):
		'Regulation'
		ret = self._oleobj_.InvokeTypes(85, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Regulation', '{94F3B76C-7223-43EA-8D03-0A87A8BD81CC}')
		return ret

	def ResetSettling(self):
		'ResetSettling'
		return self._oleobj_.InvokeTypes(115, LCID, 1, (24, 0), (),)

	def SaveConfiguration(self, strFileName=defaultNamedNotOptArg):
		'SaveConfiguration'
		return self._oleobj_.InvokeTypes(107, LCID, 1, (11, 0), ((8, 0),),strFileName
			)

	# Result is of type IAutomation
	def Scripts(self):
		'Scripts'
		ret = self._oleobj_.InvokeTypes(82, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Scripts', '{D0309162-171D-11D2-91DE-70AB00C10000}')
		return ret

	# Result is of type ISerialPort
	def SerialPort(self):
		'SerialPort'
		ret = self._oleobj_.InvokeTypes(95, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'SerialPort', '{CBCB3652-E7DF-48FB-8172-E592A139C0E9}')
		return ret

	def SetCurrentReadingFromEventParam(self, lParam=defaultNamedNotOptArg):
		'SetCurrentReadingFromEventParam'
		return self._oleobj_.InvokeTypes(121, LCID, 1, (11, 0), ((3, 0),),lParam
			)

	def SetPage(self, sPage=defaultNamedNotOptArg):
		'SetPage'
		return self._oleobj_.InvokeTypes(125, LCID, 1, (24, 0), ((2, 0),),sPage
			)

	# Result is of type ISettling
	def Settling(self):
		'Settling'
		ret = self._oleobj_.InvokeTypes(84, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Settling', '{CB72FCC1-DFBD-11D3-B0E8-00AA0011AF6D}')
		return ret

	def ShowHelpTopic(self, strHelpFile=defaultNamedNotOptArg, strHelpTopic=defaultNamedNotOptArg):
		'ShowHelpTopic'
		return self._oleobj_.InvokeTypes(122, LCID, 1, (24, 0), ((8, 0), (8, 0)),strHelpFile
			, strHelpTopic)

	# Result is of type ISignalAnalyzer
	def SignalAnalyzer(self):
		'SignalAnalyzer'
		ret = self._oleobj_.InvokeTypes(74, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'SignalAnalyzer', '{31080A22-11BC-11D2-91DE-70AB00C10000}')
		return ret

	# Result is of type ISignalGenerator
	def SignalGenerator(self):
		'SignalGenerator'
		ret = self._oleobj_.InvokeTypes(67, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'SignalGenerator', '{85AFFE41-E654-11D1-91DD-70AB00C10000}')
		return ret

	def Sleep(self, lNumMilliseconds=defaultNamedNotOptArg):
		'Sleep'
		return self._oleobj_.InvokeTypes(110, LCID, 1, (24, 0), ((3, 0),),lNumMilliseconds
			)

	# Result is of type ISoundcardInputs
	def SoundcardInputs(self):
		'SoundcardInputs'
		ret = self._oleobj_.InvokeTypes(72, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'SoundcardInputs', '{3361DF2F-D9BC-4C5D-9898-FAE3BFF8A42F}')
		return ret

	# Result is of type ISoundcardOutputs
	def SoundcardOutputs(self):
		'SoundcardOutputs'
		ret = self._oleobj_.InvokeTypes(66, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'SoundcardOutputs', '{49EDD76B-5B81-4494-AD07-EDEB49287493}')
		return ret

	def StartTimer(self, iNumMilliseconds=defaultNamedNotOptArg):
		'StartTimer'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (3, 0), ((3, 0),),iNumMilliseconds
			)

	# Result is of type ISweep
	def Sweep(self):
		'Sweep'
		ret = self._oleobj_.InvokeTypes(81, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Sweep', '{2787A930-AC57-11D2-91DE-00AA0011AF6D}')
		return ret

	# Result is of type ISwitcher
	def Switcher(self):
		'Switcher'
		ret = self._oleobj_.InvokeTypes(97, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Switcher', '{8EF24D41-887F-4024-AB39-43844B96DDF8}')
		return ret

	# Result is of type ITrace
	def Trace(self):
		'Trace'
		ret = self._oleobj_.InvokeTypes(91, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Trace', '{FB1F67C4-5C0C-11D5-9C7E-0050046915E5}')
		return ret

	# Result is of type ITraceWindow
	def TraceWindow(self):
		'TraceWindow'
		ret = self._oleobj_.InvokeTypes(90, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'TraceWindow', '{920A1BE2-2C44-11D2-91DE-70AB00C10000}')
		return ret

	# Result is of type IUserTable
	def UserTable(self):
		'UserTable'
		ret = self._oleobj_.InvokeTypes(88, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'UserTable', '{0BE39BE5-725C-11D3-B0E8-00AA0011AF6D}')
		return ret

	# Result is of type IVSIOAdapter
	def VSIOAdapter(self):
		'VSIOAdapter'
		ret = self._oleobj_.InvokeTypes(100, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'VSIOAdapter', '{117A5950-05EB-47F3-B76B-9EE38C222F5B}')
		return ret

	# Result is of type IdSNet
	def dSNet(self):
		'dSNet'
		ret = self._oleobj_.InvokeTypes(96, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'dSNet', '{2DA438F9-47DC-4FA0-BC9E-29B479667BF5}')
		return ret

	_prop_map_get_ = {
		"CHANNEL_A": (46, 2, (2, 0), (), "CHANNEL_A", None),
		"CHANNEL_B": (47, 2, (2, 0), (), "CHANNEL_B", None),
		"CHANNEL_BOTH": (48, 2, (2, 0), (), "CHANNEL_BOTH", None),
		"CHANNEL_NONSEL": (50, 2, (2, 0), (), "CHANNEL_NONSEL", None),
		"CHANNEL_SEL": (49, 2, (2, 0), (), "CHANNEL_SEL", None),
		"CHANNEL_UNSEL": (51, 2, (2, 0), (), "CHANNEL_UNSEL", None),
		"DISPLAY_HIDE": (43, 2, (2, 0), (), "DISPLAY_HIDE", None),
		"DISPLAY_MAXIMIZED": (45, 2, (2, 0), (), "DISPLAY_MAXIMIZED", None),
		"DISPLAY_MINIMIZED": (44, 2, (2, 0), (), "DISPLAY_MINIMIZED", None),
		"DISPLAY_SHOW": (42, 2, (2, 0), (), "DISPLAY_SHOW", None),
		"MODELNUMBER_ANALOGUE": (53, 2, (2, 0), (), "MODELNUMBER_ANALOGUE", None),
		"MODELNUMBER_ANALOGUEANDDIGITAL": (57, 2, (2, 0), (), "MODELNUMBER_ANALOGUEANDDIGITAL", None),
		"MODELNUMBER_ANALOGUEPLUS": (55, 2, (2, 0), (), "MODELNUMBER_ANALOGUEPLUS", None),
		"MODELNUMBER_DS3_ANALOGUE": (52, 2, (2, 0), (), "MODELNUMBER_DS3_ANALOGUE", None),
		"MODELNUMBER_DS3_ANALOGUEANDDIGITAL": (56, 2, (2, 0), (), "MODELNUMBER_DS3_ANALOGUEANDDIGITAL", None),
		"MODELNUMBER_DS3_ANALOGUEPLUS": (54, 2, (2, 0), (), "MODELNUMBER_DS3_ANALOGUEPLUS", None),
		"MODELNUMBER_DS3_ESSENTIALS": (58, 2, (2, 0), (), "MODELNUMBER_DS3_ESSENTIALS", None),
		"MODELNUMBER_ESSENTIALS": (59, 2, (2, 0), (), "MODELNUMBER_ESSENTIALS", None),
		"ModelNumber": (61, 2, (2, 0), (), "ModelNumber", None),
		"ShowMessages": (60, 2, (11, 0), (), "ShowMessages", None),
		"ShowUserBar": (62, 2, (11, 0), (), "ShowUserBar", None),
		"UNIT_BINPOWER": (39, 2, (2, 0), (), "UNIT_BINPOWER", None),
		"UNIT_DBFS": (7, 2, (2, 0), (), "UNIT_DBFS", None),
		"UNIT_DBM": (17, 2, (2, 0), (), "UNIT_DBM", None),
		"UNIT_DBR": (20, 2, (2, 0), (), "UNIT_DBR", None),
		"UNIT_DBSPL": (19, 2, (2, 0), (), "UNIT_DBSPL", None),
		"UNIT_DBU": (15, 2, (2, 0), (), "UNIT_DBU", None),
		"UNIT_DBV": (16, 2, (2, 0), (), "UNIT_DBV", None),
		"UNIT_DUTYCYCLE_PERCENT": (34, 2, (2, 0), (), "UNIT_DUTYCYCLE_PERCENT", None),
		"UNIT_DUTYCYCLE_SAMPLES": (35, 2, (2, 0), (), "UNIT_DUTYCYCLE_SAMPLES", None),
		"UNIT_FFS": (10, 2, (2, 0), (), "UNIT_FFS", None),
		"UNIT_FREQ_HZ": (4, 2, (2, 0), (), "UNIT_FREQ_HZ", None),
		"UNIT_FREQ_OFFSET": (5, 2, (2, 0), (), "UNIT_FREQ_OFFSET", None),
		"UNIT_FREQ_RATIO": (6, 2, (2, 0), (), "UNIT_FREQ_RATIO", None),
		"UNIT_FS": (8, 2, (2, 0), (), "UNIT_FS", None),
		"UNIT_HEX": (11, 2, (2, 0), (), "UNIT_HEX", None),
		"UNIT_IMPEDANCE_R": (38, 2, (2, 0), (), "UNIT_IMPEDANCE_R", None),
		"UNIT_JITTER_NS": (27, 2, (2, 0), (), "UNIT_JITTER_NS", None),
		"UNIT_JITTER_UI": (26, 2, (2, 0), (), "UNIT_JITTER_UI", None),
		"UNIT_MS": (2, 2, (2, 0), (), "UNIT_MS", None),
		"UNIT_NULL": (1, 2, (2, 0), (), "UNIT_NULL", None),
		"UNIT_NUMPERIODS": (41, 2, (2, 0), (), "UNIT_NUMPERIODS", None),
		"UNIT_PERCENTFS": (9, 2, (2, 0), (), "UNIT_PERCENTFS", None),
		"UNIT_PERCENTREF": (21, 2, (2, 0), (), "UNIT_PERCENTREF", None),
		"UNIT_PHASE_DEGREES": (31, 2, (2, 0), (), "UNIT_PHASE_DEGREES", None),
		"UNIT_PHASE_PERCENT": (29, 2, (2, 0), (), "UNIT_PHASE_PERCENT", None),
		"UNIT_PHASE_RADIANS": (32, 2, (2, 0), (), "UNIT_PHASE_RADIANS", None),
		"UNIT_PHASE_SAMPLES": (30, 2, (2, 0), (), "UNIT_PHASE_SAMPLES", None),
		"UNIT_PHASE_UI": (28, 2, (2, 0), (), "UNIT_PHASE_UI", None),
		"UNIT_PHASE_US": (33, 2, (2, 0), (), "UNIT_PHASE_US", None),
		"UNIT_PPM": (37, 2, (2, 0), (), "UNIT_PPM", None),
		"UNIT_RELATIVE_ANAVSGEN": (25, 2, (2, 0), (), "UNIT_RELATIVE_ANAVSGEN", None),
		"UNIT_RELATIVE_DB": (22, 2, (2, 0), (), "UNIT_RELATIVE_DB", None),
		"UNIT_RELATIVE_GAIN": (24, 2, (2, 0), (), "UNIT_RELATIVE_GAIN", None),
		"UNIT_RELATIVE_PERCENT": (23, 2, (2, 0), (), "UNIT_RELATIVE_PERCENT", None),
		"UNIT_SAMPLES": (3, 2, (2, 0), (), "UNIT_SAMPLES", None),
		"UNIT_SECONDS": (40, 2, (2, 0), (), "UNIT_SECONDS", None),
		"UNIT_V": (36, 2, (2, 0), (), "UNIT_V", None),
		"UNIT_VP": (13, 2, (2, 0), (), "UNIT_VP", None),
		"UNIT_VPP": (14, 2, (2, 0), (), "UNIT_VPP", None),
		"UNIT_VRMS": (12, 2, (2, 0), (), "UNIT_VRMS", None),
		"UNIT_W": (18, 2, (2, 0), (), "UNIT_W", None),
	}
	_prop_map_put_ = {
		"CHANNEL_A" : ((46, LCID, 4, 0),()),
		"CHANNEL_B" : ((47, LCID, 4, 0),()),
		"CHANNEL_BOTH" : ((48, LCID, 4, 0),()),
		"CHANNEL_NONSEL" : ((50, LCID, 4, 0),()),
		"CHANNEL_SEL" : ((49, LCID, 4, 0),()),
		"CHANNEL_UNSEL" : ((51, LCID, 4, 0),()),
		"DISPLAY_HIDE" : ((43, LCID, 4, 0),()),
		"DISPLAY_MAXIMIZED" : ((45, LCID, 4, 0),()),
		"DISPLAY_MINIMIZED" : ((44, LCID, 4, 0),()),
		"DISPLAY_SHOW" : ((42, LCID, 4, 0),()),
		"MODELNUMBER_ANALOGUE" : ((53, LCID, 4, 0),()),
		"MODELNUMBER_ANALOGUEANDDIGITAL" : ((57, LCID, 4, 0),()),
		"MODELNUMBER_ANALOGUEPLUS" : ((55, LCID, 4, 0),()),
		"MODELNUMBER_DS3_ANALOGUE" : ((52, LCID, 4, 0),()),
		"MODELNUMBER_DS3_ANALOGUEANDDIGITAL" : ((56, LCID, 4, 0),()),
		"MODELNUMBER_DS3_ANALOGUEPLUS" : ((54, LCID, 4, 0),()),
		"MODELNUMBER_DS3_ESSENTIALS" : ((58, LCID, 4, 0),()),
		"MODELNUMBER_ESSENTIALS" : ((59, LCID, 4, 0),()),
		"ModelNumber" : ((61, LCID, 4, 0),()),
		"ShowMessages" : ((60, LCID, 4, 0),()),
		"ShowUserBar" : ((62, LCID, 4, 0),()),
		"UNIT_BINPOWER" : ((39, LCID, 4, 0),()),
		"UNIT_DBFS" : ((7, LCID, 4, 0),()),
		"UNIT_DBM" : ((17, LCID, 4, 0),()),
		"UNIT_DBR" : ((20, LCID, 4, 0),()),
		"UNIT_DBSPL" : ((19, LCID, 4, 0),()),
		"UNIT_DBU" : ((15, LCID, 4, 0),()),
		"UNIT_DBV" : ((16, LCID, 4, 0),()),
		"UNIT_DUTYCYCLE_PERCENT" : ((34, LCID, 4, 0),()),
		"UNIT_DUTYCYCLE_SAMPLES" : ((35, LCID, 4, 0),()),
		"UNIT_FFS" : ((10, LCID, 4, 0),()),
		"UNIT_FREQ_HZ" : ((4, LCID, 4, 0),()),
		"UNIT_FREQ_OFFSET" : ((5, LCID, 4, 0),()),
		"UNIT_FREQ_RATIO" : ((6, LCID, 4, 0),()),
		"UNIT_FS" : ((8, LCID, 4, 0),()),
		"UNIT_HEX" : ((11, LCID, 4, 0),()),
		"UNIT_IMPEDANCE_R" : ((38, LCID, 4, 0),()),
		"UNIT_JITTER_NS" : ((27, LCID, 4, 0),()),
		"UNIT_JITTER_UI" : ((26, LCID, 4, 0),()),
		"UNIT_MS" : ((2, LCID, 4, 0),()),
		"UNIT_NULL" : ((1, LCID, 4, 0),()),
		"UNIT_NUMPERIODS" : ((41, LCID, 4, 0),()),
		"UNIT_PERCENTFS" : ((9, LCID, 4, 0),()),
		"UNIT_PERCENTREF" : ((21, LCID, 4, 0),()),
		"UNIT_PHASE_DEGREES" : ((31, LCID, 4, 0),()),
		"UNIT_PHASE_PERCENT" : ((29, LCID, 4, 0),()),
		"UNIT_PHASE_RADIANS" : ((32, LCID, 4, 0),()),
		"UNIT_PHASE_SAMPLES" : ((30, LCID, 4, 0),()),
		"UNIT_PHASE_UI" : ((28, LCID, 4, 0),()),
		"UNIT_PHASE_US" : ((33, LCID, 4, 0),()),
		"UNIT_PPM" : ((37, LCID, 4, 0),()),
		"UNIT_RELATIVE_ANAVSGEN" : ((25, LCID, 4, 0),()),
		"UNIT_RELATIVE_DB" : ((22, LCID, 4, 0),()),
		"UNIT_RELATIVE_GAIN" : ((24, LCID, 4, 0),()),
		"UNIT_RELATIVE_PERCENT" : ((23, LCID, 4, 0),()),
		"UNIT_SAMPLES" : ((3, LCID, 4, 0),()),
		"UNIT_SECONDS" : ((40, LCID, 4, 0),()),
		"UNIT_V" : ((36, LCID, 4, 0),()),
		"UNIT_VP" : ((13, LCID, 4, 0),()),
		"UNIT_VPP" : ((14, LCID, 4, 0),()),
		"UNIT_VRMS" : ((12, LCID, 4, 0),()),
		"UNIT_W" : ((18, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDScopeEvents:
	CLSID = CLSID_Sink = IID('{FC6A62CC-C2FD-11D1-91DD-70AB00C10000}')
	coclass_clsid = IID('{21973E01-D1B6-11D4-AA54-0050046915E5}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnMain",
		      102 : "OnChAValidBit",
		      103 : "OnChBValidBit",
		      104 : "OnCarrierInputLocking",
		      105 : "OnCarrierBiphase",
		      106 : "OnCarrierBlockLength",
		      107 : "OnCarrierEyeNarrowing",
		      108 : "OnCarrierAsync",
		      109 : "OnChAChannelCheckFailed",
		      110 : "OnChBChannelCheckFailed",
		      209 : "OnCSProfBit",
		      210 : "OnCSCopyrightBit",
		      211 : "OnCSEmphasis",
		      212 : "OnCSChannelMode",
		      213 : "OnCSCRCError",
		      214 : "OnCSANotEqualToB",
		      301 : "OnChAUserBitActive",
		      302 : "OnChBUserBitActive",
		      303 : "OnChAUserBitError",
		      304 : "OnChBUserBitError",
		      417 : "OnTrigger",
		      418 : "OnBufferProcessed",
		      419 : "OnReadingMinLimit",
		      420 : "OnReadingMaxLimit",
		      421 : "OnTraceMinLimit",
		      422 : "OnTraceMaxLimit",
		      523 : "OnSweepStarted",
		      524 : "OnSweepStepDone",
		      525 : "OnSweepFinished",
		      526 : "OnSweepSense",
		      627 : "OnTimer",
		      630 : "OnKeypress",
		      631 : "OnScripted",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnMain(self):
#		'Main'
#	def OnChAValidBit(self):
#		'ChAValidBit'
#	def OnChBValidBit(self):
#		'ChBValidBit'
#	def OnCarrierInputLocking(self):
#		'CarrierInputLocking'
#	def OnCarrierBiphase(self):
#		'CarrierBiphase'
#	def OnCarrierBlockLength(self):
#		'CarrierBlockLength'
#	def OnCarrierEyeNarrowing(self):
#		'CarrierEyeNarrowing'
#	def OnCarrierAsync(self):
#		'CarrierAsync'
#	def OnChAChannelCheckFailed(self):
#		'ChAChannelCheckFailed'
#	def OnChBChannelCheckFailed(self):
#		'ChBChannelCheckFailed'
#	def OnCSProfBit(self):
#		'CSProfBit'
#	def OnCSCopyrightBit(self):
#		'CSCopyrightBit'
#	def OnCSEmphasis(self):
#		'CSEmphasis'
#	def OnCSChannelMode(self):
#		'CSChannelMode'
#	def OnCSCRCError(self):
#		'CSCRCError'
#	def OnCSANotEqualToB(self):
#		'CSANotEqualToB'
#	def OnChAUserBitActive(self):
#		'ChAUserBitActive'
#	def OnChBUserBitActive(self):
#		'ChBUserBitActive'
#	def OnChAUserBitError(self):
#		'ChAUserBitError'
#	def OnChBUserBitError(self):
#		'ChBUserBitError'
#	def OnTrigger(self):
#		'Trigger'
#	def OnBufferProcessed(self):
#		'BufferProcessed'
#	def OnReadingMinLimit(self, lParam=defaultNamedNotOptArg):
#		'ReadingMinLimit'
#	def OnReadingMaxLimit(self, lParam=defaultNamedNotOptArg):
#		'ReadingMaxLimit'
#	def OnTraceMinLimit(self, lParam=defaultNamedNotOptArg):
#		'TraceMinLimit'
#	def OnTraceMaxLimit(self, lParam=defaultNamedNotOptArg):
#		'TraceMaxLimit'
#	def OnSweepStarted(self):
#		'SweepStarted'
#	def OnSweepStepDone(self):
#		'SweepStepDone'
#	def OnSweepFinished(self):
#		'SweepFinished'
#	def OnSweepSense(self):
#		'SweepSense'
#	def OnTimer(self, lTimerID=defaultNamedNotOptArg):
#		'Timer'
#	def OnKeypress(self):
#		'Keypress'
#	def OnScripted(self, lParam=defaultNamedNotOptArg):
#		'Scripted'


class IDigitalInputCarrier(DispatchBaseClass):
	CLSID = IID('{E302BAC4-E4DC-11D1-91DD-70AB00C10000}')
	coclass_clsid = IID('{E302BAC6-E4DC-11D1-91DD-70AB00C10000}')

	_prop_map_get_ = {
		"DIC_CARRIERAMPLMODE_AUDIOBAND": (4, 2, (2, 0), (), "DIC_CARRIERAMPLMODE_AUDIOBAND", None),
		"DIC_CARRIERAMPLMODE_COMMONMODE": (3, 2, (2, 0), (), "DIC_CARRIERAMPLMODE_COMMONMODE", None),
		"DIC_CARRIERAMPLMODE_DIFFERENTIAL": (2, 2, (2, 0), (), "DIC_CARRIERAMPLMODE_DIFFERENTIAL", None),
		"DIC_CARRIERPHASEMODE_GEN": (15, 2, (2, 0), (), "DIC_CARRIERPHASEMODE_GEN", None),
		"DIC_CARRIERPHASEMODE_REF": (16, 2, (2, 0), (), "DIC_CARRIERPHASEMODE_REF", None),
		"DIC_CarrierAmpl": (5, 2, (5, 0), (), "DIC_CarrierAmpl", None),
		"DIC_CarrierAmplMode": (1, 2, (2, 0), (), "DIC_CarrierAmplMode", None),
		"DIC_CarrierPhase": (17, 2, (5, 0), (), "DIC_CarrierPhase", None),
		"DIC_CarrierPhaseMode": (14, 2, (2, 0), (), "DIC_CarrierPhaseMode", None),
		"DIC_CarrierPhaseUnit": (18, 2, (2, 0), (), "DIC_CarrierPhaseUnit", None),
		"DIC_JITTERMODE_CARRIERDISPLAY": (11, 2, (2, 0), (), "DIC_JITTERMODE_CARRIERDISPLAY", None),
		"DIC_JITTERMODE_DATAJITTER": (8, 2, (2, 0), (), "DIC_JITTERMODE_DATAJITTER", None),
		"DIC_JITTERMODE_EYENARROWING_0X": (9, 2, (2, 0), (), "DIC_JITTERMODE_EYENARROWING_0X", None),
		"DIC_JITTERMODE_EYENARROWING_200MV": (10, 2, (2, 0), (), "DIC_JITTERMODE_EYENARROWING_200MV", None),
		"DIC_JITTERMODE_FSJITTER": (7, 2, (2, 0), (), "DIC_JITTERMODE_FSJITTER", None),
		"DIC_Jitter": (12, 2, (5, 0), (), "DIC_Jitter", None),
		"DIC_JitterMode": (6, 2, (2, 0), (), "DIC_JitterMode", None),
		"DIC_JitterUnit": (13, 2, (2, 0), (), "DIC_JitterUnit", None),
	}
	_prop_map_put_ = {
		"DIC_CARRIERAMPLMODE_AUDIOBAND" : ((4, LCID, 4, 0),()),
		"DIC_CARRIERAMPLMODE_COMMONMODE" : ((3, LCID, 4, 0),()),
		"DIC_CARRIERAMPLMODE_DIFFERENTIAL" : ((2, LCID, 4, 0),()),
		"DIC_CARRIERPHASEMODE_GEN" : ((15, LCID, 4, 0),()),
		"DIC_CARRIERPHASEMODE_REF" : ((16, LCID, 4, 0),()),
		"DIC_CarrierAmpl" : ((5, LCID, 4, 0),()),
		"DIC_CarrierAmplMode" : ((1, LCID, 4, 0),()),
		"DIC_CarrierPhase" : ((17, LCID, 4, 0),()),
		"DIC_CarrierPhaseMode" : ((14, LCID, 4, 0),()),
		"DIC_CarrierPhaseUnit" : ((18, LCID, 4, 0),()),
		"DIC_JITTERMODE_CARRIERDISPLAY" : ((11, LCID, 4, 0),()),
		"DIC_JITTERMODE_DATAJITTER" : ((8, LCID, 4, 0),()),
		"DIC_JITTERMODE_EYENARROWING_0X" : ((9, LCID, 4, 0),()),
		"DIC_JITTERMODE_EYENARROWING_200MV" : ((10, LCID, 4, 0),()),
		"DIC_JITTERMODE_FSJITTER" : ((7, LCID, 4, 0),()),
		"DIC_Jitter" : ((12, LCID, 4, 0),()),
		"DIC_JitterMode" : ((6, LCID, 4, 0),()),
		"DIC_JitterUnit" : ((13, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDigitalInputs(DispatchBaseClass):
	CLSID = IID('{E302BAC1-E4DC-11D1-91DD-70AB00C10000}')
	coclass_clsid = IID('{E302BAC3-E4DC-11D1-91DD-70AB00C10000}')

	_prop_map_get_ = {
		"DI_ActualFrameRate": (20, 2, (5, 0), (), "DI_ActualFrameRate", None),
		"DI_Asynchronous": (18, 2, (11, 0), (), "DI_Asynchronous", None),
		"DI_BiphaseViolation": (15, 2, (11, 0), (), "DI_BiphaseViolation", None),
		"DI_BlockLengthError": (16, 2, (11, 0), (), "DI_BlockLengthError", None),
		"DI_CHANNELCHECK_16BITS": (36, 2, (2, 0), (), "DI_CHANNELCHECK_16BITS", None),
		"DI_CHANNELCHECK_20BITS": (37, 2, (2, 0), (), "DI_CHANNELCHECK_20BITS", None),
		"DI_CHANNELCHECK_24BITS": (38, 2, (2, 0), (), "DI_CHANNELCHECK_24BITS", None),
		"DI_CHANNELCHECK_OFF": (35, 2, (2, 0), (), "DI_CHANNELCHECK_OFF", None),
		"DI_ChABitActivity": (22, 2, (3, 0), (), "DI_ChABitActivity", None),
		"DI_ChABitState": (23, 2, (3, 0), (), "DI_ChABitState", None),
		"DI_ChAChannelCheckFailed": (41, 2, (11, 0), (), "DI_ChAChannelCheckFailed", None),
		"DI_ChAUserBitActive": (28, 2, (11, 0), (), "DI_ChAUserBitActive", None),
		"DI_ChAUserBitError": (30, 2, (11, 0), (), "DI_ChAUserBitError", None),
		"DI_ChAValid": (26, 2, (11, 0), (), "DI_ChAValid", None),
		"DI_ChBBitActivity": (24, 2, (3, 0), (), "DI_ChBBitActivity", None),
		"DI_ChBBitState": (25, 2, (3, 0), (), "DI_ChBBitState", None),
		"DI_ChBChannelCheckFailed": (42, 2, (11, 0), (), "DI_ChBChannelCheckFailed", None),
		"DI_ChBUserBitActive": (29, 2, (11, 0), (), "DI_ChBUserBitActive", None),
		"DI_ChBUserBitError": (31, 2, (11, 0), (), "DI_ChBUserBitError", None),
		"DI_ChBValid": (27, 2, (11, 0), (), "DI_ChBValid", None),
		"DI_ChannelCheck": (34, 2, (2, 0), (), "DI_ChannelCheck", None),
		"DI_ChannelCheckFailedChA": (39, 2, (11, 0), (), "DI_ChannelCheckFailedChA", None),
		"DI_ChannelCheckFailedChB": (40, 2, (11, 0), (), "DI_ChannelCheckFailedChB", None),
		"DI_EyeNarrowing": (17, 2, (11, 0), (), "DI_EyeNarrowing", None),
		"DI_FrameRate": (19, 2, (5, 0), (), "DI_FrameRate", None),
		"DI_FrameRateDeviation": (21, 2, (5, 0), (), "DI_FrameRateDeviation", None),
		"DI_InputUnlocked": (14, 2, (11, 0), (), "DI_InputUnlocked", None),
		"DI_InputsTerminated": (13, 2, (11, 0), (), "DI_InputsTerminated", None),
		"DI_LOOPBACK_CHA": (11, 2, (2, 0), (), "DI_LOOPBACK_CHA", None),
		"DI_LOOPBACK_CHB": (12, 2, (2, 0), (), "DI_LOOPBACK_CHB", None),
		"DI_LOOPBACK_NONE": (10, 2, (2, 0), (), "DI_LOOPBACK_NONE", None),
		"DI_Loopback": (9, 2, (2, 0), (), "DI_Loopback", None),
		"DI_MaskBits": (32, 2, (2, 0), (), "DI_MaskBits", None),
		"DI_SOURCE_BNC": (3, 2, (2, 0), (), "DI_SOURCE_BNC", None),
		"DI_SOURCE_GENBNC": (7, 2, (2, 0), (), "DI_SOURCE_GENBNC", None),
		"DI_SOURCE_GENRCA": (8, 2, (2, 0), (), "DI_SOURCE_GENRCA", None),
		"DI_SOURCE_GENXLR": (6, 2, (2, 0), (), "DI_SOURCE_GENXLR", None),
		"DI_SOURCE_RCA": (4, 2, (2, 0), (), "DI_SOURCE_RCA", None),
		"DI_SOURCE_TOSLINK": (5, 2, (2, 0), (), "DI_SOURCE_TOSLINK", None),
		"DI_SOURCE_XLR": (2, 2, (2, 0), (), "DI_SOURCE_XLR", None),
		"DI_Source": (1, 2, (2, 0), (), "DI_Source", None),
		"DI_Split96": (33, 2, (11, 0), (), "DI_Split96", None),
	}
	_prop_map_put_ = {
		"DI_ActualFrameRate" : ((20, LCID, 4, 0),()),
		"DI_Asynchronous" : ((18, LCID, 4, 0),()),
		"DI_BiphaseViolation" : ((15, LCID, 4, 0),()),
		"DI_BlockLengthError" : ((16, LCID, 4, 0),()),
		"DI_CHANNELCHECK_16BITS" : ((36, LCID, 4, 0),()),
		"DI_CHANNELCHECK_20BITS" : ((37, LCID, 4, 0),()),
		"DI_CHANNELCHECK_24BITS" : ((38, LCID, 4, 0),()),
		"DI_CHANNELCHECK_OFF" : ((35, LCID, 4, 0),()),
		"DI_ChABitActivity" : ((22, LCID, 4, 0),()),
		"DI_ChABitState" : ((23, LCID, 4, 0),()),
		"DI_ChAChannelCheckFailed" : ((41, LCID, 4, 0),()),
		"DI_ChAUserBitActive" : ((28, LCID, 4, 0),()),
		"DI_ChAUserBitError" : ((30, LCID, 4, 0),()),
		"DI_ChAValid" : ((26, LCID, 4, 0),()),
		"DI_ChBBitActivity" : ((24, LCID, 4, 0),()),
		"DI_ChBBitState" : ((25, LCID, 4, 0),()),
		"DI_ChBChannelCheckFailed" : ((42, LCID, 4, 0),()),
		"DI_ChBUserBitActive" : ((29, LCID, 4, 0),()),
		"DI_ChBUserBitError" : ((31, LCID, 4, 0),()),
		"DI_ChBValid" : ((27, LCID, 4, 0),()),
		"DI_ChannelCheck" : ((34, LCID, 4, 0),()),
		"DI_ChannelCheckFailedChA" : ((39, LCID, 4, 0),()),
		"DI_ChannelCheckFailedChB" : ((40, LCID, 4, 0),()),
		"DI_EyeNarrowing" : ((17, LCID, 4, 0),()),
		"DI_FrameRate" : ((19, LCID, 4, 0),()),
		"DI_FrameRateDeviation" : ((21, LCID, 4, 0),()),
		"DI_InputUnlocked" : ((14, LCID, 4, 0),()),
		"DI_InputsTerminated" : ((13, LCID, 4, 0),()),
		"DI_LOOPBACK_CHA" : ((11, LCID, 4, 0),()),
		"DI_LOOPBACK_CHB" : ((12, LCID, 4, 0),()),
		"DI_LOOPBACK_NONE" : ((10, LCID, 4, 0),()),
		"DI_Loopback" : ((9, LCID, 4, 0),()),
		"DI_MaskBits" : ((32, LCID, 4, 0),()),
		"DI_SOURCE_BNC" : ((3, LCID, 4, 0),()),
		"DI_SOURCE_GENBNC" : ((7, LCID, 4, 0),()),
		"DI_SOURCE_GENRCA" : ((8, LCID, 4, 0),()),
		"DI_SOURCE_GENXLR" : ((6, LCID, 4, 0),()),
		"DI_SOURCE_RCA" : ((4, LCID, 4, 0),()),
		"DI_SOURCE_TOSLINK" : ((5, LCID, 4, 0),()),
		"DI_SOURCE_XLR" : ((2, LCID, 4, 0),()),
		"DI_Source" : ((1, LCID, 4, 0),()),
		"DI_Split96" : ((33, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDigitalOutputCarrier(DispatchBaseClass):
	CLSID = IID('{12E40661-E0F8-11D1-91DD-70AB00C10000}')
	coclass_clsid = IID('{12E40663-E0F8-11D1-91DD-70AB00C10000}')

	_prop_map_get_ = {
		"DOC_AddCMSignal": (29, 2, (11, 0), (), "DOC_AddCMSignal", None),
		"DOC_AddDifferentialNoise": (41, 2, (11, 0), (), "DOC_AddDifferentialNoise", None),
		"DOC_AddJitter": (32, 2, (11, 0), (), "DOC_AddJitter", None),
		"DOC_BNCAmpl": (2, 2, (5, 0), (), "DOC_BNCAmpl", None),
		"DOC_BNCNoiseAmpl": (43, 2, (5, 0), (), "DOC_BNCNoiseAmpl", None),
		"DOC_BNCRISETIME_10": (17, 2, (2, 0), (), "DOC_BNCRISETIME_10", None),
		"DOC_BNCRISETIME_100": (26, 2, (2, 0), (), "DOC_BNCRISETIME_100", None),
		"DOC_BNCRISETIME_20": (18, 2, (2, 0), (), "DOC_BNCRISETIME_20", None),
		"DOC_BNCRISETIME_30": (19, 2, (2, 0), (), "DOC_BNCRISETIME_30", None),
		"DOC_BNCRISETIME_40": (20, 2, (2, 0), (), "DOC_BNCRISETIME_40", None),
		"DOC_BNCRISETIME_5": (16, 2, (2, 0), (), "DOC_BNCRISETIME_5", None),
		"DOC_BNCRISETIME_50": (21, 2, (2, 0), (), "DOC_BNCRISETIME_50", None),
		"DOC_BNCRISETIME_60": (22, 2, (2, 0), (), "DOC_BNCRISETIME_60", None),
		"DOC_BNCRISETIME_70": (23, 2, (2, 0), (), "DOC_BNCRISETIME_70", None),
		"DOC_BNCRISETIME_80": (24, 2, (2, 0), (), "DOC_BNCRISETIME_80", None),
		"DOC_BNCRISETIME_90": (25, 2, (2, 0), (), "DOC_BNCRISETIME_90", None),
		"DOC_BNCRiseTime": (15, 2, (2, 0), (), "DOC_BNCRiseTime", None),
		"DOC_CMAmpl": (31, 2, (5, 0), (), "DOC_CMAmpl", None),
		"DOC_CMFreq": (30, 2, (5, 0), (), "DOC_CMFreq", None),
		"DOC_JITTERFUNCTION_AUDIONOISE": (36, 2, (2, 0), (), "DOC_JITTERFUNCTION_AUDIONOISE", None),
		"DOC_JITTERFUNCTION_LFSINE": (35, 2, (2, 0), (), "DOC_JITTERFUNCTION_LFSINE", None),
		"DOC_JITTERFUNCTION_SINE": (34, 2, (2, 0), (), "DOC_JITTERFUNCTION_SINE", None),
		"DOC_JITTERFUNCTION_WIDEBANDNOISE": (37, 2, (2, 0), (), "DOC_JITTERFUNCTION_WIDEBANDNOISE", None),
		"DOC_JitterAmpl": (39, 2, (5, 0), (), "DOC_JitterAmpl", None),
		"DOC_JitterAmplUnit": (40, 2, (2, 0), (), "DOC_JitterAmplUnit", None),
		"DOC_JitterFreq": (38, 2, (5, 0), (), "DOC_JitterFreq", None),
		"DOC_JitterFunction": (33, 2, (2, 0), (), "DOC_JitterFunction", None),
		"DOC_PhaseOffset": (27, 2, (5, 0), (), "DOC_PhaseOffset", None),
		"DOC_PhaseOffsetUnit": (28, 2, (2, 0), (), "DOC_PhaseOffsetUnit", None),
		"DOC_RCANoiseAmpl": (44, 2, (5, 0), (), "DOC_RCANoiseAmpl", None),
		"DOC_XLRAmpl": (1, 2, (5, 0), (), "DOC_XLRAmpl", None),
		"DOC_XLRNoiseAmpl": (42, 2, (5, 0), (), "DOC_XLRNoiseAmpl", None),
		"DOC_XLRRISETIME_10": (5, 2, (2, 0), (), "DOC_XLRRISETIME_10", None),
		"DOC_XLRRISETIME_100": (14, 2, (2, 0), (), "DOC_XLRRISETIME_100", None),
		"DOC_XLRRISETIME_20": (6, 2, (2, 0), (), "DOC_XLRRISETIME_20", None),
		"DOC_XLRRISETIME_30": (7, 2, (2, 0), (), "DOC_XLRRISETIME_30", None),
		"DOC_XLRRISETIME_40": (8, 2, (2, 0), (), "DOC_XLRRISETIME_40", None),
		"DOC_XLRRISETIME_5": (4, 2, (2, 0), (), "DOC_XLRRISETIME_5", None),
		"DOC_XLRRISETIME_50": (9, 2, (2, 0), (), "DOC_XLRRISETIME_50", None),
		"DOC_XLRRISETIME_60": (10, 2, (2, 0), (), "DOC_XLRRISETIME_60", None),
		"DOC_XLRRISETIME_70": (11, 2, (2, 0), (), "DOC_XLRRISETIME_70", None),
		"DOC_XLRRISETIME_80": (12, 2, (2, 0), (), "DOC_XLRRISETIME_80", None),
		"DOC_XLRRISETIME_90": (13, 2, (2, 0), (), "DOC_XLRRISETIME_90", None),
		"DOC_XLRRiseTime": (3, 2, (2, 0), (), "DOC_XLRRiseTime", None),
	}
	_prop_map_put_ = {
		"DOC_AddCMSignal" : ((29, LCID, 4, 0),()),
		"DOC_AddDifferentialNoise" : ((41, LCID, 4, 0),()),
		"DOC_AddJitter" : ((32, LCID, 4, 0),()),
		"DOC_BNCAmpl" : ((2, LCID, 4, 0),()),
		"DOC_BNCNoiseAmpl" : ((43, LCID, 4, 0),()),
		"DOC_BNCRISETIME_10" : ((17, LCID, 4, 0),()),
		"DOC_BNCRISETIME_100" : ((26, LCID, 4, 0),()),
		"DOC_BNCRISETIME_20" : ((18, LCID, 4, 0),()),
		"DOC_BNCRISETIME_30" : ((19, LCID, 4, 0),()),
		"DOC_BNCRISETIME_40" : ((20, LCID, 4, 0),()),
		"DOC_BNCRISETIME_5" : ((16, LCID, 4, 0),()),
		"DOC_BNCRISETIME_50" : ((21, LCID, 4, 0),()),
		"DOC_BNCRISETIME_60" : ((22, LCID, 4, 0),()),
		"DOC_BNCRISETIME_70" : ((23, LCID, 4, 0),()),
		"DOC_BNCRISETIME_80" : ((24, LCID, 4, 0),()),
		"DOC_BNCRISETIME_90" : ((25, LCID, 4, 0),()),
		"DOC_BNCRiseTime" : ((15, LCID, 4, 0),()),
		"DOC_CMAmpl" : ((31, LCID, 4, 0),()),
		"DOC_CMFreq" : ((30, LCID, 4, 0),()),
		"DOC_JITTERFUNCTION_AUDIONOISE" : ((36, LCID, 4, 0),()),
		"DOC_JITTERFUNCTION_LFSINE" : ((35, LCID, 4, 0),()),
		"DOC_JITTERFUNCTION_SINE" : ((34, LCID, 4, 0),()),
		"DOC_JITTERFUNCTION_WIDEBANDNOISE" : ((37, LCID, 4, 0),()),
		"DOC_JitterAmpl" : ((39, LCID, 4, 0),()),
		"DOC_JitterAmplUnit" : ((40, LCID, 4, 0),()),
		"DOC_JitterFreq" : ((38, LCID, 4, 0),()),
		"DOC_JitterFunction" : ((33, LCID, 4, 0),()),
		"DOC_PhaseOffset" : ((27, LCID, 4, 0),()),
		"DOC_PhaseOffsetUnit" : ((28, LCID, 4, 0),()),
		"DOC_RCANoiseAmpl" : ((44, LCID, 4, 0),()),
		"DOC_XLRAmpl" : ((1, LCID, 4, 0),()),
		"DOC_XLRNoiseAmpl" : ((42, LCID, 4, 0),()),
		"DOC_XLRRISETIME_10" : ((5, LCID, 4, 0),()),
		"DOC_XLRRISETIME_100" : ((14, LCID, 4, 0),()),
		"DOC_XLRRISETIME_20" : ((6, LCID, 4, 0),()),
		"DOC_XLRRISETIME_30" : ((7, LCID, 4, 0),()),
		"DOC_XLRRISETIME_40" : ((8, LCID, 4, 0),()),
		"DOC_XLRRISETIME_5" : ((4, LCID, 4, 0),()),
		"DOC_XLRRISETIME_50" : ((9, LCID, 4, 0),()),
		"DOC_XLRRISETIME_60" : ((10, LCID, 4, 0),()),
		"DOC_XLRRISETIME_70" : ((11, LCID, 4, 0),()),
		"DOC_XLRRISETIME_80" : ((12, LCID, 4, 0),()),
		"DOC_XLRRISETIME_90" : ((13, LCID, 4, 0),()),
		"DOC_XLRRiseTime" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDigitalOutputs(DispatchBaseClass):
	CLSID = IID('{C8EA98A6-E3F7-11D1-91DD-70AB00C10000}')
	coclass_clsid = IID('{C8EA98A8-E3F7-11D1-91DD-70AB00C10000}')

	_prop_map_get_ = {
		"DO_AddFrameRateDeviation": (33, 2, (11, 0), (), "DO_AddFrameRateDeviation", None),
		"DO_CHANNELCHECK_16BITS": (9, 2, (2, 0), (), "DO_CHANNELCHECK_16BITS", None),
		"DO_CHANNELCHECK_20BITS": (10, 2, (2, 0), (), "DO_CHANNELCHECK_20BITS", None),
		"DO_CHANNELCHECK_24BITS": (11, 2, (2, 0), (), "DO_CHANNELCHECK_24BITS", None),
		"DO_ChAValidBit": (35, 2, (2, 0), (), "DO_ChAValidBit", None),
		"DO_ChBValidBit": (36, 2, (2, 0), (), "DO_ChBValidBit", None),
		"DO_ChannelCheck": (8, 2, (2, 0), (), "DO_ChannelCheck", None),
		"DO_DCOFFSETPOLARITY_NEG": (49, 2, (2, 0), (), "DO_DCOFFSETPOLARITY_NEG", None),
		"DO_DCOFFSETPOLARITY_POS": (48, 2, (2, 0), (), "DO_DCOFFSETPOLARITY_POS", None),
		"DO_DCOffset": (45, 2, (5, 0), (), "DO_DCOffset", None),
		"DO_DCOffsetPolarity": (47, 2, (2, 0), (), "DO_DCOffsetPolarity", None),
		"DO_DCOffsetUnit": (46, 2, (2, 0), (), "DO_DCOffsetUnit", None),
		"DO_DITHERING_UNDITHERED": (42, 2, (2, 0), (), "DO_DITHERING_UNDITHERED", None),
		"DO_DITHERING_WHITE": (43, 2, (2, 0), (), "DO_DITHERING_WHITE", None),
		"DO_Dithering": (41, 2, (2, 0), (), "DO_Dithering", None),
		"DO_FRAMERATE_176400": (30, 2, (3, 0), (), "DO_FRAMERATE_176400", None),
		"DO_FRAMERATE_192000": (31, 2, (3, 0), (), "DO_FRAMERATE_192000", None),
		"DO_FRAMERATE_32000": (25, 2, (3, 0), (), "DO_FRAMERATE_32000", None),
		"DO_FRAMERATE_44100": (26, 2, (3, 0), (), "DO_FRAMERATE_44100", None),
		"DO_FRAMERATE_48000": (27, 2, (3, 0), (), "DO_FRAMERATE_48000", None),
		"DO_FRAMERATE_88200": (28, 2, (3, 0), (), "DO_FRAMERATE_88200", None),
		"DO_FRAMERATE_96000": (29, 2, (3, 0), (), "DO_FRAMERATE_96000", None),
		"DO_FRAMERATE_FOLLOWSYNC": (32, 2, (3, 0), (), "DO_FRAMERATE_FOLLOWSYNC", None),
		"DO_FrameRate": (24, 2, (3, 0), (), "DO_FrameRate", None),
		"DO_FrameRateDeviation": (34, 2, (2, 0), (), "DO_FrameRateDeviation", None),
		"DO_Mute": (1, 2, (11, 0), (), "DO_Mute", None),
		"DO_MuteChA": (2, 2, (11, 0), (), "DO_MuteChA", None),
		"DO_MuteChB": (3, 2, (11, 0), (), "DO_MuteChB", None),
		"DO_NoiseShaper": (44, 2, (2, 0), (), "DO_NoiseShaper", None),
		"DO_REFSYNCSOURCE_BNCAES11DARS": (16, 2, (2, 0), (), "DO_REFSYNCSOURCE_BNCAES11DARS", None),
		"DO_REFSYNCSOURCE_BNCVIDEO": (19, 2, (2, 0), (), "DO_REFSYNCSOURCE_BNCVIDEO", None),
		"DO_REFSYNCSOURCE_BNCVIDEONTSC30": (18, 2, (2, 0), (), "DO_REFSYNCSOURCE_BNCVIDEONTSC30", None),
		"DO_REFSYNCSOURCE_BNCWORDCLOCK": (17, 2, (2, 0), (), "DO_REFSYNCSOURCE_BNCWORDCLOCK", None),
		"DO_REFSYNCSOURCE_DIGINPUT": (14, 2, (2, 0), (), "DO_REFSYNCSOURCE_DIGINPUT", None),
		"DO_REFSYNCSOURCE_INTERNAL": (13, 2, (2, 0), (), "DO_REFSYNCSOURCE_INTERNAL", None),
		"DO_REFSYNCSOURCE_XLRAES11DARS": (15, 2, (2, 0), (), "DO_REFSYNCSOURCE_XLRAES11DARS", None),
		"DO_RefSyncActualFrameRate": (22, 2, (5, 0), (), "DO_RefSyncActualFrameRate", None),
		"DO_RefSyncFrameRate": (21, 2, (5, 0), (), "DO_RefSyncFrameRate", None),
		"DO_RefSyncFrameRateDeviation": (23, 2, (5, 0), (), "DO_RefSyncFrameRateDeviation", None),
		"DO_RefSyncInputsTerminated": (20, 2, (11, 0), (), "DO_RefSyncInputsTerminated", None),
		"DO_RefSyncSource": (12, 2, (2, 0), (), "DO_RefSyncSource", None),
		"DO_SOURCE_CHANNELCHECK": (7, 2, (2, 0), (), "DO_SOURCE_CHANNELCHECK", None),
		"DO_SOURCE_GEN": (5, 2, (2, 0), (), "DO_SOURCE_GEN", None),
		"DO_SOURCE_LOOPTHROUGH": (6, 2, (2, 0), (), "DO_SOURCE_LOOPTHROUGH", None),
		"DO_Source": (4, 2, (2, 0), (), "DO_Source", None),
		"DO_Split96": (50, 2, (11, 0), (), "DO_Split96", None),
		"DO_UserBitCheck": (39, 2, (11, 0), (), "DO_UserBitCheck", None),
		"DO_VBIT_INVALID": (38, 2, (2, 0), (), "DO_VBIT_INVALID", None),
		"DO_VBIT_VALID": (37, 2, (2, 0), (), "DO_VBIT_VALID", None),
		"DO_Wordlength": (40, 2, (2, 0), (), "DO_Wordlength", None),
	}
	_prop_map_put_ = {
		"DO_AddFrameRateDeviation" : ((33, LCID, 4, 0),()),
		"DO_CHANNELCHECK_16BITS" : ((9, LCID, 4, 0),()),
		"DO_CHANNELCHECK_20BITS" : ((10, LCID, 4, 0),()),
		"DO_CHANNELCHECK_24BITS" : ((11, LCID, 4, 0),()),
		"DO_ChAValidBit" : ((35, LCID, 4, 0),()),
		"DO_ChBValidBit" : ((36, LCID, 4, 0),()),
		"DO_ChannelCheck" : ((8, LCID, 4, 0),()),
		"DO_DCOFFSETPOLARITY_NEG" : ((49, LCID, 4, 0),()),
		"DO_DCOFFSETPOLARITY_POS" : ((48, LCID, 4, 0),()),
		"DO_DCOffset" : ((45, LCID, 4, 0),()),
		"DO_DCOffsetPolarity" : ((47, LCID, 4, 0),()),
		"DO_DCOffsetUnit" : ((46, LCID, 4, 0),()),
		"DO_DITHERING_UNDITHERED" : ((42, LCID, 4, 0),()),
		"DO_DITHERING_WHITE" : ((43, LCID, 4, 0),()),
		"DO_Dithering" : ((41, LCID, 4, 0),()),
		"DO_FRAMERATE_176400" : ((30, LCID, 4, 0),()),
		"DO_FRAMERATE_192000" : ((31, LCID, 4, 0),()),
		"DO_FRAMERATE_32000" : ((25, LCID, 4, 0),()),
		"DO_FRAMERATE_44100" : ((26, LCID, 4, 0),()),
		"DO_FRAMERATE_48000" : ((27, LCID, 4, 0),()),
		"DO_FRAMERATE_88200" : ((28, LCID, 4, 0),()),
		"DO_FRAMERATE_96000" : ((29, LCID, 4, 0),()),
		"DO_FRAMERATE_FOLLOWSYNC" : ((32, LCID, 4, 0),()),
		"DO_FrameRate" : ((24, LCID, 4, 0),()),
		"DO_FrameRateDeviation" : ((34, LCID, 4, 0),()),
		"DO_Mute" : ((1, LCID, 4, 0),()),
		"DO_MuteChA" : ((2, LCID, 4, 0),()),
		"DO_MuteChB" : ((3, LCID, 4, 0),()),
		"DO_NoiseShaper" : ((44, LCID, 4, 0),()),
		"DO_REFSYNCSOURCE_BNCAES11DARS" : ((16, LCID, 4, 0),()),
		"DO_REFSYNCSOURCE_BNCVIDEO" : ((19, LCID, 4, 0),()),
		"DO_REFSYNCSOURCE_BNCVIDEONTSC30" : ((18, LCID, 4, 0),()),
		"DO_REFSYNCSOURCE_BNCWORDCLOCK" : ((17, LCID, 4, 0),()),
		"DO_REFSYNCSOURCE_DIGINPUT" : ((14, LCID, 4, 0),()),
		"DO_REFSYNCSOURCE_INTERNAL" : ((13, LCID, 4, 0),()),
		"DO_REFSYNCSOURCE_XLRAES11DARS" : ((15, LCID, 4, 0),()),
		"DO_RefSyncActualFrameRate" : ((22, LCID, 4, 0),()),
		"DO_RefSyncFrameRate" : ((21, LCID, 4, 0),()),
		"DO_RefSyncFrameRateDeviation" : ((23, LCID, 4, 0),()),
		"DO_RefSyncInputsTerminated" : ((20, LCID, 4, 0),()),
		"DO_RefSyncSource" : ((12, LCID, 4, 0),()),
		"DO_SOURCE_CHANNELCHECK" : ((7, LCID, 4, 0),()),
		"DO_SOURCE_GEN" : ((5, LCID, 4, 0),()),
		"DO_SOURCE_LOOPTHROUGH" : ((6, LCID, 4, 0),()),
		"DO_Source" : ((4, LCID, 4, 0),()),
		"DO_Split96" : ((50, LCID, 4, 0),()),
		"DO_UserBitCheck" : ((39, LCID, 4, 0),()),
		"DO_VBIT_INVALID" : ((38, LCID, 4, 0),()),
		"DO_VBIT_VALID" : ((37, LCID, 4, 0),()),
		"DO_Wordlength" : ((40, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IEventManager(DispatchBaseClass):
	CLSID = IID('{D59FA601-A542-11D2-91DE-70AB00C10000}')
	coclass_clsid = IID('{BB07F160-D1B6-11D4-AA54-0050046915E5}')

	def EM_EventOn(self, sEventID=defaultNamedNotOptArg, bOn=defaultNamedNotOptArg):
		'EM_EventOn'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (24, 0), ((2, 0), (11, 0)),sEventID
			, bOn)

	def EM_GetEvent(self, sEventID=defaultNamedNotOptArg, bEventOn=defaultNamedNotOptArg, bBeep=defaultNamedNotOptArg, bLogToFile=defaultNamedNotOptArg
			, strScriptName=defaultNamedNotOptArg):
		'EM_GetEvent'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (11, 0), ((2, 0), (16396, 0), (16396, 0), (16396, 0), (16396, 0)),sEventID
			, bEventOn, bBeep, bLogToFile, strScriptName)

	def EM_SetEvent(self, sEventID=defaultNamedNotOptArg, bEventOn=defaultNamedNotOptArg, bBeep=defaultNamedNotOptArg, bLogToFile=defaultNamedNotOptArg
			, strScriptName=defaultNamedNotOptArg):
		'EM_SetEvent'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (24, 0), ((2, 0), (11, 0), (11, 0), (11, 0), (8, 0)),sEventID
			, bEventOn, bBeep, bLogToFile, strScriptName)

	_prop_map_get_ = {
		"EM_EVENT_CARRIERASYNC": (9, 2, (2, 0), (), "EM_EVENT_CARRIERASYNC", None),
		"EM_EVENT_CARRIERBIPHASE": (6, 2, (2, 0), (), "EM_EVENT_CARRIERBIPHASE", None),
		"EM_EVENT_CARRIERBLOCKLENGTH": (7, 2, (2, 0), (), "EM_EVENT_CARRIERBLOCKLENGTH", None),
		"EM_EVENT_CARRIEREYENARROWING": (8, 2, (2, 0), (), "EM_EVENT_CARRIEREYENARROWING", None),
		"EM_EVENT_CARRIERINPUTLOCKING": (5, 2, (2, 0), (), "EM_EVENT_CARRIERINPUTLOCKING", None),
		"EM_EVENT_CHANNELCHECKFAILED_CHA": (10, 2, (2, 0), (), "EM_EVENT_CHANNELCHECKFAILED_CHA", None),
		"EM_EVENT_CHANNELCHECKFAILED_CHB": (11, 2, (2, 0), (), "EM_EVENT_CHANNELCHECKFAILED_CHB", None),
		"EM_EVENT_CHAVALIDBIT": (3, 2, (2, 0), (), "EM_EVENT_CHAVALIDBIT", None),
		"EM_EVENT_CHBVALIDBIT": (4, 2, (2, 0), (), "EM_EVENT_CHBVALIDBIT", None),
		"EM_EVENT_CSANOTEQUALTOB": (17, 2, (2, 0), (), "EM_EVENT_CSANOTEQUALTOB", None),
		"EM_EVENT_CSCHANNELMODE": (15, 2, (2, 0), (), "EM_EVENT_CSCHANNELMODE", None),
		"EM_EVENT_CSCOPYRIGHTBIT": (13, 2, (2, 0), (), "EM_EVENT_CSCOPYRIGHTBIT", None),
		"EM_EVENT_CSCRCERROR": (16, 2, (2, 0), (), "EM_EVENT_CSCRCERROR", None),
		"EM_EVENT_CSEMPHASIS": (14, 2, (2, 0), (), "EM_EVENT_CSEMPHASIS", None),
		"EM_EVENT_CSPROFBIT": (12, 2, (2, 0), (), "EM_EVENT_CSPROFBIT", None),
		"EM_EVENT_FFTBUFFERPROCESSED": (23, 2, (2, 0), (), "EM_EVENT_FFTBUFFERPROCESSED", None),
		"EM_EVENT_FFTTRIGGER": (22, 2, (2, 0), (), "EM_EVENT_FFTTRIGGER", None),
		"EM_EVENT_KEYPRESS": (33, 2, (2, 0), (), "EM_EVENT_KEYPRESS", None),
		"EM_EVENT_READINGMAXLIMIT": (25, 2, (2, 0), (), "EM_EVENT_READINGMAXLIMIT", None),
		"EM_EVENT_READINGMINLIMIT": (24, 2, (2, 0), (), "EM_EVENT_READINGMINLIMIT", None),
		"EM_EVENT_SCRIPTED": (34, 2, (2, 0), (), "EM_EVENT_SCRIPTED", None),
		"EM_EVENT_SWEEPFINISHED": (30, 2, (2, 0), (), "EM_EVENT_SWEEPFINISHED", None),
		"EM_EVENT_SWEEPSENSE": (31, 2, (2, 0), (), "EM_EVENT_SWEEPSENSE", None),
		"EM_EVENT_SWEEPSTARTED": (28, 2, (2, 0), (), "EM_EVENT_SWEEPSTARTED", None),
		"EM_EVENT_SWEEPSTEPDONE": (29, 2, (2, 0), (), "EM_EVENT_SWEEPSTEPDONE", None),
		"EM_EVENT_TIMER": (32, 2, (2, 0), (), "EM_EVENT_TIMER", None),
		"EM_EVENT_TRACEMAXLIMIT": (27, 2, (2, 0), (), "EM_EVENT_TRACEMAXLIMIT", None),
		"EM_EVENT_TRACEMINLIMIT": (26, 2, (2, 0), (), "EM_EVENT_TRACEMINLIMIT", None),
		"EM_EVENT_USERBITACTIVE_CHA": (18, 2, (2, 0), (), "EM_EVENT_USERBITACTIVE_CHA", None),
		"EM_EVENT_USERBITACTIVE_CHB": (19, 2, (2, 0), (), "EM_EVENT_USERBITACTIVE_CHB", None),
		"EM_EVENT_USERBITERROR_CHA": (20, 2, (2, 0), (), "EM_EVENT_USERBITERROR_CHA", None),
		"EM_EVENT_USERBITERROR_CHB": (21, 2, (2, 0), (), "EM_EVENT_USERBITERROR_CHB", None),
		"EM_LogFile": (2, 2, (8, 0), (), "EM_LogFile", None),
		"EM_On": (1, 2, (11, 0), (), "EM_On", None),
	}
	_prop_map_put_ = {
		"EM_EVENT_CARRIERASYNC" : ((9, LCID, 4, 0),()),
		"EM_EVENT_CARRIERBIPHASE" : ((6, LCID, 4, 0),()),
		"EM_EVENT_CARRIERBLOCKLENGTH" : ((7, LCID, 4, 0),()),
		"EM_EVENT_CARRIEREYENARROWING" : ((8, LCID, 4, 0),()),
		"EM_EVENT_CARRIERINPUTLOCKING" : ((5, LCID, 4, 0),()),
		"EM_EVENT_CHANNELCHECKFAILED_CHA" : ((10, LCID, 4, 0),()),
		"EM_EVENT_CHANNELCHECKFAILED_CHB" : ((11, LCID, 4, 0),()),
		"EM_EVENT_CHAVALIDBIT" : ((3, LCID, 4, 0),()),
		"EM_EVENT_CHBVALIDBIT" : ((4, LCID, 4, 0),()),
		"EM_EVENT_CSANOTEQUALTOB" : ((17, LCID, 4, 0),()),
		"EM_EVENT_CSCHANNELMODE" : ((15, LCID, 4, 0),()),
		"EM_EVENT_CSCOPYRIGHTBIT" : ((13, LCID, 4, 0),()),
		"EM_EVENT_CSCRCERROR" : ((16, LCID, 4, 0),()),
		"EM_EVENT_CSEMPHASIS" : ((14, LCID, 4, 0),()),
		"EM_EVENT_CSPROFBIT" : ((12, LCID, 4, 0),()),
		"EM_EVENT_FFTBUFFERPROCESSED" : ((23, LCID, 4, 0),()),
		"EM_EVENT_FFTTRIGGER" : ((22, LCID, 4, 0),()),
		"EM_EVENT_KEYPRESS" : ((33, LCID, 4, 0),()),
		"EM_EVENT_READINGMAXLIMIT" : ((25, LCID, 4, 0),()),
		"EM_EVENT_READINGMINLIMIT" : ((24, LCID, 4, 0),()),
		"EM_EVENT_SCRIPTED" : ((34, LCID, 4, 0),()),
		"EM_EVENT_SWEEPFINISHED" : ((30, LCID, 4, 0),()),
		"EM_EVENT_SWEEPSENSE" : ((31, LCID, 4, 0),()),
		"EM_EVENT_SWEEPSTARTED" : ((28, LCID, 4, 0),()),
		"EM_EVENT_SWEEPSTEPDONE" : ((29, LCID, 4, 0),()),
		"EM_EVENT_TIMER" : ((32, LCID, 4, 0),()),
		"EM_EVENT_TRACEMAXLIMIT" : ((27, LCID, 4, 0),()),
		"EM_EVENT_TRACEMINLIMIT" : ((26, LCID, 4, 0),()),
		"EM_EVENT_USERBITACTIVE_CHA" : ((18, LCID, 4, 0),()),
		"EM_EVENT_USERBITACTIVE_CHB" : ((19, LCID, 4, 0),()),
		"EM_EVENT_USERBITERROR_CHA" : ((20, LCID, 4, 0),()),
		"EM_EVENT_USERBITERROR_CHB" : ((21, LCID, 4, 0),()),
		"EM_LogFile" : ((2, LCID, 4, 0),()),
		"EM_On" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IFFTDetector(DispatchBaseClass):
	CLSID = IID('{B9A66201-2AB2-11D2-91DE-70AB00C10000}')
	coclass_clsid = IID('{B9A66203-2AB2-11D2-91DE-70AB00C10000}')

	def FFTD_GetBuffer(self, sBuffer=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg, lStartIndex=defaultNamedNotOptArg, lEndIndex=defaultNamedNotOptArg
			, sUnit=defaultNamedNotOptArg, sRelativity=defaultNamedNotOptArg, pdBuffer=defaultNamedNotOptArg):
		'FFTD_GetBuffer'
		return self._oleobj_.InvokeTypes(86, LCID, 1, (11, 0), ((2, 0), (2, 0), (3, 0), (3, 0), (2, 0), (2, 0), (16396, 0)),sBuffer
			, sChannel, lStartIndex, lEndIndex, sUnit, sRelativity
			, pdBuffer)

	def FFTD_GetBufferHighestAmplToneBin(self, sBuffer=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg, lStartBin=defaultNamedNotOptArg, lEndBin=defaultNamedNotOptArg):
		'FFTD_GetBufferHighestAmplTone'
		return self._oleobj_.InvokeTypes(84, LCID, 1, (3, 0), ((2, 0), (2, 0), (3, 0), (3, 0)),sBuffer
			, sChannel, lStartBin, lEndBin)

	def FFTD_GetBufferLowestAmplToneBin(self, sBuffer=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg, lStartBin=defaultNamedNotOptArg, lEndBin=defaultNamedNotOptArg
			, dThreshold=defaultNamedNotOptArg, sThresholdUnit=defaultNamedNotOptArg, sThresholdRelativity=defaultNamedNotOptArg):
		'FFTD_GetBufferLowestAmplToneBi'
		return self._oleobj_.InvokeTypes(85, LCID, 1, (3, 0), ((2, 0), (2, 0), (3, 0), (3, 0), (5, 0), (2, 0), (2, 0)),sBuffer
			, sChannel, lStartBin, lEndBin, dThreshold, sThresholdUnit
			, sThresholdRelativity)

	def FFTD_GetBufferSize(self, sBuffer=defaultNamedNotOptArg):
		'FFTD_GetBufferSize'
		return self._oleobj_.InvokeTypes(76, LCID, 1, (3, 0), ((2, 0),),sBuffer
			)

	def FFTD_GetBufferValueAt(self, sBuffer=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg, lIndex=defaultNamedNotOptArg, sUnit=defaultNamedNotOptArg
			, sRelativity=defaultNamedNotOptArg):
		'FFTD_GetBufferValueAt'
		return self._oleobj_.InvokeTypes(77, LCID, 1, (5, 0), ((2, 0), (2, 0), (3, 0), (2, 0), (2, 0)),sBuffer
			, sChannel, lIndex, sUnit, sRelativity)

	def FFTD_GetFFTBinPowerInUnit(self, dValue=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg, sUnit=defaultNamedNotOptArg, sRelativity=defaultNamedNotOptArg):
		'FFTD_GetFFTBinPowerInUnit'
		return self._oleobj_.InvokeTypes(78, LCID, 1, (5, 0), ((5, 0), (2, 0), (2, 0), (2, 0)),dValue
			, sChannel, sUnit, sRelativity)

	def FFTD_GetFilteredFFTBinTotal(self, sChannel=defaultNamedNotOptArg, sUnit=defaultNamedNotOptArg, sRelativity=defaultNamedNotOptArg):
		'FFTD_GetFilteredFFTBinTotal'
		return self._oleobj_.InvokeTypes(80, LCID, 1, (5, 0), ((2, 0), (2, 0), (2, 0)),sChannel
			, sUnit, sRelativity)

	def FFTD_GetUnfilteredFFTBinTotal(self, sChannel=defaultNamedNotOptArg, sUnit=defaultNamedNotOptArg, sRelativity=defaultNamedNotOptArg):
		'FFTD_GetUnfilteredFFTBinTotal'
		return self._oleobj_.InvokeTypes(79, LCID, 1, (5, 0), ((2, 0), (2, 0), (2, 0)),sChannel
			, sUnit, sRelativity)

	def FFTD_SetChannelA(self, dValue=defaultNamedNotOptArg, sUnit=defaultNamedNotOptArg, sRelativity=defaultNamedNotOptArg):
		'FFTD_SetChannelA'
		return self._oleobj_.InvokeTypes(74, LCID, 1, (24, 0), ((5, 0), (2, 0), (2, 0)),dValue
			, sUnit, sRelativity)

	def FFTD_SetChannelB(self, dValue=defaultNamedNotOptArg, sUnit=defaultNamedNotOptArg, sRelativity=defaultNamedNotOptArg):
		'FFTD_SetChannelB'
		return self._oleobj_.InvokeTypes(75, LCID, 1, (24, 0), ((5, 0), (2, 0), (2, 0)),dValue
			, sUnit, sRelativity)

	def FFTD_SumBufferBins(self, sBuffer=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg, lStartBin=defaultNamedNotOptArg, lEndBin=defaultNamedNotOptArg
			, sUnit=defaultNamedNotOptArg, sRelativity=defaultNamedNotOptArg):
		'FFTD_SumBufferBins'
		return self._oleobj_.InvokeTypes(81, LCID, 1, (5, 0), ((2, 0), (2, 0), (3, 0), (3, 0), (2, 0), (2, 0)),sBuffer
			, sChannel, lStartBin, lEndBin, sUnit, sRelativity
			)

	def FFTD_SumBufferEvenBins(self, sBuffer=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg, lStartBin=defaultNamedNotOptArg, lEndBin=defaultNamedNotOptArg
			, sUnit=defaultNamedNotOptArg, sRelativity=defaultNamedNotOptArg):
		'FFTD_SumBufferEvenBins'
		return self._oleobj_.InvokeTypes(82, LCID, 1, (5, 0), ((2, 0), (2, 0), (3, 0), (3, 0), (2, 0), (2, 0)),sBuffer
			, sChannel, lStartBin, lEndBin, sUnit, sRelativity
			)

	def FFTD_SumBufferOddBins(self, sBuffer=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg, lStartBin=defaultNamedNotOptArg, lEndBin=defaultNamedNotOptArg
			, sUnit=defaultNamedNotOptArg, sRelativity=defaultNamedNotOptArg):
		'FFTD_SumBufferOddBins'
		return self._oleobj_.InvokeTypes(83, LCID, 1, (5, 0), ((2, 0), (2, 0), (3, 0), (3, 0), (2, 0), (2, 0)),sBuffer
			, sChannel, lStartBin, lEndBin, sUnit, sRelativity
			)

	_prop_map_get_ = {
		"FFTD_BPBRBANDWIDTH_12": (14, 2, (2, 0), (), "FFTD_BPBRBANDWIDTH_12", None),
		"FFTD_BPBRBANDWIDTH_24": (15, 2, (2, 0), (), "FFTD_BPBRBANDWIDTH_24", None),
		"FFTD_BPBRBANDWIDTH_3": (12, 2, (2, 0), (), "FFTD_BPBRBANDWIDTH_3", None),
		"FFTD_BPBRBANDWIDTH_6": (13, 2, (2, 0), (), "FFTD_BPBRBANDWIDTH_6", None),
		"FFTD_BPBRBANDWIDTH_NOTCH": (16, 2, (2, 0), (), "FFTD_BPBRBANDWIDTH_NOTCH", None),
		"FFTD_BPBRBandwidth": (11, 2, (2, 0), (), "FFTD_BPBRBandwidth", None),
		"FFTD_BPBRFREQMODE_2NDHARM": (26, 2, (2, 0), (), "FFTD_BPBRFREQMODE_2NDHARM", None),
		"FFTD_BPBRFREQMODE_3RDHARM": (27, 2, (2, 0), (), "FFTD_BPBRFREQMODE_3RDHARM", None),
		"FFTD_BPBRFREQMODE_4THHARM": (28, 2, (2, 0), (), "FFTD_BPBRFREQMODE_4THHARM", None),
		"FFTD_BPBRFREQMODE_ALLHARM": (24, 2, (2, 0), (), "FFTD_BPBRFREQMODE_ALLHARM", None),
		"FFTD_BPBRFREQMODE_ALLHARM_FUND": (25, 2, (2, 0), (), "FFTD_BPBRFREQMODE_ALLHARM_FUND", None),
		"FFTD_BPBRFREQMODE_FIXED": (21, 2, (2, 0), (), "FFTD_BPBRFREQMODE_FIXED", None),
		"FFTD_BPBRFREQMODE_GEN": (19, 2, (2, 0), (), "FFTD_BPBRFREQMODE_GEN", None),
		"FFTD_BPBRFREQMODE_GENOTHER": (20, 2, (2, 0), (), "FFTD_BPBRFREQMODE_GENOTHER", None),
		"FFTD_BPBRFREQMODE_IMDDIFF": (22, 2, (2, 0), (), "FFTD_BPBRFREQMODE_IMDDIFF", None),
		"FFTD_BPBRFREQMODE_IMDSIDE": (23, 2, (2, 0), (), "FFTD_BPBRFREQMODE_IMDSIDE", None),
		"FFTD_BPBRFREQMODE_INPUT": (18, 2, (2, 0), (), "FFTD_BPBRFREQMODE_INPUT", None),
		"FFTD_BPBRFREQMODE_NTHHARM": (29, 2, (2, 0), (), "FFTD_BPBRFREQMODE_NTHHARM", None),
		"FFTD_BPBRFreq": (30, 2, (5, 0), (), "FFTD_BPBRFreq", None),
		"FFTD_BPBRFreqMode": (17, 2, (2, 0), (), "FFTD_BPBRFreqMode", None),
		"FFTD_BPBRMODE_BP": (9, 2, (2, 0), (), "FFTD_BPBRMODE_BP", None),
		"FFTD_BPBRMODE_BR": (10, 2, (2, 0), (), "FFTD_BPBRMODE_BR", None),
		"FFTD_BPBRMODE_OFF": (8, 2, (2, 0), (), "FFTD_BPBRMODE_OFF", None),
		"FFTD_BPBRMode": (7, 2, (2, 0), (), "FFTD_BPBRMode", None),
		"FFTD_BUFFER_CTA": (68, 2, (2, 0), (), "FFTD_BUFFER_CTA", None),
		"FFTD_BUFFER_CTA_FFT": (69, 2, (2, 0), (), "FFTD_BUFFER_CTA_FFT", None),
		"FFTD_BUFFER_FFT_FILTERED": (73, 2, (2, 0), (), "FFTD_BUFFER_FFT_FILTERED", None),
		"FFTD_BUFFER_FFT_PREWEIGHTED": (72, 2, (2, 0), (), "FFTD_BUFFER_FFT_PREWEIGHTED", None),
		"FFTD_BUFFER_FFT_UNFILTERED": (71, 2, (2, 0), (), "FFTD_BUFFER_FFT_UNFILTERED", None),
		"FFTD_BUFFER_PHASE": (70, 2, (2, 0), (), "FFTD_BUFFER_PHASE", None),
		"FFTD_BUFFER_SAMPLE": (67, 2, (2, 0), (), "FFTD_BUFFER_SAMPLE", None),
		"FFTD_BrickWallHPFilter": (50, 2, (11, 0), (), "FFTD_BrickWallHPFilter", None),
		"FFTD_BrickWallLPFilter": (51, 2, (11, 0), (), "FFTD_BrickWallLPFilter", None),
		"FFTD_ChA": (2, 2, (5, 0), (), "FFTD_ChA", None),
		"FFTD_ChB": (3, 2, (5, 0), (), "FFTD_ChB", None),
		"FFTD_Function": (5, 2, (8, 0), (), "FFTD_Function", None),
		"FFTD_HPFilter": (32, 2, (2, 0), (), "FFTD_HPFilter", None),
		"FFTD_HPFilterFreq": (33, 2, (3, 0), (), "FFTD_HPFilterFreq", None),
		"FFTD_HP_100HZ": (38, 2, (2, 0), (), "FFTD_HP_100HZ", None),
		"FFTD_HP_10HZ": (36, 2, (2, 0), (), "FFTD_HP_10HZ", None),
		"FFTD_HP_22HZ": (37, 2, (2, 0), (), "FFTD_HP_22HZ", None),
		"FFTD_HP_400HZ": (39, 2, (2, 0), (), "FFTD_HP_400HZ", None),
		"FFTD_HP_DCB": (35, 2, (2, 0), (), "FFTD_HP_DCB", None),
		"FFTD_HP_DEFAULT": (40, 2, (2, 0), (), "FFTD_HP_DEFAULT", None),
		"FFTD_HP_OFF": (34, 2, (2, 0), (), "FFTD_HP_OFF", None),
		"FFTD_Harmonic": (31, 2, (2, 0), (), "FFTD_Harmonic", None),
		"FFTD_ID": (1, 2, (2, 0), (), "FFTD_ID", None),
		"FFTD_LPFilter": (41, 2, (2, 0), (), "FFTD_LPFilter", None),
		"FFTD_LPFilterFreq": (42, 2, (3, 0), (), "FFTD_LPFilterFreq", None),
		"FFTD_LP_20KHZ_AES17": (48, 2, (2, 0), (), "FFTD_LP_20KHZ_AES17", None),
		"FFTD_LP_22KHZ": (44, 2, (2, 0), (), "FFTD_LP_22KHZ", None),
		"FFTD_LP_30KHZ": (45, 2, (2, 0), (), "FFTD_LP_30KHZ", None),
		"FFTD_LP_40KHZ": (46, 2, (2, 0), (), "FFTD_LP_40KHZ", None),
		"FFTD_LP_80KHZ": (47, 2, (2, 0), (), "FFTD_LP_80KHZ", None),
		"FFTD_LP_DEFAULT": (49, 2, (2, 0), (), "FFTD_LP_DEFAULT", None),
		"FFTD_LP_OFF": (43, 2, (2, 0), (), "FFTD_LP_OFF", None),
		"FFTD_RELATIVITY_ABS": (62, 2, (2, 0), (), "FFTD_RELATIVITY_ABS", None),
		"FFTD_RELATIVITY_CHANNEL": (65, 2, (2, 0), (), "FFTD_RELATIVITY_CHANNEL", None),
		"FFTD_RELATIVITY_GEN": (64, 2, (2, 0), (), "FFTD_RELATIVITY_GEN", None),
		"FFTD_RELATIVITY_SELF": (63, 2, (2, 0), (), "FFTD_RELATIVITY_SELF", None),
		"FFTD_RELATIVITY_USER": (66, 2, (2, 0), (), "FFTD_RELATIVITY_USER", None),
		"FFTD_Relativity": (61, 2, (2, 0), (), "FFTD_Relativity", None),
		"FFTD_Unit": (4, 2, (2, 0), (), "FFTD_Unit", None),
		"FFTD_UserScript": (6, 2, (8, 0), (), "FFTD_UserScript", None),
		"FFTD_UserWeightingFilter": (60, 2, (8, 0), (), "FFTD_UserWeightingFilter", None),
		"FFTD_WEIGHTING_AWEIGHTING": (54, 2, (2, 0), (), "FFTD_WEIGHTING_AWEIGHTING", None),
		"FFTD_WEIGHTING_CCIR468_1K": (56, 2, (2, 0), (), "FFTD_WEIGHTING_CCIR468_1K", None),
		"FFTD_WEIGHTING_CCIR468_2K": (57, 2, (2, 0), (), "FFTD_WEIGHTING_CCIR468_2K", None),
		"FFTD_WEIGHTING_CWEIGHTING": (55, 2, (2, 0), (), "FFTD_WEIGHTING_CWEIGHTING", None),
		"FFTD_WEIGHTING_DEFAULT": (58, 2, (2, 0), (), "FFTD_WEIGHTING_DEFAULT", None),
		"FFTD_WEIGHTING_NONE": (53, 2, (2, 0), (), "FFTD_WEIGHTING_NONE", None),
		"FFTD_WEIGHTING_USER": (59, 2, (2, 0), (), "FFTD_WEIGHTING_USER", None),
		"FFTD_WeightingFilter": (52, 2, (2, 0), (), "FFTD_WeightingFilter", None),
	}
	_prop_map_put_ = {
		"FFTD_BPBRBANDWIDTH_12" : ((14, LCID, 4, 0),()),
		"FFTD_BPBRBANDWIDTH_24" : ((15, LCID, 4, 0),()),
		"FFTD_BPBRBANDWIDTH_3" : ((12, LCID, 4, 0),()),
		"FFTD_BPBRBANDWIDTH_6" : ((13, LCID, 4, 0),()),
		"FFTD_BPBRBANDWIDTH_NOTCH" : ((16, LCID, 4, 0),()),
		"FFTD_BPBRBandwidth" : ((11, LCID, 4, 0),()),
		"FFTD_BPBRFREQMODE_2NDHARM" : ((26, LCID, 4, 0),()),
		"FFTD_BPBRFREQMODE_3RDHARM" : ((27, LCID, 4, 0),()),
		"FFTD_BPBRFREQMODE_4THHARM" : ((28, LCID, 4, 0),()),
		"FFTD_BPBRFREQMODE_ALLHARM" : ((24, LCID, 4, 0),()),
		"FFTD_BPBRFREQMODE_ALLHARM_FUND" : ((25, LCID, 4, 0),()),
		"FFTD_BPBRFREQMODE_FIXED" : ((21, LCID, 4, 0),()),
		"FFTD_BPBRFREQMODE_GEN" : ((19, LCID, 4, 0),()),
		"FFTD_BPBRFREQMODE_GENOTHER" : ((20, LCID, 4, 0),()),
		"FFTD_BPBRFREQMODE_IMDDIFF" : ((22, LCID, 4, 0),()),
		"FFTD_BPBRFREQMODE_IMDSIDE" : ((23, LCID, 4, 0),()),
		"FFTD_BPBRFREQMODE_INPUT" : ((18, LCID, 4, 0),()),
		"FFTD_BPBRFREQMODE_NTHHARM" : ((29, LCID, 4, 0),()),
		"FFTD_BPBRFreq" : ((30, LCID, 4, 0),()),
		"FFTD_BPBRFreqMode" : ((17, LCID, 4, 0),()),
		"FFTD_BPBRMODE_BP" : ((9, LCID, 4, 0),()),
		"FFTD_BPBRMODE_BR" : ((10, LCID, 4, 0),()),
		"FFTD_BPBRMODE_OFF" : ((8, LCID, 4, 0),()),
		"FFTD_BPBRMode" : ((7, LCID, 4, 0),()),
		"FFTD_BUFFER_CTA" : ((68, LCID, 4, 0),()),
		"FFTD_BUFFER_CTA_FFT" : ((69, LCID, 4, 0),()),
		"FFTD_BUFFER_FFT_FILTERED" : ((73, LCID, 4, 0),()),
		"FFTD_BUFFER_FFT_PREWEIGHTED" : ((72, LCID, 4, 0),()),
		"FFTD_BUFFER_FFT_UNFILTERED" : ((71, LCID, 4, 0),()),
		"FFTD_BUFFER_PHASE" : ((70, LCID, 4, 0),()),
		"FFTD_BUFFER_SAMPLE" : ((67, LCID, 4, 0),()),
		"FFTD_BrickWallHPFilter" : ((50, LCID, 4, 0),()),
		"FFTD_BrickWallLPFilter" : ((51, LCID, 4, 0),()),
		"FFTD_ChA" : ((2, LCID, 4, 0),()),
		"FFTD_ChB" : ((3, LCID, 4, 0),()),
		"FFTD_Function" : ((5, LCID, 4, 0),()),
		"FFTD_HPFilter" : ((32, LCID, 4, 0),()),
		"FFTD_HPFilterFreq" : ((33, LCID, 4, 0),()),
		"FFTD_HP_100HZ" : ((38, LCID, 4, 0),()),
		"FFTD_HP_10HZ" : ((36, LCID, 4, 0),()),
		"FFTD_HP_22HZ" : ((37, LCID, 4, 0),()),
		"FFTD_HP_400HZ" : ((39, LCID, 4, 0),()),
		"FFTD_HP_DCB" : ((35, LCID, 4, 0),()),
		"FFTD_HP_DEFAULT" : ((40, LCID, 4, 0),()),
		"FFTD_HP_OFF" : ((34, LCID, 4, 0),()),
		"FFTD_Harmonic" : ((31, LCID, 4, 0),()),
		"FFTD_ID" : ((1, LCID, 4, 0),()),
		"FFTD_LPFilter" : ((41, LCID, 4, 0),()),
		"FFTD_LPFilterFreq" : ((42, LCID, 4, 0),()),
		"FFTD_LP_20KHZ_AES17" : ((48, LCID, 4, 0),()),
		"FFTD_LP_22KHZ" : ((44, LCID, 4, 0),()),
		"FFTD_LP_30KHZ" : ((45, LCID, 4, 0),()),
		"FFTD_LP_40KHZ" : ((46, LCID, 4, 0),()),
		"FFTD_LP_80KHZ" : ((47, LCID, 4, 0),()),
		"FFTD_LP_DEFAULT" : ((49, LCID, 4, 0),()),
		"FFTD_LP_OFF" : ((43, LCID, 4, 0),()),
		"FFTD_RELATIVITY_ABS" : ((62, LCID, 4, 0),()),
		"FFTD_RELATIVITY_CHANNEL" : ((65, LCID, 4, 0),()),
		"FFTD_RELATIVITY_GEN" : ((64, LCID, 4, 0),()),
		"FFTD_RELATIVITY_SELF" : ((63, LCID, 4, 0),()),
		"FFTD_RELATIVITY_USER" : ((66, LCID, 4, 0),()),
		"FFTD_Relativity" : ((61, LCID, 4, 0),()),
		"FFTD_Unit" : ((4, LCID, 4, 0),()),
		"FFTD_UserScript" : ((6, LCID, 4, 0),()),
		"FFTD_UserWeightingFilter" : ((60, LCID, 4, 0),()),
		"FFTD_WEIGHTING_AWEIGHTING" : ((54, LCID, 4, 0),()),
		"FFTD_WEIGHTING_CCIR468_1K" : ((56, LCID, 4, 0),()),
		"FFTD_WEIGHTING_CCIR468_2K" : ((57, LCID, 4, 0),()),
		"FFTD_WEIGHTING_CWEIGHTING" : ((55, LCID, 4, 0),()),
		"FFTD_WEIGHTING_DEFAULT" : ((58, LCID, 4, 0),()),
		"FFTD_WEIGHTING_NONE" : ((53, LCID, 4, 0),()),
		"FFTD_WEIGHTING_USER" : ((59, LCID, 4, 0),()),
		"FFTD_WeightingFilter" : ((52, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IFFTParameters(DispatchBaseClass):
	CLSID = IID('{2CDD6201-17F8-11D2-91DE-70AB00C10000}')
	coclass_clsid = IID('{2CDD6203-17F8-11D2-91DE-70AB00C10000}')

	def FFTP_ExportSampleBuffer(self, lpszFileName=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg, bCTBuffer=defaultNamedNotOptArg):
		'FFTP_ExportSampleBuffer'
		return self._oleobj_.InvokeTypes(84, LCID, 1, (11, 0), ((8, 0), (2, 0), (11, 0)),lpszFileName
			, sChannel, bCTBuffer)

	def FFTP_GetPhase(self, sChannel=defaultNamedNotOptArg, lBin=defaultNamedNotOptArg, sUnit=defaultNamedNotOptArg):
		'FFTP_GetPhase'
		return self._oleobj_.InvokeTypes(83, LCID, 1, (5, 0), ((2, 0), (3, 0), (2, 0)),sChannel
			, lBin, sUnit)

	def FFTP_GetWindowSpread(self):
		'FFTP_GetWindowSpread'
		return self._oleobj_.InvokeTypes(82, LCID, 1, (2, 0), (),)

	def FFTP_ImportSampleBuffer(self, lpszFileName=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg, bCTBuffer=defaultNamedNotOptArg, sOptions=defaultNamedNotOptArg):
		'FFTP_ImportSampleBuffer'
		return self._oleobj_.InvokeTypes(85, LCID, 1, (11, 0), ((8, 0), (2, 0), (11, 0), (2, 0)),lpszFileName
			, sChannel, bCTBuffer, sOptions)

	_prop_map_get_ = {
		"FFTP_AVERAGETYPE_CONTIGUOUS": (40, 2, (2, 0), (), "FFTP_AVERAGETYPE_CONTIGUOUS", None),
		"FFTP_AVERAGETYPE_ONCE": (46, 2, (2, 0), (), "FFTP_AVERAGETYPE_ONCE", None),
		"FFTP_AVERAGETYPE_PSEUDOROLLING": (47, 2, (2, 0), (), "FFTP_AVERAGETYPE_PSEUDOROLLING", None),
		"FFTP_AVERAGETYPE_TRIGGERED": (41, 2, (2, 0), (), "FFTP_AVERAGETYPE_TRIGGERED", None),
		"FFTP_Average": (43, 2, (11, 0), (), "FFTP_Average", None),
		"FFTP_AverageSamples": (37, 2, (11, 0), (), "FFTP_AverageSamples", None),
		"FFTP_AverageTimes": (44, 2, (2, 0), (), "FFTP_AverageTimes", None),
		"FFTP_AverageTimesSamples": (38, 2, (2, 0), (), "FFTP_AverageTimesSamples", None),
		"FFTP_AverageType": (45, 2, (2, 0), (), "FFTP_AverageType", None),
		"FFTP_AverageTypeSamples": (39, 2, (2, 0), (), "FFTP_AverageTypeSamples", None),
		"FFTP_AveragesDone": (48, 2, (2, 0), (), "FFTP_AveragesDone", None),
		"FFTP_AveragesDoneSamples": (42, 2, (2, 0), (), "FFTP_AveragesDoneSamples", None),
		"FFTP_BuffersProcessed": (81, 2, (11, 0), (), "FFTP_BuffersProcessed", None),
		"FFTP_CalcPhaseInfo": (74, 2, (11, 0), (), "FFTP_CalcPhaseInfo", None),
		"FFTP_IMPORTSAMPLEBUFFER_AUTOADJUST": (79, 2, (2, 0), (), "FFTP_IMPORTSAMPLEBUFFER_AUTOADJUST", None),
		"FFTP_IMPORTSAMPLEBUFFER_AUTOADJUST_ZEROPAD": (80, 2, (2, 0), (), "FFTP_IMPORTSAMPLEBUFFER_AUTOADJUST_ZEROPAD", None),
		"FFTP_IMPORTSAMPLEBUFFER_EXPAND": (77, 2, (2, 0), (), "FFTP_IMPORTSAMPLEBUFFER_EXPAND", None),
		"FFTP_IMPORTSAMPLEBUFFER_EXPAND_ZEROPAD": (78, 2, (2, 0), (), "FFTP_IMPORTSAMPLEBUFFER_EXPAND_ZEROPAD", None),
		"FFTP_IMPORTSAMPLEBUFFER_TRIM": (76, 2, (2, 0), (), "FFTP_IMPORTSAMPLEBUFFER_TRIM", None),
		"FFTP_NUMPOINTS_128K": (9, 2, (3, 0), (), "FFTP_NUMPOINTS_128K", None),
		"FFTP_NUMPOINTS_16K": (6, 2, (3, 0), (), "FFTP_NUMPOINTS_16K", None),
		"FFTP_NUMPOINTS_1K": (2, 2, (3, 0), (), "FFTP_NUMPOINTS_1K", None),
		"FFTP_NUMPOINTS_256K": (10, 2, (3, 0), (), "FFTP_NUMPOINTS_256K", None),
		"FFTP_NUMPOINTS_2K": (3, 2, (3, 0), (), "FFTP_NUMPOINTS_2K", None),
		"FFTP_NUMPOINTS_32K": (7, 2, (3, 0), (), "FFTP_NUMPOINTS_32K", None),
		"FFTP_NUMPOINTS_4K": (4, 2, (3, 0), (), "FFTP_NUMPOINTS_4K", None),
		"FFTP_NUMPOINTS_64K": (8, 2, (3, 0), (), "FFTP_NUMPOINTS_64K", None),
		"FFTP_NUMPOINTS_8K": (5, 2, (3, 0), (), "FFTP_NUMPOINTS_8K", None),
		"FFTP_NumPoints": (1, 2, (3, 0), (), "FFTP_NumPoints", None),
		"FFTP_THRESHOLDMODE_EQUALTO": (61, 2, (2, 0), (), "FFTP_THRESHOLDMODE_EQUALTO", None),
		"FFTP_THRESHOLDMODE_NEG": (62, 2, (2, 0), (), "FFTP_THRESHOLDMODE_NEG", None),
		"FFTP_THRESHOLDMODE_NOTEQUALTO": (64, 2, (2, 0), (), "FFTP_THRESHOLDMODE_NOTEQUALTO", None),
		"FFTP_THRESHOLDMODE_POS": (63, 2, (2, 0), (), "FFTP_THRESHOLDMODE_POS", None),
		"FFTP_THRESHOLDPOLARITY_NEG": (69, 2, (2, 0), (), "FFTP_THRESHOLDPOLARITY_NEG", None),
		"FFTP_THRESHOLDPOLARITY_POS": (68, 2, (2, 0), (), "FFTP_THRESHOLDPOLARITY_POS", None),
		"FFTP_TRIGGERCHANNEL_A": (71, 2, (2, 0), (), "FFTP_TRIGGERCHANNEL_A", None),
		"FFTP_TRIGGERCHANNEL_B": (72, 2, (2, 0), (), "FFTP_TRIGGERCHANNEL_B", None),
		"FFTP_TRIGGERMODE_CONTINUOUS": (50, 2, (2, 0), (), "FFTP_TRIGGERMODE_CONTINUOUS", None),
		"FFTP_TRIGGERMODE_GENWAVETABLE": (53, 2, (2, 0), (), "FFTP_TRIGGERMODE_GENWAVETABLE", None),
		"FFTP_TRIGGERMODE_NORMAL": (51, 2, (2, 0), (), "FFTP_TRIGGERMODE_NORMAL", None),
		"FFTP_TRIGGERMODE_SINGLESHOT": (52, 2, (2, 0), (), "FFTP_TRIGGERMODE_SINGLESHOT", None),
		"FFTP_TRIGGERPOINT_END": (59, 2, (3, 0), (), "FFTP_TRIGGERPOINT_END", None),
		"FFTP_TRIGGERPOINT_HALF": (57, 2, (3, 0), (), "FFTP_TRIGGERPOINT_HALF", None),
		"FFTP_TRIGGERPOINT_QUARTER": (56, 2, (3, 0), (), "FFTP_TRIGGERPOINT_QUARTER", None),
		"FFTP_TRIGGERPOINT_START": (55, 2, (3, 0), (), "FFTP_TRIGGERPOINT_START", None),
		"FFTP_TRIGGERPOINT_THREEQUARTER": (58, 2, (3, 0), (), "FFTP_TRIGGERPOINT_THREEQUARTER", None),
		"FFTP_Threshold": (65, 2, (5, 0), (), "FFTP_Threshold", None),
		"FFTP_ThresholdMode": (60, 2, (2, 0), (), "FFTP_ThresholdMode", None),
		"FFTP_ThresholdPolarity": (67, 2, (2, 0), (), "FFTP_ThresholdPolarity", None),
		"FFTP_ThresholdUnit": (66, 2, (2, 0), (), "FFTP_ThresholdUnit", None),
		"FFTP_TriggerChannel": (70, 2, (2, 0), (), "FFTP_TriggerChannel", None),
		"FFTP_TriggerMode": (49, 2, (2, 0), (), "FFTP_TriggerMode", None),
		"FFTP_TriggerOn": (75, 2, (11, 0), (), "FFTP_TriggerOn", None),
		"FFTP_TriggerOnCTDetector": (73, 2, (11, 0), (), "FFTP_TriggerOnCTDetector", None),
		"FFTP_TriggerPoint": (54, 2, (3, 0), (), "FFTP_TriggerPoint", None),
		"FFTP_UserWeightingFilter": (36, 2, (8, 0), (), "FFTP_UserWeightingFilter", None),
		"FFTP_UserWindowFunction": (27, 2, (8, 0), (), "FFTP_UserWindowFunction", None),
		"FFTP_WEIGHTING_AWEIGHTING": (30, 2, (2, 0), (), "FFTP_WEIGHTING_AWEIGHTING", None),
		"FFTP_WEIGHTING_CCIR468_1K": (32, 2, (2, 0), (), "FFTP_WEIGHTING_CCIR468_1K", None),
		"FFTP_WEIGHTING_CCIR468_2K": (33, 2, (2, 0), (), "FFTP_WEIGHTING_CCIR468_2K", None),
		"FFTP_WEIGHTING_CWEIGHTING": (31, 2, (2, 0), (), "FFTP_WEIGHTING_CWEIGHTING", None),
		"FFTP_WEIGHTING_DEFAULT": (34, 2, (2, 0), (), "FFTP_WEIGHTING_DEFAULT", None),
		"FFTP_WEIGHTING_NONE": (29, 2, (2, 0), (), "FFTP_WEIGHTING_NONE", None),
		"FFTP_WEIGHTING_USER": (35, 2, (2, 0), (), "FFTP_WEIGHTING_USER", None),
		"FFTP_WINDOW_BH4": (20, 2, (2, 0), (), "FFTP_WINDOW_BH4", None),
		"FFTP_WINDOW_BLACKMAN": (17, 2, (2, 0), (), "FFTP_WINDOW_BLACKMAN", None),
		"FFTP_WINDOW_FLATTOP": (22, 2, (2, 0), (), "FFTP_WINDOW_FLATTOP", None),
		"FFTP_WINDOW_FREQCORRECT_AO": (13, 2, (2, 0), (), "FFTP_WINDOW_FREQCORRECT_AO", None),
		"FFTP_WINDOW_FREQCORRECT_DO": (14, 2, (2, 0), (), "FFTP_WINDOW_FREQCORRECT_DO", None),
		"FFTP_WINDOW_GAUSSIAN": (21, 2, (2, 0), (), "FFTP_WINDOW_GAUSSIAN", None),
		"FFTP_WINDOW_HAMMING": (19, 2, (2, 0), (), "FFTP_WINDOW_HAMMING", None),
		"FFTP_WINDOW_HANN": (18, 2, (2, 0), (), "FFTP_WINDOW_HANN", None),
		"FFTP_WINDOW_NSHOTCORRECT": (15, 2, (2, 0), (), "FFTP_WINDOW_NSHOTCORRECT", None),
		"FFTP_WINDOW_PRISM5": (23, 2, (2, 0), (), "FFTP_WINDOW_PRISM5", None),
		"FFTP_WINDOW_PRISM6": (24, 2, (2, 0), (), "FFTP_WINDOW_PRISM6", None),
		"FFTP_WINDOW_PRISM7": (25, 2, (2, 0), (), "FFTP_WINDOW_PRISM7", None),
		"FFTP_WINDOW_RECTANGULAR": (12, 2, (2, 0), (), "FFTP_WINDOW_RECTANGULAR", None),
		"FFTP_WINDOW_TRIANGULAR": (16, 2, (2, 0), (), "FFTP_WINDOW_TRIANGULAR", None),
		"FFTP_WINDOW_USER": (26, 2, (2, 0), (), "FFTP_WINDOW_USER", None),
		"FFTP_WeightingFilter": (28, 2, (2, 0), (), "FFTP_WeightingFilter", None),
		"FFTP_WindowFunction": (11, 2, (2, 0), (), "FFTP_WindowFunction", None),
	}
	_prop_map_put_ = {
		"FFTP_AVERAGETYPE_CONTIGUOUS" : ((40, LCID, 4, 0),()),
		"FFTP_AVERAGETYPE_ONCE" : ((46, LCID, 4, 0),()),
		"FFTP_AVERAGETYPE_PSEUDOROLLING" : ((47, LCID, 4, 0),()),
		"FFTP_AVERAGETYPE_TRIGGERED" : ((41, LCID, 4, 0),()),
		"FFTP_Average" : ((43, LCID, 4, 0),()),
		"FFTP_AverageSamples" : ((37, LCID, 4, 0),()),
		"FFTP_AverageTimes" : ((44, LCID, 4, 0),()),
		"FFTP_AverageTimesSamples" : ((38, LCID, 4, 0),()),
		"FFTP_AverageType" : ((45, LCID, 4, 0),()),
		"FFTP_AverageTypeSamples" : ((39, LCID, 4, 0),()),
		"FFTP_AveragesDone" : ((48, LCID, 4, 0),()),
		"FFTP_AveragesDoneSamples" : ((42, LCID, 4, 0),()),
		"FFTP_BuffersProcessed" : ((81, LCID, 4, 0),()),
		"FFTP_CalcPhaseInfo" : ((74, LCID, 4, 0),()),
		"FFTP_IMPORTSAMPLEBUFFER_AUTOADJUST" : ((79, LCID, 4, 0),()),
		"FFTP_IMPORTSAMPLEBUFFER_AUTOADJUST_ZEROPAD" : ((80, LCID, 4, 0),()),
		"FFTP_IMPORTSAMPLEBUFFER_EXPAND" : ((77, LCID, 4, 0),()),
		"FFTP_IMPORTSAMPLEBUFFER_EXPAND_ZEROPAD" : ((78, LCID, 4, 0),()),
		"FFTP_IMPORTSAMPLEBUFFER_TRIM" : ((76, LCID, 4, 0),()),
		"FFTP_NUMPOINTS_128K" : ((9, LCID, 4, 0),()),
		"FFTP_NUMPOINTS_16K" : ((6, LCID, 4, 0),()),
		"FFTP_NUMPOINTS_1K" : ((2, LCID, 4, 0),()),
		"FFTP_NUMPOINTS_256K" : ((10, LCID, 4, 0),()),
		"FFTP_NUMPOINTS_2K" : ((3, LCID, 4, 0),()),
		"FFTP_NUMPOINTS_32K" : ((7, LCID, 4, 0),()),
		"FFTP_NUMPOINTS_4K" : ((4, LCID, 4, 0),()),
		"FFTP_NUMPOINTS_64K" : ((8, LCID, 4, 0),()),
		"FFTP_NUMPOINTS_8K" : ((5, LCID, 4, 0),()),
		"FFTP_NumPoints" : ((1, LCID, 4, 0),()),
		"FFTP_THRESHOLDMODE_EQUALTO" : ((61, LCID, 4, 0),()),
		"FFTP_THRESHOLDMODE_NEG" : ((62, LCID, 4, 0),()),
		"FFTP_THRESHOLDMODE_NOTEQUALTO" : ((64, LCID, 4, 0),()),
		"FFTP_THRESHOLDMODE_POS" : ((63, LCID, 4, 0),()),
		"FFTP_THRESHOLDPOLARITY_NEG" : ((69, LCID, 4, 0),()),
		"FFTP_THRESHOLDPOLARITY_POS" : ((68, LCID, 4, 0),()),
		"FFTP_TRIGGERCHANNEL_A" : ((71, LCID, 4, 0),()),
		"FFTP_TRIGGERCHANNEL_B" : ((72, LCID, 4, 0),()),
		"FFTP_TRIGGERMODE_CONTINUOUS" : ((50, LCID, 4, 0),()),
		"FFTP_TRIGGERMODE_GENWAVETABLE" : ((53, LCID, 4, 0),()),
		"FFTP_TRIGGERMODE_NORMAL" : ((51, LCID, 4, 0),()),
		"FFTP_TRIGGERMODE_SINGLESHOT" : ((52, LCID, 4, 0),()),
		"FFTP_TRIGGERPOINT_END" : ((59, LCID, 4, 0),()),
		"FFTP_TRIGGERPOINT_HALF" : ((57, LCID, 4, 0),()),
		"FFTP_TRIGGERPOINT_QUARTER" : ((56, LCID, 4, 0),()),
		"FFTP_TRIGGERPOINT_START" : ((55, LCID, 4, 0),()),
		"FFTP_TRIGGERPOINT_THREEQUARTER" : ((58, LCID, 4, 0),()),
		"FFTP_Threshold" : ((65, LCID, 4, 0),()),
		"FFTP_ThresholdMode" : ((60, LCID, 4, 0),()),
		"FFTP_ThresholdPolarity" : ((67, LCID, 4, 0),()),
		"FFTP_ThresholdUnit" : ((66, LCID, 4, 0),()),
		"FFTP_TriggerChannel" : ((70, LCID, 4, 0),()),
		"FFTP_TriggerMode" : ((49, LCID, 4, 0),()),
		"FFTP_TriggerOn" : ((75, LCID, 4, 0),()),
		"FFTP_TriggerOnCTDetector" : ((73, LCID, 4, 0),()),
		"FFTP_TriggerPoint" : ((54, LCID, 4, 0),()),
		"FFTP_UserWeightingFilter" : ((36, LCID, 4, 0),()),
		"FFTP_UserWindowFunction" : ((27, LCID, 4, 0),()),
		"FFTP_WEIGHTING_AWEIGHTING" : ((30, LCID, 4, 0),()),
		"FFTP_WEIGHTING_CCIR468_1K" : ((32, LCID, 4, 0),()),
		"FFTP_WEIGHTING_CCIR468_2K" : ((33, LCID, 4, 0),()),
		"FFTP_WEIGHTING_CWEIGHTING" : ((31, LCID, 4, 0),()),
		"FFTP_WEIGHTING_DEFAULT" : ((34, LCID, 4, 0),()),
		"FFTP_WEIGHTING_NONE" : ((29, LCID, 4, 0),()),
		"FFTP_WEIGHTING_USER" : ((35, LCID, 4, 0),()),
		"FFTP_WINDOW_BH4" : ((20, LCID, 4, 0),()),
		"FFTP_WINDOW_BLACKMAN" : ((17, LCID, 4, 0),()),
		"FFTP_WINDOW_FLATTOP" : ((22, LCID, 4, 0),()),
		"FFTP_WINDOW_FREQCORRECT_AO" : ((13, LCID, 4, 0),()),
		"FFTP_WINDOW_FREQCORRECT_DO" : ((14, LCID, 4, 0),()),
		"FFTP_WINDOW_GAUSSIAN" : ((21, LCID, 4, 0),()),
		"FFTP_WINDOW_HAMMING" : ((19, LCID, 4, 0),()),
		"FFTP_WINDOW_HANN" : ((18, LCID, 4, 0),()),
		"FFTP_WINDOW_NSHOTCORRECT" : ((15, LCID, 4, 0),()),
		"FFTP_WINDOW_PRISM5" : ((23, LCID, 4, 0),()),
		"FFTP_WINDOW_PRISM6" : ((24, LCID, 4, 0),()),
		"FFTP_WINDOW_PRISM7" : ((25, LCID, 4, 0),()),
		"FFTP_WINDOW_RECTANGULAR" : ((12, LCID, 4, 0),()),
		"FFTP_WINDOW_TRIANGULAR" : ((16, LCID, 4, 0),()),
		"FFTP_WINDOW_USER" : ((26, LCID, 4, 0),()),
		"FFTP_WeightingFilter" : ((28, LCID, 4, 0),()),
		"FFTP_WindowFunction" : ((11, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IFormatConverter(DispatchBaseClass):
	CLSID = IID('{2840227C-5408-4E53-B52B-0F6637199948}')
	coclass_clsid = IID('{10837BD8-6795-4F49-A626-EDC9475040BA}')

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGenerator(DispatchBaseClass):
	CLSID = IID('{318B25D0-C3FD-11D1-91DD-70AB00C10000}')
	coclass_clsid = IID('{318B25D2-C3FD-11D1-91DD-70AB00C10000}')

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IHardware(DispatchBaseClass):
	CLSID = IID('{3A499641-CE6B-11D3-B0E8-00AA0011AF6D}')
	coclass_clsid = IID('{4B8A5560-CF1B-11D3-B0E8-00AA0011AF6D}')

	def HW_AllowCalibrationWrite(self, sParam=defaultNamedNotOptArg):
		'HW_AllowCalibrationWrite'
		return self._oleobj_.InvokeTypes(34, LCID, 1, (11, 0), ((2, 0),),sParam
			)

	def HW_DSPGetMem(self, sWhichDSP=defaultNamedNotOptArg, sMemSpace=defaultNamedNotOptArg, lMemAdr=defaultNamedNotOptArg):
		'HW_DSPGetMem'
		return self._oleobj_.InvokeTypes(59, LCID, 1, (3, 0), ((2, 0), (2, 0), (3, 0)),sWhichDSP
			, sMemSpace, lMemAdr)

	def HW_DSPPutMem(self, sWhichDSP=defaultNamedNotOptArg, sMemSpace=defaultNamedNotOptArg, lMemAdr=defaultNamedNotOptArg, lValue=defaultNamedNotOptArg):
		'HW_DSPPutMem'
		return self._oleobj_.InvokeTypes(60, LCID, 1, (11, 0), ((2, 0), (2, 0), (3, 0), (3, 0)),sWhichDSP
			, sMemSpace, lMemAdr, lValue)

	def HW_GetAmbientTemp(self):
		'HW_GetAmbientTemp'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (5, 0), (),)

	def HW_GetAnalogueBoardSerialNum(self):
		'HW_GetAnalogueBoardSerialNum'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (2, 0), (),)

	def HW_GetAnalogueCalibByte(self, sOffset=defaultNamedNotOptArg):
		'HW_GetAnalogueCalibByte'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (2, 0), ((2, 0),),sOffset
			)

	def HW_GetAnalogueCalibDate(self, psYear=defaultNamedNotOptArg, psMonth=defaultNamedNotOptArg, psDay=defaultNamedNotOptArg, psHour=defaultNamedNotOptArg
			, psMinute=defaultNamedNotOptArg, psSecond=defaultNamedNotOptArg):
		'HW_GetAnalogueCalibDate'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (11, 0), ((16396, 0), (16396, 0), (16396, 0), (16396, 0), (16396, 0), (16396, 0)),psYear
			, psMonth, psDay, psHour, psMinute, psSecond
			)

	def HW_GetAnalogueCalibOperator(self):
		'HW_GetAnalogueCalibOperator'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(44, LCID, 1, (8, 0), (),)

	def HW_GetAnalogueCalibOrganisation(self):
		'HW_GetAnalogueCalibOrganisation'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(43, LCID, 1, (8, 0), (),)

	def HW_GetAnalogueCalibString(self, sOffset=defaultNamedNotOptArg, sLength=defaultNamedNotOptArg):
		'HW_GetAnalogueCalibString'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(27, LCID, 1, (8, 0), ((2, 0), (2, 0)),sOffset
			, sLength)

	def HW_GetAnalogueCalibValue(self, sOffset=defaultNamedNotOptArg):
		'HW_GetAnalogueCalibValue'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (5, 0), ((2, 0),),sOffset
			)

	def HW_GetAnalogueCalibVersion(self):
		'HW_GetAnalogueCalibVersion'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (2, 0), (),)

	def HW_GetAnalogueHWOptions(self):
		'HW_GetAnalogueHWOptions'
		return self._oleobj_.InvokeTypes(54, LCID, 1, (2, 0), (),)

	def HW_GetAnalogueHWVersion(self):
		'HW_GetAnalogueHWVersion'
		return self._oleobj_.InvokeTypes(53, LCID, 1, (2, 0), (),)

	def HW_GetAnalogueSWVersion(self):
		'HW_GetAnalogueSWVersion'
		return self._oleobj_.InvokeTypes(55, LCID, 1, (2, 0), (),)

	def HW_GetAnalogueSWVersionLetter(self):
		'HW_GetAnalogueSWVersionLetter'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(56, LCID, 1, (8, 0), (),)

	def HW_GetAnalogueTemp(self):
		'HW_GetAnalogueTemp'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (5, 0), (),)

	def HW_GetAnalogueUnitSerialNum(self):
		'HW_GetAnalogueUnitSerialNum'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (2, 0), (),)

	def HW_GetMainBoardSerialNum(self):
		'HW_GetMainBoardSerialNum'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (2, 0), (),)

	def HW_GetMainCalibByte(self, sOffset=defaultNamedNotOptArg):
		'HW_GetMainCalibByte'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (2, 0), ((2, 0),),sOffset
			)

	def HW_GetMainCalibDate(self, psYear=defaultNamedNotOptArg, psMonth=defaultNamedNotOptArg, psDay=defaultNamedNotOptArg, psHour=defaultNamedNotOptArg
			, psMinute=defaultNamedNotOptArg, psSecond=defaultNamedNotOptArg):
		'HW_GetMainCalibDate'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (11, 0), ((16396, 0), (16396, 0), (16396, 0), (16396, 0), (16396, 0), (16396, 0)),psYear
			, psMonth, psDay, psHour, psMinute, psSecond
			)

	def HW_GetMainCalibOperator(self):
		'HW_GetMainCalibOperator'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(42, LCID, 1, (8, 0), (),)

	def HW_GetMainCalibOrganisation(self):
		'HW_GetMainCalibOrganisation'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(41, LCID, 1, (8, 0), (),)

	def HW_GetMainCalibString(self, sOffset=defaultNamedNotOptArg, sLength=defaultNamedNotOptArg):
		'HW_GetMainCalibString'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(24, LCID, 1, (8, 0), ((2, 0), (2, 0)),sOffset
			, sLength)

	def HW_GetMainCalibValue(self, sOffset=defaultNamedNotOptArg):
		'HW_GetMainCalibValue'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (5, 0), ((2, 0),),sOffset
			)

	def HW_GetMainCalibVersion(self):
		'HW_GetMainCalibVersion'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (2, 0), (),)

	def HW_GetMainHWOptions(self):
		'HW_GetMainHWOptions'
		return self._oleobj_.InvokeTypes(50, LCID, 1, (2, 0), (),)

	def HW_GetMainHWVersion(self):
		'HW_GetMainHWVersion'
		return self._oleobj_.InvokeTypes(49, LCID, 1, (2, 0), (),)

	def HW_GetMainSWVersion(self):
		'HW_GetMainSWVersion'
		return self._oleobj_.InvokeTypes(51, LCID, 1, (2, 0), (),)

	def HW_GetMainSWVersionLetter(self):
		'HW_GetMainSWVersionLetter'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(52, LCID, 1, (8, 0), (),)

	def HW_GetMainTemp(self):
		'HW_GetMainTemp'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (5, 0), (),)

	def HW_GetMainUnitSerialNum(self):
		'HW_GetMainUnitSerialNum'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (2, 0), (),)

	def HW_GetPSUTemp(self):
		'HW_GetPSUTemp'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (5, 0), (),)

	def HW_I2CGetMem(self, sDeviceAddr=defaultNamedNotOptArg, sRegisterAddr=defaultNamedNotOptArg):
		'HW_I2CGetMem'
		return self._oleobj_.InvokeTypes(61, LCID, 1, (2, 0), ((2, 0), (2, 0)),sDeviceAddr
			, sRegisterAddr)

	def HW_I2CPutMem(self, sDeviceAddr=defaultNamedNotOptArg, sRegisterAddr=defaultNamedNotOptArg, sValue=defaultNamedNotOptArg):
		'HW_I2CPutMem'
		return self._oleobj_.InvokeTypes(62, LCID, 1, (11, 0), ((2, 0), (2, 0), (2, 0)),sDeviceAddr
			, sRegisterAddr, sValue)

	def HW_MicroGetMem(self, sMemSpace=defaultNamedNotOptArg, sMemAdr=defaultNamedNotOptArg):
		'HW_MicroGetMem'
		return self._oleobj_.InvokeTypes(57, LCID, 1, (2, 0), ((2, 0), (19, 0)),sMemSpace
			, sMemAdr)

	def HW_MicroPutMem(self, sMemSpace=defaultNamedNotOptArg, sMemAdr=defaultNamedNotOptArg, sValue=defaultNamedNotOptArg):
		'HW_MicroPutMem'
		return self._oleobj_.InvokeTypes(58, LCID, 1, (11, 0), ((2, 0), (19, 0), (2, 0)),sMemSpace
			, sMemAdr, sValue)

	def HW_ResetAnalogueCalibration(self):
		'HW_ResetAnalogueCalibration'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (11, 0), (),)

	def HW_ResetMainBoardCalibration(self):
		'HW_ResetMainBoardCalibration'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (11, 0), (),)

	def HW_SetAnalogueBoardSerialNum(self, sSerialNum=defaultNamedNotOptArg):
		'HW_SetAnalogueBoardSerialNum'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((2, 0),),sSerialNum
			)

	def HW_SetAnalogueCalibByte(self, sOffset=defaultNamedNotOptArg, sValue=defaultNamedNotOptArg):
		'HW_SetAnalogueCalibByte'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), ((2, 0), (2, 0)),sOffset
			, sValue)

	def HW_SetAnalogueCalibOperator(self, strName=defaultNamedNotOptArg):
		'HW_SetAnalogueCalibOperator'
		return self._oleobj_.InvokeTypes(48, LCID, 1, (11, 0), ((8, 0),),strName
			)

	def HW_SetAnalogueCalibOrganisation(self, strName=defaultNamedNotOptArg):
		'HW_SetAnalogueCalibOrganisation'
		return self._oleobj_.InvokeTypes(47, LCID, 1, (11, 0), ((8, 0),),strName
			)

	def HW_SetAnalogueCalibString(self, sOffset=defaultNamedNotOptArg, sLength=defaultNamedNotOptArg, str=defaultNamedNotOptArg):
		'HW_SetAnalogueCalibString'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), ((2, 0), (2, 0), (8, 0)),sOffset
			, sLength, str)

	def HW_SetAnalogueCalibValue(self, sOffset=defaultNamedNotOptArg, dValue=defaultNamedNotOptArg):
		'HW_SetAnalogueCalibValue'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), ((2, 0), (5, 0)),sOffset
			, dValue)

	def HW_SetAnalogueCalibVersion(self, sVersion=defaultNamedNotOptArg):
		'HW_SetAnalogueCalibVersion'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (11, 0), ((2, 0),),sVersion
			)

	def HW_SetAnalogueUnitSerialNum(self, sSerialNum=defaultNamedNotOptArg):
		'HW_SetAnalogueUnitSerialNum'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), ((2, 0),),sSerialNum
			)

	def HW_SetMainBoardSerialNum(self, sSerialNum=defaultNamedNotOptArg):
		'HW_SetMainBoardSerialNum'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((2, 0),),sSerialNum
			)

	def HW_SetMainCalibByte(self, sOffset=defaultNamedNotOptArg, sValue=defaultNamedNotOptArg):
		'HW_SetMainCalibByte'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), ((2, 0), (2, 0)),sOffset
			, sValue)

	def HW_SetMainCalibOperator(self, strName=defaultNamedNotOptArg):
		'HW_SetMainCalibOperator'
		return self._oleobj_.InvokeTypes(46, LCID, 1, (11, 0), ((8, 0),),strName
			)

	def HW_SetMainCalibOrganisation(self, strName=defaultNamedNotOptArg):
		'HW_SetMainCalibOrganisation'
		return self._oleobj_.InvokeTypes(45, LCID, 1, (11, 0), ((8, 0),),strName
			)

	def HW_SetMainCalibString(self, sOffset=defaultNamedNotOptArg, sLength=defaultNamedNotOptArg, str=defaultNamedNotOptArg):
		'HW_SetMainCalibString'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), ((2, 0), (2, 0), (8, 0)),sOffset
			, sLength, str)

	def HW_SetMainCalibValue(self, sOffset=defaultNamedNotOptArg, dValue=defaultNamedNotOptArg):
		'HW_SetMainCalibValue'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (11, 0), ((2, 0), (5, 0)),sOffset
			, dValue)

	def HW_SetMainCalibVersion(self, sVersion=defaultNamedNotOptArg):
		'HW_SetMainCalibVersion'
		return self._oleobj_.InvokeTypes(39, LCID, 1, (11, 0), ((2, 0),),sVersion
			)

	def HW_SetMainUnitSerialNum(self, sSerialNum=defaultNamedNotOptArg):
		'HW_SetMainUnitSerialNum'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((2, 0),),sSerialNum
			)

	def HW_WriteAnalogueMasterTable(self):
		'HW_WriteAnalogueMasterTable'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (11, 0), (),)

	def HW_WriteAnalogueTable(self):
		'HW_WriteAnalogueTable'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (11, 0), (),)

	def HW_WriteMainMasterTable(self):
		'HW_WriteMainMasterTable'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (11, 0), (),)

	def HW_WriteMainTable(self):
		'HW_WriteMainTable'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"HW_TDACHalfUI": (3, 2, (2, 0), (), "HW_TDACHalfUI", None),
		"HW_TDACJitterEnd": (2, 2, (2, 0), (), "HW_TDACJitterEnd", None),
		"HW_TDACJitterStart": (1, 2, (2, 0), (), "HW_TDACJitterStart", None),
	}
	_prop_map_put_ = {
		"HW_TDACHalfUI" : ((3, LCID, 4, 0),()),
		"HW_TDACJitterEnd" : ((2, LCID, 4, 0),()),
		"HW_TDACJitterStart" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IIOSwitcher(DispatchBaseClass):
	CLSID = IID('{F0815F9F-99C1-4931-B018-2735C3F176A9}')
	coclass_clsid = IID('{5A73A73F-6614-409A-8E31-FCFCDED23ECF}')

	def DSNET_GetStatus(self, sAddress=defaultNamedNotOptArg, plStatus=defaultNamedNotOptArg):
		'DSNET_GetStatus'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((2, 0), (16396, 0)),sAddress
			, plStatus)

	def DSNET_Reset(self, sAddress=defaultNamedNotOptArg, bOn=defaultNamedNotOptArg, plStatus=defaultNamedNotOptArg):
		'DSNET_Reset'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((2, 0), (11, 0), (16396, 0)),sAddress
			, bOn, plStatus)

	def IOSWITCHER_AddToArray(self, sAddress=defaultNamedNotOptArg, sBus=defaultNamedNotOptArg, sGroup=defaultNamedNotOptArg, strArray=defaultNamedNotOptArg):
		'IOSWITCHER_AddToArray'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (11, 0), ((2, 0), (2, 0), (2, 0), (8, 0)),sAddress
			, sBus, sGroup, strArray)

	def IOSWITCHER_AddToStereoArray(self, sAddress=defaultNamedNotOptArg, sGroup=defaultNamedNotOptArg, strArray=defaultNamedNotOptArg):
		'IOSWITCHER_AddToStereoArray'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (11, 0), ((2, 0), (2, 0), (8, 0)),sAddress
			, sGroup, strArray)

	def IOSWITCHER_BusBalance(self, sAddress=defaultNamedNotOptArg, sBus=defaultNamedNotOptArg, bOn=defaultNamedNotOptArg):
		'IOSWITCHER_BusBalance'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), ((2, 0), (2, 0), (11, 0)),sAddress
			, sBus, bOn)

	def IOSWITCHER_BusGroupSwitch(self, sAddress=defaultNamedNotOptArg, sBus=defaultNamedNotOptArg, sGroup=defaultNamedNotOptArg, sMask=defaultNamedNotOptArg):
		'IOSWITCHER_BusGroupSwitch'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), ((2, 0), (2, 0), (2, 0), (2, 0)),sAddress
			, sBus, sGroup, sMask)

	def IOSWITCHER_BusLoad(self, sAddress=defaultNamedNotOptArg, sBus=defaultNamedNotOptArg, bOn=defaultNamedNotOptArg):
		'IOSWITCHER_BusLoad'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), ((2, 0), (2, 0), (11, 0)),sAddress
			, sBus, bOn)

	def IOSWITCHER_GetBusDC(self, sAddress=defaultNamedNotOptArg, sBus=defaultNamedNotOptArg, psPositiveDC=defaultNamedNotOptArg, psNegativeDC=defaultNamedNotOptArg):
		'IOSWITCHER_GetBusDC'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (11, 0), ((2, 0), (2, 0), (16396, 0), (16396, 0)),sAddress
			, sBus, psPositiveDC, psNegativeDC)

	def IOSWITCHER_GetBusStatus(self, sAddress=defaultNamedNotOptArg, sBus=defaultNamedNotOptArg, plBusStatus=defaultNamedNotOptArg):
		'IOSWITCHER_GetBusStatus'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (11, 0), ((2, 0), (2, 0), (16396, 0)),sAddress
			, sBus, plBusStatus)

	def IOSWITCHER_GetFullStatus(self, sAddress=defaultNamedNotOptArg, plBusAStatus=defaultNamedNotOptArg, plBusBStatus=defaultNamedNotOptArg):
		'IOSWITCHER_GetFullStatus'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), ((2, 0), (16396, 0), (16396, 0)),sAddress
			, plBusAStatus, plBusBStatus)

	def SWITCHER_AddChannel(self, strArray=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg):
		'SWITCHER_AddChannel'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((8, 0), (2, 0)),strArray
			, sChannel)

	def SWITCHER_Balance(self, strArray=defaultNamedNotOptArg, bOn=defaultNamedNotOptArg):
		'SWITCHER_Balance'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((8, 0), (11, 0)),strArray
			, bOn)

	def SWITCHER_ClearChannels(self, strArray=defaultNamedNotOptArg):
		'SWITCHER_ClearChannels'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((8, 0),),strArray
			)

	def SWITCHER_DefineArray(self, strArray=defaultNamedNotOptArg):
		'SWITCHER_DefineArray'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((8, 0),),strArray
			)

	def SWITCHER_DefineStereoArray(self, strArray=defaultNamedNotOptArg):
		'SWITCHER_DefineStereoArray'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), ((8, 0),),strArray
			)

	def SWITCHER_ExclusiveChannel(self, strArray=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg):
		'SWITCHER_ExclusiveChannel'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((8, 0), (2, 0)),strArray
			, sChannel)

	def SWITCHER_NotChannel(self, strArray=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg):
		'SWITCHER_NotChannel'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((8, 0), (2, 0)),strArray
			, sChannel)

	def SWITCHER_RemoveArray(self, strArray=defaultNamedNotOptArg):
		'SWITCHER_RemoveArray'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), ((8, 0),),strArray
			)

	def SWITCHER_RemoveChannel(self, strArray=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg):
		'SWITCHER_RemoveChannel'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((8, 0), (2, 0)),strArray
			, sChannel)

	_prop_map_get_ = {
		"DSNET_ShowErrorMessages": (1, 2, (2, 0), (), "DSNET_ShowErrorMessages", None),
		"IOSWITCHER_BUS_A": (2, 2, (2, 0), (), "IOSWITCHER_BUS_A", None),
		"IOSWITCHER_BUS_B": (3, 2, (2, 0), (), "IOSWITCHER_BUS_B", None),
		"IOSWITCHER_GROUP_X": (4, 2, (2, 0), (), "IOSWITCHER_GROUP_X", None),
		"IOSWITCHER_GROUP_Y": (5, 2, (2, 0), (), "IOSWITCHER_GROUP_Y", None),
	}
	_prop_map_put_ = {
		"DSNET_ShowErrorMessages" : ((1, LCID, 4, 0),()),
		"IOSWITCHER_BUS_A" : ((2, LCID, 4, 0),()),
		"IOSWITCHER_BUS_B" : ((3, LCID, 4, 0),()),
		"IOSWITCHER_GROUP_X" : ((4, LCID, 4, 0),()),
		"IOSWITCHER_GROUP_Y" : ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IImpulseResponse(DispatchBaseClass):
	CLSID = IID('{1CD7F788-84E1-415F-8EE0-739E3121D0AF}')
	coclass_clsid = IID('{F81A9524-8E7B-470E-A15F-CB02B18A3A76}')

	def IR_SetImpulseWindowChA(self, dStart=defaultNamedNotOptArg, dEnd=defaultNamedNotOptArg, sWindow=defaultNamedNotOptArg, bHalfWindow=defaultNamedNotOptArg):
		'IR_SetImpulseWindowChA'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (11, 0), ((5, 0), (5, 0), (2, 0), (11, 0)),dStart
			, dEnd, sWindow, bHalfWindow)

	def IR_SetImpulseWindowChB(self, dStart=defaultNamedNotOptArg, dEnd=defaultNamedNotOptArg, sWindow=defaultNamedNotOptArg, bHalfWindow=defaultNamedNotOptArg):
		'IR_SetImpulseWindowChB'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (11, 0), ((5, 0), (5, 0), (2, 0), (11, 0)),dStart
			, dEnd, sWindow, bHalfWindow)

	_prop_map_get_ = {
		"IR_APPLYWINDOW_ALWAYS": (31, 2, (2, 0), (), "IR_APPLYWINDOW_ALWAYS", None),
		"IR_APPLYWINDOW_IMPULSE": (30, 2, (2, 0), (), "IR_APPLYWINDOW_IMPULSE", None),
		"IR_ApplyWindow": (29, 2, (2, 0), (), "IR_ApplyWindow", None),
		"IR_ChannelsTied": (28, 2, (11, 0), (), "IR_ChannelsTied", None),
		"IR_EndWindowChA": (23, 2, (5, 0), (), "IR_EndWindowChA", None),
		"IR_EndWindowChB": (26, 2, (5, 0), (), "IR_EndWindowChB", None),
		"IR_GeneratedRangeOnly": (7, 2, (11, 0), (), "IR_GeneratedRangeOnly", None),
		"IR_HalfWindow": (20, 2, (11, 0), (), "IR_HalfWindow", None),
		"IR_IMPULSERELATIVITY_CHANNEL": (4, 2, (2, 0), (), "IR_IMPULSERELATIVITY_CHANNEL", None),
		"IR_IMPULSERELATIVITY_GEN": (3, 2, (2, 0), (), "IR_IMPULSERELATIVITY_GEN", None),
		"IR_ImpulseAbsolute": (5, 2, (11, 0), (), "IR_ImpulseAbsolute", None),
		"IR_ImpulseRelativity": (2, 2, (2, 0), (), "IR_ImpulseRelativity", None),
		"IR_ImpulseResponse": (1, 2, (11, 0), (), "IR_ImpulseResponse", None),
		"IR_MidWindowChA": (22, 2, (5, 0), (), "IR_MidWindowChA", None),
		"IR_MidWindowChB": (25, 2, (5, 0), (), "IR_MidWindowChB", None),
		"IR_NormalizeImpulse": (6, 2, (11, 0), (), "IR_NormalizeImpulse", None),
		"IR_StartWindowChA": (21, 2, (5, 0), (), "IR_StartWindowChA", None),
		"IR_StartWindowChB": (24, 2, (5, 0), (), "IR_StartWindowChB", None),
		"IR_WINDOW_BH4": (14, 2, (2, 0), (), "IR_WINDOW_BH4", None),
		"IR_WINDOW_BLACKMAN": (11, 2, (2, 0), (), "IR_WINDOW_BLACKMAN", None),
		"IR_WINDOW_FLATTOP": (16, 2, (2, 0), (), "IR_WINDOW_FLATTOP", None),
		"IR_WINDOW_GAUSSIAN": (15, 2, (2, 0), (), "IR_WINDOW_GAUSSIAN", None),
		"IR_WINDOW_HAMMING": (13, 2, (2, 0), (), "IR_WINDOW_HAMMING", None),
		"IR_WINDOW_HANN": (12, 2, (2, 0), (), "IR_WINDOW_HANN", None),
		"IR_WINDOW_PRISM5": (17, 2, (2, 0), (), "IR_WINDOW_PRISM5", None),
		"IR_WINDOW_PRISM6": (18, 2, (2, 0), (), "IR_WINDOW_PRISM6", None),
		"IR_WINDOW_PRISM7": (19, 2, (2, 0), (), "IR_WINDOW_PRISM7", None),
		"IR_WINDOW_RECTANGULAR": (9, 2, (2, 0), (), "IR_WINDOW_RECTANGULAR", None),
		"IR_WINDOW_TRIANGULAR": (10, 2, (2, 0), (), "IR_WINDOW_TRIANGULAR", None),
		"IR_WindowFunction": (8, 2, (2, 0), (), "IR_WindowFunction", None),
		"IR_WindowUnit": (27, 2, (2, 0), (), "IR_WindowUnit", None),
	}
	_prop_map_put_ = {
		"IR_APPLYWINDOW_ALWAYS" : ((31, LCID, 4, 0),()),
		"IR_APPLYWINDOW_IMPULSE" : ((30, LCID, 4, 0),()),
		"IR_ApplyWindow" : ((29, LCID, 4, 0),()),
		"IR_ChannelsTied" : ((28, LCID, 4, 0),()),
		"IR_EndWindowChA" : ((23, LCID, 4, 0),()),
		"IR_EndWindowChB" : ((26, LCID, 4, 0),()),
		"IR_GeneratedRangeOnly" : ((7, LCID, 4, 0),()),
		"IR_HalfWindow" : ((20, LCID, 4, 0),()),
		"IR_IMPULSERELATIVITY_CHANNEL" : ((4, LCID, 4, 0),()),
		"IR_IMPULSERELATIVITY_GEN" : ((3, LCID, 4, 0),()),
		"IR_ImpulseAbsolute" : ((5, LCID, 4, 0),()),
		"IR_ImpulseRelativity" : ((2, LCID, 4, 0),()),
		"IR_ImpulseResponse" : ((1, LCID, 4, 0),()),
		"IR_MidWindowChA" : ((22, LCID, 4, 0),()),
		"IR_MidWindowChB" : ((25, LCID, 4, 0),()),
		"IR_NormalizeImpulse" : ((6, LCID, 4, 0),()),
		"IR_StartWindowChA" : ((21, LCID, 4, 0),()),
		"IR_StartWindowChB" : ((24, LCID, 4, 0),()),
		"IR_WINDOW_BH4" : ((14, LCID, 4, 0),()),
		"IR_WINDOW_BLACKMAN" : ((11, LCID, 4, 0),()),
		"IR_WINDOW_FLATTOP" : ((16, LCID, 4, 0),()),
		"IR_WINDOW_GAUSSIAN" : ((15, LCID, 4, 0),()),
		"IR_WINDOW_HAMMING" : ((13, LCID, 4, 0),()),
		"IR_WINDOW_HANN" : ((12, LCID, 4, 0),()),
		"IR_WINDOW_PRISM5" : ((17, LCID, 4, 0),()),
		"IR_WINDOW_PRISM6" : ((18, LCID, 4, 0),()),
		"IR_WINDOW_PRISM7" : ((19, LCID, 4, 0),()),
		"IR_WINDOW_RECTANGULAR" : ((9, LCID, 4, 0),()),
		"IR_WINDOW_TRIANGULAR" : ((10, LCID, 4, 0),()),
		"IR_WindowFunction" : ((8, LCID, 4, 0),()),
		"IR_WindowUnit" : ((27, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ILimitTable(DispatchBaseClass):
	CLSID = IID('{64D4EDC2-F218-11D4-B9A2-0050046915E5}')
	coclass_clsid = IID('{64D4EDC4-F218-11D4-B9A2-0050046915E5}')

	def LMT_AddPoint(self, dXValue=defaultNamedNotOptArg, dYValue=defaultNamedNotOptArg, bLineTo=defaultNamedNotOptArg):
		'LMT_AddPoint'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((5, 0), (5, 0), (11, 0)),dXValue
			, dYValue, bLineTo)

	def LMT_InitTable(self, lpszFileName=defaultNamedNotOptArg):
		'LMT_InitTable'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((8, 0),),lpszFileName
			)

	def LMT_RemovePoint(self, dXValue=defaultNamedNotOptArg):
		'LMT_RemovePoint'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((5, 0),),dXValue
			)

	def LMT_SaveTable(self, strFileName=defaultNamedNotOptArg):
		'LMT_SaveTable'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((8, 0),),strFileName
			)

	_prop_map_get_ = {
		"LMT_XUnit": (1, 2, (2, 0), (), "LMT_XUnit", None),
		"LMT_YUnit": (2, 2, (2, 0), (), "LMT_YUnit", None),
	}
	_prop_map_put_ = {
		"LMT_XUnit" : ((1, LCID, 4, 0),()),
		"LMT_YUnit" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMonitorOutputs(DispatchBaseClass):
	CLSID = IID('{E302BACC-E4DC-11D1-91DD-70AB00C10000}')
	coclass_clsid = IID('{E302BACE-E4DC-11D1-91DD-70AB00C10000}')

	_prop_map_get_ = {
		"MO_ANABNC_CHA": (38, 2, (2, 0), (), "MO_ANABNC_CHA", None),
		"MO_ANABNC_CHB": (39, 2, (2, 0), (), "MO_ANABNC_CHB", None),
		"MO_ANABNC_CTD_CHA": (42, 2, (2, 0), (), "MO_ANABNC_CTD_CHA", None),
		"MO_ANABNC_CTD_CHB": (43, 2, (2, 0), (), "MO_ANABNC_CTD_CHB", None),
		"MO_ANABNC_CTD_NONSEL": (45, 2, (2, 0), (), "MO_ANABNC_CTD_NONSEL", None),
		"MO_ANABNC_CTD_SEL": (44, 2, (2, 0), (), "MO_ANABNC_CTD_SEL", None),
		"MO_ANABNC_NONSEL": (41, 2, (2, 0), (), "MO_ANABNC_NONSEL", None),
		"MO_ANABNC_SEL": (40, 2, (2, 0), (), "MO_ANABNC_SEL", None),
		"MO_ANAGAIN_0DB": (11, 2, (2, 0), (), "MO_ANAGAIN_0DB", None),
		"MO_ANAGAIN_102DB": (28, 2, (2, 0), (), "MO_ANAGAIN_102DB", None),
		"MO_ANAGAIN_108DB": (29, 2, (2, 0), (), "MO_ANAGAIN_108DB", None),
		"MO_ANAGAIN_114DB": (30, 2, (2, 0), (), "MO_ANAGAIN_114DB", None),
		"MO_ANAGAIN_120DB": (31, 2, (2, 0), (), "MO_ANAGAIN_120DB", None),
		"MO_ANAGAIN_12DB": (13, 2, (2, 0), (), "MO_ANAGAIN_12DB", None),
		"MO_ANAGAIN_18DB": (14, 2, (2, 0), (), "MO_ANAGAIN_18DB", None),
		"MO_ANAGAIN_24DB": (15, 2, (2, 0), (), "MO_ANAGAIN_24DB", None),
		"MO_ANAGAIN_30DB": (16, 2, (2, 0), (), "MO_ANAGAIN_30DB", None),
		"MO_ANAGAIN_36DB": (17, 2, (2, 0), (), "MO_ANAGAIN_36DB", None),
		"MO_ANAGAIN_42DB": (18, 2, (2, 0), (), "MO_ANAGAIN_42DB", None),
		"MO_ANAGAIN_48DB": (19, 2, (2, 0), (), "MO_ANAGAIN_48DB", None),
		"MO_ANAGAIN_54DB": (20, 2, (2, 0), (), "MO_ANAGAIN_54DB", None),
		"MO_ANAGAIN_60DB": (21, 2, (2, 0), (), "MO_ANAGAIN_60DB", None),
		"MO_ANAGAIN_66DB": (22, 2, (2, 0), (), "MO_ANAGAIN_66DB", None),
		"MO_ANAGAIN_6DB": (12, 2, (2, 0), (), "MO_ANAGAIN_6DB", None),
		"MO_ANAGAIN_72DB": (23, 2, (2, 0), (), "MO_ANAGAIN_72DB", None),
		"MO_ANAGAIN_78DB": (24, 2, (2, 0), (), "MO_ANAGAIN_78DB", None),
		"MO_ANAGAIN_84DB": (25, 2, (2, 0), (), "MO_ANAGAIN_84DB", None),
		"MO_ANAGAIN_90DB": (26, 2, (2, 0), (), "MO_ANAGAIN_90DB", None),
		"MO_ANAGAIN_96DB": (27, 2, (2, 0), (), "MO_ANAGAIN_96DB", None),
		"MO_ANAGAIN_AUTO": (10, 2, (2, 0), (), "MO_ANAGAIN_AUTO", None),
		"MO_AnaBNC1": (34, 2, (2, 0), (), "MO_AnaBNC1", None),
		"MO_AnaBNC1Clipped": (32, 2, (2, 0), (), "MO_AnaBNC1Clipped", None),
		"MO_AnaBNC1Pulse": (35, 2, (11, 0), (), "MO_AnaBNC1Pulse", None),
		"MO_AnaBNC2": (36, 2, (2, 0), (), "MO_AnaBNC2", None),
		"MO_AnaBNC2Clipped": (33, 2, (2, 0), (), "MO_AnaBNC2Clipped", None),
		"MO_AnaBNC2Pulse": (37, 2, (11, 0), (), "MO_AnaBNC2Pulse", None),
		"MO_AnaGain": (9, 2, (2, 0), (), "MO_AnaGain", None),
		"MO_CARRIERBNC2_BITCLOCK": (50, 2, (2, 0), (), "MO_CARRIERBNC2_BITCLOCK", None),
		"MO_CARRIERBNC2_GEN": (51, 2, (2, 0), (), "MO_CARRIERBNC2_GEN", None),
		"MO_CARRIERBNC2_X": (48, 2, (2, 0), (), "MO_CARRIERBNC2_X", None),
		"MO_CARRIERBNC2_Y": (49, 2, (2, 0), (), "MO_CARRIERBNC2_Y", None),
		"MO_CarrierBNC2": (47, 2, (2, 0), (), "MO_CarrierBNC2", None),
		"MO_CarrierBNC2VidDiv": (52, 2, (11, 0), (), "MO_CarrierBNC2VidDiv", None),
		"MO_CarrierWaveform": (46, 2, (11, 0), (), "MO_CarrierWaveform", None),
		"MO_DOMOnly": (8, 2, (11, 0), (), "MO_DOMOnly", None),
		"MO_GENBNC_CHA": (6, 2, (2, 0), (), "MO_GENBNC_CHA", None),
		"MO_GENBNC_CHB": (7, 2, (2, 0), (), "MO_GENBNC_CHB", None),
		"MO_GenBNC1": (2, 2, (2, 0), (), "MO_GenBNC1", None),
		"MO_GenBNC1Pulse": (3, 2, (11, 0), (), "MO_GenBNC1Pulse", None),
		"MO_GenBNC2": (4, 2, (2, 0), (), "MO_GenBNC2", None),
		"MO_GenBNC2Pulse": (5, 2, (11, 0), (), "MO_GenBNC2Pulse", None),
		"MO_HEADPHONES_ANABNC1": (57, 2, (2, 0), (), "MO_HEADPHONES_ANABNC1", None),
		"MO_HEADPHONES_ANABNC1AND2": (59, 2, (2, 0), (), "MO_HEADPHONES_ANABNC1AND2", None),
		"MO_HEADPHONES_ANABNC2": (58, 2, (2, 0), (), "MO_HEADPHONES_ANABNC2", None),
		"MO_HEADPHONES_GENBNC1": (54, 2, (2, 0), (), "MO_HEADPHONES_GENBNC1", None),
		"MO_HEADPHONES_GENBNC1AND2": (56, 2, (2, 0), (), "MO_HEADPHONES_GENBNC1AND2", None),
		"MO_HEADPHONES_GENBNC2": (55, 2, (2, 0), (), "MO_HEADPHONES_GENBNC2", None),
		"MO_HeadphonesAndSpeaker": (53, 2, (2, 0), (), "MO_HeadphonesAndSpeaker", None),
		"MO_Mute": (1, 2, (11, 0), (), "MO_Mute", None),
	}
	_prop_map_put_ = {
		"MO_ANABNC_CHA" : ((38, LCID, 4, 0),()),
		"MO_ANABNC_CHB" : ((39, LCID, 4, 0),()),
		"MO_ANABNC_CTD_CHA" : ((42, LCID, 4, 0),()),
		"MO_ANABNC_CTD_CHB" : ((43, LCID, 4, 0),()),
		"MO_ANABNC_CTD_NONSEL" : ((45, LCID, 4, 0),()),
		"MO_ANABNC_CTD_SEL" : ((44, LCID, 4, 0),()),
		"MO_ANABNC_NONSEL" : ((41, LCID, 4, 0),()),
		"MO_ANABNC_SEL" : ((40, LCID, 4, 0),()),
		"MO_ANAGAIN_0DB" : ((11, LCID, 4, 0),()),
		"MO_ANAGAIN_102DB" : ((28, LCID, 4, 0),()),
		"MO_ANAGAIN_108DB" : ((29, LCID, 4, 0),()),
		"MO_ANAGAIN_114DB" : ((30, LCID, 4, 0),()),
		"MO_ANAGAIN_120DB" : ((31, LCID, 4, 0),()),
		"MO_ANAGAIN_12DB" : ((13, LCID, 4, 0),()),
		"MO_ANAGAIN_18DB" : ((14, LCID, 4, 0),()),
		"MO_ANAGAIN_24DB" : ((15, LCID, 4, 0),()),
		"MO_ANAGAIN_30DB" : ((16, LCID, 4, 0),()),
		"MO_ANAGAIN_36DB" : ((17, LCID, 4, 0),()),
		"MO_ANAGAIN_42DB" : ((18, LCID, 4, 0),()),
		"MO_ANAGAIN_48DB" : ((19, LCID, 4, 0),()),
		"MO_ANAGAIN_54DB" : ((20, LCID, 4, 0),()),
		"MO_ANAGAIN_60DB" : ((21, LCID, 4, 0),()),
		"MO_ANAGAIN_66DB" : ((22, LCID, 4, 0),()),
		"MO_ANAGAIN_6DB" : ((12, LCID, 4, 0),()),
		"MO_ANAGAIN_72DB" : ((23, LCID, 4, 0),()),
		"MO_ANAGAIN_78DB" : ((24, LCID, 4, 0),()),
		"MO_ANAGAIN_84DB" : ((25, LCID, 4, 0),()),
		"MO_ANAGAIN_90DB" : ((26, LCID, 4, 0),()),
		"MO_ANAGAIN_96DB" : ((27, LCID, 4, 0),()),
		"MO_ANAGAIN_AUTO" : ((10, LCID, 4, 0),()),
		"MO_AnaBNC1" : ((34, LCID, 4, 0),()),
		"MO_AnaBNC1Clipped" : ((32, LCID, 4, 0),()),
		"MO_AnaBNC1Pulse" : ((35, LCID, 4, 0),()),
		"MO_AnaBNC2" : ((36, LCID, 4, 0),()),
		"MO_AnaBNC2Clipped" : ((33, LCID, 4, 0),()),
		"MO_AnaBNC2Pulse" : ((37, LCID, 4, 0),()),
		"MO_AnaGain" : ((9, LCID, 4, 0),()),
		"MO_CARRIERBNC2_BITCLOCK" : ((50, LCID, 4, 0),()),
		"MO_CARRIERBNC2_GEN" : ((51, LCID, 4, 0),()),
		"MO_CARRIERBNC2_X" : ((48, LCID, 4, 0),()),
		"MO_CARRIERBNC2_Y" : ((49, LCID, 4, 0),()),
		"MO_CarrierBNC2" : ((47, LCID, 4, 0),()),
		"MO_CarrierBNC2VidDiv" : ((52, LCID, 4, 0),()),
		"MO_CarrierWaveform" : ((46, LCID, 4, 0),()),
		"MO_DOMOnly" : ((8, LCID, 4, 0),()),
		"MO_GENBNC_CHA" : ((6, LCID, 4, 0),()),
		"MO_GENBNC_CHB" : ((7, LCID, 4, 0),()),
		"MO_GenBNC1" : ((2, LCID, 4, 0),()),
		"MO_GenBNC1Pulse" : ((3, LCID, 4, 0),()),
		"MO_GenBNC2" : ((4, LCID, 4, 0),()),
		"MO_GenBNC2Pulse" : ((5, LCID, 4, 0),()),
		"MO_HEADPHONES_ANABNC1" : ((57, LCID, 4, 0),()),
		"MO_HEADPHONES_ANABNC1AND2" : ((59, LCID, 4, 0),()),
		"MO_HEADPHONES_ANABNC2" : ((58, LCID, 4, 0),()),
		"MO_HEADPHONES_GENBNC1" : ((54, LCID, 4, 0),()),
		"MO_HEADPHONES_GENBNC1AND2" : ((56, LCID, 4, 0),()),
		"MO_HEADPHONES_GENBNC2" : ((55, LCID, 4, 0),()),
		"MO_HeadphonesAndSpeaker" : ((53, LCID, 4, 0),()),
		"MO_Mute" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IOptions(DispatchBaseClass):
	CLSID = IID('{A3AB5423-CD5E-11D2-B0E8-00AA0011AF6D}')
	coclass_clsid = IID('{662F8E40-D1B7-11D4-AA54-0050046915E5}')

	_prop_map_get_ = {
		"OPT_ConfigurationsFolder": (4, 2, (8, 0), (), "OPT_ConfigurationsFolder", None),
		"OPT_DataTablesFolder": (8, 2, (8, 0), (), "OPT_DataTablesFolder", None),
		"OPT_DrawCurrentTraceBold": (28, 2, (11, 0), (), "OPT_DrawCurrentTraceBold", None),
		"OPT_EventLogsFolder": (12, 2, (8, 0), (), "OPT_EventLogsFolder", None),
		"OPT_FFTWindowsFolder": (10, 2, (8, 0), (), "OPT_FFTWindowsFolder", None),
		"OPT_GangTraceChannels": (27, 2, (11, 0), (), "OPT_GangTraceChannels", None),
		"OPT_GangYScales": (26, 2, (11, 0), (), "OPT_GangYScales", None),
		"OPT_GraphExportsFolder": (13, 2, (8, 0), (), "OPT_GraphExportsFolder", None),
		"OPT_LimitFilesFolder": (6, 2, (8, 0), (), "OPT_LimitFilesFolder", None),
		"OPT_LockDALineUp": (16, 2, (11, 0), (), "OPT_LockDALineUp", None),
		"OPT_LockRefFreq": (18, 2, (11, 0), (), "OPT_LockRefFreq", None),
		"OPT_LockdBr": (17, 2, (11, 0), (), "OPT_LockdBr", None),
		"OPT_PanelsOnTop": (25, 2, (11, 0), (), "OPT_PanelsOnTop", None),
		"OPT_RecentFileList": (1, 2, (2, 0), (), "OPT_RecentFileList", None),
		"OPT_RememberDetectorDetails": (20, 2, (11, 0), (), "OPT_RememberDetectorDetails", None),
		"OPT_SampleBuffersFolder": (14, 2, (8, 0), (), "OPT_SampleBuffersFolder", None),
		"OPT_ScriptsFolder": (5, 2, (8, 0), (), "OPT_ScriptsFolder", None),
		"OPT_ShowHexNeg": (19, 2, (11, 0), (), "OPT_ShowHexNeg", None),
		"OPT_StartupConfiguration": (2, 2, (8, 0), (), "OPT_StartupConfiguration", None),
		"OPT_StartupScript": (3, 2, (8, 0), (), "OPT_StartupScript", None),
		"OPT_TracesFolder": (9, 2, (8, 0), (), "OPT_TracesFolder", None),
		"OPT_TriggerPointRelative": (22, 2, (11, 0), (), "OPT_TriggerPointRelative", None),
		"OPT_UseLastFolder": (15, 2, (11, 0), (), "OPT_UseLastFolder", None),
		"OPT_UseLoadImpedance": (23, 2, (11, 0), (), "OPT_UseLoadImpedance", None),
		"OPT_UseSettlingsFromScripts": (21, 2, (11, 0), (), "OPT_UseSettlingsFromScripts", None),
		"OPT_WaitForMissingHardware": (24, 2, (11, 0), (), "OPT_WaitForMissingHardware", None),
		"OPT_WavetablesFolder": (7, 2, (8, 0), (), "OPT_WavetablesFolder", None),
		"OPT_WeightingFiltersFolder": (11, 2, (8, 0), (), "OPT_WeightingFiltersFolder", None),
	}
	_prop_map_put_ = {
		"OPT_ConfigurationsFolder" : ((4, LCID, 4, 0),()),
		"OPT_DataTablesFolder" : ((8, LCID, 4, 0),()),
		"OPT_DrawCurrentTraceBold" : ((28, LCID, 4, 0),()),
		"OPT_EventLogsFolder" : ((12, LCID, 4, 0),()),
		"OPT_FFTWindowsFolder" : ((10, LCID, 4, 0),()),
		"OPT_GangTraceChannels" : ((27, LCID, 4, 0),()),
		"OPT_GangYScales" : ((26, LCID, 4, 0),()),
		"OPT_GraphExportsFolder" : ((13, LCID, 4, 0),()),
		"OPT_LimitFilesFolder" : ((6, LCID, 4, 0),()),
		"OPT_LockDALineUp" : ((16, LCID, 4, 0),()),
		"OPT_LockRefFreq" : ((18, LCID, 4, 0),()),
		"OPT_LockdBr" : ((17, LCID, 4, 0),()),
		"OPT_PanelsOnTop" : ((25, LCID, 4, 0),()),
		"OPT_RecentFileList" : ((1, LCID, 4, 0),()),
		"OPT_RememberDetectorDetails" : ((20, LCID, 4, 0),()),
		"OPT_SampleBuffersFolder" : ((14, LCID, 4, 0),()),
		"OPT_ScriptsFolder" : ((5, LCID, 4, 0),()),
		"OPT_ShowHexNeg" : ((19, LCID, 4, 0),()),
		"OPT_StartupConfiguration" : ((2, LCID, 4, 0),()),
		"OPT_StartupScript" : ((3, LCID, 4, 0),()),
		"OPT_TracesFolder" : ((9, LCID, 4, 0),()),
		"OPT_TriggerPointRelative" : ((22, LCID, 4, 0),()),
		"OPT_UseLastFolder" : ((15, LCID, 4, 0),()),
		"OPT_UseLoadImpedance" : ((23, LCID, 4, 0),()),
		"OPT_UseSettlingsFromScripts" : ((21, LCID, 4, 0),()),
		"OPT_WaitForMissingHardware" : ((24, LCID, 4, 0),()),
		"OPT_WavetablesFolder" : ((7, LCID, 4, 0),()),
		"OPT_WeightingFiltersFolder" : ((11, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IPorts(DispatchBaseClass):
	CLSID = IID('{0211EBA7-BFF6-4C67-9E59-58EA93952CCD}')
	coclass_clsid = IID('{D9DE3A55-08AD-414C-BF6F-F0104B498432}')

	def PORTS_CreateSerialPort(self, sPort=defaultNamedNotOptArg):
		'PORTS_CreateSerialPort'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((2, 0),),sPort
			)

	def PORTS_DeleteSerialPort(self, sPort=defaultNamedNotOptArg):
		'PORTS_DeleteSerialPort'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((2, 0),),sPort
			)

	def PORTS_SetSerialPort(self, sPort=defaultNamedNotOptArg):
		'PORTS_SetSerialPort'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((2, 0),),sPort
			)

	def PORTS_WriteValue(self, sPort=defaultNamedNotOptArg, sValue=defaultNamedNotOptArg):
		'PORTS_WriteValue'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((2, 0), (2, 0)),sPort
			, sValue)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IReading(DispatchBaseClass):
	CLSID = IID('{BABA8F2B-2405-48C6-B991-337B5B00DBD8}')
	coclass_clsid = IID('{635D9E3E-E49C-4197-A003-C1BD4C0035EF}')

	def RDG_ResetMinAndMaxValues(self):
		'RDG_ResetMinAndMaxValues'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (24, 0), (),)

	def RDG_SetBackgroundColour(self, bRed=defaultNamedNotOptArg, bGreen=defaultNamedNotOptArg, bBlue=defaultNamedNotOptArg):
		'RDG_SetBackgroundColour'
		return self._oleobj_.InvokeTypes(34, LCID, 1, (24, 0), ((2, 0), (2, 0), (2, 0)),bRed
			, bGreen, bBlue)

	def RDG_SetBarColour(self, bRed=defaultNamedNotOptArg, bGreen=defaultNamedNotOptArg, bBlue=defaultNamedNotOptArg):
		'RDG_SetBarColour'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (24, 0), ((2, 0), (2, 0), (2, 0)),bRed
			, bGreen, bBlue)

	def RDG_SetLimitBackgroundColour(self, bRed=defaultNamedNotOptArg, bGreen=defaultNamedNotOptArg, bBlue=defaultNamedNotOptArg):
		'RDG_SetLimitBackgroundColour'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (24, 0), ((2, 0), (2, 0), (2, 0)),bRed
			, bGreen, bBlue)

	def RDG_SetLimitTextColour(self, bRed=defaultNamedNotOptArg, bGreen=defaultNamedNotOptArg, bBlue=defaultNamedNotOptArg):
		'RDG_SetLimitTextColour'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (24, 0), ((2, 0), (2, 0), (2, 0)),bRed
			, bGreen, bBlue)

	def RDG_SetTextColour(self, bRed=defaultNamedNotOptArg, bGreen=defaultNamedNotOptArg, bBlue=defaultNamedNotOptArg):
		'RDG_SetTextColour'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((2, 0), (2, 0), (2, 0)),bRed
			, bGreen, bBlue)

	_prop_map_get_ = {
		"RDG_AlwaysDisplayLimitStatus": (19, 2, (11, 0), (), "RDG_AlwaysDisplayLimitStatus", None),
		"RDG_BarMaxValue": (14, 2, (5, 0), (), "RDG_BarMaxValue", None),
		"RDG_BarMinValue": (13, 2, (5, 0), (), "RDG_BarMinValue", None),
		"RDG_BarNumSegments": (15, 2, (2, 0), (), "RDG_BarNumSegments", None),
		"RDG_Channel": (11, 2, (2, 0), (), "RDG_Channel", None),
		"RDG_Description": (2, 2, (8, 0), (), "RDG_Description", None),
		"RDG_FollowUnit": (8, 2, (11, 0), (), "RDG_FollowUnit", None),
		"RDG_LastMaxLimitBreachValue": (27, 2, (5, 0), (), "RDG_LastMaxLimitBreachValue", None),
		"RDG_LastMinLimitBreachValue": (26, 2, (5, 0), (), "RDG_LastMinLimitBreachValue", None),
		"RDG_LimitAudibleAlarm": (20, 2, (11, 0), (), "RDG_LimitAudibleAlarm", None),
		"RDG_LimitChangeBackgroundColour": (22, 2, (11, 0), (), "RDG_LimitChangeBackgroundColour", None),
		"RDG_LimitChangeTextColour": (21, 2, (11, 0), (), "RDG_LimitChangeTextColour", None),
		"RDG_LimitCheckingOn": (16, 2, (11, 0), (), "RDG_LimitCheckingOn", None),
		"RDG_LimitEventLog": (23, 2, (11, 0), (), "RDG_LimitEventLog", None),
		"RDG_MaxLimit": (18, 2, (5, 0), (), "RDG_MaxLimit", None),
		"RDG_MaxLimitBreached": (25, 2, (11, 0), (), "RDG_MaxLimitBreached", None),
		"RDG_MaxValue": (30, 2, (5, 0), (), "RDG_MaxValue", None),
		"RDG_MinLimit": (17, 2, (5, 0), (), "RDG_MinLimit", None),
		"RDG_MinLimitBreached": (24, 2, (11, 0), (), "RDG_MinLimitBreached", None),
		"RDG_MinValue": (29, 2, (5, 0), (), "RDG_MinValue", None),
		"RDG_RESOLUTION_DPS": (5, 2, (2, 0), (), "RDG_RESOLUTION_DPS", None),
		"RDG_RESOLUTION_SIGFIGS": (6, 2, (2, 0), (), "RDG_RESOLUTION_SIGFIGS", None),
		"RDG_Resolution": (7, 2, (2, 0), (), "RDG_Resolution", None),
		"RDG_ResolutionType": (4, 2, (2, 0), (), "RDG_ResolutionType", None),
		"RDG_ShowBarGraph": (12, 2, (11, 0), (), "RDG_ShowBarGraph", None),
		"RDG_ShowLimitsOnBarGraph": (32, 2, (11, 0), (), "RDG_ShowLimitsOnBarGraph", None),
		"RDG_ShowMinAndMaxOnBarGraph": (31, 2, (11, 0), (), "RDG_ShowMinAndMaxOnBarGraph", None),
		"RDG_ShowMinAndMaxValues": (28, 2, (11, 0), (), "RDG_ShowMinAndMaxValues", None),
		"RDG_ShowResultValue": (3, 2, (11, 0), (), "RDG_ShowResultValue", None),
		"RDG_ShowUnit": (10, 2, (11, 0), (), "RDG_ShowUnit", None),
		"RDG_Unit": (9, 2, (2, 0), (), "RDG_Unit", None),
		"RDG_Value": (1, 2, (5, 0), (), "RDG_Value", None),
	}
	_prop_map_put_ = {
		"RDG_AlwaysDisplayLimitStatus" : ((19, LCID, 4, 0),()),
		"RDG_BarMaxValue" : ((14, LCID, 4, 0),()),
		"RDG_BarMinValue" : ((13, LCID, 4, 0),()),
		"RDG_BarNumSegments" : ((15, LCID, 4, 0),()),
		"RDG_Channel" : ((11, LCID, 4, 0),()),
		"RDG_Description" : ((2, LCID, 4, 0),()),
		"RDG_FollowUnit" : ((8, LCID, 4, 0),()),
		"RDG_LastMaxLimitBreachValue" : ((27, LCID, 4, 0),()),
		"RDG_LastMinLimitBreachValue" : ((26, LCID, 4, 0),()),
		"RDG_LimitAudibleAlarm" : ((20, LCID, 4, 0),()),
		"RDG_LimitChangeBackgroundColour" : ((22, LCID, 4, 0),()),
		"RDG_LimitChangeTextColour" : ((21, LCID, 4, 0),()),
		"RDG_LimitCheckingOn" : ((16, LCID, 4, 0),()),
		"RDG_LimitEventLog" : ((23, LCID, 4, 0),()),
		"RDG_MaxLimit" : ((18, LCID, 4, 0),()),
		"RDG_MaxLimitBreached" : ((25, LCID, 4, 0),()),
		"RDG_MaxValue" : ((30, LCID, 4, 0),()),
		"RDG_MinLimit" : ((17, LCID, 4, 0),()),
		"RDG_MinLimitBreached" : ((24, LCID, 4, 0),()),
		"RDG_MinValue" : ((29, LCID, 4, 0),()),
		"RDG_RESOLUTION_DPS" : ((5, LCID, 4, 0),()),
		"RDG_RESOLUTION_SIGFIGS" : ((6, LCID, 4, 0),()),
		"RDG_Resolution" : ((7, LCID, 4, 0),()),
		"RDG_ResolutionType" : ((4, LCID, 4, 0),()),
		"RDG_ShowBarGraph" : ((12, LCID, 4, 0),()),
		"RDG_ShowLimitsOnBarGraph" : ((32, LCID, 4, 0),()),
		"RDG_ShowMinAndMaxOnBarGraph" : ((31, LCID, 4, 0),()),
		"RDG_ShowMinAndMaxValues" : ((28, LCID, 4, 0),()),
		"RDG_ShowResultValue" : ((3, LCID, 4, 0),()),
		"RDG_ShowUnit" : ((10, LCID, 4, 0),()),
		"RDG_Unit" : ((9, LCID, 4, 0),()),
		"RDG_Value" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRegulation(DispatchBaseClass):
	CLSID = IID('{94F3B76C-7223-43EA-8D03-0A87A8BD81CC}')
	coclass_clsid = IID('{601BF482-A141-47D2-83BD-EFF57A2685A7}')

	def REG_GetStatus(self):
		'REG_GetStatus'
		return self._oleobj_.InvokeTypes(59, LCID, 1, (2, 0), (),)

	def REG_Start(self):
		'REG_Start'
		return self._oleobj_.InvokeTypes(57, LCID, 1, (11, 0), (),)

	def REG_Stop(self):
		'REG_Stop'
		return self._oleobj_.InvokeTypes(58, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"REG_CHANNEL_A": (9, 2, (2, 0), (), "REG_CHANNEL_A", None),
		"REG_CHANNEL_B": (10, 2, (2, 0), (), "REG_CHANNEL_B", None),
		"REG_CHANNEL_BOTH": (13, 2, (2, 0), (), "REG_CHANNEL_BOTH", None),
		"REG_CHANNEL_BOTHTIED": (14, 2, (2, 0), (), "REG_CHANNEL_BOTHTIED", None),
		"REG_CHANNEL_EITHER": (15, 2, (2, 0), (), "REG_CHANNEL_EITHER", None),
		"REG_CHANNEL_NONSEL": (12, 2, (2, 0), (), "REG_CHANNEL_NONSEL", None),
		"REG_CHANNEL_SEL": (11, 2, (2, 0), (), "REG_CHANNEL_SEL", None),
		"REG_Channel": (8, 2, (2, 0), (), "REG_Channel", None),
		"REG_Continuous": (29, 2, (11, 0), (), "REG_Continuous", None),
		"REG_DIRECTION_DOWN": (50, 2, (2, 0), (), "REG_DIRECTION_DOWN", None),
		"REG_DIRECTION_UNKNOWN": (51, 2, (2, 0), (), "REG_DIRECTION_UNKNOWN", None),
		"REG_DIRECTION_UP": (49, 2, (2, 0), (), "REG_DIRECTION_UP", None),
		"REG_DIRECTION_USEHISTORY": (52, 2, (2, 0), (), "REG_DIRECTION_USEHISTORY", None),
		"REG_Direction": (48, 2, (2, 0), (), "REG_Direction", None),
		"REG_REGULATIONTYPE_ABSOLUTE": (17, 2, (2, 0), (), "REG_REGULATIONTYPE_ABSOLUTE", None),
		"REG_REGULATIONTYPE_MAXIMUM": (18, 2, (2, 0), (), "REG_REGULATIONTYPE_MAXIMUM", None),
		"REG_REGULATIONTYPE_MINIMUM": (19, 2, (2, 0), (), "REG_REGULATIONTYPE_MINIMUM", None),
		"REG_RESULT_CTDETECTOR": (5, 2, (2, 0), (), "REG_RESULT_CTDETECTOR", None),
		"REG_RESULT_FFTDETECTOR": (6, 2, (2, 0), (), "REG_RESULT_FFTDETECTOR", None),
		"REG_RESULT_FREQUENCY": (3, 2, (2, 0), (), "REG_RESULT_FREQUENCY", None),
		"REG_RESULT_PHASE": (4, 2, (2, 0), (), "REG_RESULT_PHASE", None),
		"REG_RESULT_RMSAMPLITUDE": (2, 2, (2, 0), (), "REG_RESULT_RMSAMPLITUDE", None),
		"REG_RegulateTo": (20, 2, (5, 0), (), "REG_RegulateTo", None),
		"REG_RegulationType": (16, 2, (2, 0), (), "REG_RegulationType", None),
		"REG_Result": (1, 2, (2, 0), (), "REG_Result", None),
		"REG_ResultFFTDetector": (7, 2, (2, 0), (), "REG_ResultFFTDetector", None),
		"REG_ResultUnit": (21, 2, (2, 0), (), "REG_ResultUnit", None),
		"REG_SOURCE_DCOFFSET": (34, 2, (2, 0), (), "REG_SOURCE_DCOFFSET", None),
		"REG_SOURCE_GENAMPL": (33, 2, (2, 0), (), "REG_SOURCE_GENAMPL", None),
		"REG_SOURCE_GENFREQ": (32, 2, (2, 0), (), "REG_SOURCE_GENFREQ", None),
		"REG_SOURCE_JITTERAMPL": (36, 2, (2, 0), (), "REG_SOURCE_JITTERAMPL", None),
		"REG_SOURCE_JITTERFREQ": (35, 2, (2, 0), (), "REG_SOURCE_JITTERFREQ", None),
		"REG_STATUS_FAILED": (56, 2, (2, 0), (), "REG_STATUS_FAILED", None),
		"REG_STATUS_INPROGRESS": (54, 2, (2, 0), (), "REG_STATUS_INPROGRESS", None),
		"REG_STATUS_NONE": (53, 2, (2, 0), (), "REG_STATUS_NONE", None),
		"REG_STATUS_OK": (55, 2, (2, 0), (), "REG_STATUS_OK", None),
		"REG_Sensitivity": (27, 2, (5, 0), (), "REG_Sensitivity", None),
		"REG_Source": (31, 2, (2, 0), (), "REG_Source", None),
		"REG_SourceMaxLimit": (39, 2, (5, 0), (), "REG_SourceMaxLimit", None),
		"REG_SourceMinLimit": (38, 2, (5, 0), (), "REG_SourceMinLimit", None),
		"REG_SourceOppChannel": (37, 2, (11, 0), (), "REG_SourceOppChannel", None),
		"REG_SourceUnit": (40, 2, (2, 0), (), "REG_SourceUnit", None),
		"REG_StepSize": (46, 2, (5, 0), (), "REG_StepSize", None),
		"REG_StepSizeAuto": (47, 2, (11, 0), (), "REG_StepSizeAuto", None),
		"REG_TOLERANCETYPE_OFFSET": (23, 2, (2, 0), (), "REG_TOLERANCETYPE_OFFSET", None),
		"REG_TOLERANCETYPE_RATIO": (24, 2, (2, 0), (), "REG_TOLERANCETYPE_RATIO", None),
		"REG_TREND_DECREASING": (43, 2, (2, 0), (), "REG_TREND_DECREASING", None),
		"REG_TREND_INCREASING": (42, 2, (2, 0), (), "REG_TREND_INCREASING", None),
		"REG_TREND_NONMONOTONIC": (45, 2, (2, 0), (), "REG_TREND_NONMONOTONIC", None),
		"REG_TREND_UNKNOWN": (44, 2, (2, 0), (), "REG_TREND_UNKNOWN", None),
		"REG_Timeout": (30, 2, (2, 0), (), "REG_Timeout", None),
		"REG_Tolerance": (25, 2, (5, 0), (), "REG_Tolerance", None),
		"REG_ToleranceType": (22, 2, (2, 0), (), "REG_ToleranceType", None),
		"REG_ToleranceUnit": (26, 2, (2, 0), (), "REG_ToleranceUnit", None),
		"REG_Trend": (41, 2, (2, 0), (), "REG_Trend", None),
		"REG_UseSettling": (28, 2, (11, 0), (), "REG_UseSettling", None),
	}
	_prop_map_put_ = {
		"REG_CHANNEL_A" : ((9, LCID, 4, 0),()),
		"REG_CHANNEL_B" : ((10, LCID, 4, 0),()),
		"REG_CHANNEL_BOTH" : ((13, LCID, 4, 0),()),
		"REG_CHANNEL_BOTHTIED" : ((14, LCID, 4, 0),()),
		"REG_CHANNEL_EITHER" : ((15, LCID, 4, 0),()),
		"REG_CHANNEL_NONSEL" : ((12, LCID, 4, 0),()),
		"REG_CHANNEL_SEL" : ((11, LCID, 4, 0),()),
		"REG_Channel" : ((8, LCID, 4, 0),()),
		"REG_Continuous" : ((29, LCID, 4, 0),()),
		"REG_DIRECTION_DOWN" : ((50, LCID, 4, 0),()),
		"REG_DIRECTION_UNKNOWN" : ((51, LCID, 4, 0),()),
		"REG_DIRECTION_UP" : ((49, LCID, 4, 0),()),
		"REG_DIRECTION_USEHISTORY" : ((52, LCID, 4, 0),()),
		"REG_Direction" : ((48, LCID, 4, 0),()),
		"REG_REGULATIONTYPE_ABSOLUTE" : ((17, LCID, 4, 0),()),
		"REG_REGULATIONTYPE_MAXIMUM" : ((18, LCID, 4, 0),()),
		"REG_REGULATIONTYPE_MINIMUM" : ((19, LCID, 4, 0),()),
		"REG_RESULT_CTDETECTOR" : ((5, LCID, 4, 0),()),
		"REG_RESULT_FFTDETECTOR" : ((6, LCID, 4, 0),()),
		"REG_RESULT_FREQUENCY" : ((3, LCID, 4, 0),()),
		"REG_RESULT_PHASE" : ((4, LCID, 4, 0),()),
		"REG_RESULT_RMSAMPLITUDE" : ((2, LCID, 4, 0),()),
		"REG_RegulateTo" : ((20, LCID, 4, 0),()),
		"REG_RegulationType" : ((16, LCID, 4, 0),()),
		"REG_Result" : ((1, LCID, 4, 0),()),
		"REG_ResultFFTDetector" : ((7, LCID, 4, 0),()),
		"REG_ResultUnit" : ((21, LCID, 4, 0),()),
		"REG_SOURCE_DCOFFSET" : ((34, LCID, 4, 0),()),
		"REG_SOURCE_GENAMPL" : ((33, LCID, 4, 0),()),
		"REG_SOURCE_GENFREQ" : ((32, LCID, 4, 0),()),
		"REG_SOURCE_JITTERAMPL" : ((36, LCID, 4, 0),()),
		"REG_SOURCE_JITTERFREQ" : ((35, LCID, 4, 0),()),
		"REG_STATUS_FAILED" : ((56, LCID, 4, 0),()),
		"REG_STATUS_INPROGRESS" : ((54, LCID, 4, 0),()),
		"REG_STATUS_NONE" : ((53, LCID, 4, 0),()),
		"REG_STATUS_OK" : ((55, LCID, 4, 0),()),
		"REG_Sensitivity" : ((27, LCID, 4, 0),()),
		"REG_Source" : ((31, LCID, 4, 0),()),
		"REG_SourceMaxLimit" : ((39, LCID, 4, 0),()),
		"REG_SourceMinLimit" : ((38, LCID, 4, 0),()),
		"REG_SourceOppChannel" : ((37, LCID, 4, 0),()),
		"REG_SourceUnit" : ((40, LCID, 4, 0),()),
		"REG_StepSize" : ((46, LCID, 4, 0),()),
		"REG_StepSizeAuto" : ((47, LCID, 4, 0),()),
		"REG_TOLERANCETYPE_OFFSET" : ((23, LCID, 4, 0),()),
		"REG_TOLERANCETYPE_RATIO" : ((24, LCID, 4, 0),()),
		"REG_TREND_DECREASING" : ((43, LCID, 4, 0),()),
		"REG_TREND_INCREASING" : ((42, LCID, 4, 0),()),
		"REG_TREND_NONMONOTONIC" : ((45, LCID, 4, 0),()),
		"REG_TREND_UNKNOWN" : ((44, LCID, 4, 0),()),
		"REG_Timeout" : ((30, LCID, 4, 0),()),
		"REG_Tolerance" : ((25, LCID, 4, 0),()),
		"REG_ToleranceType" : ((22, LCID, 4, 0),()),
		"REG_ToleranceUnit" : ((26, LCID, 4, 0),()),
		"REG_Trend" : ((41, LCID, 4, 0),()),
		"REG_UseSettling" : ((28, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISerialPort(DispatchBaseClass):
	CLSID = IID('{CBCB3652-E7DF-48FB-8172-E592A139C0E9}')
	coclass_clsid = IID('{9ADBC289-7D5F-47F4-A5AB-09A4617B63E0}')

	_prop_map_get_ = {
		"SP_Break": (8, 2, (11, 0), (), "SP_Break", None),
		"SP_CDHolding": (1, 2, (11, 0), (), "SP_CDHolding", None),
		"SP_CTSHolding": (2, 2, (11, 0), (), "SP_CTSHolding", None),
		"SP_CommEvent": (19, 2, (2, 0), (), "SP_CommEvent", None),
		"SP_DSRHolding": (3, 2, (11, 0), (), "SP_DSRHolding", None),
		"SP_DTREnable": (4, 2, (11, 0), (), "SP_DTREnable", None),
		"SP_EOFEnable": (20, 2, (11, 0), (), "SP_EOFEnable", None),
		"SP_Handshaking": (5, 2, (3, 0), (), "SP_Handshaking", None),
		"SP_InBufferCount": (7, 2, (2, 0), (), "SP_InBufferCount", None),
		"SP_InBufferSize": (6, 2, (2, 0), (), "SP_InBufferSize", None),
		"SP_Input": (18, 2, (12, 0), (), "SP_Input", None),
		"SP_InputLen": (9, 2, (2, 0), (), "SP_InputLen", None),
		"SP_InputMode": (21, 2, (3, 0), (), "SP_InputMode", None),
		"SP_NullDiscard": (10, 2, (11, 0), (), "SP_NullDiscard", None),
		"SP_OutBufferCount": (12, 2, (2, 0), (), "SP_OutBufferCount", None),
		"SP_OutBufferSize": (11, 2, (2, 0), (), "SP_OutBufferSize", None),
		"SP_Output": (17, 2, (12, 0), (), "SP_Output", None),
		"SP_ParityReplace": (13, 2, (8, 0), (), "SP_ParityReplace", None),
		"SP_PortOpen": (14, 2, (11, 0), (), "SP_PortOpen", None),
		"SP_RTSEnable": (15, 2, (11, 0), (), "SP_RTSEnable", None),
		"SP_Settings": (16, 2, (8, 0), (), "SP_Settings", None),
	}
	_prop_map_put_ = {
		"SP_Break" : ((8, LCID, 4, 0),()),
		"SP_CDHolding" : ((1, LCID, 4, 0),()),
		"SP_CTSHolding" : ((2, LCID, 4, 0),()),
		"SP_CommEvent" : ((19, LCID, 4, 0),()),
		"SP_DSRHolding" : ((3, LCID, 4, 0),()),
		"SP_DTREnable" : ((4, LCID, 4, 0),()),
		"SP_EOFEnable" : ((20, LCID, 4, 0),()),
		"SP_Handshaking" : ((5, LCID, 4, 0),()),
		"SP_InBufferCount" : ((7, LCID, 4, 0),()),
		"SP_InBufferSize" : ((6, LCID, 4, 0),()),
		"SP_Input" : ((18, LCID, 4, 0),()),
		"SP_InputLen" : ((9, LCID, 4, 0),()),
		"SP_InputMode" : ((21, LCID, 4, 0),()),
		"SP_NullDiscard" : ((10, LCID, 4, 0),()),
		"SP_OutBufferCount" : ((12, LCID, 4, 0),()),
		"SP_OutBufferSize" : ((11, LCID, 4, 0),()),
		"SP_Output" : ((17, LCID, 4, 0),()),
		"SP_ParityReplace" : ((13, LCID, 4, 0),()),
		"SP_PortOpen" : ((14, LCID, 4, 0),()),
		"SP_RTSEnable" : ((15, LCID, 4, 0),()),
		"SP_Settings" : ((16, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISettling(DispatchBaseClass):
	CLSID = IID('{CB72FCC1-DFBD-11D3-B0E8-00AA0011AF6D}')
	coclass_clsid = IID('{CB72FCC3-DFBD-11D3-B0E8-00AA0011AF6D}')

	_prop_map_get_ = {
		"SETT_CTDAverage": (20, 2, (11, 0), (), "SETT_CTDAverage", None),
		"SETT_CTDConvergence": (16, 2, (2, 0), (), "SETT_CTDConvergence", None),
		"SETT_CTDNumResults": (19, 2, (2, 0), (), "SETT_CTDNumResults", None),
		"SETT_CTDSettlingTime": (18, 2, (2, 0), (), "SETT_CTDSettlingTime", None),
		"SETT_CTDTolerance": (17, 2, (5, 0), (), "SETT_CTDTolerance", None),
		"SETT_DICAmplAverage": (30, 2, (11, 0), (), "SETT_DICAmplAverage", None),
		"SETT_DICAmplConvergence": (26, 2, (2, 0), (), "SETT_DICAmplConvergence", None),
		"SETT_DICAmplNumResults": (29, 2, (2, 0), (), "SETT_DICAmplNumResults", None),
		"SETT_DICAmplSettlingTime": (28, 2, (2, 0), (), "SETT_DICAmplSettlingTime", None),
		"SETT_DICAmplTolerance": (27, 2, (5, 0), (), "SETT_DICAmplTolerance", None),
		"SETT_DICJitterAverage": (35, 2, (11, 0), (), "SETT_DICJitterAverage", None),
		"SETT_DICJitterConvergence": (31, 2, (2, 0), (), "SETT_DICJitterConvergence", None),
		"SETT_DICJitterNumResults": (34, 2, (2, 0), (), "SETT_DICJitterNumResults", None),
		"SETT_DICJitterSettlingTime": (33, 2, (2, 0), (), "SETT_DICJitterSettlingTime", None),
		"SETT_DICJitterTolerance": (32, 2, (5, 0), (), "SETT_DICJitterTolerance", None),
		"SETT_DICPhaseAverage": (40, 2, (11, 0), (), "SETT_DICPhaseAverage", None),
		"SETT_DICPhaseConvergence": (36, 2, (2, 0), (), "SETT_DICPhaseConvergence", None),
		"SETT_DICPhaseNumResults": (39, 2, (2, 0), (), "SETT_DICPhaseNumResults", None),
		"SETT_DICPhaseSettlingTime": (38, 2, (2, 0), (), "SETT_DICPhaseSettlingTime", None),
		"SETT_DICPhaseTolerance": (37, 2, (5, 0), (), "SETT_DICPhaseTolerance", None),
		"SETT_DIFrameRateAverage": (45, 2, (11, 0), (), "SETT_DIFrameRateAverage", None),
		"SETT_DIFrameRateConvergence": (41, 2, (2, 0), (), "SETT_DIFrameRateConvergence", None),
		"SETT_DIFrameRateNumResults": (44, 2, (2, 0), (), "SETT_DIFrameRateNumResults", None),
		"SETT_DIFrameRateSettlingTime": (43, 2, (2, 0), (), "SETT_DIFrameRateSettlingTime", None),
		"SETT_DIFrameRateTolerance": (42, 2, (5, 0), (), "SETT_DIFrameRateTolerance", None),
		"SETT_FFTDAverage": (25, 2, (11, 0), (), "SETT_FFTDAverage", None),
		"SETT_FFTDConvergence": (21, 2, (2, 0), (), "SETT_FFTDConvergence", None),
		"SETT_FFTDNumResults": (24, 2, (2, 0), (), "SETT_FFTDNumResults", None),
		"SETT_FFTDSettlingTime": (23, 2, (2, 0), (), "SETT_FFTDSettlingTime", None),
		"SETT_FFTDTolerance": (22, 2, (5, 0), (), "SETT_FFTDTolerance", None),
		"SETT_RefSyncSourceAverage": (50, 2, (11, 0), (), "SETT_RefSyncSourceAverage", None),
		"SETT_RefSyncSourceConvergence": (46, 2, (2, 0), (), "SETT_RefSyncSourceConvergence", None),
		"SETT_RefSyncSourceNumResults": (49, 2, (2, 0), (), "SETT_RefSyncSourceNumResults", None),
		"SETT_RefSyncSourceSettlingTime": (48, 2, (2, 0), (), "SETT_RefSyncSourceSettlingTime", None),
		"SETT_RefSyncSourceTolerance": (47, 2, (5, 0), (), "SETT_RefSyncSourceTolerance", None),
		"SETT_SAAmplAverage": (5, 2, (11, 0), (), "SETT_SAAmplAverage", None),
		"SETT_SAAmplConvergence": (1, 2, (2, 0), (), "SETT_SAAmplConvergence", None),
		"SETT_SAAmplNumResults": (4, 2, (2, 0), (), "SETT_SAAmplNumResults", None),
		"SETT_SAAmplSettlingTime": (3, 2, (2, 0), (), "SETT_SAAmplSettlingTime", None),
		"SETT_SAAmplTolerance": (2, 2, (5, 0), (), "SETT_SAAmplTolerance", None),
		"SETT_SAFreqAverage": (10, 2, (11, 0), (), "SETT_SAFreqAverage", None),
		"SETT_SAFreqConvergence": (6, 2, (2, 0), (), "SETT_SAFreqConvergence", None),
		"SETT_SAFreqNumResults": (9, 2, (2, 0), (), "SETT_SAFreqNumResults", None),
		"SETT_SAFreqSettlingTime": (8, 2, (2, 0), (), "SETT_SAFreqSettlingTime", None),
		"SETT_SAFreqTolerance": (7, 2, (5, 0), (), "SETT_SAFreqTolerance", None),
		"SETT_SAPhaseAverage": (15, 2, (11, 0), (), "SETT_SAPhaseAverage", None),
		"SETT_SAPhaseConvergence": (11, 2, (2, 0), (), "SETT_SAPhaseConvergence", None),
		"SETT_SAPhaseNumResults": (14, 2, (2, 0), (), "SETT_SAPhaseNumResults", None),
		"SETT_SAPhaseSettlingTime": (13, 2, (2, 0), (), "SETT_SAPhaseSettlingTime", None),
		"SETT_SAPhaseTolerance": (12, 2, (5, 0), (), "SETT_SAPhaseTolerance", None),
		"SW_CONVERGENCE_EXPONENTIAL": (53, 2, (2, 0), (), "SW_CONVERGENCE_EXPONENTIAL", None),
		"SW_CONVERGENCE_NONE": (51, 2, (2, 0), (), "SW_CONVERGENCE_NONE", None),
		"SW_CONVERGENCE_NORMAL": (52, 2, (2, 0), (), "SW_CONVERGENCE_NORMAL", None),
	}
	_prop_map_put_ = {
		"SETT_CTDAverage" : ((20, LCID, 4, 0),()),
		"SETT_CTDConvergence" : ((16, LCID, 4, 0),()),
		"SETT_CTDNumResults" : ((19, LCID, 4, 0),()),
		"SETT_CTDSettlingTime" : ((18, LCID, 4, 0),()),
		"SETT_CTDTolerance" : ((17, LCID, 4, 0),()),
		"SETT_DICAmplAverage" : ((30, LCID, 4, 0),()),
		"SETT_DICAmplConvergence" : ((26, LCID, 4, 0),()),
		"SETT_DICAmplNumResults" : ((29, LCID, 4, 0),()),
		"SETT_DICAmplSettlingTime" : ((28, LCID, 4, 0),()),
		"SETT_DICAmplTolerance" : ((27, LCID, 4, 0),()),
		"SETT_DICJitterAverage" : ((35, LCID, 4, 0),()),
		"SETT_DICJitterConvergence" : ((31, LCID, 4, 0),()),
		"SETT_DICJitterNumResults" : ((34, LCID, 4, 0),()),
		"SETT_DICJitterSettlingTime" : ((33, LCID, 4, 0),()),
		"SETT_DICJitterTolerance" : ((32, LCID, 4, 0),()),
		"SETT_DICPhaseAverage" : ((40, LCID, 4, 0),()),
		"SETT_DICPhaseConvergence" : ((36, LCID, 4, 0),()),
		"SETT_DICPhaseNumResults" : ((39, LCID, 4, 0),()),
		"SETT_DICPhaseSettlingTime" : ((38, LCID, 4, 0),()),
		"SETT_DICPhaseTolerance" : ((37, LCID, 4, 0),()),
		"SETT_DIFrameRateAverage" : ((45, LCID, 4, 0),()),
		"SETT_DIFrameRateConvergence" : ((41, LCID, 4, 0),()),
		"SETT_DIFrameRateNumResults" : ((44, LCID, 4, 0),()),
		"SETT_DIFrameRateSettlingTime" : ((43, LCID, 4, 0),()),
		"SETT_DIFrameRateTolerance" : ((42, LCID, 4, 0),()),
		"SETT_FFTDAverage" : ((25, LCID, 4, 0),()),
		"SETT_FFTDConvergence" : ((21, LCID, 4, 0),()),
		"SETT_FFTDNumResults" : ((24, LCID, 4, 0),()),
		"SETT_FFTDSettlingTime" : ((23, LCID, 4, 0),()),
		"SETT_FFTDTolerance" : ((22, LCID, 4, 0),()),
		"SETT_RefSyncSourceAverage" : ((50, LCID, 4, 0),()),
		"SETT_RefSyncSourceConvergence" : ((46, LCID, 4, 0),()),
		"SETT_RefSyncSourceNumResults" : ((49, LCID, 4, 0),()),
		"SETT_RefSyncSourceSettlingTime" : ((48, LCID, 4, 0),()),
		"SETT_RefSyncSourceTolerance" : ((47, LCID, 4, 0),()),
		"SETT_SAAmplAverage" : ((5, LCID, 4, 0),()),
		"SETT_SAAmplConvergence" : ((1, LCID, 4, 0),()),
		"SETT_SAAmplNumResults" : ((4, LCID, 4, 0),()),
		"SETT_SAAmplSettlingTime" : ((3, LCID, 4, 0),()),
		"SETT_SAAmplTolerance" : ((2, LCID, 4, 0),()),
		"SETT_SAFreqAverage" : ((10, LCID, 4, 0),()),
		"SETT_SAFreqConvergence" : ((6, LCID, 4, 0),()),
		"SETT_SAFreqNumResults" : ((9, LCID, 4, 0),()),
		"SETT_SAFreqSettlingTime" : ((8, LCID, 4, 0),()),
		"SETT_SAFreqTolerance" : ((7, LCID, 4, 0),()),
		"SETT_SAPhaseAverage" : ((15, LCID, 4, 0),()),
		"SETT_SAPhaseConvergence" : ((11, LCID, 4, 0),()),
		"SETT_SAPhaseNumResults" : ((14, LCID, 4, 0),()),
		"SETT_SAPhaseSettlingTime" : ((13, LCID, 4, 0),()),
		"SETT_SAPhaseTolerance" : ((12, LCID, 4, 0),()),
		"SW_CONVERGENCE_EXPONENTIAL" : ((53, LCID, 4, 0),()),
		"SW_CONVERGENCE_NONE" : ((51, LCID, 4, 0),()),
		"SW_CONVERGENCE_NORMAL" : ((52, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISignalAnalyzer(DispatchBaseClass):
	CLSID = IID('{31080A22-11BC-11D2-91DE-70AB00C10000}')
	coclass_clsid = IID('{31080A24-11BC-11D2-91DE-70AB00C10000}')

	def SA_RefAmplFromChA(self):
		'SA_RefAmplFromChA'
		return self._oleobj_.InvokeTypes(59, LCID, 1, (24, 0), (),)

	def SA_RefAmplFromChB(self):
		'SA_RefAmplFromChB'
		return self._oleobj_.InvokeTypes(60, LCID, 1, (24, 0), (),)

	def SA_RefFreqFromChA(self):
		'SA_RefFreqFromChA'
		return self._oleobj_.InvokeTypes(61, LCID, 1, (24, 0), (),)

	def SA_RefFreqFromChB(self):
		'SA_RefFreqFromChB'
		return self._oleobj_.InvokeTypes(62, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"SA_ANALOGUE": (3, 2, (2, 0), (), "SA_ANALOGUE", None),
		"SA_CHA": (12, 2, (2, 0), (), "SA_CHA", None),
		"SA_CHB": (13, 2, (2, 0), (), "SA_CHB", None),
		"SA_CHBOTH": (14, 2, (2, 0), (), "SA_CHBOTH", None),
		"SA_ChAFreq": (18, 2, (5, 0), (), "SA_ChAFreq", None),
		"SA_ChARMSAmpl": (15, 2, (5, 0), (), "SA_ChARMSAmpl", None),
		"SA_ChARefAmpl": (24, 2, (5, 0), (), "SA_ChARefAmpl", None),
		"SA_ChBFreq": (19, 2, (5, 0), (), "SA_ChBFreq", None),
		"SA_ChBRMSAmpl": (16, 2, (5, 0), (), "SA_ChBRMSAmpl", None),
		"SA_ChBRefAmpl": (25, 2, (5, 0), (), "SA_ChBRefAmpl", None),
		"SA_Channel": (11, 2, (2, 0), (), "SA_Channel", None),
		"SA_DALineUp": (35, 2, (5, 0), (), "SA_DALineUp", None),
		"SA_DALineUpUnit": (36, 2, (2, 0), (), "SA_DALineUpUnit", None),
		"SA_DIGITAL": (2, 2, (2, 0), (), "SA_DIGITAL", None),
		"SA_DefaultHPFilter": (37, 2, (2, 0), (), "SA_DefaultHPFilter", None),
		"SA_DefaultHPFilterFreq": (38, 2, (3, 0), (), "SA_DefaultHPFilterFreq", None),
		"SA_DefaultLPFilter": (45, 2, (2, 0), (), "SA_DefaultLPFilter", None),
		"SA_DefaultLPFilterFreq": (46, 2, (3, 0), (), "SA_DefaultLPFilterFreq", None),
		"SA_DefaultWeightingFilter": (53, 2, (2, 0), (), "SA_DefaultWeightingFilter", None),
		"SA_FreqUnit": (20, 2, (2, 0), (), "SA_FreqUnit", None),
		"SA_Gain": (30, 2, (5, 0), (), "SA_Gain", None),
		"SA_GainUnit": (31, 2, (2, 0), (), "SA_GainUnit", None),
		"SA_HP_100HZ": (43, 2, (2, 0), (), "SA_HP_100HZ", None),
		"SA_HP_10HZ": (41, 2, (2, 0), (), "SA_HP_10HZ", None),
		"SA_HP_22HZ": (42, 2, (2, 0), (), "SA_HP_22HZ", None),
		"SA_HP_400HZ": (44, 2, (2, 0), (), "SA_HP_400HZ", None),
		"SA_HP_DCB": (40, 2, (2, 0), (), "SA_HP_DCB", None),
		"SA_HP_OFF": (39, 2, (2, 0), (), "SA_HP_OFF", None),
		"SA_LP_20KHZ_AES17": (52, 2, (2, 0), (), "SA_LP_20KHZ_AES17", None),
		"SA_LP_22KHZ": (48, 2, (2, 0), (), "SA_LP_22KHZ", None),
		"SA_LP_30KHZ": (49, 2, (2, 0), (), "SA_LP_30KHZ", None),
		"SA_LP_40KHZ": (50, 2, (2, 0), (), "SA_LP_40KHZ", None),
		"SA_LP_80KHZ": (51, 2, (2, 0), (), "SA_LP_80KHZ", None),
		"SA_LP_OFF": (47, 2, (2, 0), (), "SA_LP_OFF", None),
		"SA_Phase": (21, 2, (5, 0), (), "SA_Phase", None),
		"SA_PhaseUnit": (22, 2, (2, 0), (), "SA_PhaseUnit", None),
		"SA_RMSAmplUnit": (17, 2, (2, 0), (), "SA_RMSAmplUnit", None),
		"SA_RefAmpl": (23, 2, (5, 0), (), "SA_RefAmpl", None),
		"SA_RefAmplTied": (26, 2, (11, 0), (), "SA_RefAmplTied", None),
		"SA_RefAmplUnit": (27, 2, (2, 0), (), "SA_RefAmplUnit", None),
		"SA_RefFreq": (28, 2, (5, 0), (), "SA_RefFreq", None),
		"SA_RefImpedance": (29, 2, (5, 0), (), "SA_RefImpedance", None),
		"SA_SOUNDCARD": (4, 2, (2, 0), (), "SA_SOUNDCARD", None),
		"SA_SPLRef": (33, 2, (5, 0), (), "SA_SPLRef", None),
		"SA_SPLRefUnit": (34, 2, (2, 0), (), "SA_SPLRefUnit", None),
		"SA_Source": (1, 2, (2, 0), (), "SA_Source", None),
		"SA_UPDATERATE_16": (9, 2, (2, 0), (), "SA_UPDATERATE_16", None),
		"SA_UPDATERATE_32": (10, 2, (2, 0), (), "SA_UPDATERATE_32", None),
		"SA_UPDATERATE_4": (7, 2, (2, 0), (), "SA_UPDATERATE_4", None),
		"SA_UPDATERATE_8": (8, 2, (2, 0), (), "SA_UPDATERATE_8", None),
		"SA_UPDATERATE_AUTO": (6, 2, (2, 0), (), "SA_UPDATERATE_AUTO", None),
		"SA_UpdateRate": (5, 2, (2, 0), (), "SA_UpdateRate", None),
		"SA_WEIGHTING_AWEIGHTING": (55, 2, (2, 0), (), "SA_WEIGHTING_AWEIGHTING", None),
		"SA_WEIGHTING_CCIR468_1K": (57, 2, (2, 0), (), "SA_WEIGHTING_CCIR468_1K", None),
		"SA_WEIGHTING_CCIR468_2K": (58, 2, (2, 0), (), "SA_WEIGHTING_CCIR468_2K", None),
		"SA_WEIGHTING_CWEIGHTING": (56, 2, (2, 0), (), "SA_WEIGHTING_CWEIGHTING", None),
		"SA_WEIGHTING_NONE": (54, 2, (2, 0), (), "SA_WEIGHTING_NONE", None),
		"SA_dBSPLValue": (32, 2, (5, 0), (), "SA_dBSPLValue", None),
	}
	_prop_map_put_ = {
		"SA_ANALOGUE" : ((3, LCID, 4, 0),()),
		"SA_CHA" : ((12, LCID, 4, 0),()),
		"SA_CHB" : ((13, LCID, 4, 0),()),
		"SA_CHBOTH" : ((14, LCID, 4, 0),()),
		"SA_ChAFreq" : ((18, LCID, 4, 0),()),
		"SA_ChARMSAmpl" : ((15, LCID, 4, 0),()),
		"SA_ChARefAmpl" : ((24, LCID, 4, 0),()),
		"SA_ChBFreq" : ((19, LCID, 4, 0),()),
		"SA_ChBRMSAmpl" : ((16, LCID, 4, 0),()),
		"SA_ChBRefAmpl" : ((25, LCID, 4, 0),()),
		"SA_Channel" : ((11, LCID, 4, 0),()),
		"SA_DALineUp" : ((35, LCID, 4, 0),()),
		"SA_DALineUpUnit" : ((36, LCID, 4, 0),()),
		"SA_DIGITAL" : ((2, LCID, 4, 0),()),
		"SA_DefaultHPFilter" : ((37, LCID, 4, 0),()),
		"SA_DefaultHPFilterFreq" : ((38, LCID, 4, 0),()),
		"SA_DefaultLPFilter" : ((45, LCID, 4, 0),()),
		"SA_DefaultLPFilterFreq" : ((46, LCID, 4, 0),()),
		"SA_DefaultWeightingFilter" : ((53, LCID, 4, 0),()),
		"SA_FreqUnit" : ((20, LCID, 4, 0),()),
		"SA_Gain" : ((30, LCID, 4, 0),()),
		"SA_GainUnit" : ((31, LCID, 4, 0),()),
		"SA_HP_100HZ" : ((43, LCID, 4, 0),()),
		"SA_HP_10HZ" : ((41, LCID, 4, 0),()),
		"SA_HP_22HZ" : ((42, LCID, 4, 0),()),
		"SA_HP_400HZ" : ((44, LCID, 4, 0),()),
		"SA_HP_DCB" : ((40, LCID, 4, 0),()),
		"SA_HP_OFF" : ((39, LCID, 4, 0),()),
		"SA_LP_20KHZ_AES17" : ((52, LCID, 4, 0),()),
		"SA_LP_22KHZ" : ((48, LCID, 4, 0),()),
		"SA_LP_30KHZ" : ((49, LCID, 4, 0),()),
		"SA_LP_40KHZ" : ((50, LCID, 4, 0),()),
		"SA_LP_80KHZ" : ((51, LCID, 4, 0),()),
		"SA_LP_OFF" : ((47, LCID, 4, 0),()),
		"SA_Phase" : ((21, LCID, 4, 0),()),
		"SA_PhaseUnit" : ((22, LCID, 4, 0),()),
		"SA_RMSAmplUnit" : ((17, LCID, 4, 0),()),
		"SA_RefAmpl" : ((23, LCID, 4, 0),()),
		"SA_RefAmplTied" : ((26, LCID, 4, 0),()),
		"SA_RefAmplUnit" : ((27, LCID, 4, 0),()),
		"SA_RefFreq" : ((28, LCID, 4, 0),()),
		"SA_RefImpedance" : ((29, LCID, 4, 0),()),
		"SA_SOUNDCARD" : ((4, LCID, 4, 0),()),
		"SA_SPLRef" : ((33, LCID, 4, 0),()),
		"SA_SPLRefUnit" : ((34, LCID, 4, 0),()),
		"SA_Source" : ((1, LCID, 4, 0),()),
		"SA_UPDATERATE_16" : ((9, LCID, 4, 0),()),
		"SA_UPDATERATE_32" : ((10, LCID, 4, 0),()),
		"SA_UPDATERATE_4" : ((7, LCID, 4, 0),()),
		"SA_UPDATERATE_8" : ((8, LCID, 4, 0),()),
		"SA_UPDATERATE_AUTO" : ((6, LCID, 4, 0),()),
		"SA_UpdateRate" : ((5, LCID, 4, 0),()),
		"SA_WEIGHTING_AWEIGHTING" : ((55, LCID, 4, 0),()),
		"SA_WEIGHTING_CCIR468_1K" : ((57, LCID, 4, 0),()),
		"SA_WEIGHTING_CCIR468_2K" : ((58, LCID, 4, 0),()),
		"SA_WEIGHTING_CWEIGHTING" : ((56, LCID, 4, 0),()),
		"SA_WEIGHTING_NONE" : ((54, LCID, 4, 0),()),
		"SA_dBSPLValue" : ((32, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISignalGenerator(DispatchBaseClass):
	CLSID = IID('{85AFFE41-E654-11D1-91DD-70AB00C10000}')
	coclass_clsid = IID('{85AFFE43-E654-11D1-91DD-70AB00C10000}')

	def SG_ChACopy(self):
		'SG_ChACopy'
		return self._oleobj_.InvokeTypes(135, LCID, 1, (24, 0), (),)

	def SG_ChBCopy(self):
		'SG_ChBCopy'
		return self._oleobj_.InvokeTypes(136, LCID, 1, (24, 0), (),)

	def SG_GetChAAmpl(self, sUnit=defaultNamedNotOptArg):
		'SG_GetChAAmpl'
		return self._oleobj_.InvokeTypes(143, LCID, 1, (5, 0), ((2, 0),),sUnit
			)

	def SG_GetChAAmplInFFS(self):
		'SG_GetChAAmplInFFS'
		return self._oleobj_.InvokeTypes(141, LCID, 1, (5, 0), (),)

	def SG_GetChBAmpl(self, sUnit=defaultNamedNotOptArg):
		'SG_GetChBAmpl'
		return self._oleobj_.InvokeTypes(144, LCID, 1, (5, 0), ((2, 0),),sUnit
			)

	def SG_GetChBAmplInFFS(self):
		'SG_GetChBAmplInFFS'
		return self._oleobj_.InvokeTypes(142, LCID, 1, (5, 0), (),)

	def SG_RefAmplFromChA(self):
		'SG_RefAmplFromChA'
		return self._oleobj_.InvokeTypes(137, LCID, 1, (24, 0), (),)

	def SG_RefAmplFromChB(self):
		'SG_RefAmplFromChB'
		return self._oleobj_.InvokeTypes(138, LCID, 1, (24, 0), (),)

	def SG_RefFreqFromChA(self):
		'SG_RefFreqFromChA'
		return self._oleobj_.InvokeTypes(139, LCID, 1, (24, 0), (),)

	def SG_RefFreqFromChB(self):
		'SG_RefFreqFromChB'
		return self._oleobj_.InvokeTypes(140, LCID, 1, (24, 0), (),)

	def SG_UserWaveformPlay(self, sChannel=defaultNamedNotOptArg):
		'SG_UserWaveformPlay'
		return self._oleobj_.InvokeTypes(145, LCID, 1, (24, 0), ((2, 0),),sChannel
			)

	_prop_map_get_ = {
		"SG_2NDAMPLOFFSET_ABS": (37, 2, (2, 0), (), "SG_2NDAMPLOFFSET_ABS", None),
		"SG_2NDAMPLOFFSET_OFFSET": (38, 2, (2, 0), (), "SG_2NDAMPLOFFSET_OFFSET", None),
		"SG_2NDAMPLOFFSET_RATIO": (39, 2, (2, 0), (), "SG_2NDAMPLOFFSET_RATIO", None),
		"SG_2NDFREQOFFSET_ABS": (32, 2, (2, 0), (), "SG_2NDFREQOFFSET_ABS", None),
		"SG_2NDFREQOFFSET_OFFSET": (33, 2, (2, 0), (), "SG_2NDFREQOFFSET_OFFSET", None),
		"SG_2NDFREQOFFSET_RATIO": (34, 2, (2, 0), (), "SG_2NDFREQOFFSET_RATIO", None),
		"SG_AMPLSTEPMODE_OFFSET": (120, 2, (2, 0), (), "SG_AMPLSTEPMODE_OFFSET", None),
		"SG_AMPLSTEPMODE_RATIO": (121, 2, (2, 0), (), "SG_AMPLSTEPMODE_RATIO", None),
		"SG_AmplStep": (122, 2, (5, 0), (), "SG_AmplStep", None),
		"SG_AmplStepMode": (119, 2, (2, 0), (), "SG_AmplStepMode", None),
		"SG_BURSTMODE_NUMPERIODS": (45, 2, (2, 0), (), "SG_BURSTMODE_NUMPERIODS", None),
		"SG_BURSTMODE_TIMEPERIOD": (46, 2, (2, 0), (), "SG_BURSTMODE_TIMEPERIOD", None),
		"SG_ChA2ndAmpl": (40, 2, (5, 0), (), "SG_ChA2ndAmpl", None),
		"SG_ChA2ndAmplOffset": (36, 2, (2, 0), (), "SG_ChA2ndAmplOffset", None),
		"SG_ChA2ndFreq": (35, 2, (5, 0), (), "SG_ChA2ndFreq", None),
		"SG_ChA2ndFreqOffset": (31, 2, (2, 0), (), "SG_ChA2ndFreqOffset", None),
		"SG_ChAAmpl": (19, 2, (5, 0), (), "SG_ChAAmpl", None),
		"SG_ChAAmplUnit": (20, 2, (2, 0), (), "SG_ChAAmplUnit", None),
		"SG_ChABurst2ndAmplDuration": (48, 2, (5, 0), (), "SG_ChABurst2ndAmplDuration", None),
		"SG_ChABurstAmplDuration": (47, 2, (5, 0), (), "SG_ChABurstAmplDuration", None),
		"SG_ChABurstMode": (44, 2, (2, 0), (), "SG_ChABurstMode", None),
		"SG_ChABurstNumPeriods": (49, 2, (3, 0), (), "SG_ChABurstNumPeriods", None),
		"SG_ChABurstSpacePeriod": (50, 2, (3, 0), (), "SG_ChABurstSpacePeriod", None),
		"SG_ChADutyCycle": (23, 2, (5, 0), (), "SG_ChADutyCycle", None),
		"SG_ChADutyCycleUnit": (24, 2, (2, 0), (), "SG_ChADutyCycleUnit", None),
		"SG_ChAFreq": (21, 2, (5, 0), (), "SG_ChAFreq", None),
		"SG_ChAFreqUnit": (22, 2, (2, 0), (), "SG_ChAFreqUnit", None),
		"SG_ChAFunction": (6, 2, (2, 0), (), "SG_ChAFunction", None),
		"SG_ChALog": (53, 2, (11, 0), (), "SG_ChALog", None),
		"SG_ChAMLSLength": (41, 2, (2, 0), (), "SG_ChAMLSLength", None),
		"SG_ChANumSamples": (54, 2, (3, 0), (), "SG_ChANumSamples", None),
		"SG_ChAOn": (4, 2, (11, 0), (), "SG_ChAOn", None),
		"SG_ChAPhaseInvert": (5, 2, (11, 0), (), "SG_ChAPhaseInvert", None),
		"SG_ChAPhases": (69, 2, (2, 0), (), "SG_ChAPhases", None),
		"SG_ChAPink": (68, 2, (11, 0), (), "SG_ChAPink", None),
		"SG_ChAPolarity": (25, 2, (2, 0), (), "SG_ChAPolarity", None),
		"SG_ChAPulseNumMarks": (42, 2, (2, 0), (), "SG_ChAPulseNumMarks", None),
		"SG_ChAPulseSpacePeriod": (43, 2, (3, 0), (), "SG_ChAPulseSpacePeriod", None),
		"SG_ChARampDown": (66, 2, (5, 0), (), "SG_ChARampDown", None),
		"SG_ChARampUp": (65, 2, (5, 0), (), "SG_ChARampUp", None),
		"SG_ChARefAmpl": (108, 2, (5, 0), (), "SG_ChARefAmpl", None),
		"SG_ChAStartFreq": (51, 2, (5, 0), (), "SG_ChAStartFreq", None),
		"SG_ChAStopFreq": (52, 2, (5, 0), (), "SG_ChAStopFreq", None),
		"SG_ChASweptSineUnit": (67, 2, (2, 0), (), "SG_ChASweptSineUnit", None),
		"SG_ChATrailSpace": (64, 2, (5, 0), (), "SG_ChATrailSpace", None),
		"SG_ChAUserWaveform": (29, 2, (8, 0), (), "SG_ChAUserWaveform", None),
		"SG_ChAUserWaveformRepeat": (30, 2, (2, 0), (), "SG_ChAUserWaveformRepeat", None),
		"SG_ChB2ndAmpl": (88, 2, (5, 0), (), "SG_ChB2ndAmpl", None),
		"SG_ChB2ndAmplOffset": (87, 2, (2, 0), (), "SG_ChB2ndAmplOffset", None),
		"SG_ChB2ndFreq": (86, 2, (5, 0), (), "SG_ChB2ndFreq", None),
		"SG_ChB2ndFreqOffset": (85, 2, (2, 0), (), "SG_ChB2ndFreqOffset", None),
		"SG_ChBAmpl": (76, 2, (5, 0), (), "SG_ChBAmpl", None),
		"SG_ChBAmplUnit": (77, 2, (2, 0), (), "SG_ChBAmplUnit", None),
		"SG_ChBBurst2ndAmplDuration": (94, 2, (3, 0), (), "SG_ChBBurst2ndAmplDuration", None),
		"SG_ChBBurstAmplDuration": (93, 2, (3, 0), (), "SG_ChBBurstAmplDuration", None),
		"SG_ChBBurstMode": (92, 2, (2, 0), (), "SG_ChBBurstMode", None),
		"SG_ChBBurstNumPeriods": (95, 2, (3, 0), (), "SG_ChBBurstNumPeriods", None),
		"SG_ChBBurstSpacePeriod": (96, 2, (3, 0), (), "SG_ChBBurstSpacePeriod", None),
		"SG_ChBDutyCycle": (80, 2, (5, 0), (), "SG_ChBDutyCycle", None),
		"SG_ChBDutyCycleUnit": (81, 2, (2, 0), (), "SG_ChBDutyCycleUnit", None),
		"SG_ChBFreq": (78, 2, (5, 0), (), "SG_ChBFreq", None),
		"SG_ChBFreqUnit": (79, 2, (2, 0), (), "SG_ChBFreqUnit", None),
		"SG_ChBFunction": (75, 2, (2, 0), (), "SG_ChBFunction", None),
		"SG_ChBLog": (99, 2, (11, 0), (), "SG_ChBLog", None),
		"SG_ChBMLSLength": (89, 2, (2, 0), (), "SG_ChBMLSLength", None),
		"SG_ChBNumSamples": (100, 2, (3, 0), (), "SG_ChBNumSamples", None),
		"SG_ChBOn": (72, 2, (11, 0), (), "SG_ChBOn", None),
		"SG_ChBPhaseInvert": (73, 2, (11, 0), (), "SG_ChBPhaseInvert", None),
		"SG_ChBPhaseInvertTied": (74, 2, (11, 0), (), "SG_ChBPhaseInvertTied", None),
		"SG_ChBPhases": (106, 2, (2, 0), (), "SG_ChBPhases", None),
		"SG_ChBPink": (105, 2, (11, 0), (), "SG_ChBPink", None),
		"SG_ChBPolarity": (82, 2, (2, 0), (), "SG_ChBPolarity", None),
		"SG_ChBPulseNumMarks": (90, 2, (2, 0), (), "SG_ChBPulseNumMarks", None),
		"SG_ChBPulseSpacePeriod": (91, 2, (3, 0), (), "SG_ChBPulseSpacePeriod", None),
		"SG_ChBRampDown": (103, 2, (5, 0), (), "SG_ChBRampDown", None),
		"SG_ChBRampUp": (102, 2, (5, 0), (), "SG_ChBRampUp", None),
		"SG_ChBRefAmpl": (109, 2, (5, 0), (), "SG_ChBRefAmpl", None),
		"SG_ChBStartFreq": (97, 2, (5, 0), (), "SG_ChBStartFreq", None),
		"SG_ChBStopFreq": (98, 2, (5, 0), (), "SG_ChBStopFreq", None),
		"SG_ChBSweptSineUnit": (104, 2, (2, 0), (), "SG_ChBSweptSineUnit", None),
		"SG_ChBTrailSpace": (101, 2, (5, 0), (), "SG_ChBTrailSpace", None),
		"SG_ChBUserWaveform": (83, 2, (8, 0), (), "SG_ChBUserWaveform", None),
		"SG_ChBUserWaveformRepeat": (84, 2, (2, 0), (), "SG_ChBUserWaveformRepeat", None),
		"SG_DALineUp": (133, 2, (5, 0), (), "SG_DALineUp", None),
		"SG_DALineUpUnit": (134, 2, (2, 0), (), "SG_DALineUpUnit", None),
		"SG_FREQSTEPMODE_OCTAVE": (129, 2, (2, 0), (), "SG_FREQSTEPMODE_OCTAVE", None),
		"SG_FREQSTEPMODE_OCTAVE12": (124, 2, (2, 0), (), "SG_FREQSTEPMODE_OCTAVE12", None),
		"SG_FREQSTEPMODE_OCTAVE2": (128, 2, (2, 0), (), "SG_FREQSTEPMODE_OCTAVE2", None),
		"SG_FREQSTEPMODE_OCTAVE3": (127, 2, (2, 0), (), "SG_FREQSTEPMODE_OCTAVE3", None),
		"SG_FREQSTEPMODE_OCTAVE4": (126, 2, (2, 0), (), "SG_FREQSTEPMODE_OCTAVE4", None),
		"SG_FREQSTEPMODE_OCTAVE6": (125, 2, (2, 0), (), "SG_FREQSTEPMODE_OCTAVE6", None),
		"SG_FREQSTEPMODE_OFFSET": (130, 2, (2, 0), (), "SG_FREQSTEPMODE_OFFSET", None),
		"SG_FREQSTEPMODE_RATIO": (131, 2, (2, 0), (), "SG_FREQSTEPMODE_RATIO", None),
		"SG_FUNCTION_BINCENTRES": (16, 2, (2, 0), (), "SG_FUNCTION_BINCENTRES", None),
		"SG_FUNCTION_BURST": (10, 2, (2, 0), (), "SG_FUNCTION_BURST", None),
		"SG_FUNCTION_MLS": (14, 2, (2, 0), (), "SG_FUNCTION_MLS", None),
		"SG_FUNCTION_PINKNOISE": (12, 2, (2, 0), (), "SG_FUNCTION_PINKNOISE", None),
		"SG_FUNCTION_PULSE": (13, 2, (2, 0), (), "SG_FUNCTION_PULSE", None),
		"SG_FUNCTION_RAMP": (9, 2, (2, 0), (), "SG_FUNCTION_RAMP", None),
		"SG_FUNCTION_SINE": (7, 2, (2, 0), (), "SG_FUNCTION_SINE", None),
		"SG_FUNCTION_SQUARE_ANALYTICAL": (8, 2, (2, 0), (), "SG_FUNCTION_SQUARE_ANALYTICAL", None),
		"SG_FUNCTION_SWEPTSINE": (15, 2, (2, 0), (), "SG_FUNCTION_SWEPTSINE", None),
		"SG_FUNCTION_TWINTONE": (17, 2, (2, 0), (), "SG_FUNCTION_TWINTONE", None),
		"SG_FUNCTION_USER": (18, 2, (2, 0), (), "SG_FUNCTION_USER", None),
		"SG_FUNCTION_WHITENOISE": (11, 2, (2, 0), (), "SG_FUNCTION_WHITENOISE", None),
		"SG_FreqStep": (132, 2, (5, 0), (), "SG_FreqStep", None),
		"SG_FreqStepMode": (123, 2, (2, 0), (), "SG_FreqStepMode", None),
		"SG_GENMODE_SPLIT": (3, 2, (2, 0), (), "SG_GENMODE_SPLIT", None),
		"SG_GENMODE_TIED": (2, 2, (2, 0), (), "SG_GENMODE_TIED", None),
		"SG_Gain": (114, 2, (5, 0), (), "SG_Gain", None),
		"SG_GainUnit": (115, 2, (2, 0), (), "SG_GainUnit", None),
		"SG_GenMode": (1, 2, (2, 0), (), "SG_GenMode", None),
		"SG_NUMSAMPLES_128K": (62, 2, (3, 0), (), "SG_NUMSAMPLES_128K", None),
		"SG_NUMSAMPLES_16K": (59, 2, (3, 0), (), "SG_NUMSAMPLES_16K", None),
		"SG_NUMSAMPLES_1K": (55, 2, (3, 0), (), "SG_NUMSAMPLES_1K", None),
		"SG_NUMSAMPLES_256K": (63, 2, (3, 0), (), "SG_NUMSAMPLES_256K", None),
		"SG_NUMSAMPLES_2K": (56, 2, (3, 0), (), "SG_NUMSAMPLES_2K", None),
		"SG_NUMSAMPLES_32K": (60, 2, (3, 0), (), "SG_NUMSAMPLES_32K", None),
		"SG_NUMSAMPLES_4K": (57, 2, (3, 0), (), "SG_NUMSAMPLES_4K", None),
		"SG_NUMSAMPLES_64K": (61, 2, (3, 0), (), "SG_NUMSAMPLES_64K", None),
		"SG_NUMSAMPLES_8K": (58, 2, (3, 0), (), "SG_NUMSAMPLES_8K", None),
		"SG_PHASES_NEWMAN": (71, 2, (3, 0), (), "SG_PHASES_NEWMAN", None),
		"SG_PHASES_RANDOM": (70, 2, (3, 0), (), "SG_PHASES_RANDOM", None),
		"SG_POLARITY_BOTH": (27, 2, (2, 0), (), "SG_POLARITY_BOTH", None),
		"SG_POLARITY_NEG": (26, 2, (2, 0), (), "SG_POLARITY_NEG", None),
		"SG_POLARITY_POS": (28, 2, (2, 0), (), "SG_POLARITY_POS", None),
		"SG_RefAmpl": (107, 2, (5, 0), (), "SG_RefAmpl", None),
		"SG_RefAmplTied": (110, 2, (11, 0), (), "SG_RefAmplTied", None),
		"SG_RefAmplUnit": (111, 2, (2, 0), (), "SG_RefAmplUnit", None),
		"SG_RefFreq": (112, 2, (5, 0), (), "SG_RefFreq", None),
		"SG_RefImpedance": (113, 2, (5, 0), (), "SG_RefImpedance", None),
		"SG_SPLRef": (117, 2, (5, 0), (), "SG_SPLRef", None),
		"SG_SPLRefUnit": (118, 2, (2, 0), (), "SG_SPLRefUnit", None),
		"SG_dBSPLValue": (116, 2, (5, 0), (), "SG_dBSPLValue", None),
	}
	_prop_map_put_ = {
		"SG_2NDAMPLOFFSET_ABS" : ((37, LCID, 4, 0),()),
		"SG_2NDAMPLOFFSET_OFFSET" : ((38, LCID, 4, 0),()),
		"SG_2NDAMPLOFFSET_RATIO" : ((39, LCID, 4, 0),()),
		"SG_2NDFREQOFFSET_ABS" : ((32, LCID, 4, 0),()),
		"SG_2NDFREQOFFSET_OFFSET" : ((33, LCID, 4, 0),()),
		"SG_2NDFREQOFFSET_RATIO" : ((34, LCID, 4, 0),()),
		"SG_AMPLSTEPMODE_OFFSET" : ((120, LCID, 4, 0),()),
		"SG_AMPLSTEPMODE_RATIO" : ((121, LCID, 4, 0),()),
		"SG_AmplStep" : ((122, LCID, 4, 0),()),
		"SG_AmplStepMode" : ((119, LCID, 4, 0),()),
		"SG_BURSTMODE_NUMPERIODS" : ((45, LCID, 4, 0),()),
		"SG_BURSTMODE_TIMEPERIOD" : ((46, LCID, 4, 0),()),
		"SG_ChA2ndAmpl" : ((40, LCID, 4, 0),()),
		"SG_ChA2ndAmplOffset" : ((36, LCID, 4, 0),()),
		"SG_ChA2ndFreq" : ((35, LCID, 4, 0),()),
		"SG_ChA2ndFreqOffset" : ((31, LCID, 4, 0),()),
		"SG_ChAAmpl" : ((19, LCID, 4, 0),()),
		"SG_ChAAmplUnit" : ((20, LCID, 4, 0),()),
		"SG_ChABurst2ndAmplDuration" : ((48, LCID, 4, 0),()),
		"SG_ChABurstAmplDuration" : ((47, LCID, 4, 0),()),
		"SG_ChABurstMode" : ((44, LCID, 4, 0),()),
		"SG_ChABurstNumPeriods" : ((49, LCID, 4, 0),()),
		"SG_ChABurstSpacePeriod" : ((50, LCID, 4, 0),()),
		"SG_ChADutyCycle" : ((23, LCID, 4, 0),()),
		"SG_ChADutyCycleUnit" : ((24, LCID, 4, 0),()),
		"SG_ChAFreq" : ((21, LCID, 4, 0),()),
		"SG_ChAFreqUnit" : ((22, LCID, 4, 0),()),
		"SG_ChAFunction" : ((6, LCID, 4, 0),()),
		"SG_ChALog" : ((53, LCID, 4, 0),()),
		"SG_ChAMLSLength" : ((41, LCID, 4, 0),()),
		"SG_ChANumSamples" : ((54, LCID, 4, 0),()),
		"SG_ChAOn" : ((4, LCID, 4, 0),()),
		"SG_ChAPhaseInvert" : ((5, LCID, 4, 0),()),
		"SG_ChAPhases" : ((69, LCID, 4, 0),()),
		"SG_ChAPink" : ((68, LCID, 4, 0),()),
		"SG_ChAPolarity" : ((25, LCID, 4, 0),()),
		"SG_ChAPulseNumMarks" : ((42, LCID, 4, 0),()),
		"SG_ChAPulseSpacePeriod" : ((43, LCID, 4, 0),()),
		"SG_ChARampDown" : ((66, LCID, 4, 0),()),
		"SG_ChARampUp" : ((65, LCID, 4, 0),()),
		"SG_ChARefAmpl" : ((108, LCID, 4, 0),()),
		"SG_ChAStartFreq" : ((51, LCID, 4, 0),()),
		"SG_ChAStopFreq" : ((52, LCID, 4, 0),()),
		"SG_ChASweptSineUnit" : ((67, LCID, 4, 0),()),
		"SG_ChATrailSpace" : ((64, LCID, 4, 0),()),
		"SG_ChAUserWaveform" : ((29, LCID, 4, 0),()),
		"SG_ChAUserWaveformRepeat" : ((30, LCID, 4, 0),()),
		"SG_ChB2ndAmpl" : ((88, LCID, 4, 0),()),
		"SG_ChB2ndAmplOffset" : ((87, LCID, 4, 0),()),
		"SG_ChB2ndFreq" : ((86, LCID, 4, 0),()),
		"SG_ChB2ndFreqOffset" : ((85, LCID, 4, 0),()),
		"SG_ChBAmpl" : ((76, LCID, 4, 0),()),
		"SG_ChBAmplUnit" : ((77, LCID, 4, 0),()),
		"SG_ChBBurst2ndAmplDuration" : ((94, LCID, 4, 0),()),
		"SG_ChBBurstAmplDuration" : ((93, LCID, 4, 0),()),
		"SG_ChBBurstMode" : ((92, LCID, 4, 0),()),
		"SG_ChBBurstNumPeriods" : ((95, LCID, 4, 0),()),
		"SG_ChBBurstSpacePeriod" : ((96, LCID, 4, 0),()),
		"SG_ChBDutyCycle" : ((80, LCID, 4, 0),()),
		"SG_ChBDutyCycleUnit" : ((81, LCID, 4, 0),()),
		"SG_ChBFreq" : ((78, LCID, 4, 0),()),
		"SG_ChBFreqUnit" : ((79, LCID, 4, 0),()),
		"SG_ChBFunction" : ((75, LCID, 4, 0),()),
		"SG_ChBLog" : ((99, LCID, 4, 0),()),
		"SG_ChBMLSLength" : ((89, LCID, 4, 0),()),
		"SG_ChBNumSamples" : ((100, LCID, 4, 0),()),
		"SG_ChBOn" : ((72, LCID, 4, 0),()),
		"SG_ChBPhaseInvert" : ((73, LCID, 4, 0),()),
		"SG_ChBPhaseInvertTied" : ((74, LCID, 4, 0),()),
		"SG_ChBPhases" : ((106, LCID, 4, 0),()),
		"SG_ChBPink" : ((105, LCID, 4, 0),()),
		"SG_ChBPolarity" : ((82, LCID, 4, 0),()),
		"SG_ChBPulseNumMarks" : ((90, LCID, 4, 0),()),
		"SG_ChBPulseSpacePeriod" : ((91, LCID, 4, 0),()),
		"SG_ChBRampDown" : ((103, LCID, 4, 0),()),
		"SG_ChBRampUp" : ((102, LCID, 4, 0),()),
		"SG_ChBRefAmpl" : ((109, LCID, 4, 0),()),
		"SG_ChBStartFreq" : ((97, LCID, 4, 0),()),
		"SG_ChBStopFreq" : ((98, LCID, 4, 0),()),
		"SG_ChBSweptSineUnit" : ((104, LCID, 4, 0),()),
		"SG_ChBTrailSpace" : ((101, LCID, 4, 0),()),
		"SG_ChBUserWaveform" : ((83, LCID, 4, 0),()),
		"SG_ChBUserWaveformRepeat" : ((84, LCID, 4, 0),()),
		"SG_DALineUp" : ((133, LCID, 4, 0),()),
		"SG_DALineUpUnit" : ((134, LCID, 4, 0),()),
		"SG_FREQSTEPMODE_OCTAVE" : ((129, LCID, 4, 0),()),
		"SG_FREQSTEPMODE_OCTAVE12" : ((124, LCID, 4, 0),()),
		"SG_FREQSTEPMODE_OCTAVE2" : ((128, LCID, 4, 0),()),
		"SG_FREQSTEPMODE_OCTAVE3" : ((127, LCID, 4, 0),()),
		"SG_FREQSTEPMODE_OCTAVE4" : ((126, LCID, 4, 0),()),
		"SG_FREQSTEPMODE_OCTAVE6" : ((125, LCID, 4, 0),()),
		"SG_FREQSTEPMODE_OFFSET" : ((130, LCID, 4, 0),()),
		"SG_FREQSTEPMODE_RATIO" : ((131, LCID, 4, 0),()),
		"SG_FUNCTION_BINCENTRES" : ((16, LCID, 4, 0),()),
		"SG_FUNCTION_BURST" : ((10, LCID, 4, 0),()),
		"SG_FUNCTION_MLS" : ((14, LCID, 4, 0),()),
		"SG_FUNCTION_PINKNOISE" : ((12, LCID, 4, 0),()),
		"SG_FUNCTION_PULSE" : ((13, LCID, 4, 0),()),
		"SG_FUNCTION_RAMP" : ((9, LCID, 4, 0),()),
		"SG_FUNCTION_SINE" : ((7, LCID, 4, 0),()),
		"SG_FUNCTION_SQUARE_ANALYTICAL" : ((8, LCID, 4, 0),()),
		"SG_FUNCTION_SWEPTSINE" : ((15, LCID, 4, 0),()),
		"SG_FUNCTION_TWINTONE" : ((17, LCID, 4, 0),()),
		"SG_FUNCTION_USER" : ((18, LCID, 4, 0),()),
		"SG_FUNCTION_WHITENOISE" : ((11, LCID, 4, 0),()),
		"SG_FreqStep" : ((132, LCID, 4, 0),()),
		"SG_FreqStepMode" : ((123, LCID, 4, 0),()),
		"SG_GENMODE_SPLIT" : ((3, LCID, 4, 0),()),
		"SG_GENMODE_TIED" : ((2, LCID, 4, 0),()),
		"SG_Gain" : ((114, LCID, 4, 0),()),
		"SG_GainUnit" : ((115, LCID, 4, 0),()),
		"SG_GenMode" : ((1, LCID, 4, 0),()),
		"SG_NUMSAMPLES_128K" : ((62, LCID, 4, 0),()),
		"SG_NUMSAMPLES_16K" : ((59, LCID, 4, 0),()),
		"SG_NUMSAMPLES_1K" : ((55, LCID, 4, 0),()),
		"SG_NUMSAMPLES_256K" : ((63, LCID, 4, 0),()),
		"SG_NUMSAMPLES_2K" : ((56, LCID, 4, 0),()),
		"SG_NUMSAMPLES_32K" : ((60, LCID, 4, 0),()),
		"SG_NUMSAMPLES_4K" : ((57, LCID, 4, 0),()),
		"SG_NUMSAMPLES_64K" : ((61, LCID, 4, 0),()),
		"SG_NUMSAMPLES_8K" : ((58, LCID, 4, 0),()),
		"SG_PHASES_NEWMAN" : ((71, LCID, 4, 0),()),
		"SG_PHASES_RANDOM" : ((70, LCID, 4, 0),()),
		"SG_POLARITY_BOTH" : ((27, LCID, 4, 0),()),
		"SG_POLARITY_NEG" : ((26, LCID, 4, 0),()),
		"SG_POLARITY_POS" : ((28, LCID, 4, 0),()),
		"SG_RefAmpl" : ((107, LCID, 4, 0),()),
		"SG_RefAmplTied" : ((110, LCID, 4, 0),()),
		"SG_RefAmplUnit" : ((111, LCID, 4, 0),()),
		"SG_RefFreq" : ((112, LCID, 4, 0),()),
		"SG_RefImpedance" : ((113, LCID, 4, 0),()),
		"SG_SPLRef" : ((117, LCID, 4, 0),()),
		"SG_SPLRefUnit" : ((118, LCID, 4, 0),()),
		"SG_dBSPLValue" : ((116, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISoundcardInputs(DispatchBaseClass):
	CLSID = IID('{3361DF2F-D9BC-4C5D-9898-FAE3BFF8A42F}')
	coclass_clsid = IID('{DDB7596A-1605-4B32-8CA9-161640A3A2D5}')

	_prop_map_get_ = {
		"SI_ASIOSoundcard": (3, 2, (8, 0), (), "SI_ASIOSoundcard", None),
		"SI_BypassACM": (7, 2, (11, 0), (), "SI_BypassACM", None),
		"SI_ChannelA": (8, 2, (2, 0), (), "SI_ChannelA", None),
		"SI_ChannelB": (9, 2, (2, 0), (), "SI_ChannelB", None),
		"SI_NoInput": (10, 2, (2, 0), (), "SI_NoInput", None),
		"SI_SampleRate": (5, 2, (3, 0), (), "SI_SampleRate", None),
		"SI_Soundcard": (4, 2, (8, 0), (), "SI_Soundcard", None),
		"SI_UseWDM": (1, 2, (11, 0), (), "SI_UseWDM", None),
		"SI_WDMSoundcard": (2, 2, (8, 0), (), "SI_WDMSoundcard", None),
		"SI_Wordlength": (6, 2, (2, 0), (), "SI_Wordlength", None),
	}
	_prop_map_put_ = {
		"SI_ASIOSoundcard" : ((3, LCID, 4, 0),()),
		"SI_BypassACM" : ((7, LCID, 4, 0),()),
		"SI_ChannelA" : ((8, LCID, 4, 0),()),
		"SI_ChannelB" : ((9, LCID, 4, 0),()),
		"SI_NoInput" : ((10, LCID, 4, 0),()),
		"SI_SampleRate" : ((5, LCID, 4, 0),()),
		"SI_Soundcard" : ((4, LCID, 4, 0),()),
		"SI_UseWDM" : ((1, LCID, 4, 0),()),
		"SI_WDMSoundcard" : ((2, LCID, 4, 0),()),
		"SI_Wordlength" : ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISoundcardOutputs(DispatchBaseClass):
	CLSID = IID('{49EDD76B-5B81-4494-AD07-EDEB49287493}')
	coclass_clsid = IID('{47E31141-03D5-4EB9-8E3B-6FD62829A010}')

	def SO_GetChannel(self, sDevChannel=defaultNamedNotOptArg):
		'SO_GetChannel'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (2, 0), ((2, 0),),sDevChannel
			)

	def SO_SetChannel(self, sDevChannel=defaultNamedNotOptArg, sGenChannel=defaultNamedNotOptArg):
		'SO_SetChannel'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), ((2, 0), (2, 0)),sDevChannel
			, sGenChannel)

	_prop_map_get_ = {
		"SO_ASIOSoundcard": (3, 2, (8, 0), (), "SO_ASIOSoundcard", None),
		"SO_BypassACM": (7, 2, (11, 0), (), "SO_BypassACM", None),
		"SO_DEVCHANNEL_ALL": (14, 2, (2, 0), (), "SO_DEVCHANNEL_ALL", None),
		"SO_DITHERING_UNDITHERED": (12, 2, (2, 0), (), "SO_DITHERING_UNDITHERED", None),
		"SO_DITHERING_WHITE": (13, 2, (2, 0), (), "SO_DITHERING_WHITE", None),
		"SO_Dithering": (11, 2, (11, 0), (), "SO_Dithering", None),
		"SO_GENCHANNEL_A": (16, 2, (2, 0), (), "SO_GENCHANNEL_A", None),
		"SO_GENCHANNEL_B": (17, 2, (2, 0), (), "SO_GENCHANNEL_B", None),
		"SO_GENCHANNEL_MUTED": (15, 2, (2, 0), (), "SO_GENCHANNEL_MUTED", None),
		"SO_GENCHANNEL_STEREO": (18, 2, (2, 0), (), "SO_GENCHANNEL_STEREO", None),
		"SO_Mute": (8, 2, (11, 0), (), "SO_Mute", None),
		"SO_MuteChA": (9, 2, (11, 0), (), "SO_MuteChA", None),
		"SO_MuteChB": (10, 2, (11, 0), (), "SO_MuteChB", None),
		"SO_SampleRate": (5, 2, (3, 0), (), "SO_SampleRate", None),
		"SO_Soundcard": (4, 2, (8, 0), (), "SO_Soundcard", None),
		"SO_UseWDM": (1, 2, (11, 0), (), "SO_UseWDM", None),
		"SO_WDMSoundcard": (2, 2, (8, 0), (), "SO_WDMSoundcard", None),
		"SO_Wordlength": (6, 2, (2, 0), (), "SO_Wordlength", None),
	}
	_prop_map_put_ = {
		"SO_ASIOSoundcard" : ((3, LCID, 4, 0),()),
		"SO_BypassACM" : ((7, LCID, 4, 0),()),
		"SO_DEVCHANNEL_ALL" : ((14, LCID, 4, 0),()),
		"SO_DITHERING_UNDITHERED" : ((12, LCID, 4, 0),()),
		"SO_DITHERING_WHITE" : ((13, LCID, 4, 0),()),
		"SO_Dithering" : ((11, LCID, 4, 0),()),
		"SO_GENCHANNEL_A" : ((16, LCID, 4, 0),()),
		"SO_GENCHANNEL_B" : ((17, LCID, 4, 0),()),
		"SO_GENCHANNEL_MUTED" : ((15, LCID, 4, 0),()),
		"SO_GENCHANNEL_STEREO" : ((18, LCID, 4, 0),()),
		"SO_Mute" : ((8, LCID, 4, 0),()),
		"SO_MuteChA" : ((9, LCID, 4, 0),()),
		"SO_MuteChB" : ((10, LCID, 4, 0),()),
		"SO_SampleRate" : ((5, LCID, 4, 0),()),
		"SO_Soundcard" : ((4, LCID, 4, 0),()),
		"SO_UseWDM" : ((1, LCID, 4, 0),()),
		"SO_WDMSoundcard" : ((2, LCID, 4, 0),()),
		"SO_Wordlength" : ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISweep(DispatchBaseClass):
	CLSID = IID('{2787A930-AC57-11D2-91DE-00AA0011AF6D}')
	coclass_clsid = IID('{2787A932-AC57-11D2-91DE-00AA0011AF6D}')

	def SW_GetYRange(self, sResult=defaultNamedNotOptArg, dMinValue=defaultNamedNotOptArg, dMaxValue=defaultNamedNotOptArg):
		'SW_GetYRange'
		return self._oleobj_.InvokeTypes(112, LCID, 1, (11, 0), ((2, 0), (16396, 0), (16396, 0)),sResult
			, dMinValue, dMaxValue)

	def SW_GetYUnit(self, sResult=defaultNamedNotOptArg):
		'SW_GetYUnit'
		return self._oleobj_.InvokeTypes(111, LCID, 1, (2, 0), ((2, 0),),sResult
			)

	def SW_Go(self):
		'SW_Go'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), (),)

	def SW_IsSweepFinished(self):
		'SW_IsSweepFinished'
		return self._oleobj_.InvokeTypes(108, LCID, 1, (11, 0), (),)

	def SW_MaxLimitBreached(self, sTraceType=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg):
		'SW_MaxLimitBreached'
		return self._oleobj_.InvokeTypes(110, LCID, 1, (11, 0), ((2, 0), (2, 0)),sTraceType
			, sChannel)

	def SW_MinLimitBreached(self, sTraceType=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg):
		'SW_MinLimitBreached'
		return self._oleobj_.InvokeTypes(109, LCID, 1, (11, 0), ((2, 0), (2, 0)),sTraceType
			, sChannel)

	def SW_Pause(self):
		'SW_Pause'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (24, 0), (),)

	def SW_ResetYDefaults(self, sResult=defaultNamedNotOptArg):
		'SW_ResetYDefaults'
		return self._oleobj_.InvokeTypes(118, LCID, 1, (11, 0), ((2, 0),),sResult
			)

	def SW_SetMaxLimit(self, sResult=defaultNamedNotOptArg, strLimitFile=defaultNamedNotOptArg):
		'SW_SetMaxLimit'
		return self._oleobj_.InvokeTypes(116, LCID, 1, (11, 0), ((2, 0), (8, 0)),sResult
			, strLimitFile)

	def SW_SetMinLimit(self, sResult=defaultNamedNotOptArg, strLimitFile=defaultNamedNotOptArg):
		'SW_SetMinLimit'
		return self._oleobj_.InvokeTypes(117, LCID, 1, (11, 0), ((2, 0), (8, 0)),sResult
			, strLimitFile)

	def SW_SetXAxisFFTDetector(self, sDetectorID=defaultNamedNotOptArg):
		'SW_SetXAxisFFTDetector'
		return self._oleobj_.InvokeTypes(120, LCID, 1, (11, 0), ((2, 0),),sDetectorID
			)

	def SW_SetXAxisResult(self, sResult=defaultNamedNotOptArg):
		'SW_SetXAxisResult'
		return self._oleobj_.InvokeTypes(119, LCID, 1, (11, 0), ((2, 0),),sResult
			)

	def SW_SetXIntervals(self, sNumIntervals=defaultNamedNotOptArg, bLog=defaultNamedNotOptArg):
		'SW_SetXIntervals'
		return self._oleobj_.InvokeTypes(123, LCID, 1, (11, 0), ((2, 0), (11, 0)),sNumIntervals
			, bLog)

	def SW_SetXRange(self, dMinValue=defaultNamedNotOptArg, dMaxValue=defaultNamedNotOptArg):
		'SW_SetXRange'
		return self._oleobj_.InvokeTypes(122, LCID, 1, (11, 0), ((5, 0), (5, 0)),dMinValue
			, dMaxValue)

	def SW_SetXUnit(self, sUnit=defaultNamedNotOptArg):
		'SW_SetXUnit'
		return self._oleobj_.InvokeTypes(121, LCID, 1, (11, 0), ((2, 0),),sUnit
			)

	def SW_SetYIntervals(self, sResult=defaultNamedNotOptArg, sNumIntervals=defaultNamedNotOptArg, bLog=defaultNamedNotOptArg):
		'SW_SetYIntervals'
		return self._oleobj_.InvokeTypes(115, LCID, 1, (11, 0), ((2, 0), (2, 0), (11, 0)),sResult
			, sNumIntervals, bLog)

	def SW_SetYRange(self, sResult=defaultNamedNotOptArg, dMinValue=defaultNamedNotOptArg, dMaxValue=defaultNamedNotOptArg):
		'SW_SetYRange'
		return self._oleobj_.InvokeTypes(114, LCID, 1, (11, 0), ((2, 0), (5, 0), (5, 0)),sResult
			, dMinValue, dMaxValue)

	def SW_SetYUnit(self, sResult=defaultNamedNotOptArg, sUnit=defaultNamedNotOptArg):
		'SW_SetYUnit'
		return self._oleobj_.InvokeTypes(113, LCID, 1, (11, 0), ((2, 0), (2, 0)),sResult
			, sUnit)

	def SW_SingleStep(self):
		'SW_SingleStep'
		return self._oleobj_.InvokeTypes(107, LCID, 1, (24, 0), (),)

	def SW_Stop(self):
		'SW_Stop'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"RESULT_CTD_CHA": (31, 2, (2, 0), (), "RESULT_CTD_CHA", None),
		"RESULT_CTD_CHB": (32, 2, (2, 0), (), "RESULT_CTD_CHB", None),
		"RESULT_CTD_NONSEL": (34, 2, (2, 0), (), "RESULT_CTD_NONSEL", None),
		"RESULT_CTD_SEL": (33, 2, (2, 0), (), "RESULT_CTD_SEL", None),
		"RESULT_CTD_UNSEL": (35, 2, (2, 0), (), "RESULT_CTD_UNSEL", None),
		"RESULT_DIC_AMPL": (17, 2, (2, 0), (), "RESULT_DIC_AMPL", None),
		"RESULT_DIC_JITTERAMPL": (18, 2, (2, 0), (), "RESULT_DIC_JITTERAMPL", None),
		"RESULT_DIC_PHASE": (19, 2, (2, 0), (), "RESULT_DIC_PHASE", None),
		"RESULT_DI_FRAMERATE": (15, 2, (2, 0), (), "RESULT_DI_FRAMERATE", None),
		"RESULT_DI_FRAMERATEDEVIATION": (16, 2, (2, 0), (), "RESULT_DI_FRAMERATEDEVIATION", None),
		"RESULT_DO_REFSYNCFRAMERATE": (13, 2, (2, 0), (), "RESULT_DO_REFSYNCFRAMERATE", None),
		"RESULT_DO_REFSYNCFRAMERATEDEVIATION": (14, 2, (2, 0), (), "RESULT_DO_REFSYNCFRAMERATEDEVIATION", None),
		"RESULT_FFTD_CHA": (36, 2, (2, 0), (), "RESULT_FFTD_CHA", None),
		"RESULT_FFTD_CHB": (37, 2, (2, 0), (), "RESULT_FFTD_CHB", None),
		"RESULT_FFTD_NONSEL": (39, 2, (2, 0), (), "RESULT_FFTD_NONSEL", None),
		"RESULT_FFTD_SEL": (38, 2, (2, 0), (), "RESULT_FFTD_SEL", None),
		"RESULT_FFTD_UNSEL": (40, 2, (2, 0), (), "RESULT_FFTD_UNSEL", None),
		"RESULT_NONE": (12, 2, (2, 0), (), "RESULT_NONE", None),
		"RESULT_SA_FREQ_CHA": (25, 2, (2, 0), (), "RESULT_SA_FREQ_CHA", None),
		"RESULT_SA_FREQ_CHB": (26, 2, (2, 0), (), "RESULT_SA_FREQ_CHB", None),
		"RESULT_SA_FREQ_NONSEL": (28, 2, (2, 0), (), "RESULT_SA_FREQ_NONSEL", None),
		"RESULT_SA_FREQ_SEL": (27, 2, (2, 0), (), "RESULT_SA_FREQ_SEL", None),
		"RESULT_SA_FREQ_UNSEL": (29, 2, (2, 0), (), "RESULT_SA_FREQ_UNSEL", None),
		"RESULT_SA_PHASE": (30, 2, (2, 0), (), "RESULT_SA_PHASE", None),
		"RESULT_SA_RMSAMPL_CHA": (20, 2, (2, 0), (), "RESULT_SA_RMSAMPL_CHA", None),
		"RESULT_SA_RMSAMPL_CHB": (21, 2, (2, 0), (), "RESULT_SA_RMSAMPL_CHB", None),
		"RESULT_SA_RMSAMPL_NONSEL": (23, 2, (2, 0), (), "RESULT_SA_RMSAMPL_NONSEL", None),
		"RESULT_SA_RMSAMPL_SEL": (22, 2, (2, 0), (), "RESULT_SA_RMSAMPL_SEL", None),
		"RESULT_SA_RMSAMPL_UNSEL": (24, 2, (2, 0), (), "RESULT_SA_RMSAMPL_UNSEL", None),
		"SW_AUTOZOOM_END": (44, 2, (2, 0), (), "SW_AUTOZOOM_END", None),
		"SW_AUTOZOOM_NONE": (42, 2, (2, 0), (), "SW_AUTOZOOM_NONE", None),
		"SW_AUTOZOOM_STEP": (43, 2, (2, 0), (), "SW_AUTOZOOM_STEP", None),
		"SW_AlarmOn": (3, 2, (11, 0), (), "SW_AlarmOn", None),
		"SW_Append": (1, 2, (11, 0), (), "SW_Append", None),
		"SW_CHANNELARRAYMODE_OFF": (89, 2, (2, 0), (), "SW_CHANNELARRAYMODE_OFF", None),
		"SW_CHANNELARRAYMODE_ON": (88, 2, (2, 0), (), "SW_CHANNELARRAYMODE_ON", None),
		"SW_ChannelArray": (84, 2, (8, 0), (), "SW_ChannelArray", None),
		"SW_ChannelArrayMode": (87, 2, (2, 0), (), "SW_ChannelArrayMode", None),
		"SW_CurrentStep": (99, 2, (2, 0), (), "SW_CurrentStep", None),
		"SW_DataTable": (83, 2, (8, 0), (), "SW_DataTable", None),
		"SW_EndChannel": (86, 2, (2, 0), (), "SW_EndChannel", None),
		"SW_Factor": (73, 2, (5, 0), (), "SW_Factor", None),
		"SW_INTERVAL_LINEAR": (70, 2, (2, 0), (), "SW_INTERVAL_LINEAR", None),
		"SW_INTERVAL_LOG": (71, 2, (2, 0), (), "SW_INTERVAL_LOG", None),
		"SW_Interval": (69, 2, (2, 0), (), "SW_Interval", None),
		"SW_NumSteps": (90, 2, (2, 0), (), "SW_NumSteps", None),
		"SW_Offset": (72, 2, (5, 0), (), "SW_Offset", None),
		"SW_OptimizeForSpeed": (2, 2, (11, 0), (), "SW_OptimizeForSpeed", None),
		"SW_RUNSCRIPTWHEN_AFTERREGULATION": (97, 2, (2, 0), (), "SW_RUNSCRIPTWHEN_AFTERREGULATION", None),
		"SW_RUNSCRIPTWHEN_AFTERSOURCE": (96, 2, (2, 0), (), "SW_RUNSCRIPTWHEN_AFTERSOURCE", None),
		"SW_RUNSCRIPTWHEN_ATEND": (98, 2, (2, 0), (), "SW_RUNSCRIPTWHEN_ATEND", None),
		"SW_RUNSCRIPTWHEN_ATSTART": (95, 2, (2, 0), (), "SW_RUNSCRIPTWHEN_ATSTART", None),
		"SW_Regulate": (91, 2, (11, 0), (), "SW_Regulate", None),
		"SW_Result1": (4, 2, (2, 0), (), "SW_Result1", None),
		"SW_Result1FFTDetector": (5, 2, (2, 0), (), "SW_Result1FFTDetector", None),
		"SW_Result2": (6, 2, (2, 0), (), "SW_Result2", None),
		"SW_Result2FFTDetector": (7, 2, (2, 0), (), "SW_Result2FFTDetector", None),
		"SW_Result3": (8, 2, (2, 0), (), "SW_Result3", None),
		"SW_Result3FFTDetector": (9, 2, (2, 0), (), "SW_Result3FFTDetector", None),
		"SW_Result4": (10, 2, (2, 0), (), "SW_Result4", None),
		"SW_Result4FFTDetector": (11, 2, (2, 0), (), "SW_Result4FFTDetector", None),
		"SW_RunScript": (92, 2, (11, 0), (), "SW_RunScript", None),
		"SW_RunScriptWhen": (94, 2, (2, 0), (), "SW_RunScriptWhen", None),
		"SW_SENSETYPE_FACTOR": (76, 2, (2, 0), (), "SW_SENSETYPE_FACTOR", None),
		"SW_SENSETYPE_OFFSET": (75, 2, (2, 0), (), "SW_SENSETYPE_OFFSET", None),
		"SW_SOURCETAB_INNER": (102, 2, (2, 0), (), "SW_SOURCETAB_INNER", None),
		"SW_SOURCETAB_OUTER": (103, 2, (2, 0), (), "SW_SOURCETAB_OUTER", None),
		"SW_SOURCE_CHANNELARRAY": (65, 2, (2, 0), (), "SW_SOURCE_CHANNELARRAY", None),
		"SW_SOURCE_CTD_BPBRFREQ": (56, 2, (2, 0), (), "SW_SOURCE_CTD_BPBRFREQ", None),
		"SW_SOURCE_DATATABLE": (63, 2, (2, 0), (), "SW_SOURCE_DATATABLE", None),
		"SW_SOURCE_DCOFFSET": (53, 2, (2, 0), (), "SW_SOURCE_DCOFFSET", None),
		"SW_SOURCE_FFTD_BPBRFREQ": (57, 2, (2, 0), (), "SW_SOURCE_FFTD_BPBRFREQ", None),
		"SW_SOURCE_GENAMPL_BOTH": (52, 2, (2, 0), (), "SW_SOURCE_GENAMPL_BOTH", None),
		"SW_SOURCE_GENAMPL_CHA": (50, 2, (2, 0), (), "SW_SOURCE_GENAMPL_CHA", None),
		"SW_SOURCE_GENAMPL_CHB": (51, 2, (2, 0), (), "SW_SOURCE_GENAMPL_CHB", None),
		"SW_SOURCE_GENFREQ_BOTH": (49, 2, (2, 0), (), "SW_SOURCE_GENFREQ_BOTH", None),
		"SW_SOURCE_GENFREQ_CHA": (47, 2, (2, 0), (), "SW_SOURCE_GENFREQ_CHA", None),
		"SW_SOURCE_GENFREQ_CHB": (48, 2, (2, 0), (), "SW_SOURCE_GENFREQ_CHB", None),
		"SW_SOURCE_JITTERAMPL": (55, 2, (2, 0), (), "SW_SOURCE_JITTERAMPL", None),
		"SW_SOURCE_JITTERFREQ": (54, 2, (2, 0), (), "SW_SOURCE_JITTERFREQ", None),
		"SW_SOURCE_MANUAL": (64, 2, (2, 0), (), "SW_SOURCE_MANUAL", None),
		"SW_SOURCE_NONE": (46, 2, (2, 0), (), "SW_SOURCE_NONE", None),
		"SW_SOURCE_SENSEAMPL_CHA": (60, 2, (2, 0), (), "SW_SOURCE_SENSEAMPL_CHA", None),
		"SW_SOURCE_SENSEAMPL_CHB": (61, 2, (2, 0), (), "SW_SOURCE_SENSEAMPL_CHB", None),
		"SW_SOURCE_SENSEFREQ_CHA": (58, 2, (2, 0), (), "SW_SOURCE_SENSEFREQ_CHA", None),
		"SW_SOURCE_SENSEFREQ_CHB": (59, 2, (2, 0), (), "SW_SOURCE_SENSEFREQ_CHB", None),
		"SW_SOURCE_TIME": (62, 2, (2, 0), (), "SW_SOURCE_TIME", None),
		"SW_Script": (93, 2, (8, 0), (), "SW_Script", None),
		"SW_SenseEndValue": (79, 2, (5, 0), (), "SW_SenseEndValue", None),
		"SW_SenseInterval": (77, 2, (5, 0), (), "SW_SenseInterval", None),
		"SW_SenseThreshold": (80, 2, (5, 0), (), "SW_SenseThreshold", None),
		"SW_SenseThresholdUnit": (81, 2, (2, 0), (), "SW_SenseThresholdUnit", None),
		"SW_SenseType": (74, 2, (2, 0), (), "SW_SenseType", None),
		"SW_SenseUnit": (78, 2, (2, 0), (), "SW_SenseUnit", None),
		"SW_SourceTab": (101, 2, (2, 0), (), "SW_SourceTab", None),
		"SW_StartChannel": (85, 2, (2, 0), (), "SW_StartChannel", None),
		"SW_StartValue": (66, 2, (5, 0), (), "SW_StartValue", None),
		"SW_StopValue": (67, 2, (5, 0), (), "SW_StopValue", None),
		"SW_SweepSource": (45, 2, (2, 0), (), "SW_SweepSource", None),
		"SW_TimeInterval": (82, 2, (5, 0), (), "SW_TimeInterval", None),
		"SW_Unit": (68, 2, (2, 0), (), "SW_Unit", None),
		"SW_XAxisAutoZoom": (100, 2, (2, 0), (), "SW_XAxisAutoZoom", None),
		"SW_YAxisAutoZoom": (41, 2, (2, 0), (), "SW_YAxisAutoZoom", None),
	}
	_prop_map_put_ = {
		"RESULT_CTD_CHA" : ((31, LCID, 4, 0),()),
		"RESULT_CTD_CHB" : ((32, LCID, 4, 0),()),
		"RESULT_CTD_NONSEL" : ((34, LCID, 4, 0),()),
		"RESULT_CTD_SEL" : ((33, LCID, 4, 0),()),
		"RESULT_CTD_UNSEL" : ((35, LCID, 4, 0),()),
		"RESULT_DIC_AMPL" : ((17, LCID, 4, 0),()),
		"RESULT_DIC_JITTERAMPL" : ((18, LCID, 4, 0),()),
		"RESULT_DIC_PHASE" : ((19, LCID, 4, 0),()),
		"RESULT_DI_FRAMERATE" : ((15, LCID, 4, 0),()),
		"RESULT_DI_FRAMERATEDEVIATION" : ((16, LCID, 4, 0),()),
		"RESULT_DO_REFSYNCFRAMERATE" : ((13, LCID, 4, 0),()),
		"RESULT_DO_REFSYNCFRAMERATEDEVIATION" : ((14, LCID, 4, 0),()),
		"RESULT_FFTD_CHA" : ((36, LCID, 4, 0),()),
		"RESULT_FFTD_CHB" : ((37, LCID, 4, 0),()),
		"RESULT_FFTD_NONSEL" : ((39, LCID, 4, 0),()),
		"RESULT_FFTD_SEL" : ((38, LCID, 4, 0),()),
		"RESULT_FFTD_UNSEL" : ((40, LCID, 4, 0),()),
		"RESULT_NONE" : ((12, LCID, 4, 0),()),
		"RESULT_SA_FREQ_CHA" : ((25, LCID, 4, 0),()),
		"RESULT_SA_FREQ_CHB" : ((26, LCID, 4, 0),()),
		"RESULT_SA_FREQ_NONSEL" : ((28, LCID, 4, 0),()),
		"RESULT_SA_FREQ_SEL" : ((27, LCID, 4, 0),()),
		"RESULT_SA_FREQ_UNSEL" : ((29, LCID, 4, 0),()),
		"RESULT_SA_PHASE" : ((30, LCID, 4, 0),()),
		"RESULT_SA_RMSAMPL_CHA" : ((20, LCID, 4, 0),()),
		"RESULT_SA_RMSAMPL_CHB" : ((21, LCID, 4, 0),()),
		"RESULT_SA_RMSAMPL_NONSEL" : ((23, LCID, 4, 0),()),
		"RESULT_SA_RMSAMPL_SEL" : ((22, LCID, 4, 0),()),
		"RESULT_SA_RMSAMPL_UNSEL" : ((24, LCID, 4, 0),()),
		"SW_AUTOZOOM_END" : ((44, LCID, 4, 0),()),
		"SW_AUTOZOOM_NONE" : ((42, LCID, 4, 0),()),
		"SW_AUTOZOOM_STEP" : ((43, LCID, 4, 0),()),
		"SW_AlarmOn" : ((3, LCID, 4, 0),()),
		"SW_Append" : ((1, LCID, 4, 0),()),
		"SW_CHANNELARRAYMODE_OFF" : ((89, LCID, 4, 0),()),
		"SW_CHANNELARRAYMODE_ON" : ((88, LCID, 4, 0),()),
		"SW_ChannelArray" : ((84, LCID, 4, 0),()),
		"SW_ChannelArrayMode" : ((87, LCID, 4, 0),()),
		"SW_CurrentStep" : ((99, LCID, 4, 0),()),
		"SW_DataTable" : ((83, LCID, 4, 0),()),
		"SW_EndChannel" : ((86, LCID, 4, 0),()),
		"SW_Factor" : ((73, LCID, 4, 0),()),
		"SW_INTERVAL_LINEAR" : ((70, LCID, 4, 0),()),
		"SW_INTERVAL_LOG" : ((71, LCID, 4, 0),()),
		"SW_Interval" : ((69, LCID, 4, 0),()),
		"SW_NumSteps" : ((90, LCID, 4, 0),()),
		"SW_Offset" : ((72, LCID, 4, 0),()),
		"SW_OptimizeForSpeed" : ((2, LCID, 4, 0),()),
		"SW_RUNSCRIPTWHEN_AFTERREGULATION" : ((97, LCID, 4, 0),()),
		"SW_RUNSCRIPTWHEN_AFTERSOURCE" : ((96, LCID, 4, 0),()),
		"SW_RUNSCRIPTWHEN_ATEND" : ((98, LCID, 4, 0),()),
		"SW_RUNSCRIPTWHEN_ATSTART" : ((95, LCID, 4, 0),()),
		"SW_Regulate" : ((91, LCID, 4, 0),()),
		"SW_Result1" : ((4, LCID, 4, 0),()),
		"SW_Result1FFTDetector" : ((5, LCID, 4, 0),()),
		"SW_Result2" : ((6, LCID, 4, 0),()),
		"SW_Result2FFTDetector" : ((7, LCID, 4, 0),()),
		"SW_Result3" : ((8, LCID, 4, 0),()),
		"SW_Result3FFTDetector" : ((9, LCID, 4, 0),()),
		"SW_Result4" : ((10, LCID, 4, 0),()),
		"SW_Result4FFTDetector" : ((11, LCID, 4, 0),()),
		"SW_RunScript" : ((92, LCID, 4, 0),()),
		"SW_RunScriptWhen" : ((94, LCID, 4, 0),()),
		"SW_SENSETYPE_FACTOR" : ((76, LCID, 4, 0),()),
		"SW_SENSETYPE_OFFSET" : ((75, LCID, 4, 0),()),
		"SW_SOURCETAB_INNER" : ((102, LCID, 4, 0),()),
		"SW_SOURCETAB_OUTER" : ((103, LCID, 4, 0),()),
		"SW_SOURCE_CHANNELARRAY" : ((65, LCID, 4, 0),()),
		"SW_SOURCE_CTD_BPBRFREQ" : ((56, LCID, 4, 0),()),
		"SW_SOURCE_DATATABLE" : ((63, LCID, 4, 0),()),
		"SW_SOURCE_DCOFFSET" : ((53, LCID, 4, 0),()),
		"SW_SOURCE_FFTD_BPBRFREQ" : ((57, LCID, 4, 0),()),
		"SW_SOURCE_GENAMPL_BOTH" : ((52, LCID, 4, 0),()),
		"SW_SOURCE_GENAMPL_CHA" : ((50, LCID, 4, 0),()),
		"SW_SOURCE_GENAMPL_CHB" : ((51, LCID, 4, 0),()),
		"SW_SOURCE_GENFREQ_BOTH" : ((49, LCID, 4, 0),()),
		"SW_SOURCE_GENFREQ_CHA" : ((47, LCID, 4, 0),()),
		"SW_SOURCE_GENFREQ_CHB" : ((48, LCID, 4, 0),()),
		"SW_SOURCE_JITTERAMPL" : ((55, LCID, 4, 0),()),
		"SW_SOURCE_JITTERFREQ" : ((54, LCID, 4, 0),()),
		"SW_SOURCE_MANUAL" : ((64, LCID, 4, 0),()),
		"SW_SOURCE_NONE" : ((46, LCID, 4, 0),()),
		"SW_SOURCE_SENSEAMPL_CHA" : ((60, LCID, 4, 0),()),
		"SW_SOURCE_SENSEAMPL_CHB" : ((61, LCID, 4, 0),()),
		"SW_SOURCE_SENSEFREQ_CHA" : ((58, LCID, 4, 0),()),
		"SW_SOURCE_SENSEFREQ_CHB" : ((59, LCID, 4, 0),()),
		"SW_SOURCE_TIME" : ((62, LCID, 4, 0),()),
		"SW_Script" : ((93, LCID, 4, 0),()),
		"SW_SenseEndValue" : ((79, LCID, 4, 0),()),
		"SW_SenseInterval" : ((77, LCID, 4, 0),()),
		"SW_SenseThreshold" : ((80, LCID, 4, 0),()),
		"SW_SenseThresholdUnit" : ((81, LCID, 4, 0),()),
		"SW_SenseType" : ((74, LCID, 4, 0),()),
		"SW_SenseUnit" : ((78, LCID, 4, 0),()),
		"SW_SourceTab" : ((101, LCID, 4, 0),()),
		"SW_StartChannel" : ((85, LCID, 4, 0),()),
		"SW_StartValue" : ((66, LCID, 4, 0),()),
		"SW_StopValue" : ((67, LCID, 4, 0),()),
		"SW_SweepSource" : ((45, LCID, 4, 0),()),
		"SW_TimeInterval" : ((82, LCID, 4, 0),()),
		"SW_Unit" : ((68, LCID, 4, 0),()),
		"SW_XAxisAutoZoom" : ((100, LCID, 4, 0),()),
		"SW_YAxisAutoZoom" : ((41, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISwitcher(DispatchBaseClass):
	CLSID = IID('{8EF24D41-887F-4024-AB39-43844B96DDF8}')
	coclass_clsid = IID('{F565E4D0-B030-4417-8FFA-12BA9C756338}')

	def SWITCHER_AddChannel(self, strArray=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg):
		'SWITCHER_AddChannel'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((8, 0), (2, 0)),strArray
			, sChannel)

	def SWITCHER_Balance(self, strArray=defaultNamedNotOptArg, bOn=defaultNamedNotOptArg):
		'SWITCHER_Balance'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((8, 0), (11, 0)),strArray
			, bOn)

	def SWITCHER_ClearChannels(self, strArray=defaultNamedNotOptArg):
		'SWITCHER_ClearChannels'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((8, 0),),strArray
			)

	def SWITCHER_DefineArray(self, strArray=defaultNamedNotOptArg):
		'SWITCHER_DefineArray'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((8, 0),),strArray
			)

	def SWITCHER_DefineStereoArray(self, strArray=defaultNamedNotOptArg):
		'SWITCHER_DefineStereoArray'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((8, 0),),strArray
			)

	def SWITCHER_ExclusiveChannel(self, strArray=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg):
		'SWITCHER_ExclusiveChannel'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((8, 0), (2, 0)),strArray
			, sChannel)

	def SWITCHER_NotChannel(self, strArray=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg):
		'SWITCHER_NotChannel'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((8, 0), (2, 0)),strArray
			, sChannel)

	def SWITCHER_RemoveArray(self, strArray=defaultNamedNotOptArg):
		'SWITCHER_RemoveArray'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((8, 0),),strArray
			)

	def SWITCHER_RemoveChannel(self, strArray=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg):
		'SWITCHER_RemoveChannel'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((8, 0), (2, 0)),strArray
			, sChannel)

	def SWITCHER_SetAllChannels(self, strArray=defaultNamedNotOptArg):
		'SWITCHER_SetAllChannels'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((8, 0),),strArray
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrace(DispatchBaseClass):
	CLSID = IID('{FB1F67C4-5C0C-11D5-9C7E-0050046915E5}')
	coclass_clsid = IID('{FB1F67C6-5C0C-11D5-9C7E-0050046915E5}')

	def TRACE_AddMark(self, lPos=defaultNamedNotOptArg, strLabel=defaultNamedNotOptArg):
		'TRACE_AddMark'
		return self._oleobj_.InvokeTypes(50, LCID, 1, (2, 0), ((3, 0), (8, 0)),lPos
			, strLabel)

	def TRACE_AutoZoomX(self):
		'TRACE_AutoZoomX'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (24, 0), (),)

	def TRACE_AutoZoomY(self):
		'TRACE_AutoZoomY'
		return self._oleobj_.InvokeTypes(42, LCID, 1, (24, 0), (),)

	def TRACE_DefaultZoomX(self):
		'TRACE_DefaultZoomX'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (24, 0), (),)

	def TRACE_DefaultZoomY(self):
		'TRACE_DefaultZoomY'
		return self._oleobj_.InvokeTypes(43, LCID, 1, (24, 0), (),)

	def TRACE_DrawTrace(self):
		'TRACE_DrawTrace'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), (),)

	def TRACE_GetColour(self, sRed=defaultNamedNotOptArg, sGreen=defaultNamedNotOptArg, sBlue=defaultNamedNotOptArg):
		'TRACE_GetColour'
		return self._oleobj_.InvokeTypes(55, LCID, 1, (24, 0), ((16396, 0), (16396, 0), (16396, 0)),sRed
			, sGreen, sBlue)

	def TRACE_GetCursorPos(self):
		'TRACE_GetCursorPos'
		return self._oleobj_.InvokeTypes(48, LCID, 1, (3, 0), (),)

	def TRACE_GetFullXRange(self, dMinValue=defaultNamedNotOptArg, dMaxValue=defaultNamedNotOptArg):
		'TRACE_GetFullXRange'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((16396, 0), (16396, 0)),dMinValue
			, dMaxValue)

	def TRACE_GetFullYRange(self, dMinValue=defaultNamedNotOptArg, dMaxValue=defaultNamedNotOptArg):
		'TRACE_GetFullYRange'
		return self._oleobj_.InvokeTypes(39, LCID, 1, (24, 0), ((16396, 0), (16396, 0)),dMinValue
			, dMaxValue)

	def TRACE_GetMarkLabel(self, sMark=defaultNamedNotOptArg):
		'TRACE_GetMarkLabel'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(53, LCID, 1, (8, 0), ((2, 0),),sMark
			)

	def TRACE_GetMaxLimitLine(self):
		'TRACE_GetMaxLimitLine'
		return self._oleobj_.InvokeTypes(46, LCID, 1, (2, 0), (),)

	def TRACE_GetMinLimitLine(self):
		'TRACE_GetMinLimitLine'
		return self._oleobj_.InvokeTypes(47, LCID, 1, (2, 0), (),)

	def TRACE_GetNumPoints(self):
		'TRACE_GetNumPoints'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (3, 0), (),)

	def TRACE_GetXIntervals(self, sNumIntervals=defaultNamedNotOptArg, bLog=defaultNamedNotOptArg):
		'TRACE_GetXIntervals'
		return self._oleobj_.InvokeTypes(56, LCID, 1, (24, 0), ((16396, 0), (16396, 0)),sNumIntervals
			, bLog)

	def TRACE_GetXRange(self, dMinValue=defaultNamedNotOptArg, dMaxValue=defaultNamedNotOptArg):
		'TRACE_GetXRange'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), ((16396, 0), (16396, 0)),dMinValue
			, dMaxValue)

	def TRACE_GetXValueAt(self, lPos=defaultNamedNotOptArg):
		'TRACE_GetXValueAt'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (5, 0), ((3, 0),),lPos
			)

	def TRACE_GetYIntervals(self, sNumIntervals=defaultNamedNotOptArg, bLog=defaultNamedNotOptArg):
		'TRACE_GetYIntervals'
		return self._oleobj_.InvokeTypes(57, LCID, 1, (24, 0), ((16396, 0), (16396, 0)),sNumIntervals
			, bLog)

	def TRACE_GetYRange(self, dMinValue=defaultNamedNotOptArg, dMaxValue=defaultNamedNotOptArg):
		'TRACE_GetYRange'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (24, 0), ((16396, 0), (16396, 0)),dMinValue
			, dMaxValue)

	def TRACE_GetYValueAt(self, lPos=defaultNamedNotOptArg):
		'TRACE_GetYValueAt'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (5, 0), ((3, 0),),lPos
			)

	def TRACE_RemoveAllMarks(self):
		'TRACE_RemoveAllMarks'
		return self._oleobj_.InvokeTypes(54, LCID, 1, (24, 0), (),)

	def TRACE_RemoveMark(self, sMark=defaultNamedNotOptArg):
		'TRACE_RemoveMark'
		return self._oleobj_.InvokeTypes(51, LCID, 1, (11, 0), ((2, 0),),sMark
			)

	def TRACE_SaveTrace(self, strFileName=defaultNamedNotOptArg):
		'TRACE_SaveTrace'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (11, 0), ((8, 0),),strFileName
			)

	def TRACE_SetColour(self, sRed=defaultNamedNotOptArg, sGreen=defaultNamedNotOptArg, sBlue=defaultNamedNotOptArg):
		'TRACE_SetColour'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), ((2, 0), (2, 0), (2, 0)),sRed
			, sGreen, sBlue)

	def TRACE_SetCursorPos(self, lPos=defaultNamedNotOptArg):
		'TRACE_SetCursorPos'
		return self._oleobj_.InvokeTypes(49, LCID, 1, (11, 0), ((3, 0),),lPos
			)

	def TRACE_SetMarkLabel(self, sMark=defaultNamedNotOptArg, strLabel=defaultNamedNotOptArg):
		'TRACE_SetMarkLabel'
		return self._oleobj_.InvokeTypes(52, LCID, 1, (11, 0), ((2, 0), (8, 0)),sMark
			, strLabel)

	def TRACE_SetMaxLimit(self, strLimitFile=defaultNamedNotOptArg):
		'TRACE_SetMaxLimit'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (11, 0), ((8, 0),),strLimitFile
			)

	def TRACE_SetMinLimit(self, strLimitFile=defaultNamedNotOptArg):
		'TRACE_SetMinLimit'
		return self._oleobj_.InvokeTypes(45, LCID, 1, (11, 0), ((8, 0),),strLimitFile
			)

	def TRACE_SetPoint(self, lPos=defaultNamedNotOptArg, dXValue=defaultNamedNotOptArg, dYValue=defaultNamedNotOptArg, bUpdateDisplay=defaultNamedNotOptArg):
		'TRACE_SetPoint'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (11, 0), ((3, 0), (5, 0), (5, 0), (11, 0)),lPos
			, dXValue, dYValue, bUpdateDisplay)

	def TRACE_SetXIntervals(self, sNumIntervals=defaultNamedNotOptArg, bLog=defaultNamedNotOptArg):
		'TRACE_SetXIntervals'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (11, 0), ((2, 0), (11, 0)),sNumIntervals
			, bLog)

	def TRACE_SetXRange(self, dMinValue=defaultNamedNotOptArg, dMaxValue=defaultNamedNotOptArg):
		'TRACE_SetXRange'
		return self._oleobj_.InvokeTypes(34, LCID, 1, (11, 0), ((5, 0), (5, 0)),dMinValue
			, dMaxValue)

	def TRACE_SetYIntervals(self, sNumIntervals=defaultNamedNotOptArg, bLog=defaultNamedNotOptArg):
		'TRACE_SetYIntervals'
		return self._oleobj_.InvokeTypes(41, LCID, 1, (11, 0), ((2, 0), (11, 0)),sNumIntervals
			, bLog)

	def TRACE_SetYRange(self, dMinValue=defaultNamedNotOptArg, dMaxValue=defaultNamedNotOptArg):
		'TRACE_SetYRange'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (11, 0), ((5, 0), (5, 0)),dMinValue
			, dMaxValue)

	_prop_map_get_ = {
		"TRACE_Channel": (4, 2, (2, 0), (), "TRACE_Channel", None),
		"TRACE_Comment": (8, 2, (8, 0), (), "TRACE_Comment", None),
		"TRACE_CursorOn": (18, 2, (11, 0), (), "TRACE_CursorOn", None),
		"TRACE_CursorXUnit": (20, 2, (2, 0), (), "TRACE_CursorXUnit", None),
		"TRACE_CursorXValue": (19, 2, (5, 0), (), "TRACE_CursorXValue", None),
		"TRACE_CursorYUnit": (22, 2, (2, 0), (), "TRACE_CursorYUnit", None),
		"TRACE_CursorYValue": (21, 2, (5, 0), (), "TRACE_CursorYValue", None),
		"TRACE_ID": (2, 2, (2, 0), (), "TRACE_ID", None),
		"TRACE_INTERVALS_AUTO": (24, 2, (2, 0), (), "TRACE_INTERVALS_AUTO", None),
		"TRACE_MarksOn": (23, 2, (11, 0), (), "TRACE_MarksOn", None),
		"TRACE_MaxLimitBreached": (16, 2, (11, 0), (), "TRACE_MaxLimitBreached", None),
		"TRACE_MinLimitBreached": (17, 2, (11, 0), (), "TRACE_MinLimitBreached", None),
		"TRACE_Name": (1, 2, (8, 0), (), "TRACE_Name", None),
		"TRACE_On": (7, 2, (11, 0), (), "TRACE_On", None),
		"TRACE_PRINTSTYLE_DASH": (12, 2, (2, 0), (), "TRACE_PRINTSTYLE_DASH", None),
		"TRACE_PRINTSTYLE_DASHDOT": (13, 2, (2, 0), (), "TRACE_PRINTSTYLE_DASHDOT", None),
		"TRACE_PRINTSTYLE_DASHDOTDOT": (14, 2, (2, 0), (), "TRACE_PRINTSTYLE_DASHDOTDOT", None),
		"TRACE_PRINTSTYLE_DOT": (11, 2, (2, 0), (), "TRACE_PRINTSTYLE_DOT", None),
		"TRACE_PRINTSTYLE_SOLID": (10, 2, (2, 0), (), "TRACE_PRINTSTYLE_SOLID", None),
		"TRACE_PrintStyle": (9, 2, (2, 0), (), "TRACE_PrintStyle", None),
		"TRACE_ShowTransformedData": (15, 2, (11, 0), (), "TRACE_ShowTransformedData", None),
		"TRACE_Type": (3, 2, (2, 0), (), "TRACE_Type", None),
		"TRACE_XUnit": (5, 2, (2, 0), (), "TRACE_XUnit", None),
		"TRACE_YUnit": (6, 2, (2, 0), (), "TRACE_YUnit", None),
	}
	_prop_map_put_ = {
		"TRACE_Channel" : ((4, LCID, 4, 0),()),
		"TRACE_Comment" : ((8, LCID, 4, 0),()),
		"TRACE_CursorOn" : ((18, LCID, 4, 0),()),
		"TRACE_CursorXUnit" : ((20, LCID, 4, 0),()),
		"TRACE_CursorXValue" : ((19, LCID, 4, 0),()),
		"TRACE_CursorYUnit" : ((22, LCID, 4, 0),()),
		"TRACE_CursorYValue" : ((21, LCID, 4, 0),()),
		"TRACE_ID" : ((2, LCID, 4, 0),()),
		"TRACE_INTERVALS_AUTO" : ((24, LCID, 4, 0),()),
		"TRACE_MarksOn" : ((23, LCID, 4, 0),()),
		"TRACE_MaxLimitBreached" : ((16, LCID, 4, 0),()),
		"TRACE_MinLimitBreached" : ((17, LCID, 4, 0),()),
		"TRACE_Name" : ((1, LCID, 4, 0),()),
		"TRACE_On" : ((7, LCID, 4, 0),()),
		"TRACE_PRINTSTYLE_DASH" : ((12, LCID, 4, 0),()),
		"TRACE_PRINTSTYLE_DASHDOT" : ((13, LCID, 4, 0),()),
		"TRACE_PRINTSTYLE_DASHDOTDOT" : ((14, LCID, 4, 0),()),
		"TRACE_PRINTSTYLE_DOT" : ((11, LCID, 4, 0),()),
		"TRACE_PRINTSTYLE_SOLID" : ((10, LCID, 4, 0),()),
		"TRACE_PrintStyle" : ((9, LCID, 4, 0),()),
		"TRACE_ShowTransformedData" : ((15, LCID, 4, 0),()),
		"TRACE_Type" : ((3, LCID, 4, 0),()),
		"TRACE_XUnit" : ((5, LCID, 4, 0),()),
		"TRACE_YUnit" : ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITraceWindow(DispatchBaseClass):
	CLSID = IID('{920A1BE2-2C44-11D2-91DE-70AB00C10000}')
	coclass_clsid = IID('{920A1BE4-2C44-11D2-91DE-70AB00C10000}')

	def LMT_InitTable(self, lpszFileName=defaultNamedNotOptArg):
		'LMT_InitTable'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (11, 0), ((8, 0),),lpszFileName
			)

	def TW_AutoZoomAll(self, sChannel=defaultNamedNotOptArg):
		'TW_AutoZoomAll'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (11, 0), ((2, 0),),sChannel
			)

	def TW_CopyToClipboard(self, sChannel=defaultNamedNotOptArg):
		'TW_CopyToClipboard'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (11, 0), ((2, 0),),sChannel
			)

	def TW_CopyTrace(self, sTraceID=defaultNamedNotOptArg):
		'TW_CopyTrace'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (2, 0), ((2, 0),),sTraceID
			)

	def TW_CreateTrace(self, sChannel=defaultNamedNotOptArg, sNumPoints=defaultNamedNotOptArg, dXMin=defaultNamedNotOptArg, dXMax=defaultNamedNotOptArg
			, dYMin=defaultNamedNotOptArg, dYMax=defaultNamedNotOptArg):
		'TW_CreateTrace'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (2, 0), ((2, 0), (3, 0), (5, 0), (5, 0), (5, 0), (5, 0)),sChannel
			, sNumPoints, dXMin, dXMax, dYMin, dYMax
			)

	def TW_CreateTraceFromSweepTrace(self, sTraceType=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg):
		'TW_CreateTraceFromSweepTrace'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (2, 0), ((2, 0), (2, 0)),sTraceType
			, sChannel)

	def TW_DefaultZoomAll(self, sChannel=defaultNamedNotOptArg):
		'TW_DefaultZoomAll'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (11, 0), ((2, 0),),sChannel
			)

	def TW_Export(self, sChannel=defaultNamedNotOptArg, strFileName=defaultNamedNotOptArg):
		'TW_Export'
		return self._oleobj_.InvokeTypes(34, LCID, 1, (11, 0), ((2, 0), (8, 0)),sChannel
			, strFileName)

	def TW_GetCurrentTrace(self):
		'TW_GetCurrentTrace'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (2, 0), (),)

	def TW_GetFirstTraceOfType(self, sTraceType=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg):
		'TW_GetFirstTraceOfType'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (2, 0), ((2, 0), (2, 0)),sTraceType
			, sChannel)

	def TW_GetNextTraceOfType(self, sTraceType=defaultNamedNotOptArg):
		'TW_GetNextTraceOfType'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (2, 0), ((2, 0),),sTraceType
			)

	def TW_LoadTrace(self, strFileName=defaultNamedNotOptArg, sChannel=defaultNamedNotOptArg):
		'TW_LoadTrace'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (2, 0), ((8, 0), (2, 0)),strFileName
			, sChannel)

	def TW_Print(self, sChannel=defaultNamedNotOptArg):
		'TW_Print'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (11, 0), ((2, 0),),sChannel
			)

	def TW_RemoveTrace(self, sTraceID=defaultNamedNotOptArg):
		'TW_RemoveTrace'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (11, 0), ((2, 0),),sTraceID
			)

	def TW_SetCurrentTrace(self, sTraceID=defaultNamedNotOptArg, bUpdateDisplay=defaultNamedNotOptArg):
		'TW_SetCurrentTrace'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (11, 0), ((2, 0), (11, 0)),sTraceID
			, bUpdateDisplay)

	def TW_SetCurrentTraceFromEventParam(self, lParam=defaultNamedNotOptArg, bUpdateDisplay=defaultNamedNotOptArg):
		'TW_SetCurrentTraceFromEventParam'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (11, 0), ((3, 0), (11, 0)),lParam
			, bUpdateDisplay)

	_prop_map_get_ = {
		"TRACETYPE_CTA": (10, 2, (2, 0), (), "TRACETYPE_CTA", None),
		"TRACETYPE_CTFFT": (11, 2, (2, 0), (), "TRACETYPE_CTFFT", None),
		"TRACETYPE_FFT": (9, 2, (2, 0), (), "TRACETYPE_FFT", None),
		"TRACETYPE_FFTRESPONSE": (19, 2, (2, 0), (), "TRACETYPE_FFTRESPONSE", None),
		"TRACETYPE_FILTER": (12, 2, (2, 0), (), "TRACETYPE_FILTER", None),
		"TRACETYPE_MAXLIMITLINE": (20, 2, (2, 0), (), "TRACETYPE_MAXLIMITLINE", None),
		"TRACETYPE_MINLIMITLINE": (21, 2, (2, 0), (), "TRACETYPE_MINLIMITLINE", None),
		"TRACETYPE_SCOPE": (8, 2, (2, 0), (), "TRACETYPE_SCOPE", None),
		"TRACETYPE_SWEEP1": (14, 2, (2, 0), (), "TRACETYPE_SWEEP1", None),
		"TRACETYPE_SWEEP2": (15, 2, (2, 0), (), "TRACETYPE_SWEEP2", None),
		"TRACETYPE_SWEEP3": (16, 2, (2, 0), (), "TRACETYPE_SWEEP3", None),
		"TRACETYPE_SWEEP4": (17, 2, (2, 0), (), "TRACETYPE_SWEEP4", None),
		"TRACETYPE_USER": (18, 2, (2, 0), (), "TRACETYPE_USER", None),
		"TRACETYPE_WINDOW": (13, 2, (2, 0), (), "TRACETYPE_WINDOW", None),
		"TRACE_NULL_ID": (6, 2, (2, 0), (), "TRACE_NULL_ID", None),
		"TRACE_NULL_VALUE": (7, 2, (5, 0), (), "TRACE_NULL_VALUE", None),
		"TW_CHA": (3, 2, (2, 0), (), "TW_CHA", None),
		"TW_CHB": (4, 2, (2, 0), (), "TW_CHB", None),
		"TW_CHBOTH": (5, 2, (2, 0), (), "TW_CHBOTH", None),
		"TW_EditImpulseWindow": (22, 2, (11, 0), (), "TW_EditImpulseWindow", None),
		"TW_GraphComment": (2, 2, (8, 0), (), "TW_GraphComment", None),
		"TW_GraphTitle": (1, 2, (8, 0), (), "TW_GraphTitle", None),
	}
	_prop_map_put_ = {
		"TRACETYPE_CTA" : ((10, LCID, 4, 0),()),
		"TRACETYPE_CTFFT" : ((11, LCID, 4, 0),()),
		"TRACETYPE_FFT" : ((9, LCID, 4, 0),()),
		"TRACETYPE_FFTRESPONSE" : ((19, LCID, 4, 0),()),
		"TRACETYPE_FILTER" : ((12, LCID, 4, 0),()),
		"TRACETYPE_MAXLIMITLINE" : ((20, LCID, 4, 0),()),
		"TRACETYPE_MINLIMITLINE" : ((21, LCID, 4, 0),()),
		"TRACETYPE_SCOPE" : ((8, LCID, 4, 0),()),
		"TRACETYPE_SWEEP1" : ((14, LCID, 4, 0),()),
		"TRACETYPE_SWEEP2" : ((15, LCID, 4, 0),()),
		"TRACETYPE_SWEEP3" : ((16, LCID, 4, 0),()),
		"TRACETYPE_SWEEP4" : ((17, LCID, 4, 0),()),
		"TRACETYPE_USER" : ((18, LCID, 4, 0),()),
		"TRACETYPE_WINDOW" : ((13, LCID, 4, 0),()),
		"TRACE_NULL_ID" : ((6, LCID, 4, 0),()),
		"TRACE_NULL_VALUE" : ((7, LCID, 4, 0),()),
		"TW_CHA" : ((3, LCID, 4, 0),()),
		"TW_CHB" : ((4, LCID, 4, 0),()),
		"TW_CHBOTH" : ((5, LCID, 4, 0),()),
		"TW_EditImpulseWindow" : ((22, LCID, 4, 0),()),
		"TW_GraphComment" : ((2, LCID, 4, 0),()),
		"TW_GraphTitle" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IUserTable(DispatchBaseClass):
	CLSID = IID('{0BE39BE5-725C-11D3-B0E8-00AA0011AF6D}')
	coclass_clsid = IID('{0BE39BE7-725C-11D3-B0E8-00AA0011AF6D}')

	def USR_GetGeneratorChannel(self):
		'USR_GetGeneratorChannel'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), (),)

	def USR_InitTable(self, lpszFileName=defaultNamedNotOptArg, lNumPoints=defaultNamedNotOptArg):
		'USR_InitTable'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((8, 0), (3, 0)),lpszFileName
			, lNumPoints)

	def USR_MinimizeCrestFactor(self, paFrequencies=defaultNamedNotOptArg, paPhaseOffsets=defaultNamedNotOptArg, sNumTries=defaultNamedNotOptArg, bRandomize=defaultNamedNotOptArg
			, lBufferSize=defaultNamedNotOptArg, dSampleRate=defaultNamedNotOptArg):
		'USR_MinimizeCrestFactor'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (5, 0), ((16396, 0), (16396, 0), (2, 0), (11, 0), (3, 0), (5, 0)),paFrequencies
			, paPhaseOffsets, sNumTries, bRandomize, lBufferSize, dSampleRate
			)

	def USR_SaveTable(self, strFileName=defaultNamedNotOptArg):
		'USR_SaveTable'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), ((8, 0),),strFileName
			)

	def USR_SetAmplUse(self, sAmplUse=defaultNamedNotOptArg):
		'USR_SetAmplUse'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((2, 0),),sAmplUse
			)

	def USR_SetDefaultAmpl(self, dAmpl=defaultNamedNotOptArg):
		'USR_SetDefaultAmpl'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((5, 0),),dAmpl
			)

	def USR_SetDefaultAmplUnit(self, sUnit=defaultNamedNotOptArg):
		'USR_SetDefaultAmplUnit'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((2, 0),),sUnit
			)

	def USR_SetMaxAmpl(self, dMaxAmpl=defaultNamedNotOptArg):
		'USR_SetMaxAmpl'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((5, 0),),dMaxAmpl
			)

	def USR_SetPseudoCrestFactor(self, dPseudoCrestFactor=defaultNamedNotOptArg):
		'USR_SetPseudoCrestFactor'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((5, 0),),dPseudoCrestFactor
			)

	def USR_SetSweepSource(self, sSweepSource=defaultNamedNotOptArg):
		'USR_SetSweepSource'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((2, 0),),sSweepSource
			)

	def USR_SetSweepSourceUnit(self, sSweepSourceUnit=defaultNamedNotOptArg):
		'USR_SetSweepSourceUnit'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((2, 0),),sSweepSourceUnit
			)

	def USR_SetValue(self, dValue=defaultNamedNotOptArg):
		'USR_SetValue'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((5, 0),),dValue
			)

	def USR_SetValueAt(self, lPos=defaultNamedNotOptArg, dValue=defaultNamedNotOptArg):
		'USR_SetValueAt'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((3, 0), (5, 0)),lPos
			, dValue)

	def USR_SetValues(self, lNumValues=defaultNamedNotOptArg, dValue=defaultNamedNotOptArg):
		'USR_SetValues'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((3, 0), (5, 0)),lNumValues
			, dValue)

	def USR_SetValuesAt(self, lStartPos=defaultNamedNotOptArg, lEndPos=defaultNamedNotOptArg, dValue=defaultNamedNotOptArg):
		'USR_SetValuesAt'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((3, 0), (3, 0), (5, 0)),lStartPos
			, lEndPos, dValue)

	def USR_SetWindowWidth(self, sWindowWidth=defaultNamedNotOptArg):
		'USR_SetWindowWidth'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((2, 0),),sWindowWidth
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVSIOAdapter(DispatchBaseClass):
	CLSID = IID('{117A5950-05EB-47F3-B76B-9EE38C222F5B}')
	coclass_clsid = IID('{17054E24-21E6-4D06-89D7-2052C999341D}')

	# Result is of type IVSIOAdapter
	def Analyzer(self):
		'Analyzer'
		ret = self._oleobj_.InvokeTypes(42, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Analyzer', '{117A5950-05EB-47F3-B76B-9EE38C222F5B}')
		return ret

	# Result is of type IVSIOAdapter
	def Generator(self):
		'Generator'
		ret = self._oleobj_.InvokeTypes(41, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Generator', '{117A5950-05EB-47F3-B76B-9EE38C222F5B}')
		return ret

	def VSIO_AddToArray(self, sAddress=defaultNamedNotOptArg, sBus=defaultNamedNotOptArg, sGroup=defaultNamedNotOptArg, strArray=defaultNamedNotOptArg):
		'VSIO_AddToArray'
		return self._oleobj_.InvokeTypes(47, LCID, 1, (11, 0), ((2, 0), (2, 0), (2, 0), (8, 0)),sAddress
			, sBus, sGroup, strArray)

	def VSIO_AddToStereoArray(self, sAddress=defaultNamedNotOptArg, sGroup=defaultNamedNotOptArg, strArray=defaultNamedNotOptArg):
		'VSIO_AddToStereoArray'
		return self._oleobj_.InvokeTypes(48, LCID, 1, (11, 0), ((2, 0), (2, 0), (8, 0)),sAddress
			, sGroup, strArray)

	def VSIO_SendI2CData(self, sSlaveAddress=defaultNamedNotOptArg, sNumChars=defaultNamedNotOptArg, pTxBuf=defaultNamedNotOptArg):
		'VSIO_SendI2CData'
		return self._oleobj_.InvokeTypes(46, LCID, 1, (11, 0), ((2, 0), (2, 0), (16396, 0)),sSlaveAddress
			, sNumChars, pTxBuf)

	def VSIO_SendSPIData(self, sNumChars=defaultNamedNotOptArg, pTxBuf=defaultNamedNotOptArg, pRxBuf=defaultNamedNotOptArg):
		'VSIO_SendSPIData'
		return self._oleobj_.InvokeTypes(45, LCID, 1, (11, 0), ((2, 0), (16396, 0), (16396, 0)),sNumChars
			, pTxBuf, pRxBuf)

	def VSIO_SetAnalyzerRouting(self, sChannel=defaultNamedNotOptArg, sWire=defaultNamedNotOptArg, sSlot=defaultNamedNotOptArg):
		'VSIO_SetAnalyzerRouting'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (11, 0), ((2, 0), (2, 0), (2, 0)),sChannel
			, sWire, sSlot)

	def VSIO_SetCurrentDevice(self, sDevice=defaultNamedNotOptArg):
		'VSIO_SetCurrentDevice'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (11, 0), ((2, 0),),sDevice
			)

	def VSIO_SetGeneratorRouting(self, sWire=defaultNamedNotOptArg, sSlot=defaultNamedNotOptArg, sRouting=defaultNamedNotOptArg):
		'VSIO_SetGeneratorRouting'
		return self._oleobj_.InvokeTypes(43, LCID, 1, (11, 0), ((2, 0), (2, 0), (2, 0)),sWire
			, sSlot, sRouting)

	_prop_map_get_ = {
		"VSIO_AudioOn": (3, 2, (11, 0), (), "VSIO_AudioOn", None),
		"VSIO_AudioVoltage": (4, 2, (2, 0), (), "VSIO_AudioVoltage", None),
		"VSIO_BitClockFreq": (28, 2, (3, 0), (), "VSIO_BitClockFreq", None),
		"VSIO_BitClockInvert": (27, 2, (11, 0), (), "VSIO_BitClockInvert", None),
		"VSIO_CLOCKDIR_IN": (21, 2, (2, 0), (), "VSIO_CLOCKDIR_IN", None),
		"VSIO_CLOCKDIR_NONE": (20, 2, (2, 0), (), "VSIO_CLOCKDIR_NONE", None),
		"VSIO_CLOCKDIR_OUT": (22, 2, (2, 0), (), "VSIO_CLOCKDIR_OUT", None),
		"VSIO_ControlOn": (10, 2, (11, 0), (), "VSIO_ControlOn", None),
		"VSIO_ControlVoltage": (11, 2, (2, 0), (), "VSIO_ControlVoltage", None),
		"VSIO_DataLength": (15, 2, (2, 0), (), "VSIO_DataLength", None),
		"VSIO_Delay": (32, 2, (2, 0), (), "VSIO_Delay", None),
		"VSIO_EnableAnalyzer": (2, 2, (11, 0), (), "VSIO_EnableAnalyzer", None),
		"VSIO_EnableGenerator": (1, 2, (11, 0), (), "VSIO_EnableGenerator", None),
		"VSIO_FrameClock1Bit": (24, 2, (11, 0), (), "VSIO_FrameClock1Bit", None),
		"VSIO_FrameClockEarly": (25, 2, (11, 0), (), "VSIO_FrameClockEarly", None),
		"VSIO_FrameClockFreq": (26, 2, (3, 0), (), "VSIO_FrameClockFreq", None),
		"VSIO_FrameClockInvert": (23, 2, (11, 0), (), "VSIO_FrameClockInvert", None),
		"VSIO_GROUP_ANALYZER": (39, 2, (2, 0), (), "VSIO_GROUP_ANALYZER", None),
		"VSIO_GROUP_GENERATOR": (38, 2, (2, 0), (), "VSIO_GROUP_GENERATOR", None),
		"VSIO_LSBFirst": (13, 2, (11, 0), (), "VSIO_LSBFirst", None),
		"VSIO_LeadPadLength": (14, 2, (2, 0), (), "VSIO_LeadPadLength", None),
		"VSIO_MasterClockDir": (29, 2, (2, 0), (), "VSIO_MasterClockDir", None),
		"VSIO_MasterClockFreq": (31, 2, (3, 0), (), "VSIO_MasterClockFreq", None),
		"VSIO_MasterClockMultiplier": (30, 2, (2, 0), (), "VSIO_MasterClockMultiplier", None),
		"VSIO_ROUTING_A": (36, 2, (2, 0), (), "VSIO_ROUTING_A", None),
		"VSIO_ROUTING_B": (37, 2, (2, 0), (), "VSIO_ROUTING_B", None),
		"VSIO_ROUTING_OFF": (35, 2, (2, 0), (), "VSIO_ROUTING_OFF", None),
		"VSIO_SPIClockPhase": (34, 2, (11, 0), (), "VSIO_SPIClockPhase", None),
		"VSIO_SPIClockPolarity": (33, 2, (11, 0), (), "VSIO_SPIClockPolarity", None),
		"VSIO_SerialClockDir": (19, 2, (2, 0), (), "VSIO_SerialClockDir", None),
		"VSIO_SignExtend": (18, 2, (11, 0), (), "VSIO_SignExtend", None),
		"VSIO_SlotLength": (12, 2, (2, 0), (), "VSIO_SlotLength", None),
		"VSIO_SlotsPerWire": (17, 2, (2, 0), (), "VSIO_SlotsPerWire", None),
		"VSIO_TrailPadLength": (16, 2, (2, 0), (), "VSIO_TrailPadLength", None),
		"VSIO_VSEL_1V8": (5, 2, (2, 0), (), "VSIO_VSEL_1V8", None),
		"VSIO_VSEL_2V5": (6, 2, (2, 0), (), "VSIO_VSEL_2V5", None),
		"VSIO_VSEL_3V3": (7, 2, (2, 0), (), "VSIO_VSEL_3V3", None),
		"VSIO_VSEL_5V0_CMOS": (8, 2, (2, 0), (), "VSIO_VSEL_5V0_CMOS", None),
		"VSIO_VSEL_5V0_TTL": (9, 2, (2, 0), (), "VSIO_VSEL_5V0_TTL", None),
	}
	_prop_map_put_ = {
		"VSIO_AudioOn" : ((3, LCID, 4, 0),()),
		"VSIO_AudioVoltage" : ((4, LCID, 4, 0),()),
		"VSIO_BitClockFreq" : ((28, LCID, 4, 0),()),
		"VSIO_BitClockInvert" : ((27, LCID, 4, 0),()),
		"VSIO_CLOCKDIR_IN" : ((21, LCID, 4, 0),()),
		"VSIO_CLOCKDIR_NONE" : ((20, LCID, 4, 0),()),
		"VSIO_CLOCKDIR_OUT" : ((22, LCID, 4, 0),()),
		"VSIO_ControlOn" : ((10, LCID, 4, 0),()),
		"VSIO_ControlVoltage" : ((11, LCID, 4, 0),()),
		"VSIO_DataLength" : ((15, LCID, 4, 0),()),
		"VSIO_Delay" : ((32, LCID, 4, 0),()),
		"VSIO_EnableAnalyzer" : ((2, LCID, 4, 0),()),
		"VSIO_EnableGenerator" : ((1, LCID, 4, 0),()),
		"VSIO_FrameClock1Bit" : ((24, LCID, 4, 0),()),
		"VSIO_FrameClockEarly" : ((25, LCID, 4, 0),()),
		"VSIO_FrameClockFreq" : ((26, LCID, 4, 0),()),
		"VSIO_FrameClockInvert" : ((23, LCID, 4, 0),()),
		"VSIO_GROUP_ANALYZER" : ((39, LCID, 4, 0),()),
		"VSIO_GROUP_GENERATOR" : ((38, LCID, 4, 0),()),
		"VSIO_LSBFirst" : ((13, LCID, 4, 0),()),
		"VSIO_LeadPadLength" : ((14, LCID, 4, 0),()),
		"VSIO_MasterClockDir" : ((29, LCID, 4, 0),()),
		"VSIO_MasterClockFreq" : ((31, LCID, 4, 0),()),
		"VSIO_MasterClockMultiplier" : ((30, LCID, 4, 0),()),
		"VSIO_ROUTING_A" : ((36, LCID, 4, 0),()),
		"VSIO_ROUTING_B" : ((37, LCID, 4, 0),()),
		"VSIO_ROUTING_OFF" : ((35, LCID, 4, 0),()),
		"VSIO_SPIClockPhase" : ((34, LCID, 4, 0),()),
		"VSIO_SPIClockPolarity" : ((33, LCID, 4, 0),()),
		"VSIO_SerialClockDir" : ((19, LCID, 4, 0),()),
		"VSIO_SignExtend" : ((18, LCID, 4, 0),()),
		"VSIO_SlotLength" : ((12, LCID, 4, 0),()),
		"VSIO_SlotsPerWire" : ((17, LCID, 4, 0),()),
		"VSIO_TrailPadLength" : ((16, LCID, 4, 0),()),
		"VSIO_VSEL_1V8" : ((5, LCID, 4, 0),()),
		"VSIO_VSEL_2V5" : ((6, LCID, 4, 0),()),
		"VSIO_VSEL_3V3" : ((7, LCID, 4, 0),()),
		"VSIO_VSEL_5V0_CMOS" : ((8, LCID, 4, 0),()),
		"VSIO_VSEL_5V0_TTL" : ((9, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IdSNet(DispatchBaseClass):
	CLSID = IID('{2DA438F9-47DC-4FA0-BC9E-29B479667BF5}')
	coclass_clsid = IID('{96EACA9E-34BE-45EA-B6C5-EA2773680BCF}')

	def CA_AddChannel(self, sChannel=defaultNamedNotOptArg):
		'CA_AddChannel'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((2, 0),),sChannel
			)

	def CA_Balance(self, bOn=defaultNamedNotOptArg):
		'CA_Balance'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((11, 0),),bOn
			)

	def CA_ClearChannels(self):
		'CA_ClearChannels'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), (),)

	def CA_ExclusiveChannel(self, sChannel=defaultNamedNotOptArg):
		'CA_ExclusiveChannel'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((2, 0),),sChannel
			)

	def CA_NotChannel(self, sChannel=defaultNamedNotOptArg):
		'CA_NotChannel'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((2, 0),),sChannel
			)

	def CA_RemoveChannel(self, sChannel=defaultNamedNotOptArg):
		'CA_RemoveChannel'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((2, 0),),sChannel
			)

	def CA_SetAllChannels(self):
		'CA_SetAllChannels'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), (),)

	def DSNET_DefineChannelArray(self, strArray=defaultNamedNotOptArg, bStereo=defaultNamedNotOptArg, bExclusiveOnly=defaultNamedNotOptArg):
		'DSNET_DefineChannelArray'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((8, 0), (11, 0), (11, 0)),strArray
			, bStereo, bExclusiveOnly)

	def DSNET_GetStatus(self, sAddress=defaultNamedNotOptArg, plStatus=defaultNamedNotOptArg):
		'DSNET_GetStatus'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((2, 0), (16396, 0)),sAddress
			, plStatus)

	def DSNET_RemoveChannelArray(self, strArray=defaultNamedNotOptArg):
		'DSNET_RemoveChannelArray'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((8, 0),),strArray
			)

	def DSNET_Reset(self, sAddress=defaultNamedNotOptArg, bOn=defaultNamedNotOptArg, plStatus=defaultNamedNotOptArg):
		'DSNET_Reset'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((2, 0), (11, 0), (16396, 0)),sAddress
			, bOn, plStatus)

	def DSNET_SetChannelArray(self, strArray=defaultNamedNotOptArg):
		'DSNET_SetChannelArray'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), ((8, 0),),strArray
			)

	_prop_map_get_ = {
		"DSNET_ShowErrorMessages": (1, 2, (2, 0), (), "DSNET_ShowErrorMessages", None),
	}
	_prop_map_put_ = {
		"DSNET_ShowErrorMessages" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

from win32com.client import CoClassBaseClass
class AnalogueInputs(CoClassBaseClass): # A CoClass
	CLSID = IID('{E302BACB-E4DC-11D1-91DD-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IAnalogueInputs,
	]
	default_interface = IAnalogueInputs

class AnalogueOutputs(CoClassBaseClass): # A CoClass
	CLSID = IID('{C8EA98A5-E3F7-11D1-91DD-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IAnalogueOutputs,
	]
	default_interface = IAnalogueOutputs

class Analyzer(CoClassBaseClass): # A CoClass
	CLSID = IID('{8E6A39A1-C230-11D1-91DD-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IAnalyzer,
	]
	default_interface = IAnalyzer

# This CoClass is known by the name 'dScope.Application'
class Application(CoClassBaseClass): # A CoClass
	CLSID = IID('{5F1D8E24-2D90-11D4-AA54-0050046915E5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDScope,
	]
	default_interface = IDScope

class Automation(CoClassBaseClass): # A CoClass
	CLSID = IID('{21973E01-D1B6-11D4-AA54-0050046915E5}')
	coclass_sources = [
		IDScopeEvents,
	]
	default_source = IDScopeEvents
	coclass_interfaces = [
		IAutomation,
	]
	default_interface = IAutomation

class CTDetector(CoClassBaseClass): # A CoClass
	CLSID = IID('{E76688E3-1596-11D2-91DE-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICTDetector,
	]
	default_interface = ICTDetector

class CarrierDisplay(CoClassBaseClass): # A CoClass
	CLSID = IID('{BA01E3C3-6CDB-11D3-B0E8-00AA0011AF6D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICarrierDisplay,
	]
	default_interface = ICarrierDisplay

class ChannelStatus(CoClassBaseClass): # A CoClass
	CLSID = IID('{C2433363-FA1B-11D1-91DD-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChannelStatus,
	]
	default_interface = IChannelStatus

class ChannelStatusStream(CoClassBaseClass): # A CoClass
	CLSID = IID('{EF2310A6-0B44-11D2-91DD-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChannelStatusStream,
	]
	default_interface = IChannelStatusStream

class DigitalInputCarrier(CoClassBaseClass): # A CoClass
	CLSID = IID('{E302BAC6-E4DC-11D1-91DD-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDigitalInputCarrier,
	]
	default_interface = IDigitalInputCarrier

class DigitalInputs(CoClassBaseClass): # A CoClass
	CLSID = IID('{E302BAC3-E4DC-11D1-91DD-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDigitalInputs,
	]
	default_interface = IDigitalInputs

class DigitalOutputCarrier(CoClassBaseClass): # A CoClass
	CLSID = IID('{12E40663-E0F8-11D1-91DD-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDigitalOutputCarrier,
	]
	default_interface = IDigitalOutputCarrier

class DigitalOutputs(CoClassBaseClass): # A CoClass
	CLSID = IID('{C8EA98A8-E3F7-11D1-91DD-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDigitalOutputs,
	]
	default_interface = IDigitalOutputs

class EventManager(CoClassBaseClass): # A CoClass
	CLSID = IID('{BB07F160-D1B6-11D4-AA54-0050046915E5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IEventManager,
	]
	default_interface = IEventManager

class FFTDetector(CoClassBaseClass): # A CoClass
	CLSID = IID('{B9A66203-2AB2-11D2-91DE-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFFTDetector,
	]
	default_interface = IFFTDetector

class FFTParameters(CoClassBaseClass): # A CoClass
	CLSID = IID('{2CDD6203-17F8-11D2-91DE-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFFTParameters,
	]
	default_interface = IFFTParameters

class FormatConverter(CoClassBaseClass): # A CoClass
	CLSID = IID('{10837BD8-6795-4F49-A626-EDC9475040BA}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFormatConverter,
	]
	default_interface = IFormatConverter

class Generator(CoClassBaseClass): # A CoClass
	CLSID = IID('{318B25D2-C3FD-11D1-91DD-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IGenerator,
	]
	default_interface = IGenerator

class Hardware(CoClassBaseClass): # A CoClass
	CLSID = IID('{4B8A5560-CF1B-11D3-B0E8-00AA0011AF6D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IHardware,
	]
	default_interface = IHardware

class IOSwitcher(CoClassBaseClass): # A CoClass
	CLSID = IID('{5A73A73F-6614-409A-8E31-FCFCDED23ECF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IIOSwitcher,
	]
	default_interface = IIOSwitcher

class ImpulseResponse(CoClassBaseClass): # A CoClass
	CLSID = IID('{F81A9524-8E7B-470E-A15F-CB02B18A3A76}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IImpulseResponse,
	]
	default_interface = IImpulseResponse

class LimitTable(CoClassBaseClass): # A CoClass
	CLSID = IID('{64D4EDC4-F218-11D4-B9A2-0050046915E5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ILimitTable,
	]
	default_interface = ILimitTable

class MonitorOutputs(CoClassBaseClass): # A CoClass
	CLSID = IID('{E302BACE-E4DC-11D1-91DD-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMonitorOutputs,
	]
	default_interface = IMonitorOutputs

class Options(CoClassBaseClass): # A CoClass
	CLSID = IID('{662F8E40-D1B7-11D4-AA54-0050046915E5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IOptions,
	]
	default_interface = IOptions

class Port(CoClassBaseClass): # A CoClass
	CLSID = IID('{D9DE3A55-08AD-414C-BF6F-F0104B498432}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPorts,
	]
	default_interface = IPorts

class Reading(CoClassBaseClass): # A CoClass
	CLSID = IID('{635D9E3E-E49C-4197-A003-C1BD4C0035EF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IReading,
	]
	default_interface = IReading

class Regulation(CoClassBaseClass): # A CoClass
	CLSID = IID('{601BF482-A141-47D2-83BD-EFF57A2685A7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRegulation,
	]
	default_interface = IRegulation

class SerialPort(CoClassBaseClass): # A CoClass
	CLSID = IID('{9ADBC289-7D5F-47F4-A5AB-09A4617B63E0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISerialPort,
	]
	default_interface = ISerialPort

class Settling(CoClassBaseClass): # A CoClass
	CLSID = IID('{CB72FCC3-DFBD-11D3-B0E8-00AA0011AF6D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISettling,
	]
	default_interface = ISettling

class SignalAnalyzer(CoClassBaseClass): # A CoClass
	CLSID = IID('{31080A24-11BC-11D2-91DE-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISignalAnalyzer,
	]
	default_interface = ISignalAnalyzer

class SignalGenerator(CoClassBaseClass): # A CoClass
	CLSID = IID('{85AFFE43-E654-11D1-91DD-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISignalGenerator,
	]
	default_interface = ISignalGenerator

class SoundcardInputs(CoClassBaseClass): # A CoClass
	CLSID = IID('{DDB7596A-1605-4B32-8CA9-161640A3A2D5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISoundcardInputs,
	]
	default_interface = ISoundcardInputs

class SoundcardOutputs(CoClassBaseClass): # A CoClass
	CLSID = IID('{47E31141-03D5-4EB9-8E3B-6FD62829A010}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISoundcardOutputs,
	]
	default_interface = ISoundcardOutputs

class Sweeps(CoClassBaseClass): # A CoClass
	CLSID = IID('{2787A932-AC57-11D2-91DE-00AA0011AF6D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISweep,
	]
	default_interface = ISweep

class Switcher(CoClassBaseClass): # A CoClass
	CLSID = IID('{F565E4D0-B030-4417-8FFA-12BA9C756338}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISwitcher,
	]
	default_interface = ISwitcher

class Trace(CoClassBaseClass): # A CoClass
	CLSID = IID('{FB1F67C6-5C0C-11D5-9C7E-0050046915E5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ITrace,
	]
	default_interface = ITrace

class TraceWindow(CoClassBaseClass): # A CoClass
	CLSID = IID('{920A1BE4-2C44-11D2-91DE-70AB00C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ITraceWindow,
	]
	default_interface = ITraceWindow

class UserTable(CoClassBaseClass): # A CoClass
	CLSID = IID('{0BE39BE7-725C-11D3-B0E8-00AA0011AF6D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IUserTable,
	]
	default_interface = IUserTable

class VSIOAdapter(CoClassBaseClass): # A CoClass
	CLSID = IID('{17054E24-21E6-4D06-89D7-2052C999341D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVSIOAdapter,
	]
	default_interface = IVSIOAdapter

class dSNet(CoClassBaseClass): # A CoClass
	CLSID = IID('{96EACA9E-34BE-45EA-B6C5-EA2773680BCF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IdSNet,
	]
	default_interface = IdSNet

RecordMap = {
}

CLSIDToClassMap = {
	'{8E6A399F-C230-11D1-91DD-70AB00C10000}' : IAnalyzer,
	'{8E6A39A1-C230-11D1-91DD-70AB00C10000}' : Analyzer,
	'{E302BAC1-E4DC-11D1-91DD-70AB00C10000}' : IDigitalInputs,
	'{E302BAC3-E4DC-11D1-91DD-70AB00C10000}' : DigitalInputs,
	'{E302BAC4-E4DC-11D1-91DD-70AB00C10000}' : IDigitalInputCarrier,
	'{E302BAC6-E4DC-11D1-91DD-70AB00C10000}' : DigitalInputCarrier,
	'{E302BAC9-E4DC-11D1-91DD-70AB00C10000}' : IAnalogueInputs,
	'{E302BACB-E4DC-11D1-91DD-70AB00C10000}' : AnalogueInputs,
	'{3361DF2F-D9BC-4C5D-9898-FAE3BFF8A42F}' : ISoundcardInputs,
	'{DDB7596A-1605-4B32-8CA9-161640A3A2D5}' : SoundcardInputs,
	'{E302BACC-E4DC-11D1-91DD-70AB00C10000}' : IMonitorOutputs,
	'{E302BACE-E4DC-11D1-91DD-70AB00C10000}' : MonitorOutputs,
	'{31080A22-11BC-11D2-91DE-70AB00C10000}' : ISignalAnalyzer,
	'{31080A24-11BC-11D2-91DE-70AB00C10000}' : SignalAnalyzer,
	'{E76688E1-1596-11D2-91DE-70AB00C10000}' : ICTDetector,
	'{E76688E3-1596-11D2-91DE-70AB00C10000}' : CTDetector,
	'{2CDD6201-17F8-11D2-91DE-70AB00C10000}' : IFFTParameters,
	'{2CDD6203-17F8-11D2-91DE-70AB00C10000}' : FFTParameters,
	'{1CD7F788-84E1-415F-8EE0-739E3121D0AF}' : IImpulseResponse,
	'{F81A9524-8E7B-470E-A15F-CB02B18A3A76}' : ImpulseResponse,
	'{B9A66201-2AB2-11D2-91DE-70AB00C10000}' : IFFTDetector,
	'{B9A66203-2AB2-11D2-91DE-70AB00C10000}' : FFTDetector,
	'{BA01E3C1-6CDB-11D3-B0E8-00AA0011AF6D}' : ICarrierDisplay,
	'{BA01E3C3-6CDB-11D3-B0E8-00AA0011AF6D}' : CarrierDisplay,
	'{318B25D0-C3FD-11D1-91DD-70AB00C10000}' : IGenerator,
	'{318B25D2-C3FD-11D1-91DD-70AB00C10000}' : Generator,
	'{12E40661-E0F8-11D1-91DD-70AB00C10000}' : IDigitalOutputCarrier,
	'{12E40663-E0F8-11D1-91DD-70AB00C10000}' : DigitalOutputCarrier,
	'{C8EA98A3-E3F7-11D1-91DD-70AB00C10000}' : IAnalogueOutputs,
	'{C8EA98A5-E3F7-11D1-91DD-70AB00C10000}' : AnalogueOutputs,
	'{49EDD76B-5B81-4494-AD07-EDEB49287493}' : ISoundcardOutputs,
	'{47E31141-03D5-4EB9-8E3B-6FD62829A010}' : SoundcardOutputs,
	'{C8EA98A6-E3F7-11D1-91DD-70AB00C10000}' : IDigitalOutputs,
	'{C8EA98A8-E3F7-11D1-91DD-70AB00C10000}' : DigitalOutputs,
	'{85AFFE41-E654-11D1-91DD-70AB00C10000}' : ISignalGenerator,
	'{85AFFE43-E654-11D1-91DD-70AB00C10000}' : SignalGenerator,
	'{0BE39BE5-725C-11D3-B0E8-00AA0011AF6D}' : IUserTable,
	'{0BE39BE7-725C-11D3-B0E8-00AA0011AF6D}' : UserTable,
	'{EF2310A4-0B44-11D2-91DD-70AB00C10000}' : IChannelStatusStream,
	'{EF2310A6-0B44-11D2-91DD-70AB00C10000}' : ChannelStatusStream,
	'{C2433361-FA1B-11D1-91DD-70AB00C10000}' : IChannelStatus,
	'{C2433363-FA1B-11D1-91DD-70AB00C10000}' : ChannelStatus,
	'{2787A930-AC57-11D2-91DE-00AA0011AF6D}' : ISweep,
	'{2787A932-AC57-11D2-91DE-00AA0011AF6D}' : Sweeps,
	'{CB72FCC1-DFBD-11D3-B0E8-00AA0011AF6D}' : ISettling,
	'{CB72FCC3-DFBD-11D3-B0E8-00AA0011AF6D}' : Settling,
	'{BABA8F2B-2405-48C6-B991-337B5B00DBD8}' : IReading,
	'{635D9E3E-E49C-4197-A003-C1BD4C0035EF}' : Reading,
	'{920A1BE2-2C44-11D2-91DE-70AB00C10000}' : ITraceWindow,
	'{920A1BE4-2C44-11D2-91DE-70AB00C10000}' : TraceWindow,
	'{FB1F67C4-5C0C-11D5-9C7E-0050046915E5}' : ITrace,
	'{FB1F67C6-5C0C-11D5-9C7E-0050046915E5}' : Trace,
	'{64D4EDC2-F218-11D4-B9A2-0050046915E5}' : ILimitTable,
	'{64D4EDC4-F218-11D4-B9A2-0050046915E5}' : LimitTable,
	'{FC6A62CC-C2FD-11D1-91DD-70AB00C10000}' : IDScopeEvents,
	'{D0309162-171D-11D2-91DE-70AB00C10000}' : IAutomation,
	'{21973E01-D1B6-11D4-AA54-0050046915E5}' : Automation,
	'{D59FA601-A542-11D2-91DE-70AB00C10000}' : IEventManager,
	'{BB07F160-D1B6-11D4-AA54-0050046915E5}' : EventManager,
	'{3A499641-CE6B-11D3-B0E8-00AA0011AF6D}' : IHardware,
	'{4B8A5560-CF1B-11D3-B0E8-00AA0011AF6D}' : Hardware,
	'{0211EBA7-BFF6-4C67-9E59-58EA93952CCD}' : IPorts,
	'{D9DE3A55-08AD-414C-BF6F-F0104B498432}' : Port,
	'{CBCB3652-E7DF-48FB-8172-E592A139C0E9}' : ISerialPort,
	'{9ADBC289-7D5F-47F4-A5AB-09A4617B63E0}' : SerialPort,
	'{2DA438F9-47DC-4FA0-BC9E-29B479667BF5}' : IdSNet,
	'{96EACA9E-34BE-45EA-B6C5-EA2773680BCF}' : dSNet,
	'{8EF24D41-887F-4024-AB39-43844B96DDF8}' : ISwitcher,
	'{F565E4D0-B030-4417-8FFA-12BA9C756338}' : Switcher,
	'{F0815F9F-99C1-4931-B018-2735C3F176A9}' : IIOSwitcher,
	'{5A73A73F-6614-409A-8E31-FCFCDED23ECF}' : IOSwitcher,
	'{2840227C-5408-4E53-B52B-0F6637199948}' : IFormatConverter,
	'{10837BD8-6795-4F49-A626-EDC9475040BA}' : FormatConverter,
	'{117A5950-05EB-47F3-B76B-9EE38C222F5B}' : IVSIOAdapter,
	'{17054E24-21E6-4D06-89D7-2052C999341D}' : VSIOAdapter,
	'{94F3B76C-7223-43EA-8D03-0A87A8BD81CC}' : IRegulation,
	'{601BF482-A141-47D2-83BD-EFF57A2685A7}' : Regulation,
	'{A3AB5423-CD5E-11D2-B0E8-00AA0011AF6D}' : IOptions,
	'{662F8E40-D1B7-11D4-AA54-0050046915E5}' : Options,
	'{5F1D8E26-2D90-11D4-AA54-0050046915E5}' : IDScope,
	'{5F1D8E24-2D90-11D4-AA54-0050046915E5}' : Application,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
}


NamesToIIDMap = {
	'IAnalyzer' : '{8E6A399F-C230-11D1-91DD-70AB00C10000}',
	'IDigitalInputs' : '{E302BAC1-E4DC-11D1-91DD-70AB00C10000}',
	'IDigitalInputCarrier' : '{E302BAC4-E4DC-11D1-91DD-70AB00C10000}',
	'IAnalogueInputs' : '{E302BAC9-E4DC-11D1-91DD-70AB00C10000}',
	'ISoundcardInputs' : '{3361DF2F-D9BC-4C5D-9898-FAE3BFF8A42F}',
	'IMonitorOutputs' : '{E302BACC-E4DC-11D1-91DD-70AB00C10000}',
	'ISignalAnalyzer' : '{31080A22-11BC-11D2-91DE-70AB00C10000}',
	'ICTDetector' : '{E76688E1-1596-11D2-91DE-70AB00C10000}',
	'IFFTParameters' : '{2CDD6201-17F8-11D2-91DE-70AB00C10000}',
	'IImpulseResponse' : '{1CD7F788-84E1-415F-8EE0-739E3121D0AF}',
	'IFFTDetector' : '{B9A66201-2AB2-11D2-91DE-70AB00C10000}',
	'ICarrierDisplay' : '{BA01E3C1-6CDB-11D3-B0E8-00AA0011AF6D}',
	'IGenerator' : '{318B25D0-C3FD-11D1-91DD-70AB00C10000}',
	'IDigitalOutputCarrier' : '{12E40661-E0F8-11D1-91DD-70AB00C10000}',
	'IAnalogueOutputs' : '{C8EA98A3-E3F7-11D1-91DD-70AB00C10000}',
	'ISoundcardOutputs' : '{49EDD76B-5B81-4494-AD07-EDEB49287493}',
	'IDigitalOutputs' : '{C8EA98A6-E3F7-11D1-91DD-70AB00C10000}',
	'ISignalGenerator' : '{85AFFE41-E654-11D1-91DD-70AB00C10000}',
	'IUserTable' : '{0BE39BE5-725C-11D3-B0E8-00AA0011AF6D}',
	'IChannelStatusStream' : '{EF2310A4-0B44-11D2-91DD-70AB00C10000}',
	'IChannelStatus' : '{C2433361-FA1B-11D1-91DD-70AB00C10000}',
	'ISweep' : '{2787A930-AC57-11D2-91DE-00AA0011AF6D}',
	'ISettling' : '{CB72FCC1-DFBD-11D3-B0E8-00AA0011AF6D}',
	'IReading' : '{BABA8F2B-2405-48C6-B991-337B5B00DBD8}',
	'ITraceWindow' : '{920A1BE2-2C44-11D2-91DE-70AB00C10000}',
	'ITrace' : '{FB1F67C4-5C0C-11D5-9C7E-0050046915E5}',
	'ILimitTable' : '{64D4EDC2-F218-11D4-B9A2-0050046915E5}',
	'IDScopeEvents' : '{FC6A62CC-C2FD-11D1-91DD-70AB00C10000}',
	'IAutomation' : '{D0309162-171D-11D2-91DE-70AB00C10000}',
	'IEventManager' : '{D59FA601-A542-11D2-91DE-70AB00C10000}',
	'IHardware' : '{3A499641-CE6B-11D3-B0E8-00AA0011AF6D}',
	'IPorts' : '{0211EBA7-BFF6-4C67-9E59-58EA93952CCD}',
	'ISerialPort' : '{CBCB3652-E7DF-48FB-8172-E592A139C0E9}',
	'IdSNet' : '{2DA438F9-47DC-4FA0-BC9E-29B479667BF5}',
	'ISwitcher' : '{8EF24D41-887F-4024-AB39-43844B96DDF8}',
	'IIOSwitcher' : '{F0815F9F-99C1-4931-B018-2735C3F176A9}',
	'IFormatConverter' : '{2840227C-5408-4E53-B52B-0F6637199948}',
	'IVSIOAdapter' : '{117A5950-05EB-47F3-B76B-9EE38C222F5B}',
	'IRegulation' : '{94F3B76C-7223-43EA-8D03-0A87A8BD81CC}',
	'IOptions' : '{A3AB5423-CD5E-11D2-B0E8-00AA0011AF6D}',
	'IDScope' : '{5F1D8E26-2D90-11D4-AA54-0050046915E5}',
}


