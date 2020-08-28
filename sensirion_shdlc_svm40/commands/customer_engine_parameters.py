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
# Version:      0.2.0
#
##############################################################################
##############################################################################

# flake8: noqa

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_driver.command import ShdlcCommand
from struct import pack, unpack

import logging
log = logging.getLogger(__name__)


class Svm40CmdCustomerEngineParametersBase(ShdlcCommand):
    """
    SHDLC command 0x60: "Customer Engine Parameters".
    """

    def __init__(self, *args, **kwargs):
        super(Svm40CmdCustomerEngineParametersBase, self).__init__(
            0x60, *args, **kwargs)


class Svm40CmdGetTOffset(Svm40CmdCustomerEngineParametersBase):

    def __init__(self):
        """
        Get T Offset Command

        Gets the customer T-Offset for the temperature compensation.
        """
        super(Svm40CmdGetTOffset, self).__init__(
            data=b"".join([bytes(bytearray([0x01]))]),
            max_response_time=0.05,
            post_processing_time=0.0,
            min_response_length=4,
            max_response_length=4
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: Customer temperature offset in degrees celsius.
        :rtype: float
        """
        t_offset = float(unpack(">f", data[0:4])[0])  # float
        return t_offset


class Svm40CmdStoreNvData(Svm40CmdCustomerEngineParametersBase):

    def __init__(self):
        """
        Store Nv Data Command

        Stores all customer engine parameters to the non-volatile memory.
        """
        super(Svm40CmdStoreNvData, self).__init__(
            data=b"".join([bytes(bytearray([0x80]))]),
            max_response_time=0.1,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )


class Svm40CmdSetTOffset(Svm40CmdCustomerEngineParametersBase):

    def __init__(self, t_offset):
        """
        Set T Offset Command

        Sets the customer T-Offset for the temperature compensation.

        .. note:: Execute the store command after writing the parameter to
                  store it in the non-volatile memory of the device otherwise
                  the parameter will be reset upton a device reset.

        :param float t_offset:
            Customer temperature offset in degrees celsius.
        """
        super(Svm40CmdSetTOffset, self).__init__(
            data=b"".join([bytes(bytearray([0x81])),
                           pack(">f", t_offset)]),
            max_response_time=0.05,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )