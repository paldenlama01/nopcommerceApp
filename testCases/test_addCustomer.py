import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("*************** Test_003_AddCustomer *************")
        self.driver=setup
        self.driver.get(self.baseURl)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful *************")

        self.logger.info("*************** Starting Add Customer Test *************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenu()

        self.addcust.clickAddNew()

        self.logger.info("*************** Providing Customer INFO  *************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRole("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Palden")
        self.addcust.setLastName("SDET")
        self.addcust.setDob("7/20/1999") #Format: D/ MM /YYYY
        self.addcust.setCompanyName("Pal QA")
        self.addcust.setAdminContent("This is for testing...............")
        self.addcust.clickOnSave()

        self.logger.info("*************** Saving Customer info  *************")

        self.msg=self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if 'customer has been added successfully' in self.msg:
            assert True==True
            self.logger.info("*************** Add customer Test Passed *************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png") #Screenshot
            self.logger.info("*************** Add customer Test Failed *************")
            assert True==False




def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))
