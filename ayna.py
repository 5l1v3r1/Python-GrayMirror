#!/usr/bin/env python
# -*- coding:utf-8 -*-

#########################################################
#         PYTHON - GRAY MIRROR - GH0ST S0FTWARE         #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################	

import numpy as np
import cv2 as ayna

goruntu_yakala = ayna.VideoCapture(0)

while(True):
    	ret, cerceve = goruntu_yakala.read()
    	bgr2gray = ayna.cvtColor(cerceve, ayna.COLOR_BGR2GRAY)
    	ayna.imshow('Python - Ayna | GH0ST-S0FTWARE',bgr2gray)
	if ayna.waitKey(1) & 0xFF == ord('q'):
		break

goruntu_yakala.release()
ayna.destroyAllWindows()
