from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

xpathDict = {
    "sizeOptions": "/html/body/div/div[2]/div/div/div[1]/form/div[3]/div/div/label/div[2]/select",
    "extraEspresso": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[1]/div/fieldset/div/div",
    "decafEspresso": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[1]/div/fieldset/div[3]/div",
    "singleOriginEspresso": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[1]/div/fieldset/div[4]/div",
    "whole": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[2]/div/fieldset/div[2]/div",
    "almond": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[2]/div/fieldset/div[3]/div",
    "oat": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[2]/div/fieldset/div[4]/div",
    "halfandhalf": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[2]/div/fieldset/div[5]/div",
    "light": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[2]/div/fieldset/div[6]/div",
    "extra": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[2]/div/fieldset/div[7]/div",
    "maple": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[3]/div/fieldset/div[2]/div",
    "vanilla": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[3]/div/fieldset/div[3]/div",
    "honey": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[3]/div/fieldset/div[4]/div",
    "mocha": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[3]/div/fieldset/div[5]/div",
    "lavendar": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[3]/div/fieldset/div[6]/div",
    "sugar": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[3]/div/fieldset/div[7]/div",
    "simple": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[3]/div/fieldset/div[8]/div",
    "splenda": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[3]/div/fieldset/div[9]/div",
    "xtra": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[3]/div/fieldset/div[10]/div",
    "half": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[3]/div/fieldset/div[11]/div",
    "no": "/html/body/div/div[2]/div/div/div[1]/form/div[4]/div[3]/div/fieldset/div[12]/div",
    "addToCart": "/html/body/div/div[2]/div/div/div[3]/div/div[1]/form[2]/button",
    "continueShopping": "/html/body/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/form/div[1]/div[3]/div[2]/div",
    "checkout": "/html/body/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/button",
    "email": "/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[2]/div/div[1]/div/section[1]/form/fieldset",
    "first": "/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[2]/div/div[1]/div/section[2]/div[1]/form/fieldset/div[1]/label[1]/input",
    "last": "/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[2]/div/div[1]/div/section[2]/div[1]/form/fieldset/div[1]/label[2]/input",
    "phone": "/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[2]/div/div[1]/div/section[2]/div[1]/form/fieldset/div[2]/label[2]/input",
    "nextButton": "/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[2]/div/div[1]/div/section[3]/fieldset/button",
    "nextButton2": "/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[2]/div/div[3]/div/section/section/button",
    "cardFrame": "/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[2]/div/div[4]/div/section[1]/div[3]/form/fieldset/div[2]/label/div/div/div/iframe",
    "cardNumber": "/html/body/div/div[2]/div[1]/input",
    "cardExp": "/html/body/div/div[2]/div[2]/input[1]",
    "cvv": "/html/body/div/div[2]/div[2]/input[2]",
    "zip": "/html/body/div/div[2]/div[2]/input[3]",
    "nextButton3": "/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div[2]/div/div[4]/div/section[3]/div/div[3]/button"
}

sizeDict = {
    "8oz": "8 oz",
    "12oz": "12 oz",
    "16oz": "16 oz",
    "20oz": "20 oz",
    "8ozHot": "8 oz HOT",
    "12ozHot": "12 oz HOT",
    "16ozHot": "16 oz HOT",
    "20ozHot": "20 oz HOT",
    "12ozIced": "12 oz ICED",
    "16ozIced": "15 oz ICED",
    "20ozIced": "20 oz ICED"
}

#inputs: order details, array of items in the order as seen in firebase
def lamplighterOrder(order, items, user):
    DRIVER_PATH = './chromedriver'
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get('https://lamplighter-coffee-roasters.square.site/drinks')

    #item count to keep track of index of arrays
    itemCount = 0
    try:
        for item in items:
            #select item by name
            name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, item.get('xpath'))))
            name.click()

            #select size
            sizeOptions = Select(WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("sizeOptions")))))
            sizeOptions.select_by_visible_text(sizeDict.get(order[itemCount].get("size")))

            #select Milk
            for milk in order[itemCount].get("milk"):
                milkSelect = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get(milk))))
                milkSelect.click()

            #extra Espresso or steamed milk (have the same xpath)
            if order[itemCount].get("extraEspresso") or order[itemCount].get("steamedMilk"):
                extraEspresso = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("extraEspresso"))))
                extraEspresso.click()

            #espressoOptions
            if order[itemCount].get("decafEspresso"):
                decafEspresso = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("decafEspresso"))))
                decafEspresso.click()

            if order[itemCount].get("singleOriginEspresso"):
                singleOriginEspresso = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("singleOriginEspresso"))))
                singleOriginEspresso.click()

            #select Sweeteners
            for sweetener in order[itemCount].get("sweetener"):
                sweetenerSelect = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get(sweetener))))
                sweetenerSelect.click()


            #add to cart
            addToCart = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("addToCart"))))
            addToCart.click()

            itemCount += 1
            if itemCount == len(items):
                break
            else:
                continueShopping = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("continueShopping"))))
                continueShopping.click()

        #click checkout Button
        checkout = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("checkout"))))
        checkout.click()

        #details form
        email = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("email"))))
        email.click()
        email.send_keys(user.get("email"))

        first = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("first"))))
        first.click()
        first.send_keys(user.get("first"))

        last = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("last"))))
        last.click()
        last.send_keys(user.get("last"))

        phone = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("phone"))))
        phone.click()
        phone.send_keys(user.get("phone"))


        #click next buttons
        next = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("nextButton"))))
        next.click()

        next2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("nextButton2"))))
        next2.click()

        #card info
        iframe = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("cardFrame"))))
        driver.switch_to.frame(iframe)

        cardNum = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("cardNumber"))))
        cardNum.click()
        cardNum.send_keys("5555555555555555")

        cardExp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("cardExp"))))
        cardExp.click()
        cardExp.send_keys("5555")

        cvv = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("cvv"))))
        cvv.click()
        cvv.send_keys("555")

        zip = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("zip"))))
        zip.click()
        zip.send_keys("23220")

        # switch to default frame and select next
        driver.switch_to.default_content()

        next3 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathDict.get("nextButton3"))))
        next3.click()


    except Exception as e:
        print("ERRRROOR", str(e))
    finally:
        print("Quit driver")

    return "success"