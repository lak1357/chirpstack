# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/gw/gw.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63hirpstack-api/gw/gw.proto\x12\x02gw\x1a\"chirpstack-api/common/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x95\x01\n\nModulation\x12&\n\x04lora\x18\x03 \x01(\x0b\x32\x16.gw.LoraModulationInfoH\x00\x12$\n\x03\x66sk\x18\x04 \x01(\x0b\x32\x15.gw.FskModulationInfoH\x00\x12+\n\x07lr_fhss\x18\x05 \x01(\x0b\x32\x18.gw.LrFhssModulationInfoH\x00\x42\x0c\n\nparameters\"\x8d\x02\n\x12UplinkTxInfoLegacy\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12&\n\nmodulation\x18\x02 \x01(\x0e\x32\x12.common.Modulation\x12\x36\n\x14lora_modulation_info\x18\x03 \x01(\x0b\x32\x16.gw.LoraModulationInfoH\x00\x12\x34\n\x13\x66sk_modulation_info\x18\x04 \x01(\x0b\x32\x15.gw.FskModulationInfoH\x00\x12;\n\x17lr_fhss_modulation_info\x18\x05 \x01(\x0b\x32\x18.gw.LrFhssModulationInfoH\x00\x42\x11\n\x0fmodulation_info\"E\n\x0cUplinkTxInfo\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12\"\n\nmodulation\x18\x02 \x01(\x0b\x32\x0e.gw.Modulation\"\x9c\x01\n\x12LoraModulationInfo\x12\x11\n\tbandwidth\x18\x01 \x01(\r\x12\x18\n\x10spreading_factor\x18\x02 \x01(\r\x12\x18\n\x10\x63ode_rate_legacy\x18\x03 \x01(\t\x12\x1f\n\tcode_rate\x18\x05 \x01(\x0e\x32\x0c.gw.CodeRate\x12\x1e\n\x16polarization_inversion\x18\x04 \x01(\x08\"B\n\x11\x46skModulationInfo\x12\x1b\n\x13\x66requency_deviation\x18\x01 \x01(\r\x12\x10\n\x08\x64\x61tarate\x18\x02 \x01(\r\"^\n\x14LrFhssModulationInfo\x12\x1f\n\x17operating_channel_width\x18\x01 \x01(\r\x12\x11\n\tcode_rate\x18\x02 \x01(\t\x12\x12\n\ngrid_steps\x18\x03 \x01(\r\"V\n\x16\x45ncryptedFineTimestamp\x12\x15\n\raes_key_index\x18\x01 \x01(\r\x12\x14\n\x0c\x65ncrypted_ns\x18\x02 \x01(\x0c\x12\x0f\n\x07\x66pga_id\x18\x03 \x01(\x0c\">\n\x12PlainFineTimestamp\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x94\x07\n\x0cGatewayStats\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12\n\n\x02ip\x18\t \x01(\t\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x08location\x18\x03 \x01(\x0b\x32\x10.common.Location\x12\x16\n\x0e\x63onfig_version\x18\x04 \x01(\t\x12\x1b\n\x13rx_packets_received\x18\x05 \x01(\r\x12\x1e\n\x16rx_packets_received_ok\x18\x06 \x01(\r\x12\x1b\n\x13tx_packets_received\x18\x07 \x01(\r\x12\x1a\n\x12tx_packets_emitted\x18\x08 \x01(\r\x12\x31\n\tmeta_data\x18\n \x03(\x0b\x32\x1e.gw.GatewayStats.MetaDataEntry\x12\x10\n\x08stats_id\x18\x0b \x01(\x0c\x12M\n\x18tx_packets_per_frequency\x18\x0c \x03(\x0b\x32+.gw.GatewayStats.TxPacketsPerFrequencyEntry\x12M\n\x18rx_packets_per_frequency\x18\r \x03(\x0b\x32+.gw.GatewayStats.RxPacketsPerFrequencyEntry\x12\x39\n\x19tx_packets_per_modulation\x18\x0e \x03(\x0b\x32\x16.gw.PerModulationCount\x12\x39\n\x19rx_packets_per_modulation\x18\x0f \x03(\x0b\x32\x16.gw.PerModulationCount\x12G\n\x15tx_packets_per_status\x18\x10 \x03(\x0b\x32(.gw.GatewayStats.TxPacketsPerStatusEntry\x1a/\n\rMetaDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a<\n\x1aTxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a<\n\x1aRxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x39\n\x17TxPacketsPerStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"G\n\x12PerModulationCount\x12\"\n\nmodulation\x18\x01 \x01(\x0b\x32\x0e.gw.Modulation\x12\r\n\x05\x63ount\x18\x02 \x01(\r\"\x80\x05\n\x12UplinkRxInfoLegacy\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x14time_since_gps_epoch\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x0c\n\x04rssi\x18\x05 \x01(\x05\x12\x10\n\x08lora_snr\x18\x06 \x01(\x01\x12\x0f\n\x07\x63hannel\x18\x07 \x01(\r\x12\x10\n\x08rf_chain\x18\x08 \x01(\r\x12\r\n\x05\x62oard\x18\t \x01(\r\x12\x0f\n\x07\x61ntenna\x18\n \x01(\r\x12\"\n\x08location\x18\x0b \x01(\x0b\x32\x10.common.Location\x12\x32\n\x13\x66ine_timestamp_type\x18\x0c \x01(\x0e\x32\x15.gw.FineTimestampType\x12>\n\x18\x65ncrypted_fine_timestamp\x18\r \x01(\x0b\x32\x1a.gw.EncryptedFineTimestampH\x00\x12\x36\n\x14plain_fine_timestamp\x18\x0e \x01(\x0b\x32\x16.gw.PlainFineTimestampH\x00\x12\x0f\n\x07\x63ontext\x18\x0f \x01(\x0c\x12\x11\n\tuplink_id\x18\x10 \x01(\x0c\x12!\n\ncrc_status\x18\x11 \x01(\x0e\x32\r.gw.CRCStatus\x12\x36\n\x08metadata\x18\x12 \x03(\x0b\x32$.gw.UplinkRxInfoLegacy.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x10\n\x0e\x66ine_timestamp\"\xf1\x02\n\x0cUplinkRxInfo\x12\x12\n\ngateway_id\x18\x01 \x01(\t\x12\x11\n\tuplink_id\x18\x02 \x01(\r\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x14time_since_gps_epoch\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12<\n\x19\x66ine_time_since_gps_epoch\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x0c\n\x04rssi\x18\x06 \x01(\x05\x12\x0b\n\x03snr\x18\x07 \x01(\x02\x12\r\n\x05\x62oard\x18\x08 \x01(\r\x12\x0f\n\x07\x61ntenna\x18\t \x01(\r\x12\"\n\x08location\x18\n \x01(\x0b\x32\x10.common.Location\x12\x0f\n\x07\x63ontext\x18\x0b \x01(\x0c\x12)\n\x08metadata\x18\x0c \x01(\x0b\x32\x17.google.protobuf.Struct\"\x82\x04\n\x14\x44ownlinkTxInfoLegacy\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12\x11\n\tfrequency\x18\x05 \x01(\r\x12\r\n\x05power\x18\x06 \x01(\x05\x12&\n\nmodulation\x18\x07 \x01(\x0e\x32\x12.common.Modulation\x12\x36\n\x14lora_modulation_info\x18\x08 \x01(\x0b\x32\x16.gw.LoraModulationInfoH\x00\x12\x34\n\x13\x66sk_modulation_info\x18\t \x01(\x0b\x32\x15.gw.FskModulationInfoH\x00\x12\r\n\x05\x62oard\x18\n \x01(\r\x12\x0f\n\x07\x61ntenna\x18\x0b \x01(\r\x12\"\n\x06timing\x18\x0c \x01(\x0e\x32\x12.gw.DownlinkTiming\x12<\n\x17immediately_timing_info\x18\r \x01(\x0b\x32\x19.gw.ImmediatelyTimingInfoH\x01\x12\x30\n\x11\x64\x65lay_timing_info\x18\x0e \x01(\x0b\x32\x13.gw.DelayTimingInfoH\x01\x12\x37\n\x15gps_epoch_timing_info\x18\x0f \x01(\x0b\x32\x16.gw.GPSEpochTimingInfoH\x01\x12\x0f\n\x07\x63ontext\x18\x10 \x01(\x0c\x42\x11\n\x0fmodulation_infoB\r\n\x0btiming_info\"\xa3\x01\n\x0e\x44ownlinkTxInfo\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12\r\n\x05power\x18\x02 \x01(\x05\x12\"\n\nmodulation\x18\x03 \x01(\x0b\x32\x0e.gw.Modulation\x12\r\n\x05\x62oard\x18\x04 \x01(\r\x12\x0f\n\x07\x61ntenna\x18\x05 \x01(\r\x12\x1a\n\x06timing\x18\x06 \x01(\x0b\x32\n.gw.Timing\x12\x0f\n\x07\x63ontext\x18\x07 \x01(\x0c\"\x9b\x01\n\x06Timing\x12\x30\n\x0bimmediately\x18\x01 \x01(\x0b\x32\x19.gw.ImmediatelyTimingInfoH\x00\x12$\n\x05\x64\x65lay\x18\x02 \x01(\x0b\x32\x13.gw.DelayTimingInfoH\x00\x12+\n\tgps_epoch\x18\x03 \x01(\x0b\x32\x16.gw.GPSEpochTimingInfoH\x00\x42\x0c\n\nparameters\"\x17\n\x15ImmediatelyTimingInfo\";\n\x0f\x44\x65layTimingInfo\x12(\n\x05\x64\x65lay\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"M\n\x12GPSEpochTimingInfo\x12\x37\n\x14time_since_gps_epoch\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"\xc8\x01\n\x0bUplinkFrame\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12.\n\x0etx_info_legacy\x18\x02 \x01(\x0b\x32\x16.gw.UplinkTxInfoLegacy\x12.\n\x0erx_info_legacy\x18\x03 \x01(\x0b\x32\x16.gw.UplinkRxInfoLegacy\x12!\n\x07tx_info\x18\x04 \x01(\x0b\x32\x10.gw.UplinkTxInfo\x12!\n\x07rx_info\x18\x05 \x01(\x0b\x32\x10.gw.UplinkRxInfo\"k\n\x0eUplinkFrameSet\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12!\n\x07tx_info\x18\x02 \x01(\x0b\x32\x10.gw.UplinkTxInfo\x12!\n\x07rx_info\x18\x03 \x03(\x0b\x32\x10.gw.UplinkRxInfo\"\x95\x01\n\rDownlinkFrame\x12\x13\n\x0b\x64ownlink_id\x18\x03 \x01(\r\x12\x1a\n\x12\x64ownlink_id_legacy\x18\x04 \x01(\x0c\x12$\n\x05items\x18\x05 \x03(\x0b\x32\x15.gw.DownlinkFrameItem\x12\x19\n\x11gateway_id_legacy\x18\x06 \x01(\x0c\x12\x12\n\ngateway_id\x18\x07 \x01(\t\"\x7f\n\x11\x44ownlinkFrameItem\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12\x30\n\x0etx_info_legacy\x18\x02 \x01(\x0b\x32\x18.gw.DownlinkTxInfoLegacy\x12#\n\x07tx_info\x18\x03 \x01(\x0b\x32\x12.gw.DownlinkTxInfo\"\x95\x01\n\rDownlinkTxAck\x12\x19\n\x11gateway_id_legacy\x18\x01 \x01(\x0c\x12\x12\n\ngateway_id\x18\x06 \x01(\t\x12\x13\n\x0b\x64ownlink_id\x18\x02 \x01(\r\x12\x1a\n\x12\x64ownlink_id_legacy\x18\x04 \x01(\x0c\x12$\n\x05items\x18\x05 \x03(\x0b\x32\x15.gw.DownlinkTxAckItem\"4\n\x11\x44ownlinkTxAckItem\x12\x1f\n\x06status\x18\x01 \x01(\x0e\x32\x0f.gw.TxAckStatus\"\x9a\x01\n\x14GatewayConfiguration\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12\x0f\n\x07version\x18\x02 \x01(\t\x12*\n\x08\x63hannels\x18\x03 \x03(\x0b\x32\x18.gw.ChannelConfiguration\x12\x31\n\x0estats_interval\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\"\x80\x02\n\x14\x43hannelConfiguration\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12&\n\nmodulation\x18\x02 \x01(\x0e\x32\x12.common.Modulation\x12:\n\x16lora_modulation_config\x18\x03 \x01(\x0b\x32\x18.gw.LoRaModulationConfigH\x00\x12\x38\n\x15\x66sk_modulation_config\x18\x04 \x01(\x0b\x32\x17.gw.FSKModulationConfigH\x00\x12\r\n\x05\x62oard\x18\x05 \x01(\r\x12\x13\n\x0b\x64\x65modulator\x18\x06 \x01(\rB\x13\n\x11modulation_config\"D\n\x14LoRaModulationConfig\x12\x11\n\tbandwidth\x18\x01 \x01(\r\x12\x19\n\x11spreading_factors\x18\x02 \x03(\r\"9\n\x13\x46SKModulationConfig\x12\x11\n\tbandwidth\x18\x01 \x01(\r\x12\x0f\n\x07\x62itrate\x18\x02 \x01(\r\"\xd8\x01\n\x19GatewayCommandExecRequest\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\x12\x0e\n\x06\x45xecId\x18\x03 \x01(\x0c\x12\r\n\x05stdin\x18\x04 \x01(\x0c\x12\x43\n\x0b\x65nvironment\x18\x05 \x03(\x0b\x32..gw.GatewayCommandExecRequest.EnvironmentEntry\x1a\x32\n\x10\x45nvironmentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"p\n\x1aGatewayCommandExecResponse\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12\x0f\n\x07\x65xec_id\x18\x02 \x01(\x0c\x12\x0e\n\x06stdout\x18\x03 \x01(\x0c\x12\x0e\n\x06stderr\x18\x04 \x01(\x0c\x12\r\n\x05\x65rror\x18\x05 \x01(\t\"N\n\x17RawPacketForwarderEvent\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12\x0e\n\x06raw_id\x18\x02 \x01(\x0c\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"P\n\x19RawPacketForwarderCommand\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12\x0e\n\x06raw_id\x18\x02 \x01(\x0c\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"e\n\tConnState\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12\"\n\x05state\x18\x02 \x01(\x0e\x32\x13.gw.ConnState.State\" \n\x05State\x12\x0b\n\x07OFFLINE\x10\x00\x12\n\n\x06ONLINE\x10\x01*L\n\x08\x43odeRate\x12\x10\n\x0c\x43R_UNDEFINED\x10\x00\x12\n\n\x06\x43R_4_5\x10\x01\x12\n\n\x06\x43R_4_6\x10\x02\x12\n\n\x06\x43R_4_7\x10\x03\x12\n\n\x06\x43R_4_8\x10\x04*;\n\x0e\x44ownlinkTiming\x12\x0f\n\x0bIMMEDIATELY\x10\x00\x12\t\n\x05\x44\x45LAY\x10\x01\x12\r\n\tGPS_EPOCH\x10\x02*7\n\x11\x46ineTimestampType\x12\x08\n\x04NONE\x10\x00\x12\r\n\tENCRYPTED\x10\x01\x12\t\n\x05PLAIN\x10\x02*0\n\tCRCStatus\x12\n\n\x06NO_CRC\x10\x00\x12\x0b\n\x07\x42\x41\x44_CRC\x10\x01\x12\n\n\x06\x43RC_OK\x10\x02*\xbc\x01\n\x0bTxAckStatus\x12\x0b\n\x07IGNORED\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x0c\n\x08TOO_LATE\x10\x02\x12\r\n\tTOO_EARLY\x10\x03\x12\x14\n\x10\x43OLLISION_PACKET\x10\x04\x12\x14\n\x10\x43OLLISION_BEACON\x10\x05\x12\x0b\n\x07TX_FREQ\x10\x06\x12\x0c\n\x08TX_POWER\x10\x07\x12\x10\n\x0cGPS_UNLOCKED\x10\x08\x12\x0e\n\nQUEUE_FULL\x10\t\x12\x12\n\x0eINTERNAL_ERROR\x10\nBU\n\x14io.chirpstack.api.gwB\x0cGatewayProtoP\x01Z-github.com/chirpstack/chirpstack/api/go/v4/gwb\x06proto3')

_CODERATE = DESCRIPTOR.enum_types_by_name['CodeRate']
CodeRate = enum_type_wrapper.EnumTypeWrapper(_CODERATE)
_DOWNLINKTIMING = DESCRIPTOR.enum_types_by_name['DownlinkTiming']
DownlinkTiming = enum_type_wrapper.EnumTypeWrapper(_DOWNLINKTIMING)
_FINETIMESTAMPTYPE = DESCRIPTOR.enum_types_by_name['FineTimestampType']
FineTimestampType = enum_type_wrapper.EnumTypeWrapper(_FINETIMESTAMPTYPE)
_CRCSTATUS = DESCRIPTOR.enum_types_by_name['CRCStatus']
CRCStatus = enum_type_wrapper.EnumTypeWrapper(_CRCSTATUS)
_TXACKSTATUS = DESCRIPTOR.enum_types_by_name['TxAckStatus']
TxAckStatus = enum_type_wrapper.EnumTypeWrapper(_TXACKSTATUS)
CR_UNDEFINED = 0
CR_4_5 = 1
CR_4_6 = 2
CR_4_7 = 3
CR_4_8 = 4
IMMEDIATELY = 0
DELAY = 1
GPS_EPOCH = 2
NONE = 0
ENCRYPTED = 1
PLAIN = 2
NO_CRC = 0
BAD_CRC = 1
CRC_OK = 2
IGNORED = 0
OK = 1
TOO_LATE = 2
TOO_EARLY = 3
COLLISION_PACKET = 4
COLLISION_BEACON = 5
TX_FREQ = 6
TX_POWER = 7
GPS_UNLOCKED = 8
QUEUE_FULL = 9
INTERNAL_ERROR = 10


_MODULATION = DESCRIPTOR.message_types_by_name['Modulation']
_UPLINKTXINFOLEGACY = DESCRIPTOR.message_types_by_name['UplinkTxInfoLegacy']
_UPLINKTXINFO = DESCRIPTOR.message_types_by_name['UplinkTxInfo']
_LORAMODULATIONINFO = DESCRIPTOR.message_types_by_name['LoraModulationInfo']
_FSKMODULATIONINFO = DESCRIPTOR.message_types_by_name['FskModulationInfo']
_LRFHSSMODULATIONINFO = DESCRIPTOR.message_types_by_name['LrFhssModulationInfo']
_ENCRYPTEDFINETIMESTAMP = DESCRIPTOR.message_types_by_name['EncryptedFineTimestamp']
_PLAINFINETIMESTAMP = DESCRIPTOR.message_types_by_name['PlainFineTimestamp']
_GATEWAYSTATS = DESCRIPTOR.message_types_by_name['GatewayStats']
_GATEWAYSTATS_METADATAENTRY = _GATEWAYSTATS.nested_types_by_name['MetaDataEntry']
_GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY = _GATEWAYSTATS.nested_types_by_name['TxPacketsPerFrequencyEntry']
_GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY = _GATEWAYSTATS.nested_types_by_name['RxPacketsPerFrequencyEntry']
_GATEWAYSTATS_TXPACKETSPERSTATUSENTRY = _GATEWAYSTATS.nested_types_by_name['TxPacketsPerStatusEntry']
_PERMODULATIONCOUNT = DESCRIPTOR.message_types_by_name['PerModulationCount']
_UPLINKRXINFOLEGACY = DESCRIPTOR.message_types_by_name['UplinkRxInfoLegacy']
_UPLINKRXINFOLEGACY_METADATAENTRY = _UPLINKRXINFOLEGACY.nested_types_by_name['MetadataEntry']
_UPLINKRXINFO = DESCRIPTOR.message_types_by_name['UplinkRxInfo']
_DOWNLINKTXINFOLEGACY = DESCRIPTOR.message_types_by_name['DownlinkTxInfoLegacy']
_DOWNLINKTXINFO = DESCRIPTOR.message_types_by_name['DownlinkTxInfo']
_TIMING = DESCRIPTOR.message_types_by_name['Timing']
_IMMEDIATELYTIMINGINFO = DESCRIPTOR.message_types_by_name['ImmediatelyTimingInfo']
_DELAYTIMINGINFO = DESCRIPTOR.message_types_by_name['DelayTimingInfo']
_GPSEPOCHTIMINGINFO = DESCRIPTOR.message_types_by_name['GPSEpochTimingInfo']
_UPLINKFRAME = DESCRIPTOR.message_types_by_name['UplinkFrame']
_UPLINKFRAMESET = DESCRIPTOR.message_types_by_name['UplinkFrameSet']
_DOWNLINKFRAME = DESCRIPTOR.message_types_by_name['DownlinkFrame']
_DOWNLINKFRAMEITEM = DESCRIPTOR.message_types_by_name['DownlinkFrameItem']
_DOWNLINKTXACK = DESCRIPTOR.message_types_by_name['DownlinkTxAck']
_DOWNLINKTXACKITEM = DESCRIPTOR.message_types_by_name['DownlinkTxAckItem']
_GATEWAYCONFIGURATION = DESCRIPTOR.message_types_by_name['GatewayConfiguration']
_CHANNELCONFIGURATION = DESCRIPTOR.message_types_by_name['ChannelConfiguration']
_LORAMODULATIONCONFIG = DESCRIPTOR.message_types_by_name['LoRaModulationConfig']
_FSKMODULATIONCONFIG = DESCRIPTOR.message_types_by_name['FSKModulationConfig']
_GATEWAYCOMMANDEXECREQUEST = DESCRIPTOR.message_types_by_name['GatewayCommandExecRequest']
_GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY = _GATEWAYCOMMANDEXECREQUEST.nested_types_by_name['EnvironmentEntry']
_GATEWAYCOMMANDEXECRESPONSE = DESCRIPTOR.message_types_by_name['GatewayCommandExecResponse']
_RAWPACKETFORWARDEREVENT = DESCRIPTOR.message_types_by_name['RawPacketForwarderEvent']
_RAWPACKETFORWARDERCOMMAND = DESCRIPTOR.message_types_by_name['RawPacketForwarderCommand']
_CONNSTATE = DESCRIPTOR.message_types_by_name['ConnState']
_CONNSTATE_STATE = _CONNSTATE.enum_types_by_name['State']
Modulation = _reflection.GeneratedProtocolMessageType('Modulation', (_message.Message,), {
  'DESCRIPTOR' : _MODULATION,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.Modulation)
  })
_sym_db.RegisterMessage(Modulation)

UplinkTxInfoLegacy = _reflection.GeneratedProtocolMessageType('UplinkTxInfoLegacy', (_message.Message,), {
  'DESCRIPTOR' : _UPLINKTXINFOLEGACY,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.UplinkTxInfoLegacy)
  })
_sym_db.RegisterMessage(UplinkTxInfoLegacy)

UplinkTxInfo = _reflection.GeneratedProtocolMessageType('UplinkTxInfo', (_message.Message,), {
  'DESCRIPTOR' : _UPLINKTXINFO,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.UplinkTxInfo)
  })
_sym_db.RegisterMessage(UplinkTxInfo)

LoraModulationInfo = _reflection.GeneratedProtocolMessageType('LoraModulationInfo', (_message.Message,), {
  'DESCRIPTOR' : _LORAMODULATIONINFO,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.LoraModulationInfo)
  })
_sym_db.RegisterMessage(LoraModulationInfo)

FskModulationInfo = _reflection.GeneratedProtocolMessageType('FskModulationInfo', (_message.Message,), {
  'DESCRIPTOR' : _FSKMODULATIONINFO,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.FskModulationInfo)
  })
_sym_db.RegisterMessage(FskModulationInfo)

LrFhssModulationInfo = _reflection.GeneratedProtocolMessageType('LrFhssModulationInfo', (_message.Message,), {
  'DESCRIPTOR' : _LRFHSSMODULATIONINFO,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.LrFhssModulationInfo)
  })
_sym_db.RegisterMessage(LrFhssModulationInfo)

EncryptedFineTimestamp = _reflection.GeneratedProtocolMessageType('EncryptedFineTimestamp', (_message.Message,), {
  'DESCRIPTOR' : _ENCRYPTEDFINETIMESTAMP,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.EncryptedFineTimestamp)
  })
_sym_db.RegisterMessage(EncryptedFineTimestamp)

PlainFineTimestamp = _reflection.GeneratedProtocolMessageType('PlainFineTimestamp', (_message.Message,), {
  'DESCRIPTOR' : _PLAINFINETIMESTAMP,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.PlainFineTimestamp)
  })
_sym_db.RegisterMessage(PlainFineTimestamp)

GatewayStats = _reflection.GeneratedProtocolMessageType('GatewayStats', (_message.Message,), {

  'MetaDataEntry' : _reflection.GeneratedProtocolMessageType('MetaDataEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAYSTATS_METADATAENTRY,
    '__module__' : 'chirpstack_api.gw.gw_pb2'
    # @@protoc_insertion_point(class_scope:gw.GatewayStats.MetaDataEntry)
    })
  ,

  'TxPacketsPerFrequencyEntry' : _reflection.GeneratedProtocolMessageType('TxPacketsPerFrequencyEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY,
    '__module__' : 'chirpstack_api.gw.gw_pb2'
    # @@protoc_insertion_point(class_scope:gw.GatewayStats.TxPacketsPerFrequencyEntry)
    })
  ,

  'RxPacketsPerFrequencyEntry' : _reflection.GeneratedProtocolMessageType('RxPacketsPerFrequencyEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY,
    '__module__' : 'chirpstack_api.gw.gw_pb2'
    # @@protoc_insertion_point(class_scope:gw.GatewayStats.RxPacketsPerFrequencyEntry)
    })
  ,

  'TxPacketsPerStatusEntry' : _reflection.GeneratedProtocolMessageType('TxPacketsPerStatusEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY,
    '__module__' : 'chirpstack_api.gw.gw_pb2'
    # @@protoc_insertion_point(class_scope:gw.GatewayStats.TxPacketsPerStatusEntry)
    })
  ,
  'DESCRIPTOR' : _GATEWAYSTATS,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.GatewayStats)
  })
_sym_db.RegisterMessage(GatewayStats)
_sym_db.RegisterMessage(GatewayStats.MetaDataEntry)
_sym_db.RegisterMessage(GatewayStats.TxPacketsPerFrequencyEntry)
_sym_db.RegisterMessage(GatewayStats.RxPacketsPerFrequencyEntry)
_sym_db.RegisterMessage(GatewayStats.TxPacketsPerStatusEntry)

PerModulationCount = _reflection.GeneratedProtocolMessageType('PerModulationCount', (_message.Message,), {
  'DESCRIPTOR' : _PERMODULATIONCOUNT,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.PerModulationCount)
  })
_sym_db.RegisterMessage(PerModulationCount)

UplinkRxInfoLegacy = _reflection.GeneratedProtocolMessageType('UplinkRxInfoLegacy', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPLINKRXINFOLEGACY_METADATAENTRY,
    '__module__' : 'chirpstack_api.gw.gw_pb2'
    # @@protoc_insertion_point(class_scope:gw.UplinkRxInfoLegacy.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _UPLINKRXINFOLEGACY,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.UplinkRxInfoLegacy)
  })
_sym_db.RegisterMessage(UplinkRxInfoLegacy)
_sym_db.RegisterMessage(UplinkRxInfoLegacy.MetadataEntry)

UplinkRxInfo = _reflection.GeneratedProtocolMessageType('UplinkRxInfo', (_message.Message,), {
  'DESCRIPTOR' : _UPLINKRXINFO,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.UplinkRxInfo)
  })
_sym_db.RegisterMessage(UplinkRxInfo)

DownlinkTxInfoLegacy = _reflection.GeneratedProtocolMessageType('DownlinkTxInfoLegacy', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLINKTXINFOLEGACY,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.DownlinkTxInfoLegacy)
  })
_sym_db.RegisterMessage(DownlinkTxInfoLegacy)

DownlinkTxInfo = _reflection.GeneratedProtocolMessageType('DownlinkTxInfo', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLINKTXINFO,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.DownlinkTxInfo)
  })
_sym_db.RegisterMessage(DownlinkTxInfo)

Timing = _reflection.GeneratedProtocolMessageType('Timing', (_message.Message,), {
  'DESCRIPTOR' : _TIMING,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.Timing)
  })
_sym_db.RegisterMessage(Timing)

ImmediatelyTimingInfo = _reflection.GeneratedProtocolMessageType('ImmediatelyTimingInfo', (_message.Message,), {
  'DESCRIPTOR' : _IMMEDIATELYTIMINGINFO,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.ImmediatelyTimingInfo)
  })
_sym_db.RegisterMessage(ImmediatelyTimingInfo)

DelayTimingInfo = _reflection.GeneratedProtocolMessageType('DelayTimingInfo', (_message.Message,), {
  'DESCRIPTOR' : _DELAYTIMINGINFO,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.DelayTimingInfo)
  })
_sym_db.RegisterMessage(DelayTimingInfo)

GPSEpochTimingInfo = _reflection.GeneratedProtocolMessageType('GPSEpochTimingInfo', (_message.Message,), {
  'DESCRIPTOR' : _GPSEPOCHTIMINGINFO,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.GPSEpochTimingInfo)
  })
_sym_db.RegisterMessage(GPSEpochTimingInfo)

UplinkFrame = _reflection.GeneratedProtocolMessageType('UplinkFrame', (_message.Message,), {
  'DESCRIPTOR' : _UPLINKFRAME,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.UplinkFrame)
  })
_sym_db.RegisterMessage(UplinkFrame)

UplinkFrameSet = _reflection.GeneratedProtocolMessageType('UplinkFrameSet', (_message.Message,), {
  'DESCRIPTOR' : _UPLINKFRAMESET,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.UplinkFrameSet)
  })
_sym_db.RegisterMessage(UplinkFrameSet)

DownlinkFrame = _reflection.GeneratedProtocolMessageType('DownlinkFrame', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLINKFRAME,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.DownlinkFrame)
  })
_sym_db.RegisterMessage(DownlinkFrame)

DownlinkFrameItem = _reflection.GeneratedProtocolMessageType('DownlinkFrameItem', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLINKFRAMEITEM,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.DownlinkFrameItem)
  })
_sym_db.RegisterMessage(DownlinkFrameItem)

DownlinkTxAck = _reflection.GeneratedProtocolMessageType('DownlinkTxAck', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLINKTXACK,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.DownlinkTxAck)
  })
_sym_db.RegisterMessage(DownlinkTxAck)

DownlinkTxAckItem = _reflection.GeneratedProtocolMessageType('DownlinkTxAckItem', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLINKTXACKITEM,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.DownlinkTxAckItem)
  })
_sym_db.RegisterMessage(DownlinkTxAckItem)

GatewayConfiguration = _reflection.GeneratedProtocolMessageType('GatewayConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _GATEWAYCONFIGURATION,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.GatewayConfiguration)
  })
_sym_db.RegisterMessage(GatewayConfiguration)

ChannelConfiguration = _reflection.GeneratedProtocolMessageType('ChannelConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELCONFIGURATION,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.ChannelConfiguration)
  })
_sym_db.RegisterMessage(ChannelConfiguration)

LoRaModulationConfig = _reflection.GeneratedProtocolMessageType('LoRaModulationConfig', (_message.Message,), {
  'DESCRIPTOR' : _LORAMODULATIONCONFIG,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.LoRaModulationConfig)
  })
_sym_db.RegisterMessage(LoRaModulationConfig)

FSKModulationConfig = _reflection.GeneratedProtocolMessageType('FSKModulationConfig', (_message.Message,), {
  'DESCRIPTOR' : _FSKMODULATIONCONFIG,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.FSKModulationConfig)
  })
_sym_db.RegisterMessage(FSKModulationConfig)

GatewayCommandExecRequest = _reflection.GeneratedProtocolMessageType('GatewayCommandExecRequest', (_message.Message,), {

  'EnvironmentEntry' : _reflection.GeneratedProtocolMessageType('EnvironmentEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY,
    '__module__' : 'chirpstack_api.gw.gw_pb2'
    # @@protoc_insertion_point(class_scope:gw.GatewayCommandExecRequest.EnvironmentEntry)
    })
  ,
  'DESCRIPTOR' : _GATEWAYCOMMANDEXECREQUEST,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.GatewayCommandExecRequest)
  })
_sym_db.RegisterMessage(GatewayCommandExecRequest)
_sym_db.RegisterMessage(GatewayCommandExecRequest.EnvironmentEntry)

GatewayCommandExecResponse = _reflection.GeneratedProtocolMessageType('GatewayCommandExecResponse', (_message.Message,), {
  'DESCRIPTOR' : _GATEWAYCOMMANDEXECRESPONSE,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.GatewayCommandExecResponse)
  })
_sym_db.RegisterMessage(GatewayCommandExecResponse)

RawPacketForwarderEvent = _reflection.GeneratedProtocolMessageType('RawPacketForwarderEvent', (_message.Message,), {
  'DESCRIPTOR' : _RAWPACKETFORWARDEREVENT,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.RawPacketForwarderEvent)
  })
_sym_db.RegisterMessage(RawPacketForwarderEvent)

RawPacketForwarderCommand = _reflection.GeneratedProtocolMessageType('RawPacketForwarderCommand', (_message.Message,), {
  'DESCRIPTOR' : _RAWPACKETFORWARDERCOMMAND,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.RawPacketForwarderCommand)
  })
_sym_db.RegisterMessage(RawPacketForwarderCommand)

ConnState = _reflection.GeneratedProtocolMessageType('ConnState', (_message.Message,), {
  'DESCRIPTOR' : _CONNSTATE,
  '__module__' : 'chirpstack_api.gw.gw_pb2'
  # @@protoc_insertion_point(class_scope:gw.ConnState)
  })
_sym_db.RegisterMessage(ConnState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024io.chirpstack.api.gwB\014GatewayProtoP\001Z-github.com/chirpstack/chirpstack/api/go/v4/gw'
  _GATEWAYSTATS_METADATAENTRY._options = None
  _GATEWAYSTATS_METADATAENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._options = None
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._options = None
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._options = None
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_options = b'8\001'
  _UPLINKRXINFOLEGACY_METADATAENTRY._options = None
  _UPLINKRXINFOLEGACY_METADATAENTRY._serialized_options = b'8\001'
  _GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY._options = None
  _GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY._serialized_options = b'8\001'
  _CODERATE._serialized_start=6090
  _CODERATE._serialized_end=6166
  _DOWNLINKTIMING._serialized_start=6168
  _DOWNLINKTIMING._serialized_end=6227
  _FINETIMESTAMPTYPE._serialized_start=6229
  _FINETIMESTAMPTYPE._serialized_end=6284
  _CRCSTATUS._serialized_start=6286
  _CRCSTATUS._serialized_end=6334
  _TXACKSTATUS._serialized_start=6337
  _TXACKSTATUS._serialized_end=6525
  _MODULATION._serialized_start=166
  _MODULATION._serialized_end=315
  _UPLINKTXINFOLEGACY._serialized_start=318
  _UPLINKTXINFOLEGACY._serialized_end=587
  _UPLINKTXINFO._serialized_start=589
  _UPLINKTXINFO._serialized_end=658
  _LORAMODULATIONINFO._serialized_start=661
  _LORAMODULATIONINFO._serialized_end=817
  _FSKMODULATIONINFO._serialized_start=819
  _FSKMODULATIONINFO._serialized_end=885
  _LRFHSSMODULATIONINFO._serialized_start=887
  _LRFHSSMODULATIONINFO._serialized_end=981
  _ENCRYPTEDFINETIMESTAMP._serialized_start=983
  _ENCRYPTEDFINETIMESTAMP._serialized_end=1069
  _PLAINFINETIMESTAMP._serialized_start=1071
  _PLAINFINETIMESTAMP._serialized_end=1133
  _GATEWAYSTATS._serialized_start=1136
  _GATEWAYSTATS._serialized_end=2052
  _GATEWAYSTATS_METADATAENTRY._serialized_start=1822
  _GATEWAYSTATS_METADATAENTRY._serialized_end=1869
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_start=1871
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_end=1931
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_start=1933
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_end=1993
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_start=1995
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_end=2052
  _PERMODULATIONCOUNT._serialized_start=2054
  _PERMODULATIONCOUNT._serialized_end=2125
  _UPLINKRXINFOLEGACY._serialized_start=2128
  _UPLINKRXINFOLEGACY._serialized_end=2768
  _UPLINKRXINFOLEGACY_METADATAENTRY._serialized_start=2703
  _UPLINKRXINFOLEGACY_METADATAENTRY._serialized_end=2750
  _UPLINKRXINFO._serialized_start=2771
  _UPLINKRXINFO._serialized_end=3140
  _DOWNLINKTXINFOLEGACY._serialized_start=3143
  _DOWNLINKTXINFOLEGACY._serialized_end=3657
  _DOWNLINKTXINFO._serialized_start=3660
  _DOWNLINKTXINFO._serialized_end=3823
  _TIMING._serialized_start=3826
  _TIMING._serialized_end=3981
  _IMMEDIATELYTIMINGINFO._serialized_start=3983
  _IMMEDIATELYTIMINGINFO._serialized_end=4006
  _DELAYTIMINGINFO._serialized_start=4008
  _DELAYTIMINGINFO._serialized_end=4067
  _GPSEPOCHTIMINGINFO._serialized_start=4069
  _GPSEPOCHTIMINGINFO._serialized_end=4146
  _UPLINKFRAME._serialized_start=4149
  _UPLINKFRAME._serialized_end=4349
  _UPLINKFRAMESET._serialized_start=4351
  _UPLINKFRAMESET._serialized_end=4458
  _DOWNLINKFRAME._serialized_start=4461
  _DOWNLINKFRAME._serialized_end=4610
  _DOWNLINKFRAMEITEM._serialized_start=4612
  _DOWNLINKFRAMEITEM._serialized_end=4739
  _DOWNLINKTXACK._serialized_start=4742
  _DOWNLINKTXACK._serialized_end=4891
  _DOWNLINKTXACKITEM._serialized_start=4893
  _DOWNLINKTXACKITEM._serialized_end=4945
  _GATEWAYCONFIGURATION._serialized_start=4948
  _GATEWAYCONFIGURATION._serialized_end=5102
  _CHANNELCONFIGURATION._serialized_start=5105
  _CHANNELCONFIGURATION._serialized_end=5361
  _LORAMODULATIONCONFIG._serialized_start=5363
  _LORAMODULATIONCONFIG._serialized_end=5431
  _FSKMODULATIONCONFIG._serialized_start=5433
  _FSKMODULATIONCONFIG._serialized_end=5490
  _GATEWAYCOMMANDEXECREQUEST._serialized_start=5493
  _GATEWAYCOMMANDEXECREQUEST._serialized_end=5709
  _GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY._serialized_start=5659
  _GATEWAYCOMMANDEXECREQUEST_ENVIRONMENTENTRY._serialized_end=5709
  _GATEWAYCOMMANDEXECRESPONSE._serialized_start=5711
  _GATEWAYCOMMANDEXECRESPONSE._serialized_end=5823
  _RAWPACKETFORWARDEREVENT._serialized_start=5825
  _RAWPACKETFORWARDEREVENT._serialized_end=5903
  _RAWPACKETFORWARDERCOMMAND._serialized_start=5905
  _RAWPACKETFORWARDERCOMMAND._serialized_end=5985
  _CONNSTATE._serialized_start=5987
  _CONNSTATE._serialized_end=6088
  _CONNSTATE_STATE._serialized_start=6056
  _CONNSTATE_STATE._serialized_end=6088
# @@protoc_insertion_point(module_scope)
