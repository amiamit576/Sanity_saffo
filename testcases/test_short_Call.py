from pageObject.Call import Short_call




class Test_ShortCall:




    def test_shrt_call(self,setup):
        self.driver=setup
        self.obj=Short_call(self.driver)
        self.obj.make_call('9871052407')
        self.obj.sucess_call(4)








