'''
日志模块

作者：陈毅翀
'''

import logging
import logging.handlers
import os
import sys
import platform
import time
import y_mail

def get_default_log():
    return logging.getLogger(os.path.split(os.path.splitext(sys.argv[0])[0])[-1])

def init_default_log(log):
    log.setLevel(logging.DEBUG)
    logfile = os.path.join(os.path.dirname(sys.argv[0]), 
                           'log', 
                           '{0}.{1}.{2}.{3}'.format(os.path.basename(sys.argv[0]), 
                                                    time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())), 
                                                    os.getpid(),
                                                    'log'))

    #print('init logfile %s' % (logfile))

    if not os.path.exists(os.path.dirname(logfile)):
            os.makedirs(os.path.dirname(logfile))

    file_fmt = logging.Formatter('%(levelname)-10s %(module)-20s %(funcName)-30s %(lineno)-6d %(thread)-8d  %(asctime)s : %(message)s')
    fh = logging.FileHandler(logfile)
    fh.setFormatter(file_fmt)

    con_fmt = logging.Formatter('%(module)-12s  %(lineno)-4d  %(asctime)s : %(message)s')
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(con_fmt)

    log.addHandler(fh)
    log.addHandler(ch)

#w2l = get_default_log()

#日志准备操作，放在程序的入口处
#if __name__ == "__main__":
#    init_default_log(w2l)

class clog(logging.Logger):
    '''日志记录类，对logging做简单的封装，日志默认路径在当前程序的log目录下'''
    mailsended = False
    def __init__(self, 
                 initflag = False,
                 logname = os.path.split(os.path.splitext(sys.argv[0])[0])[-1],
                 logfile = os.path.join(os.path.dirname(sys.argv[0]), 
                                        'log', 
                                        '{0}.{1}.{2}.{3}'.format(os.path.basename(sys.argv[0]), 
                                                                 time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())), 
                                                                 os.getpid(),
                                                                 'log'))
                ):
        '''日志类构造函数'''
        super(clog, self).__init__(self)

        self.logfile = logfile
        
        if not os.path.isabs(logfile):
            logfile = os.path.join(os.path.dirname(sys.argv[0]), logfile)

        if not os.path.exists(os.path.dirname(logfile)):
            os.makedirs(os.path.dirname(logfile))
            
        self.logger = logging.getLogger(logname)

        if initflag:

            print('log name %s, log file %s' % (logname, logfile))

            self.logger.setLevel(logging.DEBUG)

            file_fmt = logging.Formatter('%(name)-12s level(%(levelname)-8s) thread(%(thread)d)  %(asctime)s : %(message)s')
            fh = logging.FileHandler(logfile)
            fh.setFormatter(file_fmt)

            con_fmt = logging.Formatter('%(module)-12s  %(lineno)d  %(asctime)s : %(message)s')
            ch = logging.StreamHandler(sys.stdout)
            ch.setFormatter(con_fmt)

            self.logger.addHandler(fh)
            self.logger.addHandler(ch)


    #def __del__(self):
    #    '''日志类析构函数'''
    #    #super(clog, self).__del__(self)
    #    pass

    def _send_log(self, msg):
        # 进程生存期内，错误日志，只需要用邮件发送一次，其它的错误不发送了，避免邮件过多
        if clog.mailsended:
            return
        
        sub = '票务运行错误 ' + time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        if platform.system() == 'Linux':
        #if platform.system() == 'Windows':
            print(platform.system())
            yemail = y_mail.y_status_email(sub)
            content = msg + os.linesep + os.linesep + os.linesep
            content = content + platform.system() + os.linesep
            content = content + time.strftime("%Y-%m-%d %H:%M:%S %A(%w)",time.localtime(time.time())) + os.linesep
            content = content + 'logfile : ' + os.path.abspath(self.logfile)
            yemail.send_msg(content)
            clog.mailsended = True

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)
        self._send_log(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)
        self._send_log(msg)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)
        

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def log(self, msg, *args, **kwargs):
        self.logger.log(msg, *args, **kwargs)

w2l = clog(__name__ == "__main__")

def run_entry():
    w2l.info("{0} run.".format(__name__) )

def module_entry():
    w2l.info("{0} module run.".format(__name__))

if __name__ == "__main__":
    run_entry()
else:
    module_entry()