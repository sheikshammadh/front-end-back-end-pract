class InsuffientBalErr(Exception):
    def _init_(self,msg):
        self.msg=msg