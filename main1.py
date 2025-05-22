# n = int(input())
# k = int(0)
# if( n == 0):
#     print(1)
# else:
#     while n>0:
#         n = n//10
#         k += 1
#     print(k)
#

import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")