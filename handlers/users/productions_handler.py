import keyboards.inline.user_keyboards as ukb

from aiogram.types import CallbackQuery

from loader import dp


@dp.callback_query_handler(text_contains='productions_menu')
async def prod_menu(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(text='Каталог нашей продукции',
                              reply_markup=ukb.get_markup_prod_menu())
