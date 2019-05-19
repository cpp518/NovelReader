# -*- utf-8 -*-

#继承多线程类

import threading
import crawl.biquge

class Mythread(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemin=None):
        threading.Thread.__init__(group, target, name, args, kwargs, daemin=None)
        self._return_value = None

    def run(self):
        # 重新定义Thread类里的run方法
        try:
            if self._target:
                self._return_value = self._target(*args, **kwargs)  # 把原来的self._target方法返回值赋给self._return_value
        finally:
            del self._target, self._args, self._kwargs

    def join(self, timeout=None):
        # 重新定义join方法，等待线程执行完成，返回值
        threading.Thread.join(self, timeout)  # 调用原类的join方法，原方法中调用Thread类外方法，所以不能直接重写。
        return self._return_value




class Allweb():

        def __init__(self,novelName):
            self.web = []
            self.web.append(crawl.biquge.biquge(novelName))

        def GetWeb(self):
            if None in self.web:
                self.web.remove(None)
            return self.web

