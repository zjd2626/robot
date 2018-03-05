#!/usr/bin/env python
#coding=utf-8
#__author__='David Chung'

import os
import logging
import logging.config
logging.config.fileConfig(os.path.abspath("../conf/log.conf"))
logger=logging.getLogger('regression')
