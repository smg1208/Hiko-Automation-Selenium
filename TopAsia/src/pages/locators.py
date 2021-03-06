from selenium.webdriver.common.by import By
from TopAsia.src.pages.UIObject import UiObject


class ge(object):
    # DOMAIN = 'http://v2.fabet.info/'
    DOMAIN = 'http://dev-ta.mooo.com/'
    ProjectName = 'TopAsia'


class MainMenuLocators(object):
    MENU_THE_THAO = UiObject(By.CLASS_NAME, 'menu-sports')
    MENU_BAN_CA = UiObject(By.CLASS_NAME, 'menu-fishing')
    MENU_LIVE_CASINO = UiObject(By.CLASS_NAME, 'menu-casino')
    MENU_QUICK_GAME = UiObject(By.CLASS_NAME, 'menu-quickGames')
    MENU_TABLE_GAME = UiObject(By.CLASS_NAME, 'menu-tablegame')
    MENU_CONG_GAME = UiObject(By.CLASS_NAME, 'menu-cong-game')
    MENU_DANG_NHAP = UiObject(By.CLASS_NAME, 'not-login-user-login')
    MENU_DANG_KY = UiObject(By.CLASS_NAME, 'not-login-user-register')
    MENU_USER_INFO_DROP = UiObject(By.XPATH, '//div[@class="info-user"]')


class CongGameLocators(object):
    Type_All = UiObject(By.CLASS_NAME, 'icon-all')
    Type_No_hu = UiObject(By.CLASS_NAME, 'icon-nohu1')
    Type_Ban_ca = UiObject(By.CLASS_NAME, 'icon-banca')
    Type_Lo_de = UiObject(By.CLASS_NAME, 'icon-lode1')
    Type_Ingame = UiObject(By.CLASS_NAME, 'icon-in-game1')
    Type_Table_game = UiObject(By.CLASS_NAME, 'icon-table-game1')
    Type_Game_nhanh = UiObject(By.CLASS_NAME, 'icon-game-nhanh1')

    NCC_selector = UiObject(By.CLASS_NAME, 'btn-secondary')
    NCC_btn_All = UiObject(By.XPATH, '//div/ul/li[1][@role="presentation"]')
    NCC_btn_Techplay = UiObject(By.XPATH, '//input[@value="vingame"]/parent::div/parent::label/parent::a/parent::li')
    NCC_btn_PragmaticPlay = UiObject(By.XPATH, '//input[@value="pragmatic"]/parent::div/parent::label/parent::a/parent::li')
    NCC_btn_CQ9 = UiObject(By.XPATH, '//input[@value="cq9"]/parent::div/parent::label/parent::a/parent::li')
    NCC_btn_Tomhorn = UiObject(By.XPATH, '//input[@value="tomhorn"]/parent::div/parent::label/parent::a/parent::li')
    NCC_btn_PlaynGo = UiObject(By.XPATH, '//input[@value="playngo"]/parent::div/parent::label/parent::a/parent::li')

    Sort_Nhieu_nguoi_choi = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][1]')
    Sort_Dang_hot = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][2]')
    Sort_Pho_bien = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][3]')
    Sort_Moi_nhat = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][4]')
    Sort_a_z = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][5]')

    btn_Xem_them = UiObject(By.CLASS_NAME, 'game-section__load-more')
    List_Game_Load = UiObject(By.XPATH, '//div[contains(@class,"game-list")]/div')
    List_Game_Load_Name = UiObject(By.XPATH, '//div[contains(@class,"game-list")]/div/div/a')
    List_Game_Heading = UiObject(By.XPATH, '//h1[contains(@class,"game-section__title")]')

    List_type = [
        [Type_All, 'T???t C???', 'type=all'],
        [Type_No_hu, 'N??? H??', 'type=slots'],
        [Type_Ban_ca, 'B???n C??', 'type=fishing'],
        [Type_Game_nhanh, 'Game Nhanh', 'type=instant'],
        [Type_Ingame, 'InGame', 'type=ingame'],
        [Type_Table_game, 'Table Games', 'type=tables'],
        [Type_Lo_de, 'L?? ?????', 'type=lode']
    ]

    List_NCC = [
        # [NCC_btn_All, 'T???t C???', 'ncc=all'],
        [NCC_btn_PragmaticPlay, 'Pragmatic Play', 'ncc=pragmatic'],
        [NCC_btn_CQ9, 'CQ9', 'ncc=cq9'],
        [NCC_btn_Techplay, 'Techplay', 'ncc=vingame'],
        [NCC_btn_Tomhorn, 'Tomhorn Gaming', 'ncc=tomhorn'],
        [NCC_btn_PlaynGo, 'Play???n GO', 'ncc=playngo']
    ]

    List_Sort = [
        [Sort_Nhieu_nguoi_choi, 'Nhi???u Ng?????i Ch??i', 'sx=most-played'],
        [Sort_Dang_hot, '??ang Hot', 'sx=hot'],
        [Sort_Pho_bien, 'Ph??? Bi???n', 'sx=popular'],
        [Sort_Moi_nhat, 'M???i Nh???t', 'sx=new'],
        [Sort_a_z, 'A-Z', 'sx=name']
    ]


class CasinoLocators(object):
    NCC_All = UiObject(By.CLASS_NAME, 'game-menu-item-icon__tab')
    NCC_Evolution = UiObject(By.XPATH, '//div[contains(@class,"game-menu-item")][2]')
    NCC_Ebet = UiObject(By.XPATH, '//div[contains(@class,"game-menu-item")][3]')
    NCC_Vivo = UiObject(By.XPATH, '//div[contains(@class,"game-menu-item")][4]')
    NCC_Allbet = UiObject(By.XPATH, '//div[contains(@class,"game-menu-item")][5]')
    NCC_HGaming = UiObject(By.XPATH, '//div[contains(@class,"game-menu-item")][6]')

    Game_selector = UiObject(By.CLASS_NAME, 'btn-secondary')
    Game_Baccarat = UiObject(By.XPATH, '//input[@value="baccarat"]/parent::div/parent::label/parent::a/parent::li')
    Game_Sicbo = UiObject(By.XPATH, '//input[@value="sicbo"]/parent::div/parent::label/parent::a/parent::li')
    Game_Roulette = UiObject(By.XPATH, '//input[@value="roulette"]/parent::div/parent::label/parent::a/parent::li')

    Sort_Nhieu_nguoi_choi = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][1]')
    Sort_Dang_hot = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][2]')
    Sort_Pho_bien = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][3]')
    Sort_Moi_nhat = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][4]')
    Sort_a_z = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][5]')

    List_Game_Load = UiObject(By.XPATH, '//div[contains(@class,"lobby-casino-list")]/div')
    List_Game_Heading = UiObject(By.CLASS_NAME, 'lobby-casino-section__title')

    # Data
    List_Game = [
        [Game_Baccarat, 'Baccarat', 'type=baccarat'],
        # [Game_Sicbo, 'Sicbo', 'type=sicbo'],
        [Game_Roulette, 'Roulette', 'type=roulette']
    ]

    List_NCC = [
        [NCC_All, 'All', 'ncc=all'],
        [NCC_Evolution, 'Evolution', 'ncc=evo'],
        [NCC_Ebet, 'Ebet', 'ncc=ebet'],
        [NCC_Vivo, 'VivoGaming', 'ncc=vivo'],
        [NCC_Allbet, 'Allbet', 'ncc=allbet'],
        [NCC_HGaming, 'HGaming', 'ncc=hogaming']
    ]

    List_Sort = [
        [Sort_Nhieu_nguoi_choi, 'Nhi???u Ng?????i Ch??i', 'sx=most-played'],
        [Sort_Dang_hot, '??ang Hot', 'sx=hot'],
        [Sort_Pho_bien, 'Ph??? Bi???n', 'sx=popular'],
        [Sort_Moi_nhat, 'M???i Nh???t', 'sx=new'],
        # [Sort_a_z, 'A-Z', 'sx=name']
    ]


class LoginLocators(object):
    input_username = UiObject(By.XPATH, '//form/div[1]/div/input')
    input_password = UiObject(By.XPATH, '//form/div[2]/div/input')

    text_error_username = UiObject(By.XPATH, '//form/div[1]/p[@class="error"]')
    text_error_password = UiObject(By.XPATH, '//form/div[2]/p[@class="error"]')

    btn_show_password = UiObject(By.CLASS_NAME, 'icon-eye-hide')
    btn_hide_password = UiObject(By.CLASS_NAME, 'icon-eye-show')
    btn_login = UiObject(By.CLASS_NAME, 'login-form__submit')
    btn_close = UiObject(By.CLASS_NAME, 'close-user-modal')

    popup_error = UiObject(By.XPATH, '//div[@class="swal-modal"]')
    popup_error_title = UiObject(By.XPATH, '//div[@class="swal-title"]')
    popup_error_content = UiObject(By.XPATH, '//div[@class="swal-text"]')
    popup_error_btn_confirm = UiObject(By.CLASS_NAME, 'swal-button--confirm')


class SignupLocators(object):
    username = UiObject(By.XPATH, '//form/div[1]/div/input')
    password = UiObject(By.XPATH, '//form/div[2]/div/input')
    re_password = UiObject(By.NAME, 'confirmPassword')
    phoneno = UiObject(By.NAME, 'phoneNumber')
    invite_code = UiObject(By.XPATH, '//form/div[5]/div/input')

    username_error = UiObject(By.XPATH, '//form/div[1]/p[@class="error"]')
    password_error = UiObject(By.XPATH, '//form/div[2]/p[@class="error"]')
    re_password_error = UiObject(By.XPATH, '//form/div[3]/p[@class="error"]')
    phoneno_error = UiObject(By.XPATH, '//form/div[4]/p[@class="error"]')

    show_pass = UiObject(By.XPATH, '//input[@placeholder="M???t kh???u"]/parent::div/span[contains(@class,"icon-eye-hide")]')
    hide_pass = UiObject(By.XPATH, '//input[@placeholder="M???t kh???u"]/parent::div/span[contains(@class,"icon-eye-show")]')
    show_repass = UiObject(By.XPATH, '//input[@placeholder="Nh???p l???i m???t kh???u"]/parent::div/span[contains(@class,"icon-eye-hide")]')
    hide_repass = UiObject(By.XPATH, '//input[@placeholder="Nh???p l???i m???t kh???u"]/parent::div/span[contains(@class,"icon-eye-show")]')

    btn_register = UiObject(By.CLASS_NAME, 'register-form__submit')
    btn_close = UiObject(By.CLASS_NAME, 'close-user-modal')
    btn_agree = UiObject(By.CLASS_NAME, 'checkmark')

    popup_error = UiObject(By.XPATH, '//div[@class="swal-modal"]')
    popup_error_title = UiObject(By.XPATH, '//div[@class="swal-title"]')
    popup_error_content = UiObject(By.XPATH, '//div[@class="swal-text"]')
    popup_error_btn_confirm = UiObject(By.CLASS_NAME, 'swal-button--confirm')


class UserInfoLocator(object):
    # DROP DOWN MENU
    drop_info = UiObject(By.XPATH, '//ul/div/li[@role="presentation"][1]')
    drop_nap_tien = UiObject(By.XPATH, '//ul/div/li[@role="presentation"][2]')
    drop_rut_tien = UiObject(By.XPATH, '//ul/div/li[@role="presentation"][3]')
    drop_lich_su = UiObject(By.XPATH, '//ul/div/li[@role="presentation"][4]')
    drop_khuyen_mai = UiObject(By.XPATH, '//ul/div/li[@role="presentation"][5]')
    drop_tin_tuc = UiObject(By.XPATH, '//ul/div/li[@role="presentation"][6]')
    drop_logout = UiObject(By.XPATH, '//ul/div[@class="logout"]')
    drop_username = UiObject(By.XPATH, '//div[@class="user-name"]/span')

    # LEFT MENU
    btn_userinfo = UiObject(By.XPATH, '//span[@class="icon-information"]/parent::a/parent::li')
    btn_nap = UiObject(By.XPATH, '//span[@class="icon-deposit"]/parent::a/parent::li')
    btn_rut = UiObject(By.XPATH, '//span[@class="icon-withdraw"]/parent::a/parent::li')
    btn_history = UiObject(By.XPATH, '//span[@class="icon-history"]/parent::a/parent::li')
    btn_promotion = UiObject(By.XPATH, '//span[@class="icon-promotion"]/parent::a/parent::li')
    btn_logout = UiObject(By.CLASS_NAME, 'menu-info__logout')
    txt_username = UiObject(By.CLASS_NAME, 'menu-info__name')

    # TAB
    tab_info = UiObject(By.XPATH, '//ul/li[@class="nav-item"][1]')
    tab_changepass = UiObject(By.XPATH, '//ul/li[@class="nav-item"][2]')
    tab_bankaccount = UiObject(By.XPATH, '//ul/li[@class="nav-item"][3]')

    # C???P NH???T TH??NG TIN C?? NH??N
    info_name = UiObject(By.XPATH, '//div/div[1]/div/input')
    info_name_error = UiObject(By.XPATH, '//div/div[1]/p[@class="error"]')
    info_email = UiObject(By.XPATH, '//div/div[2]/div/input')
    info_email_error = UiObject(By.XPATH, '//div/div[2]/p[@class="error"]')
    info_email_authen = UiObject(By.XPATH, '//div/div[2]/div/p[@class="info-personal__authen"')
    info_phone = UiObject(By.XPATH, '//div/div[3]/div/input')
    info_phone_authen = UiObject(By.XPATH, '//div/div[3]/div/p[@class="info-personal__authen"')
    info_confirm = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div/button')

    # CONFIRM POPUP
    popup_cf = UiObject(By.ID, 'authen-email___BV_modal_content_')
    popup_cf_title = UiObject(By.CLASS_NAME, 'modal__content__title')
    popup_cf_content = UiObject(By.CLASS_NAME, 'content-form__desc')
    popup_cf_btn_confirm = UiObject(By.XPATH, '//div[@class="modal__content__inner"]/div/div/button')
    popup_cf_close = UiObject(By.CLASS_NAME, 'icon-close')
    popup_cf_resend = UiObject(By.XPATH, '//p[@class="content-form__note"]/span')

    # ERROR POPUP
    popup_error = UiObject(By.XPATH, '//div[@class="swal-modal"]')
    popup_error_title = UiObject(By.XPATH, '//div[@class="swal-title"]')
    popup_error_content = UiObject(By.XPATH, '//div[@class="swal-text"]')
    popup_error_btn_confirm = UiObject(By.CLASS_NAME, 'swal-button--confirm')

    # THAY ?????I M???T KH???U
    chg_cur_pass = UiObject(By.XPATH, '//div/div[1]/div/input')
    chg_cur_pass_error = UiObject(By.XPATH, '//div/div[1]/p[@class="error"]')
    chg_new_pass = UiObject(By.XPATH, '//div/div[2]/div/input')
    chg_new_pass_error = UiObject(By.XPATH, '//div/div[2]/p[@class="error"]')
    chg_re_new_pass = UiObject(By.XPATH, '//div/div[3]/div/input')
    chg_re_new_pass_error = UiObject(By.XPATH, '//div/div[3]/p[@class="error"]')
    chg_confirm = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div/button')
    show_cur_pass = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div[1]/div/span')
    hide_cur_pass = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div[1]/div/span')
    show_new_pass = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div[2]/div/span')
    hide_new_pass = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div[2]/div/span')
    show_re_new_pass = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div[3]/div/span')
    hide_re_new_pass = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div[3]/div/span')


class RechargeLocators:
    # TYPE OF RECHARGE
    rc_bank = UiObject(By.XPATH, '//span[@class="icon-bank"]/parent::div')
    rc_card = UiObject(By.XPATH, '//span[@class="icon-card"]/parent::div')
    rc_momo = UiObject(By.XPATH, '//span[@class="icon-momo"]/parent::div')
    rc_paywin = UiObject(By.XPATH, '//span[@class="icon-paywin"]/parent::div')

    # SELECT BONUS AT THE FIRST TIME
    first_100 = UiObject(By.CLASS_NAME, 'deposit-welcome__item--package-2')
    first_40 = UiObject(By.CLASS_NAME, 'deposit-welcome__item--package-3')
    first_125 = UiObject(By.CLASS_NAME, 'deposit-welcome__item--package-1')

    first_100_btn = UiObject(By.XPATH, '//li[contains(@class,"deposit-welcome__item--package-2")]/div')
    first_40_btn = UiObject(By.XPATH, '//li[contains(@class,"deposit-welcome__item--package-3")]/div')
    first_125_btn = UiObject(By.XPATH, '//li[contains(@class,"deposit-welcome__item--package-1")]/div')

    # SELECT BANK
    bank_Selector = UiObject(By.CLASS_NAME, 'base-select__inner')
    bank_Sacombank = UiObject(By.XPATH, '//span[@class="icon-select-down"]/parent::div/ul/li[2]')
    bank_Techcombank = UiObject(By.XPATH, '//span[@class="icon-select-down"]/parent::div/ul/li[3]')
    bank_Vietcombank = UiObject(By.XPATH, '//span[@class="icon-select-down"]/parent::div/ul/li[4]')
    bank_VietinBank = UiObject(By.XPATH, '//span[@class="icon-select-down"]/parent::div/ul/li[5]')
    bank_ACB = UiObject(By.XPATH, '//span[@class="icon-select-down"]/parent::div/ul/li[6]')
    bank_DongA = UiObject(By.XPATH, '//span[@class="icon-select-down"]/parent::div/ul/li[7]')

    # SELECT MOMO ACCOUNT
    momo_Selector = UiObject(By.CLASS_NAME, 'base-select__inner')
    momo_account1 = UiObject(By.XPATH, '//span[@class="icon-select-down"]/parent::div/ul/li[2]')
    momo_account2 = UiObject(By.XPATH, '//span[@class="icon-select-down"]/parent::div/ul/li[3]')
    momo_account3 = UiObject(By.XPATH, '//span[@class="icon-select-down"]/parent::div/ul/li[4]')
    momo_account4 = UiObject(By.XPATH, '//span[@class="icon-select-down"]/parent::div/ul/li[5]')

    # CARD SELECTOR
    spp_viettel = UiObject(By.XPATH, '//div[@class="deposit-select-card__list"]/div[1]')
    spp_vinaphone = UiObject(By.XPATH, '//div[@class="deposit-select-card__list"]/div[2]')
    spp_mobifone = UiObject(By.XPATH, '//div[@class="deposit-select-card__list"]/div[3]')

    card_fee_percent = {
        'viettel': 32,
        'vinaphone': 32,
        'mobifone': 34
    }

    amount_card_fee = UiObject(By.XPATH, '//li[1]/p[@class="wrapper-info__value"]')
    amount_card_real = UiObject(By.XPATH, '//li[2]/p[@class="wrapper-info__value"]')

    in_pin = UiObject(By.NAME, 'code')
    in_pin_error = UiObject(By.NAME, '')
    in_series = UiObject(By.NAME, 'serial')
    in_series_error = UiObject(By.NAME, '')

    card_Selector = UiObject(By.CLASS_NAME, 'base-select__inner')
    viettel_card_amount_10k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[10]')
    viettel_card_amount_20k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[9]')
    viettel_card_amount_30k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[8]')
    viettel_card_amount_50k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[7]')
    viettel_card_amount_100k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[6]')
    viettel_card_amount_200k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[5]')
    viettel_card_amount_300k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[4]')
    viettel_card_amount_500k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[3]')
    viettel_card_amount_1000k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[2]')

    mobi_vina_card_amount_10k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[9]')
    mobi_vina_card_amount_20k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[8]')
    mobi_vina_card_amount_30k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[7]')
    mobi_vina_card_amount_50k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[6]')
    mobi_vina_card_amount_100k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[5]')
    mobi_vina_card_amount_200k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[4]')
    mobi_vina_card_amount_300k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[3]')
    mobi_vina_card_amount_500k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[2]')

    # BANK INFO
    copy_owner_btn = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][1]/div/p[3]')
    copy_owner_text = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][1]/div/p[3]')
    copy_number_btn = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][2]/div/p[3]')
    copy_number_text = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][2]/div/p[3]')
    copy_place_btn = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][3]/div/p[3]')
    copy_place_text = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][3]/div/p[3]')

    # MOMO INFO
    momo_phoneNo_btn = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][1]/div/p[3]')
    momo_phoneNo_text = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][1]/div/p[3]')
    momo_owner_btn = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][2]/div/p[3]')
    momo_owner_text = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][2]/div/p[3]')

    # TYPE SELECTOR
    type_ibanking = UiObject(By.XPATH, '//input[@value="ibanking"]/parent::label/div')
    type_atm = UiObject(By.XPATH, '//input[@value="atm"]/parent::label/div')
    type_banking = UiObject(By.XPATH, '//input[@value="banking"]/parent::label/div')

    # INPUT FORM
    in_amount = UiObject(By.NAME, 'amount')
    in_amount_error = UiObject(By.XPATH, '//input[@name="amount"]/parent::div/parent::div/p[@class="error"]')
    out_amount = UiObject(By.XPATH, '//p[@class="base-input-custom__vnd"]')
    in_name = UiObject(By.NAME, 'fromBankName')
    in_name_error = UiObject(By.XPATH, '//input[@name="fromBankName"]/parent::div/parent::div/p[@class="error"]')
    in_code = UiObject(By.NAME, 'bankTrancode')
    in_code_error = UiObject(By.XPATH, '//input[@name="bankTrancode"]/parent::div/parent::div/p[@class="error"]')

    # PROMO SELECTOR
    promo_100 = UiObject(By.CLASS_NAME, 'promotion-item--package-2')
    promo_40 = UiObject(By.CLASS_NAME, 'promotion-item--package-3')
    promo_125 = UiObject(By.CLASS_NAME, 'promotion-item--package-1')

    amount_promo = UiObject(By.XPATH, '//div[contains(@class,"deposit-promotion__note")]/ul/li[1]/p[2]')
    amount_real = UiObject(By.XPATH, '//div[contains(@class,"deposit-promotion__note")]/ul/li[2]/p[2]')
    amount_minbet = UiObject(By.XPATH, '//div[contains(@class,"deposit-promotion__note")]/ul/li[3]/p[2]')
    finished_date = UiObject(By.XPATH, '//div[contains(@class,"deposit-promotion__note")]/ul/p/span')

    # BUTTON
    bank_TAO_PHIEU_NAP = UiObject(By.XPATH, '//div[contains(@class,"deposit-bank")]/div/div/button')
    momo_TAO_PHIEU_NAP = UiObject(By.XPATH, '//div[contains(@class,"deposit-momo")]/div/div/button')
    paywin_TAO_PHIEU_NAP = UiObject(By.XPATH, '//div[contains(@class,"deposit-paywin")]/div/div/button')
    card_TAO_PHIEU_NAP = UiObject(By.XPATH, '//div[contains(@class,"deposit-card")]/div/div/button')

    paywin_page_load = UiObject(By.ID, 'page')

    # DATA HELPTEXT:
    data_helptext = {
        'iBanking': {
            'Vietcombank': 'Vui l??ng nh???p s??? l???nh giao d???ch',
            'ACB': 'Vui l??ng nh???p s??? t??i kho???n ng?????i g???i',
            'DongA': 'Vui l??ng nh???p s??? t??i kho???n ng?????i g???i',
            'Vietinbank': 'Vui l??ng nh???p th???i gian chuy???n ti???n',
            'BIDV': 'Vui l??ng nh???p s??? t??i kho???n ng?????i g???i ho???c th???i gian chuy???n ti???n',
            'Sacombank': 'Vui l??ng nh???p th???i gian chuy???n ti???n',
            'Techcombank': 'Vui l??ng nh???p s??? b??t to??n ho???c s??? t??i kho???n ng?????i g???i'},
        'ATM': {
            'Vietcombank': 'Vui l??ng nh???p s??? t??i kho???n ng?????i g???i',
            'ACB': 'Vui l??ng nh???p s??? t??i kho???n ng?????i g???i',
            'DongA': 'Vui l??ng nh???p s??? t??i kho???n ng?????i g???i',
            'Vietinbank': 'Vui l??ng nh???p th???i gian chuy???n ti???n',
            'BIDV': 'Vui l??ng nh???p s??? t??i kho???n ng?????i g???i',
            'Sacombank': 'Vui l??ng nh???p th???i gian chuy???n ti???n',
            'Techcombank': 'Vui l??ng nh???p s??? t??i kho???n ng?????i g???i'},
        'Cash': {
            'Vietcombank': 'Vui l??ng nh???p h??? v?? t??n ng?????i g???i',
            'ACB': 'Vui l??ng nh???p h??? v?? t??n ng?????i g???i',
            'DongA': 'Vui l??ng nh???p h??? v?? t??n ng?????i g???i',
            'Vietinbank': 'Vui l??ng nh???p h??? v?? t??n ng?????i g???i',
            'BIDV': 'Vui l??ng nh???p h??? v?? t??n ng?????i g???i',
            'Sacombank': 'Vui l??ng nh???p h??? v?? t??n ng?????i g???i',
            'Techcombank': 'Vui l??ng nh???p h??? v?? t??n ng?????i g???i'}
    }

    data_listBanks = {
        'Vietcombank': bank_Vietcombank,
        'ACB': bank_ACB,
        'DongA': bank_DongA,
        'Vietinbank': bank_VietinBank,
        # 'BIDV': bank.BIDV,
        'Sacombank': bank_Sacombank,
        'Techcombank': bank_Techcombank
    }

    data_listBanks_paywin = {
        'Vietcombank': bank_Vietcombank,
        'ACB': bank_ACB,
        # 'DongA': bank_DongA,
        'Vietinbank': bank_VietinBank,
        # 'BIDV': bank.BIDV,
        'Sacombank': bank_Sacombank,
        'Techcombank': bank_Techcombank
    }

    data_listBankMethod = {
        'iBanking': type_ibanking,
        'ATM': type_atm,
        'Cash': type_banking
    }

    data_listCardAmount = {
        'viettel': {
            '10k': [viettel_card_amount_10k, 10000],
            '20k': [viettel_card_amount_20k, 20000],
            '30k': [viettel_card_amount_30k, 30000],
            '50k': [viettel_card_amount_50k, 50000],
            '100k': [viettel_card_amount_100k, 100000],
            '200k': [viettel_card_amount_200k, 200000],
            '300k': [viettel_card_amount_300k, 300000],
            '500k': [viettel_card_amount_500k, 500000],
            '1000k': [viettel_card_amount_1000k, 1000000]},
        'vinaphone': {
            '10k': [mobi_vina_card_amount_10k, 10000],
            '20k': [mobi_vina_card_amount_20k, 20000],
            '30k': [mobi_vina_card_amount_30k, 30000],
            '50k': [mobi_vina_card_amount_50k, 50000],
            '100k': [mobi_vina_card_amount_100k, 100000],
            '200k': [mobi_vina_card_amount_200k, 200000],
            '300k': [mobi_vina_card_amount_300k, 300000],
            '500k': [mobi_vina_card_amount_500k, 500000]},
        'mobifone': {
            '10k': [mobi_vina_card_amount_10k, 10000],
            '20k': [mobi_vina_card_amount_20k, 20000],
            '30k': [mobi_vina_card_amount_30k, 30000],
            '50k': [mobi_vina_card_amount_50k, 50000],
            '100k': [mobi_vina_card_amount_100k, 100000],
            '200k': [mobi_vina_card_amount_200k, 200000],
            '300k': [mobi_vina_card_amount_300k, 300000],
            '500k': [mobi_vina_card_amount_500k, 500000]}
    }

    data_listCardSupplier = {
        'viettel': spp_viettel,
        'vinaphone': spp_vinaphone,
        'mobifone': spp_mobifone
    }


class WithdrawLocators:
    tab_bank = UiObject(By.XPATH, '//span[contains(@class,"icon-bank")]/parent::div')
    tab_card = UiObject(By.XPATH, '//span[contains(@class,"icon-card")]/parent::div')

    in_amount = UiObject(By.NAME, 'amount')
    in_amount_error = UiObject(By.XPATH, '//input[@name="amount"]/parent::div/parent::div/p[contains(@class,"error")]')
    password = UiObject(By.NAME, 'password')
    card_password = UiObject(By.XPATH, '//div[@class="base-input-custom base-input-custom--password"]/div/input')
    password_error = UiObject(By.XPATH, '//input[@name="password"]/parent::div/parent::div/p[contains(@class,"error")]')
    No_ofCard = UiObject(By.XPATH, '//input[@type="tel"]')

    show_pass = UiObject(By.XPATH, '//input[@name="password"]/parent::div/span[contains(@class,"icon-eye-hide")]')
    hide_pass = UiObject(By.XPATH, '//input[@name="password"]/parent::div/span[contains(@class,"icon-eye-show")]')

    card_show_pass = UiObject(By.XPATH, '//input/parent::div/span[contains(@class,"icon-eye-hide")]')
    card_hide_pass = UiObject(By.XPATH, '//input/parent::div/span[contains(@class,"icon-eye-show")]')

    popup_error = UiObject(By.XPATH, '//div[@class="swal-modal"]')
    popup_error_title = UiObject(By.XPATH, '//div[@class="swal-title"]')
    popup_error_content = UiObject(By.XPATH, '//div[@class="swal-text"]')
    popup_error_btn_confirm = UiObject(By.CLASS_NAME, 'swal-button--confirm')

    acc_selector = UiObject(By.CLASS_NAME, 'icon-user')
    acc_1 = UiObject(By.XPATH, '//li[contains(@role,"presentation")][1]/a/label/div')
    acc_2 = UiObject(By.XPATH, '//li[contains(@role,"presentation")][2]/a/label/div')
    acc_3 = UiObject(By.XPATH, '//li[contains(@role,"presentation")][3]/a/label/div')
    acc_4 = UiObject(By.XPATH, '//li[contains(@role,"presentation")][4]/a/label/div')
    acc_5 = UiObject(By.XPATH, '//li[contains(@role,"presentation")][5]/a/label/div')

    TAO_PHIEU_RUT = UiObject(By.XPATH, '//span[@class="icon-user"]/parent::button/parent::div/parent::div/parent::div/div[@class="text-center"]/button')
    DOI_THE_CAO = UiObject(By.XPATH, '//button/parent::div/parent::div/div[@class="text-center"]/button')

    card_Selector = UiObject(By.CLASS_NAME, 'base-select__inner')
    viettel_card_amount_10k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[10]')
    viettel_card_amount_20k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[9]')
    viettel_card_amount_30k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[8]')
    viettel_card_amount_50k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[7]')
    viettel_card_amount_100k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[6]')
    viettel_card_amount_200k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[5]')
    viettel_card_amount_300k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[4]')
    viettel_card_amount_500k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[3]')
    viettel_card_amount_1000k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[2]')

    mobi_vina_card_amount_10k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[9]')
    mobi_vina_card_amount_20k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[8]')
    mobi_vina_card_amount_30k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[7]')
    mobi_vina_card_amount_50k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[6]')
    mobi_vina_card_amount_100k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[5]')
    mobi_vina_card_amount_200k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[4]')
    mobi_vina_card_amount_300k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[3]')
    mobi_vina_card_amount_500k = UiObject(By.XPATH, '//ul[@class="base-select__options"]/li[2]')

    data_listCardAmount = {
        'viettel': {
            '10k': [viettel_card_amount_10k, 10000],
            '20k': [viettel_card_amount_20k, 20000],
            '30k': [viettel_card_amount_30k, 30000],
            '50k': [viettel_card_amount_50k, 50000],
            '100k': [viettel_card_amount_100k, 100000],
            '200k': [viettel_card_amount_200k, 200000],
            '300k': [viettel_card_amount_300k, 300000],
            '500k': [viettel_card_amount_500k, 500000],
            '1000k': [viettel_card_amount_1000k, 1000000]},
        'vinaphone': {
            '10k': [mobi_vina_card_amount_10k, 10000],
            '20k': [mobi_vina_card_amount_20k, 20000],
            '30k': [mobi_vina_card_amount_30k, 30000],
            '50k': [mobi_vina_card_amount_50k, 50000],
            '100k': [mobi_vina_card_amount_100k, 100000],
            '200k': [mobi_vina_card_amount_200k, 200000],
            '300k': [mobi_vina_card_amount_300k, 300000],
            '500k': [mobi_vina_card_amount_500k, 500000]},
        'mobifone': {
            '10k': [mobi_vina_card_amount_10k, 10000],
            '20k': [mobi_vina_card_amount_20k, 20000],
            '30k': [mobi_vina_card_amount_30k, 30000],
            '50k': [mobi_vina_card_amount_50k, 50000],
            '100k': [mobi_vina_card_amount_100k, 100000],
            '200k': [mobi_vina_card_amount_200k, 200000],
            '300k': [mobi_vina_card_amount_300k, 300000],
            '500k': [mobi_vina_card_amount_500k, 500000]}
    }

    spp_viettel = UiObject(By.XPATH, '//div[@class="withdraw-select-card__list"]/div[1]')
    spp_vinaphone = UiObject(By.XPATH, '//div[@class="withdraw-select-card__list"]/div[2]')
    spp_mobifone = UiObject(By.XPATH, '//div[@class="withdraw-select-card__list"]/div[3]')

    data_listCardSupplier = {
        'viettel': spp_viettel,
        'vinaphone': spp_vinaphone,
        'mobifone': spp_mobifone
    }
