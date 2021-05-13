def checkIfAvailable(driver):
    time.sleep(2)
    global message
    NameElementList = driver.find_elements_by_xpath('//*[@class="mat-main-field center-main-field"]/mat-selection-list/div[*]/mat-list-option/div/div[2]/ion-row/ion-col/div/h5')
    StatusElementList = driver.find_elements_by_xpath('//*[@class="mat-main-field center-main-field"]/mat-selection-list/div[*]/mat-list-option/div/div[2]/ion-row/ion-col[2]/ul/li[2]/div/div/a')
    statusList=[]
    message = ""
    # message += " [Vaccination Center Name]         [STATUS]\n"
    for name,status in zip(NameElementList, StatusElementList):
        message+= name.text + "  |  " + status.text + "\n"
        statusList.append(status.text)

    for status in statusList:
        if(status!="NA" and status!="Booked" and status!=""):
            return False
    return True
    


def sendMail(sender_email, receiver_mails, password, message):
    ######################## SMTP ###########################################
    smtp_server = "smtp.gmail.com"
    port = 587
    # Create a secure SSL context
    context = ssl.create_default_context()
    ########################################################################
    emailBody = f"""From: Vaccine Notification System <{sender_email}>
        To: Your given mail ID <{receiver_email}>
        MIME-Version: 1.0
        Content-type: text/html
        Subject: Vaccine Notification

        The information regarding the current slot status is:

        Vaccination Center    |    Status 
        {message}
    """

    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        print(emailBody)
        server.sendmail(sender_email, receiver_mails, emailBody)
    except :
        print("error in sending the mail")
    finally:
        server.quit


def Bot(driver):
    ############## DONT CHANGE THIS################################
    available=False
    message = ""
    driver.get("https://selfregistration.cowin.gov.in/appointment")
    driver.refresh()
    ###############################################################

    phoneNo = driver.find_element_by_xpath('//*[@id="mat-input-0"]')
    time.sleep(2)
    phoneNo.send_keys(PHONE)
    getOtp = driver.find_element_by_xpath('//*[@class="register-box register-main-box ng-star-inserted md hydrated"]/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[2]/div/ion-button')
    getOtp.click()
    try:
        #Schedule1
        schedule1 = WebDriverWait(driver, 3000).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="beneficiary-box md hydrated"]/ion-row[2]/ion-col/ion-grid/ion-row[4]/ion-col[2]/ul/li/a'))
        )
        time.sleep(2)
        schedule1.click()

        #Schedule2
        schedule2 = WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/app-beneficiary-dashboard/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid[1]/ion-row[4]/ion-col/div/div[2]/div/ion-button'))
        )
        time.sleep(2)
        schedule2.click()

        #pinCode
        pinCode = WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mat-input-2"]'))
        )
        time.sleep(2)
        pinCode.send_keys(PINCODE)
        

        #Check if available
        while(not available):
            available = not checkIfAvailable(driver)
            time.sleep(3)
            button = WebDriverWait(driver, 300).until(
                EC.presence_of_element_located((By.XPATH, '//*[@class="register-wrap"]/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[3]/ion-button'))
            )
            button.click()
            filter18 = WebDriverWait(driver, 300).until(
                EC.presence_of_element_located((By.XPATH, '//*[@class="padding-0 ng-star-inserted md hydrated"]/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[5]/div/div/label'))
            )
            time.sleep(2)
            filter18.click()

        sendMail(sender_email, receiver_email, password, message)

    except:
        Bot(driver)
    finally:
        driver.quit()


if __name__=="__main__":
    import time
    import sys
    import smtplib, ssl
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    # from selenium.webdriver.firefox.webdriver import WebDriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC


    ############# SELENIUM CONFIG- BRAVE#############################
    PATH = "/home/siddharthm10/Documents/dump/chromedriver"
    options = Options()
    ##Change this to your current browser :)
    options.binary_location = "/usr/bin/brave-browser-stable"
    driver = webdriver.Chrome(options = options, executable_path= PATH)
    ###############################################################


    ################USER CONFIG###################################
    PHONE = "123456789"
    PINCODE = "133456"
    sender_email = "abc@gmail.com"
    password = "pass123"
    receiver_email = ["email1@gmail.com", "email2@gmail.com"]
    ##############################################################

    message = ""
    Bot(driver)