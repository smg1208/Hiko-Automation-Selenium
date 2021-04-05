from selenium.webdriver.common.by import By

class ge(object):
    # DOMAIN = 'http://v2.fabet.info/'
    DOMAIN = 'http://dev-ta.mooo.com/'
    ProjectName = 'TopAsia'
    

class MainMenuLocators(object):
    MENU_THE_THAO = (By.CLASS_NAME,'menu-sports')
    MENU_BAN_CA = (By.CLASS_NAME,'menu-fishing')
    MENU_LIVE_CASINO = (By.CLASS_NAME,'menu-casino')
    MENU_QUICK_GAME = (By.CLASS_NAME,'menu-quickGames')
    MENU_TABLE_GAME = (By.CLASS_NAME,'menu-tablegame')
    MENU_CONG_GAME = (By.CLASS_NAME,'menu-cong-game')    
    MENU_DANG_NHAP = (By.CLASS_NAME,'not-login-user-login')
    MENU_DANG_KY = (By.CLASS_NAME,'not-login-user-register')
    MENU_USER_INFO_DROP = (By.XPATH,'//div[@class="info-user"]')


class CongGameLocators(object):
    Type_All = (By.CLASS_NAME,'icon-all')
    Type_No_hu = (By.CLASS_NAME,'icon-nohu1')
    Type_Ban_ca = (By.CLASS_NAME,'icon-banca')
    Type_Lo_de = (By.CLASS_NAME,'icon-lode1')
    Type_Ingame = (By.CLASS_NAME,'icon-in-game1')
    Type_Table_game = (By.CLASS_NAME,'icon-table-game1')
    Type_Game_nhanh = (By.CLASS_NAME,'icon-game-nhanh1')

    NCC_selector = (By.CLASS_NAME,'btn-secondary')
    NCC_btn_All = (By.XPATH,'//div/ul/li[1][@role="presentation"]')
    NCC_btn_Techplay = (By.XPATH,'//input[@value="vingame"]/parent::div/parent::label/parent::a/parent::li')
    NCC_btn_PragmaticPlay = (By.XPATH,'//input[@value="pragmatic"]/parent::div/parent::label/parent::a/parent::li')
    NCC_btn_CQ9 = (By.XPATH,'//input[@value="cq9"]/parent::div/parent::label/parent::a/parent::li')
    NCC_btn_Tomhorn = (By.XPATH,'//input[@value="tomhorn"]/parent::div/parent::label/parent::a/parent::li')
    NCC_btn_PlaynGo = (By.XPATH,'//input[@value="playngo"]/parent::div/parent::label/parent::a/parent::li')

    Sort_Nhieu_nguoi_choi = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][1]')
    Sort_Dang_hot = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][2]')
    Sort_Pho_bien = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][3]')
    Sort_Moi_nhat = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][4]')
    Sort_a_z = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][5]')

    List_Game = (By.XPATH,'//div[contains(@class,"game-list")]/div')
    List_Game_Heading = (By.XPATH, '//h1[contains(@class,"game-section__title")]')

class CasinoLocators(object):
    NCC_All = (By.CLASS_NAME,'game-menu-item-icon__tab')
    NCC_Evolution = (By.XPATH,'//div[contains(@class,"game-menu-item")][2]')
    NCC_Ebet = (By.XPATH,'//div[contains(@class,"game-menu-item")][3]')
    NCC_Vivo = (By.XPATH,'//div[contains(@class,"game-menu-item")][4]')
    NCC_Allbet = (By.XPATH,'//div[contains(@class,"game-menu-item")][5]')
    NCC_HGaming = (By.XPATH,'//div[contains(@class,"game-menu-item")][6]')    

    Game_selector = (By.CLASS_NAME,'btn-secondary')
    Game_Baccarat = (By.XPATH,'//input[@value="baccarat"]/parent::div/parent::label/parent::a/parent::li')
    Game_Sicbo = (By.XPATH,'//input[@value="sicbo"]/parent::div/parent::label/parent::a/parent::li')
    Game_Roulette = (By.XPATH,'//input[@value="roulette"]/parent::div/parent::label/parent::a/parent::li')

    Sort_Nhieu_nguoi_choi = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][1]')
    Sort_Dang_hot = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][2]')
    Sort_Pho_bien = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][3]')
    Sort_Moi_nhat = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][4]')
    Sort_a_z = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][5]')

    List_Game = (By.XPATH,'//div[contains(@class,"lobby-casino-list")]/div')
    List_Game_Heading = (By.CLASS_NAME, 'lobby-casino-section__title')

class LoginLocators(object):
    input_username = (By.XPATH,'//form/div[1]/div/input')
    input_password = (By.XPATH,'//form/div[2]/div/input')

    text_error_username = (By.XPATH,'//form/div[1]/p[@class="error"]')
    text_error_password = (By.XPATH,'//form/div[2]/p[@class="error"]')

    btn_show_password = (By.CLASS_NAME,'icon-eye-hide')
    btn_hide_password = (By.CLASS_NAME,'icon-eye-show')
    btn_login = (By.CLASS_NAME,'login-form__submit')
    btn_close = (By.CLASS_NAME,'close-user-modal')

    popup_error = (By.XPATH, '//div[@class="swal-modal"]')
    popup_error_title = (By.XPATH, '//div[@class="swal-title"]')
    popup_error_content = (By.XPATH, '//div[@class="swal-text"]')
    popup_error_btn_confirm = (By.CLASS_NAME, 'swal-button--confirm')

class SignupLocators(object):
    username = (By.XPATH,'//form/div[1]/div/input')
    password = (By.XPATH,'//form/div[2]/div/input')
    re_password = (By.NAME,'confirmPassword')
    phoneno = (By.NAME,'phoneNumber')
    invite_code = (By.XPATH,'//form/div[5]/div/input')

    username_error = (By.XPATH,'//form/div[1]/p[@class="error"]')
    password_error = (By.XPATH,'//form/div[2]/p[@class="error"]')
    re_password_error = (By.XPATH,'//form/div[3]/p[@class="error"]')
    phoneno_error = (By.XPATH,'//form/div[4]/p[@class="error"]')

    show_pass = (By.XPATH,'//form/div[2]/div/span')
    hide_pass = (By.XPATH,'//form/div[2]/div/span')
    show_repass = (By.XPATH,'//form/div[3]/div/span')
    hide_repass = (By.XPATH,'//form/div[3]/div/span')

    btn_register = (By.CLASS_NAME,'register-form__submit')
    btn_close = (By.CLASS_NAME,'close-user-modal')
    btn_agree = (By.CLASS_NAME,'checkmark')

    popup_error = (By.XPATH, '//div[@class="swal-modal"]')
    popup_error_title = (By.XPATH, '//div[@class="swal-title"]')
    popup_error_content = (By.XPATH, '//div[@class="swal-text"]')
    popup_error_btn_confirm = (By.CLASS_NAME, 'swal-button--confirm')


class UserInfoLocator(object):
    # DROP DOWN MENU
    drop_info = (By.XPATH,'//ul/div/li[@role="presentation"][1]')
    drop_nap_tien = (By.XPATH,'//ul/div/li[@role="presentation"][2]')
    drop_rut_tien = (By.XPATH,'//ul/div/li[@role="presentation"][3]')
    drop_lich_su = (By.XPATH,'//ul/div/li[@role="presentation"][4]')
    drop_khuyen_mai = (By.XPATH,'//ul/div/li[@role="presentation"][5]')
    drop_tin_tuc = (By.XPATH,'//ul/div/li[@role="presentation"][6]')
    drop_logout = (By.XPATH,'//ul/div[@class="logout"]')
    drop_username = (By.XPATH,'//div[@class="user-name"]/span')

    # LEFT MENU
    btn_userinfo = (By.XPATH,'//span[@class="icon-information"]/parent::a/parent::li')
    btn_nap = (By.XPATH,'//span[@class="icon-deposit"]/parent::a/parent::li')
    btn_rut = (By.XPATH,'//span[@class="icon-withdraw"]/parent::a/parent::li')
    btn_history = (By.XPATH,'//span[@class="icon-history"]/parent::a/parent::li')
    btn_promotion = (By.XPATH,'//span[@class="icon-promotion"]/parent::a/parent::li')
    btn_logout = (By.CLASS_NAME,'menu-info__logout')    
    txt_username = (By.CLASS_NAME,'menu-info__name')

    # TAB
    tab_info = (By.XPATH,'//ul/li[@class="nav-item"][1]')
    tab_changepass = (By.XPATH,'//ul/li[@class="nav-item"][2]')
    tab_bankaccount = (By.XPATH,'//ul/li[@class="nav-item"][3]')

    # CẬP NHẬT THÔNG TIN CÁ NHÂN
    info_name = (By.XPATH,'//div/div[1]/div/input')
    info_name_error = (By.XPATH,'//div/div[1]/p[@class="error"]')
    info_email = (By.XPATH,'//div/div[2]/div/input')
    info_email_error = (By.XPATH,'//div/div[2]/p[@class="error"]')
    info_email_authen = (By.XPATH,'//div/div[2]/div/p[@class="info-personal__authen"')
    info_phone = (By.XPATH,'//div/div[3]/div/input')
    info_phone_authen = (By.XPATH,'//div/div[3]/div/p[@class="info-personal__authen"')
    info_confirm = (By.XPATH,'//div[@class="tab-content"]/div/div/div/div/button')

    # CONFIRM POPUP
    popup_cf = (By.ID, 'authen-email___BV_modal_content_')
    popup_cf_title = (By.CLASS_NAME, 'modal__content__title')
    popup_cf_content = (By.CLASS_NAME, 'content-form__desc')
    popup_cf_btn_confirm = (By.XPATH, '//div[@class="modal__content__inner"]/div/div/button')
    popup_cf_close = (By.CLASS_NAME,'icon-close')
    popup_cf_resend = (By.XPATH,'//p[@class="content-form__note"]/span')

    # ERROR POPUP
    popup_error = (By.XPATH, '//div[@class="swal-modal"]')
    popup_error_title = (By.XPATH, '//div[@class="swal-title"]')
    popup_error_content = (By.XPATH, '//div[@class="swal-text"]')
    popup_error_btn_confirm = (By.CLASS_NAME, 'swal-button--confirm')
    
    # THAY ĐỔI MẬT KHẨU
    chg_cur_pass = (By.XPATH,'//div/div[1]/div/input')
    chg_cur_pass_error = (By.XPATH,'//div/div[1]/p[@class="error"]')
    chg_new_pass = (By.XPATH,'//div/div[2]/div/input')
    chg_new_pass_error = (By.XPATH,'//div/div[2]/p[@class="error"]')
    chg_re_new_pass = (By.XPATH,'//div/div[3]/div/input')
    chg_re_new_pass_error = (By.XPATH,'//div/div[3]/p[@class="error"]')
    chg_confirm = (By.XPATH,'//div[@class="tab-content"]/div/div/div/div/button')
    show_cur_pass = (By.XPATH,'//div[@class="tab-content"]/div/div/div/div[1]/div/span')
    hide_cur_pass = (By.XPATH,'//div[@class="tab-content"]/div/div/div/div[1]/div/span')
    show_new_pass = (By.XPATH,'//div[@class="tab-content"]/div/div/div/div[2]/div/span')
    hide_new_pass = (By.XPATH,'//div[@class="tab-content"]/div/div/div/div[2]/div/span')
    show_re_new_pass = (By.XPATH,'//div[@class="tab-content"]/div/div/div/div[3]/div/span')
    hide_re_new_pass = (By.XPATH,'//div[@class="tab-content"]/div/div/div/div[3]/div/span')

class DepositLocator:
    # SELECT BONUS AT THE FIRST TIME
    first_100 = (By.CLASS_NAME,'deposit-welcome__item--package-2')    
    first_40 = (By.CLASS_NAME,'deposit-welcome__item--package-3')
    first_125 = (By.CLASS_NAME,'deposit-welcome__item--package-1')

    first_100_btn = (By.XPATH,'//li[contains(@class,"deposit-welcome__item--package-2")]/div')    
    first_40_btn = (By.XPATH,'//li[contains(@class,"deposit-welcome__item--package-3")]/div')
    first_125_btn = (By.XPATH,'//li[contains(@class,"deposit-welcome__item--package-1")]/div')

    # SELECT BANK
    bank_Selector = (By.CLASS_NAME,'base-select__inner')
    bank_Sacombank = (By.LINK_TEXT,'Sacombank')
    bank_Techcombank = (By.LINK_TEXT,'Techcombank')
    bank_Vietcombank = (By.LINK_TEXT,'Vietcombank')
    bank_VietinBank = (By.LINK_TEXT,'VietinBank')
    bank_ACB = (By.LINK_TEXT,'ACB')
    bank_DongA = (By.LINK_TEXT,'DongA')

    # BANK INFO
    copy_owner_btn = (By.XPATH,'//li[contains(@class,"deposit-bank-account__item")][1]/div')
    copy_owner_text = (By.XPATH,'//li[contains(@class,"deposit-bank-account__item")][1]/div/p[3]')
    copy_number_btn = (By.XPATH,'//li[contains(@class,"deposit-bank-account__item")][2]/div')
    copy_number_text = (By.XPATH,'//li[contains(@class,"deposit-bank-account__item")][2]/div/p[3]')
    copy_place_btn = (By.XPATH,'//li[contains(@class,"deposit-bank-account__item")][3]/div')
    copy_place_text = (By.XPATH,'//li[contains(@class,"deposit-bank-account__item")][3]/div/p[3]')

    # TYPE SELECTOR
    type_ibanking = (By.XPATH,'//input[@value="ibanking"]/parent::label/div')
    type_atm = (By.XPATH,'//input[@value="atm"]/parent::label/div')
    type_banking = (By.XPATH,'//input[@value="banking"]/parent::label/div')

    # INPUT FORM
    in_amount = (By.NAME,'amount')
    in_amount_error = (By.XPATH,'//input[@name="amount"]/parent::div/parent::div/p[@class="error"]')
    out_amount = (By.XPATH,'//p[@class="base-input-custom__vnd"]')
    in_name = (By.NAME,'fromBankName')
    in_name_error = (By.XPATH,'//input[@name="fromBankName"]/parent::div/parent::div/p[@class="error"]')
    in_code = (By.NAME,'bankTrancode')
    in_code_error = (By.XPATH,'//input[@name="bankTrancode"]/parent::div/parent::div/p[@class="error"]')

    # PROMO SELECTOR
    promo_100 = (By.CLASS_NAME,'promotion-item--package-2')
    promo_40 = (By.CLASS_NAME,'promotion-item--package-3')
    promo_125 = (By.CLASS_NAME,'promotion-item--package-1')
    
    amount_promo = (By.XPATH,'//div[contains(@class,"deposit-promotion__note")]/ul/li[1]/p[2]')
    amount_real = (By.XPATH,'//div[contains(@class,"deposit-promotion__note")]/ul/li[2]/p[2]')
    amount_minbet = (By.XPATH,'//div[contains(@class,"deposit-promotion__note")]/ul/li[3]/p[2]')
    finished_date = (By.XPATH,'//div[contains(@class,"deposit-promotion__note")]/ul/p/span')

    # BUTTON
    TAO_PHIEU_NAP = (By.XPATH,'//div[contains(@class,"deposit-bank")]/div/div/button')

    

