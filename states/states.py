from aiogram.dispatcher.filters.state import StatesGroup, State



class MailingAdmins(StatesGroup):
    Text = State()
    SendToAdmins = State()


class MailingManagers(StatesGroup):
    Text = State()
    SendToManagers = State()


class MailingClients(StatesGroup):
    Text = State()
    SendToClients = State()