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


class Svm40CmdGetSystemUpTimeBase(ShdlcCommand):
    """
    SHDLC command 0x93: "Get System Up Time".
    """

    def __init__(self, *args, **kwargs):
        super(Svm40CmdGetSystemUpTimeBase, self).__init__(
            0x93, *args, **kwargs)


class Svm40CmdGetSystemUpTime(Svm40CmdGetSystemUpTimeBase):

    def __init__(self):
        """
        Get System Up Time Command

        Get the system up time of the device.
        """
        super(Svm40CmdGetSystemUpTime, self).__init__(
            data=[],
            max_response_time=0.05,
            post_processing_time=0.0,
            min_response_length=4,
            max_response_length=4
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: The time since the last power-on or device reset in seconds.
        :rtype: int
        """
        system_up_time = int(unpack(">I", data[0:4])[0])  # uint32
        return system_up_time
