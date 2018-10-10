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
#    ####$v####.        `####$ #.     By: cdivry <>                            #
#    ####$####$`        .###  .                                                #
#     .########################                                                #
#      .$#$###################.                                                #
#        `#################$.                                                  #
#          `$$############$.`     Created: 2018/10/10 12:32:52 by cdivry       #
#            `#$##########.       Updated: 2018/10/10 12:32:52 by cdivry       #
#               `$#$$$$#$                                                      #
#                   ##$.                                                       #
#  **************************************************************************  #

import mne
import numpy
import time

def read_dataset(filename):
    raw = mne.io.read_raw_edf(filename, preload=True)
    raw.set_eeg_reference('average', projection=True)  # set EEG average reference
    raw.plot(block=True, lowpass=40)
    time.sleep(5)


if __name__ == '__main__':

    filename = u'dataset/test_eeg.edf'
    read_dataset('dataset/test_eeg.edf')
