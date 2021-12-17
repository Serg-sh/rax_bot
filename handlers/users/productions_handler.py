import keyboards.inline.user_keyboards as ukb

from aiogram.types import CallbackQuery

from loader import dp, _


@dp.callback_query_handler(text_contains='productions_menu')
async def prod_menu(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(text=_('Каталог нашей продукции'),
                              reply_markup=ukb.get_markup_prod_menu())


@dp.callback_query_handler(text_contains='region_uk_sng')
async def prod_region_uk_sng(call: CallbackQuery):
    await call.message.answer(text='данный раздел находится в разработке')


@dp.callback_query_handler(text_contains='region_eu')
async def prod_region_eu(call: CallbackQuery):
    await call.message.answer(text='данный раздел находится в разработке')


@dp.callback_query_handler(text_contains='region_na')
async def prod_region_na(call: CallbackQuery):
    await call.message.answer(text='данный раздел находится в разработке')