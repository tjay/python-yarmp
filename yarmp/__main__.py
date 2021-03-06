import logging as log, importlib as imp
from Queue import Queue, Empty
from .config import Config
from .devices import EvDevReceiver, RfidReceiver, MpdReceiver

log.basicConfig(filename="/var/log/yarmp.log",level=log.INFO, format='%(relativeCreated)6d %(threadName)s %(message)s')

queue = Queue()

# init control devices
EvDevReceiver(queue)
RfidReceiver(queue)
MpdReceiver(queue)

cm = imp.import_module('yarmp.controls')
controls = { c.lower(): getattr(cm,c,cm.Control)() for c in set(Config.controls.values()) }

log.info("Start")

while 42: # main loop
    try:
        event = queue.get(timeout=2)
        for c in controls.values(): c.handle(event)
    except Empty: pass
    except NotImplementedError as e:
        log.error("NotImplementedError %s" % e.message)
    except (KeyboardInterrupt, SystemExit):
        log.error("Exit on UserInterrupt")
        exit(0)
    except Exception as e:
        log.error("{}: {}".format(type(e).__name__, e))
        exit(1)