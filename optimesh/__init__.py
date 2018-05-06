# -*- coding: utf-8 -*-
#
from __future__ import print_function

from .__about__ import (
    __version__,
    __author__,
    __author_email__,
    __website__,
    __status__,
    __license__,
    )

from .laplace import laplace
from .lloyd import (lloyd, lloyd_submesh)
from .odt import odt, odt_chen

# try:
#     import pipdate
# except ImportError:
#     pass
# else:
#     if pipdate.needs_checking(__name__):
#         print(pipdate.check(__name__, __version__), end='')
