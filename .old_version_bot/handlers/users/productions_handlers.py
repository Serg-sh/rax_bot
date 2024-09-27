from asyncio import sleep

from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

import keyboard.inline.user_keyboards as ukb
from loader import dp, _
from utils.db_api import database
from utils.http_api import site_api

db = database.DBCommands()
region_uk_sng = ('Україна та СНД', 'Ukraine & CIS', 'Украина и СНГ')
region_eu = ('Europe', 'Європа', 'Европа')
region_na = ('North America', 'Північна Америка', 'Северная Америка')


def print_prod_info(item: dict):
    text = (f'<strong>{item["title"]}</strong>',
            f'<i>{item["body"].replace("</p>", "").replace("<p>", "")[:-2]}</i>',
            f'<b><i>{_("Регион")}:</i></b> {item["field_region"]}',
            f'<b><i>{_("Спецификация")}:</i></b> {item["field_specification"]}',
            f'<b><i>{_("Марка стали")}:</i></b> {item["field_steel_grade"]}',
            )
    return '\n'.join(text)


async def show_list_productions(call: CallbackQuery, region: tuple):
    user_lang = await db.get_language()
    list_prod = site_api.get_productions(language=user_lang)
    for item in list_prod:
        if item['field_region'] not in region:
            continue
        url = site_api.get_link_with_language(user_language=user_lang, api_link=item["api_link"])
        btn_more_details = InlineKeyboardButton(text=_('Подробнее'), url=url)
        markup = InlineKeyboardMarkup()
        markup.add(btn_more_details)
        markup.add(ukb.get_btn_back_to_prod_menu())
        await call.message.answer(text=print_prod_info(item), reply_markup=markup)
        await sleep(0.2)


@dp.callback_query_handler(text_contains='productions_menu')
async def prod_menu(call: CallbackQuery):
    user_lang = await db.get_language()
    await call.message.answer(text=_('Каталог нашей продукции'),
                              reply_markup=ukb.get_markup_prod_menu(user_lang))


@dp.callback_query_handler(text_contains='back_to_prod_menu')
async def back_to_prod_menu(call: CallbackQuery):
    await prod_menu(call)


@dp.callback_query_handler(text_contains='region_uk_sng')
async def prod_region_uk_sng(call: CallbackQuery):
    await show_list_productions(call, region_uk_sng)


@dp.callback_query_handler(text_contains='region_eu')
async def prod_region_eu(call: CallbackQuery):
    await show_list_productions(call, region_eu)


@dp.callback_query_handler(text_contains='region_na')
async def prod_region_na(call: CallbackQuery):
    await show_list_productions(call, region_na)
