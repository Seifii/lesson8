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
#
# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

# import logging
# logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w")
# logging.debug("debug")
# logging.info("info")

import logging
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s")
try:
 print(10/0)
except Exception:
 logging.exception("Exception")