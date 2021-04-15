from pcaspy import SimpleServer, Driver
from pcaspy.tools import ServerThread


class EpicsServer():
    def __init__(self, prefix : str, pvdb : dict) -> None:
        self.isRunning = False

        self.server = SimpleServer()
        self.server.createPV(prefix=prefix, pvdb=pvdb)
        self.drv = Driver()
        self.server_thread = ServerThread(self.server)
    
    def __del__(self) -> None:
        self.stop()
    
    def start(self) -> None:
        if self.isRunning == False:
            self.server_thread.start()
            self.isRunning = True
    
    def stop(self) -> None:
        if self.isRunning:
            self.server_thread.stop()
    
    def emit(self, pv_name : str, value : float) -> None:
        self.drv.setParam(pv_name, value)
        self.drv.updatePVs()

