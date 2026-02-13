import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils

class Test_002_DDT_Login:
    baseURl=ReadConfig.getApplicationURL()
    path=".//TestData/login_results.xlsx"
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("********** Test_002_DDT_Login ************")
        self.logger.info("***** Verifying Login DDT Test ******")
        self.driver=setup
        self.driver.get(self.baseURl)
        self.lp=LoginPage(self.driver)

        self.rows=ExcelUtils.get_row_count(self.path,'Login Results')

        lst_status=[]   #EMPTY LIST VARIABLES

        for r in range(2,self.rows+1):
            self.username=ExcelUtils.read_data( self.path,'Login Results',r,1)
            self.Password = ExcelUtils.read_data(self.path, 'Login Results', r, 2)
            self.Results = ExcelUtils.read_data(self.path, 'Login Results', r, 3)

            self.lp.setUserName(str(self.user))
            self.lp.setPassword(str(self.password))
            self.lp.clickLogin()
            time.sleep(3)

            act_title=self.driver.title
            exp_title="OrangeHRM"

            if act_title==exp_title:
                if self.Results=="Pass":
                    self.logger.info("*************** Passed **********")
                    lst_status.append("Pass")

                elif self.Results=="Fail":
                    self.logger.info("**************** Failed ****************")
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.Results == "Pass":
                    self.logger.info("*********** Passed **********")
                    lst_status.append("Pass")

                elif self.Results == "Fail":
                    self.logger.info("************** Failed ************")
                    lst_status.append("Fail")


            if "Fail" not in lst_status:
                self.logger.info("*************** Login DDT Test Passed *************")
                self.driver.close()
                assert True
            else:
                self.logger.info("*************** Login DDT Test Failed *************")
                self.driver.close()
                assert False


        self.logger.info("*************** End of Login DDT Test  *************")
        self.logger.info("*************** Completed TC_Login_DDT_002 *************")