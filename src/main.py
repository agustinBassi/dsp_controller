#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""DSP Final Practice Project.

Author: Agustin Bassi
Date: April 2019.
"""
import logging

from wav_file import test_wav_file_class
from flanger_filter import test_flanger_filter_class

def main():
    """Main method to run DSP Project.
    """
    print("Running DSP Final Practice. Log level %d" % logging.DEBUG)

    logging.basicConfig(level = logging.DEBUG,
                        format = '%(levelname)s - %(message)s')

    #test_wav_file_class()
    test_flanger_filter_class()

main()