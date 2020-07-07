# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

##############################################################################
##############################################################################
#                 _____         _    _ _______ _____ ____  _   _
#                / ____|   /\  | |  | |__   __|_   _/ __ \| \ | |
#               | |       /  \ | |  | |  | |    | || |  | |  \| |
#               | |      / /\ \| |  | |  | |    | || |  | | . ` |
#               | |____ / ____ \ |__| |  | |   _| || |__| | |\  |
#                \_____/_/    \_\____/   |_|  |_____\____/|_| \_|
#
#     THIS FILE IS AUTOMATICALLY GENERATED AND MUST NOT BE EDITED MANUALLY!
#
# Generator:    sensirion-shdlc-interface-generator 0.6.1
# Product:      SVM40
# Version:      0.1.0
#
##############################################################################
##############################################################################

# flake8: noqa

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_driver.command import ShdlcCommand
from struct import pack, unpack

import logging
log = logging.getLogger(__name__)


class Svm40CmdDeviceInformationBase(ShdlcCommand):
    """
    SHDLC command 0xD0: "Device Information".
    """

    def __init__(self, *args, **kwargs):
        super(Svm40CmdDeviceInformationBase, self).__init__(
            0xD0, *args, **kwargs)


class Svm40CmdGetProductType(Svm40CmdDeviceInformationBase):

    def __init__(self):
        """
        Get Product Type Command

        Gets the product type from the device.
        """
        super(Svm40CmdGetProductType, self).__init__(
            data=b"".join([bytes(bytearray([0x00]))]),
            max_response_time=0.5,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=255
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: String containing the product type.
        :rtype: str
        """
        product_type = str(data[0:].decode('utf-8').rstrip('\0'))  # string
        return product_type


class Svm40CmdGetProductName(Svm40CmdDeviceInformationBase):

    def __init__(self):
        """
        Get Product Name Command

        Gets the product name from the device.
        """
        super(Svm40CmdGetProductName, self).__init__(
            data=b"".join([bytes(bytearray([0x01]))]),
            max_response_time=0.5,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=255
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: String containing the product name.
        :rtype: str
        """
        product_name = str(data[0:].decode('utf-8').rstrip('\0'))  # string
        return product_name


class Svm40CmdGetSerialNumber(Svm40CmdDeviceInformationBase):

    def __init__(self):
        """
        Get Serial Number Command

        Gets the serial number from the device.
        """
        super(Svm40CmdGetSerialNumber, self).__init__(
            data=b"".join([bytes(bytearray([0x03]))]),
            max_response_time=0.5,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=255
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: String containing the serial number.
        :rtype: str
        """
        serial_number = str(data[0:].decode('utf-8').rstrip('\0'))  # string
        return serial_number
