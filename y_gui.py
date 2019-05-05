import y_log
import y_air_ticket

w2l = y_log.clog(__name__ == "__main__")

class airgui:
    def __init__(self):
        pass

    def test(self):
        pass
        
def run_entry():
    w2l.info("{0} run.".format(__name__))

def module_entry():
    w2l.info("{0} module run.".format(__name__))

if __name__ == "__main__":
    run_entry()
else:
    module_entry()
