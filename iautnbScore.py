from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import asyncio

from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, PicklePersistence)

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [['username', 'password', 'term'],
                  ['Done']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def facts_to_str(user_data):
    facts = list()

    for key, value in user_data.items():
        facts.append('{} : {}'.format(key, value))
        if key == "username":
            facts_to_str.username = value
        if key == "password":
            facts_to_str.password = value
        if key == "term":
            facts_to_str.term = value

    return "\n".join(facts).join(['\n', '\n'])


def start(update, context):
    reply_text = "سلام ! \n"
    if context.user_data:
        reply_text += " قبلا اینارو بهم گفتی : \n" \
                      "{}" \
                      "\n اگه میخوای با همین مشخصات ادامه بدی done رو بزن" \
                      "\nاگه میخوای چیزی رو عوض کنی هم روش روش کلیک کن و مقدار جدیدش رو وارد کن".format(", ".join(context.user_data.keys()))
    else:
        reply_text += " مشخصاتت رو " \
                      "بهم بگو"
    update.message.reply_text(reply_text, reply_markup=markup)

    return CHOOSING


def regular_choice(update, context):
    text = update.message.text.lower()
    context.user_data['choice'] = text
    if context.user_data.get(text):
        reply_text = ' قبلا راجع بهش بهم گفتی : \n' \
                     '{} : {}\n' \
                     '\nاگر هم دستت اشتباهی خورده همون قبلی رو بفرست دوباره'.format(text, context.user_data[text])
    else:
        reply_text = '{} : '.format(text)
    update.message.reply_text(reply_text)

    return TYPING_REPLY


def custom_choice(update, context):
    update.message.reply_text('Honestly ... '
                              'I dont know what this part do, but if I delete it the whole bot wont work')

    return TYPING_CHOICE


def received_information(update, context):
    text = update.message.text
    category = context.user_data['choice']
    context.user_data[category] = text.lower()
    del context.user_data['choice']

    update.message.reply_text("تا الان اینارو بهم گفتی :"
                              "{}"
                              "ادامه بده \n"
                              "(واسه عوض کردن مشخصاتت هم روش کلیک کن و مقدار جدیدش رو وارد کن)".format(facts_to_str(context.user_data)),
                              reply_markup=markup)

    return CHOOSING


def show_data(update, context):
    update.message.reply_text("تا الان اینارو بهم گفتی :"
                              "{}".format(facts_to_str(context.user_data)))


def done(update, context):
    if 'choice' in context.user_data:
        del context.user_data['choice']

    update.message.reply_text("مشخصاتت :"
                              "{}"
                              "منتظر باش الان نمره هاتو میفرستم "
                              "ممکنه چند دقیقه طول بکشه".format(facts_to_str(context.user_data)))

    async def main():
        await asyncio.sleep(5)

    def get_score():
        try:
            l1 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[2]/td[7]/span").get_attribute('innerHTML')
            l11 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[2]/td[3]").get_attribute('innerHTML')
            l1final = f"{l11} : {l1}"
            print(l11, " : ", l1)
            update.message.reply_text(l1final)
        except NoSuchElementException:
            pass

        try:
            l2 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[3]/td[7]/span").get_attribute('innerHTML')
            l22 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[3]/td[3]").get_attribute('innerHTML')
            l2final = f"{l22} : {l2}"
            print(l22, " : ", l2)
            update.message.reply_text(l2final)
        except NoSuchElementException:
            pass

        try:
            l3 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[4]/td[7]/span").get_attribute('innerHTML')
            l33 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[4]/td[3]").get_attribute('innerHTML')
            l3final = f"{l33} : {l3}"
            print(l33, " : ", l3)
            update.message.reply_text(l3final)
        except NoSuchElementException:
            pass

        try:
            l4 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[5]/td[7]/span").get_attribute('innerHTML')
            l44 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[5]/td[3]").get_attribute('innerHTML')
            l4final = f"{l44} : {l4}"
            print(l44, " : ", l4)
            update.message.reply_text(l4final)
        except NoSuchElementException:
            pass

        try:
            l5 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[6]/td[7]/span").get_attribute('innerHTML')
            l55 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[6]/td[3]").get_attribute('innerHTML')
            l5final = f"{l55} : {l5}"
            print(l55, " : ", l5)
            update.message.reply_text(l5final)
        except NoSuchElementException:
            pass

        try:
            l6 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[7]/td[7]/span").get_attribute('innerHTML')
            l66 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[7]/td[3]").get_attribute('innerHTML')
            l6final = f"{l66} : {l6}"
            print(l66, " : ", l6)
            update.message.reply_text(l6final)
        except NoSuchElementException:
            pass

        try:
            l7 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[8]/td[7]/span").get_attribute('innerHTML')
            l77 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[8]/td[3]").get_attribute('innerHTML')
            l7final = f"{l77} : {l7}"
            print(l77, " : ", l7)
            update.message.reply_text(l7final)
        except NoSuchElementException:
            pass

        try:
            l8 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[9]/td[7]/span").get_attribute('innerHTML')
            l88 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[9]/td[3]").get_attribute('innerHTML')
            l8final = f"{l88} : {l8}"
            print(l88, " : ", l8)
            update.message.reply_text(l8final)
        except NoSuchElementException:
            pass

        try:
            l9 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[10]/td[7]/span").get_attribute('innerHTML')
            l99 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[10]/td[3]").get_attribute('innerHTML')
            l9final = f"{l99} : {l9}"
            print(l99, " : ", l9)
            update.message.reply_text(l9final)
        except NoSuchElementException:
            pass

        try:
            l10 = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[11]/td[7]/span").get_attribute('innerHTML')
            l10x = driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[4]/div/div/div[2]/div/div/table/tbody/tr[11]/td[3]").get_attribute('innerHTML')
            l10final = f"{l10x} : {l10}"
            print(l10, " : ", l10x)
            update.message.reply_text(l10final)
        except NoSuchElementException:
            pass

    def term_id():
        try:
            if facts_to_str.term == "1":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[2]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "2":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[3]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "3":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[4]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "4":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[5]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "5":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[6]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "6":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[7]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "7":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[8]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "8":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[9]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "9":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[10]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "10":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[11]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "11":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[12]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "12":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[13]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "13":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[14]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "14":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[15]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "15":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[16]/td/a").click()
        except NoSuchElementException:
            pass

        try:
            if facts_to_str.term == "16":
                driver.find_element_by_xpath("/html/body/form/div[3]/div[1]/div/div/div/div[3]/div/table/tbody/tr[17]/td/a").click()
        except NoSuchElementException:
            pass

    # op = webdriver.ChromeOptions()
    # op.add_argument('headless')
    # driver = webdriver.Chrome(executable_path='/home/amiwr/Code/Python/Nomre/chromedriver', options=op)
    driver = webdriver.Chrome()
    driver.get("http://edu1.iau-tnb.ac.ir/logina.aspx")

    usernameSite = driver.find_element_by_xpath("/html/body/form/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/input")
    passwordSite = driver.find_element_by_xpath("/html/body/form/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/input")
    usernameSite.send_keys(facts_to_str.username)
    passwordSite.send_keys(facts_to_str.password)
    driver.find_element_by_xpath("/html/body/form/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/input[1]").click()

    asyncio.run(main())

    driver.get("http://edu1.iau-tnb.ac.ir/eteraz_nomreh.aspx")

    term_id()

    asyncio.run(main())

    get_score()

    driver.close()

    update.message.reply_text("اگه میخوای دوباره از بات استفاده کنی /start رو بزن")
#     update.message.reply_text("/start")

    return ConversationHandler.END


def main():

    pp = PicklePersistence(filename='conversationbot')
    updater = Updater("1246139845:AAF92Dlr6lFe2Q4IapD5QhBReQvOr0hpKA0", persistence=pp, use_context=True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            CHOOSING: [MessageHandler(Filters.regex('^(username|password|term)$'),
                                      regular_choice)
                       ],

            TYPING_CHOICE: [MessageHandler(Filters.text,
                                           regular_choice),
                            ],

            TYPING_REPLY: [MessageHandler(Filters.text,
                                          received_information),
                           ],
        },

        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
        name="my_conversation",
        persistent=True
    )

    dp.add_handler(conv_handler)

    show_data_handler = CommandHandler('show_data', show_data)
    dp.add_handler(show_data_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
