# -*- coding: utf-8 -*-

"""Interfaz para zi.ma en Turpial"""
#
# Author: Wil Alvarez (aka Satanas)
# Abr 19, 2010

import traceback

from turpial.api.interfaces.generic import GenericService
from turpial.api.interfaces.generic import ServiceResponse

class ZimaURLShorter(GenericService):
    def __init__(self):
        GenericService.__init__(self)
        self.base = "http://zi.ma/?module=ShortURL&file=Add&mode=API&url=%s"
        
    def do_service(self, longurl):
        longurl = self._quote_url(longurl)
        req = self.base % longurl
        try:
            resp = self._get_request(req)
            return ServiceResponse(resp)
        except Exception, error:
            self.log.debug("Error: %s\n%s" % (error, traceback.print_exc()))
            return ServiceResponse(err=True, err_msg=_('Problem shorting URL'))
