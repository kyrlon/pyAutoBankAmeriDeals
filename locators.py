from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class HomePageLocators:
    USERNAME_INPUT: tuple = (By.ID, 'onlineId1')
    PASSWORD_INPUT: tuple = (By.ID, 'passcode1')
    LOGIN_BUTTON: tuple = (By.ID, 'signIn')
    REMEMBER_ME_BOX: tuple = (By.ID, "saveOnlineId")
    ERROR: tuple = (By.CLASS_NAME, 'error-message')
    DISPLAY_NAME : tuple = (By.CLASS_NAME, 'DisplayName TL_NPI_L1 cnx-medium')


@dataclass
class CashBackLocators:
    CASHBACK_PAGE: str = "https://secure.bankofamerica.com/customer-deals/"
    CASHBACK_HOVER_LIST: tuple = (By.ID, 'fsd-li-cashback')
    CASHBACK_HOVER_SELECT: tuple = (By.LINK_TEXT, "Cash back deals")
    class_name = "load-available-deal available-deal columns small-6 medium-3 large-2 pbtm-20 fl-lt plt-20-s margin-top-17 dealtiles visible-deal"
    class_name = "." + class_name.replace(" ", ".")
    CASHBACK_CONTAINER: tuple = (By.CSS_SELECTOR, class_name)
    CASHBACK_ACTIVATED_STATUS: tuple = (By.CLASS_NAME, "status_text")
    CASHBACK_LOADING_STATUS: tuple = (By.CLASS_NAME, "close-icon-txt")
    # CASHBACK_LOADING_STATUS: tuple = (By.CLASS_NAME, "loading-status")
    COMPANY_DAYS_LEFT: tuple = (By.CLASS_NAME, "company_daysleft")
    DEAL_NAME: tuple = (By.CLASS_NAME, "company_name")
    DEAL_DETAILS: tuple = (By.CLASS_NAME, "col3_dealinfo")
    DEAL_INFO: tuple = (By.CLASS_NAME, "expansion_heading")
    DEAL_IMAGE: tuple = (By.CSS_SELECTOR, ".deal-tile.available-deals-wrapper")
    DEAL_EXTERNAL_LINK: tuple = (By.ID, "interstitialLinkLeavingSite")


@dataclass
class SignOnV2Locator:
    ANSWER_SECTION: tuple = (By.CLASS_NAME, "answer-section")
    QUESTION: tuple = (By.TAG_NAME, 'label')
    INPUT_ANSWER: tuple = (By.ID, 'tlpvt-challenge-answer')
    SUBMIT_BUTTON: tuple = (By.ID, 'verify-cq-submit')
    REMEMBER_RADIO: tuple = (By.ID, 'yes-recognize')