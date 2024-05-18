from pathlib import Path

import json, os, html, re
from pathlib import Path
import base64
from datetime import datetime as dt

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from locators import HomePageLocators, CashBackLocators, SignOnV2Locator


class AutoBankAmeriDeals():
    # Load client ID and Secret values
    cred_path = Path.cwd() / "account_login.json"
    with open(cred_path, "r") as cred:
        account = json.load(cred)
        
    username = account["username"]
    password = account["password"]
    DRIVERS_DIR = Path(__file__).resolve().parent / "drivers"
    DRIVERS_DIR.mkdir(exist_ok=True)
    __WEB_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36 Edg/104.0.1293.70" ## agent src: https://www.whatismybrowser.com/guides/the-latest-user-agent/edge

    def __init__(self):
        self.deals_output = Path(__file__).resolve().parent / "output"
        self.deals_output.mkdir(exist_ok=True)
        self.load_json()

        WebDriverOptions = Options()
        WebDriverOptions.add_argument("--disable-extensions")
        WebDriverOptions.add_argument("--window-size=1280,1024")
        WebDriverOptions.add_argument("--log-level=3")
        WebDriverOptions.add_argument("--disable-notifications")
        WebDriverOptions.add_argument("disable-infobars")
        WebDriverOptions.add_argument("--disable-gpu")
        os.environ["SE_CACHE_PATH"] = str( self.DRIVERS_DIR)
        self.HEADLESS = False
        self.BANK_HOME = "https://www.bankofamerica.com/"
        if self.HEADLESS:
            WebDriverOptions.add_argument("--headless")
            WebDriverOptions.add_argument("user-agent=" + self.__WEB_USER_AGENT)
        
        self.driver = webdriver.Chrome(options=WebDriverOptions)
        self.driver.get('https://bankofamerica.com')
        self.driver.implicitly_wait(30)
    
    def quit(self):
        self.driver.close()

    def set_username(self, username):
         
        element = self.driver.find_element(*HomePageLocators.USERNAME_INPUT)
        element.send_keys(username)

    def set_password(self, password):
        element = self.driver.find_element(*HomePageLocators.PASSWORD_INPUT)
        element.click()
        self.click_remember_button()
        self.driver.implicitly_wait(1)
        element.send_keys(password, Keys.RETURN)

    def click_remember_button(self):
        tick = self.driver.find_element(*HomePageLocators.REMEMBER_ME_BOX)
        if not tick.is_selected():
            try:
                tick.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", tick)

    def sign_on_v2_page(self):
        #TODO
        
        question = self.driver.find_element(*SignOnV2Locator.ANSWER_SECTION).find_element(*SignOnV2Locator.QUESTION).text

        self.driver.find_element(*SignOnV2Locator.INPUT_ANSWER).send_keys(answer)

        #  if self.driver.current_url == "https://secure.bankofamerica.com/login/sign-in/entry/signOnV2.go":

        #     if not self.account['security_questions']:
        #         self.logger.error('Security questions not configured, cannot continue.')
        #         exit(1)

        #     self.logger.info('Security question detected for ' + self.account['name'] + '. Attempting sign in.')

        #     sign_on_v2 = SignOnV2Page(self.driver)

        #     question = sign_on_v2.get_question()

        #     my_answer = self.account['security_questions'][question]

        #     if not my_answer:
        #         self.logger.error('Could not find correct security question answer for account ' + self.account['name'])
        #         exit(1)

        #     sign_on_v2.insert_answer(my_answer)

        #     try:
        #         sign_on_v2.click_recognize()
        #     except NoSuchElementException:
        #         pass

        #     sign_on_v2.submit()

    def click_recognize(self):
        return self.driver.find_element(*SignOnV2Locator.REMEMBER_RADIO).click()

    def submit(self):
        self.driver.find_element(*SignOnV2Locator.SUBMIT_BUTTON).click()

    def goto_cashbacks(self):
        self.driver.get(CashBackLocators.CASHBACK_PAGE)

    def login(self):
        #works sometimes???
        self.set_username(self.username)
        self.set_password(self.password)
        # self.click_login_button()
        # self.sign_on_v2_page()

    def click_cashbacks_and_scrape(self):
        def expired_regex_extract(text):
            matches = re.findall(r'Exp\.\s(\d{1,2}/\d{1,2}/\d{2})', text)
            expiration_date = matches[0]
            return expiration_date

        element_container = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(CashBackLocators.CASHBACK_CONTAINER))

        for element in element_container:
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            element.click()

            offer_title = element.find_element(*CashBackLocators.DEAL_NAME).get_attribute('innerText').encode("utf-8").decode("utf-8")

            if not offer_title in self.deals_dict["DEALS"]:
                self.deals_dict["DEALS"][offer_title] = {}
                offer_daysleft = element.find_element(*CashBackLocators.COMPANY_DAYS_LEFT).get_attribute('innerText')
                expired = expired_regex_extract(element.get_attribute("innerText"))
                deal_details = element.find_element(*CashBackLocators.DEAL_DETAILS).get_attribute('innerText').encode("utf-8").decode("utf-8")
                expansion_heading = element.find_element(*CashBackLocators.DEAL_INFO).get_attribute('innerText').encode("utf-8").decode("utf-8")
                try:
                    offer_external = element.find_element(*CashBackLocators.DEAL_EXTERNAL_LINK)
                    link = offer_external.get_attribute("href")
                    txt = offer_external.get_attribute("innerText").encode("utf-8").decode("utf-8")
                except:
                    link = "N/A"
                    txt = "N/A"

                deal_pic = element.find_element(*CashBackLocators.DEAL_IMAGE)
                img_name = f"dealimg_{offer_title}.png"
                deal_pic.screenshot(img_name)
                binary = self.convert_png_to_binary(img_name)

                self.deals_dict["DEALS"][offer_title]["days_left"] = offer_daysleft
                self.deals_dict["DEALS"][offer_title]["expiration_date"] = expired
                self.deals_dict["DEALS"][offer_title]["deal_info"] = expansion_heading
                self.deals_dict["DEALS"][offer_title]["description"] = deal_details
                self.deals_dict["DEALS"][offer_title]["image_png"] = {"binary_data" : binary}
                self.deals_dict["DEALS"][offer_title]["external_link"] = {"text" : txt, "link": link}
                os.remove(img_name)
        self.evaluate_deals_metadata()
        with open(self.deals_output / "cashback_deals.json", "w", encoding="utf-8") as file_t:
            file_t.write(json.dumps(self.deals_dict, sort_keys=True, indent=4, ensure_ascii=False))
   
    def evaluate_deals_metadata(self):
        keys_to_remove = []
        for offer, value in self.deals_dict["DEALS"].items():
            exp_d_s = value["expiration_date"]
            exp_d = dt.strptime(exp_d_s, "%m/%d/%y")

            diff = exp_d - dt.now()
            days = diff.days
            seconds_in_day = 24 * 60 * 60
            if days < 0:
                keys_to_remove.append(offer)
            else:
                if diff.seconds % seconds_in_day == 0:
                    d_left = days
                else:
                    d_left = days + 1
                value["days_left"] = f"{d_left} day(s) left"
        
        for key in keys_to_remove:
            del self.deals_dict["DEALS"][key]

    def load_json(self):
        if (deals_json := self.deals_output / "cashback_deals.json").exists():
            with open(deals_json, "r", encoding="utf-8") as file_t:
                self.deals_dict = json.load(file_t)
            now = dt.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            self.deals_dict["1TIMESTAMP"]["MODIFIED"] = timestamp
        else:
            self.deals_dict = {}
            now = dt.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            self.deals_dict["1TIMESTAMP"] = {"CREATED":timestamp}
            self.deals_dict["DEALS"] = {}

    def generate_html(self):
        """
        Generates an HTML file with collapsible tree structure based on JSON data.

        This method reads JSON data from the 'cashback_deals.json' file, converts it to a collapsible tree structure,
        and generates an HTML file ('tree.html') that displays the tree structure. The HTML file includes
        buttons to open and close all collapsible elements using the details tag.
        """
    


        with open(self.deals_output / 'cashback_deals.json', encoding="utf-8") as json_file:
            data = json.load(json_file)

        html_tree = self.json_to_html(data)


        with open(self.deals_output / 'cashback_deals.html', 'w', encoding="utf-8") as html_file:
            html_file.write(f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Current Deals from Bank of America</title>
                <style>
                    .tree {{padding-left: 20px;}}
                    .tree li {{list-style-type: none;}}
                    .tree li:not(:last-child)::before {{content: "›"; margin-right: 5px;}}
                    .button-container {{
                      float: right;
                    }}
                    .button-container button {{
                      display: block;
                      margin-bottom: 10px;
                    }}
                </style>
                <script>
                    function toggleDetails(open) {{
                        var detailsList = document.getElementsByTagName('details');
                        for (var i = 0; i < detailsList.length; i++) {{
                            detailsList[i].open = open;
                        }}
                    }}
                </script>
            </head>
            <body>
                <div class="button-container">
                    <button onclick="toggleDetails(true)">Open all</button>
                    <button onclick="toggleDetails(false)">Close all</button>
                </div>
                {html_tree}
            </body>
            </html>
            """)

    def json_to_html(self, json_data):
        """
        This creates the structure of the html from the passed in json data.
        """
        html_content = "<ul class='tree'>"  # Open an unordered list
        for key, value in json_data.items():
            if isinstance(value, dict):  # If the data is a dictionary
                if key == "1TIMESTAMP":
                    html_content += "<details>"
                    html_content += "<summary>" + html.escape("TIMESTAMP") + "</summary>"
                    html_content += "<dl>"
                    for t, meta in value.items():
                        html_content += "<dt>" + html.escape(f"{t}") + "</dt>"
                        html_content += "<dd>" + html.escape(f" {meta}") + "</dd>"
                    html_content += "</dl>"
                    html_content += "</details>"
                else:
                    html_content += "<details>"
                    html_content += "<summary>" + html.escape(str(key)) + "</summary>"  # Add the key as a list item
                    for deal_name, deal_meta in value.items():
                        html_content += "<details>"
                        html_content += "<summary>" + html.escape(str(deal_name)) + "</summary>"
                        encoded_b2 = deal_meta["image_png"]["binary_data"]
                        decoded_b64 = b"".join([bytes(chr(int(encoded_b2[i:i + 8], 2)), "utf-8") for i in range(0, len(encoded_b2), 8)])
                        decoded_b64 = decoded_b64.decode()
                        html_content += f"<img src='data:image/png;base64,{decoded_b64}'>"
                        html_content += "<dl>"
                        html_content += "<dt>" + html.escape("Days Remaining") + "</dt>"
                        html_content += "<dd>" + html.escape(f" {deal_meta['days_left']}") + "</dd>"
                        html_content += "<dt>" + html.escape("Expiration Date") + "</dt>"
                        html_content += "<dd>" + html.escape(f" {deal_meta['expiration_date']}") + "</dd>"
                        html_content += "<dt>" + html.escape("Deal Info") + "</dt>"
                        html_content += "<dd>" + html.escape(f" {deal_meta['deal_info']}") + "</dd>"
                        html_content += "<dt>" + html.escape("Description") + "</dt>"
                        html_content += "<dd>" + html.escape(f" {deal_meta['description']}") + "</dd>"
                        html_content += "<dt>" + html.escape("External Deal Link") + "</dt>"
                        html_content += "<dd>" + f" <a href=\"{deal_meta['external_link']['link']}\" target=\"_blank\">{deal_meta['external_link']['text']}</a>" + "</dd>"
                        html_content += "</dl>"
                        html_content += "</details>"
                html_content += "</details>"
            else:
                html_content += "<details>"
                html_content += "<summary>" + html.escape(str(key)) + "</summary>"  # Add the key as a list item
                html_content += html.escape(str(value))
                html_content += "</details>"
        html_content += "</ul>"  # Close the unordered list
        return html_content

    def convert_png_to_binary(self, img_path):
        #https://stackoverflow.com/a/67242781/13642249
        with open(img_path, "rb") as f:
            png_encoded = base64.b64encode(f.read())

            encoded_b2 = "".join([format(n, '08b') for n in png_encoded])

        return encoded_b2

    def convert_binary_to_png(self, binary, img_path):
        encoded_b2 = binary
        decoded_b64 = b"".join([bytes(chr(int(encoded_b2[i:i + 8], 2)), "utf-8") for i in range(0, len(encoded_b2), 8)])
        with open('my_image_decoded.png', 'wb') as f:
            f.write(base64.b64decode(decoded_b64))

 
if __name__ == "__main__":
    obj = AutoBankAmeriDeals()
    obj.login()
    obj.goto_cashbacks()
    obj.click_cashbacks_and_scrape()
    obj.generate_html()