# -*- coding: utf-8 -*-
#!/usr/bin/env python3

#  **************************************************************************  #
#            .      .@@                                                        #
#           $@#.@#$..@$@`     $                                                #
#         `##@$@@@$$$#@$##@@@#                                                 #
#      $@@##@$$###$##@@@@@@#$$@@#                                              #
#     `#$$$##################@`                                                #
#     #$##^$################$#$       main.py                                  #
#    #$#<--->@#######$##########.                                              #
#    ####$v####.        `####$ #.     By: cdivry <cdivry@student.42.fr>        #
#    ####$####$`        .###  .                                                #
#     .########################                                                #
#      .$#$###################.                                                #
#        `#################$.                                                  #
#          `$$############$.`     Created: 2018/10/10 12:32:52 by cdivry       #
#            `#$##########.       Updated: 2018/10/10 12:32:52 by cdivry       #
#               `$#$$$$#$                                                      #
#                   ##$.                                                       #
#  **************************************************************************  #

import sys
import mne
import numpy
import time

def usage():
    print("USAGE: python " + sys.argv[0] + " <dataset.edf>")

def check_args():
    if len(sys.argv) != 2:
        usage()
        exit()

def read_dataset(filename):
    raw = mne.io.read_raw_edf(filename, preload=True)
    raw.set_eeg_reference('average', projection=True)  # set EEG average reference
    raw.plot(block=True, lowpass=40)


if __name__ == '__main__':
    check_args()
    filename = sys.argv[1]
    read_dataset(filename)
