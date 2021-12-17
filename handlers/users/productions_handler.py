import keyboards.inline.user_keyboards as ukb

from aiogram.types import CallbackQuery

from loader import dp, _
from utils.db_api import database
from utils.http_api import site_api

db = database.DBCommands()
region_uk_sng = ('Україна та СНД', 'Ukraine & CIS', 'Украина и СНГ')

@dp.callback_query_handler(text_contains='productions_menu')
async def prod_menu(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(text=_('Каталог нашей продукции'),
                              reply_markup=ukb.get_markup_prod_menu())


@dp.callback_query_handler(text_contains='region_uk_sng')
async def prod_region_uk_sng(call: CallbackQuery):
    user_lang = await db.get_language()
    list_prod = site_api.get_productions(language=user_lang)
    for item in list_prod:
        if item['field_region'] not in region_uk_sng:
            continue

        for key, value in item.items():
            print(key, '-', value)
        print('\n\n')


@dp.callback_query_handler(text_contains='region_eu')
async def prod_region_eu(call: CallbackQuery):
    pass


@dp.callback_query_handler(text_contains='region_na')
async def prod_region_na(call: CallbackQuery):
    pass
