#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import necessary packages

class Logger:
    def __init__(self,filePath,loggername):
        self.filename = filePath
        self.loggerName = loggername

    def writeLog(self):
        """
        *This function will log the process happening in the system.
            The process happening in this code block is mentioned below:
            1. create file handler which logs even debug messages
            2. create console handler with a higher log level
            3. create formatter and add it to the handlers
            4. add the handlers to the logger
            5. returns logger

        """
        "code here"
