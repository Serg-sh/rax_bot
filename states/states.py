from aiogram.fsm.state import StatesGroup, State


class MailingAdmins(StatesGroup):
    Text = State()
    SendToAdmins = State()


class MailingManagers(StatesGroup):
    Text = State()
    SendToManagers = State()


class MailingClients(StatesGroup):
    Text = State()
    SendToClients = State()
    Language = State()


class SetPermissions(StatesGroup):
    GetAdminId = State()
    GetManagerId = State()


class SetUserProfile(StatesGroup):
    GetPhone = State()
    GetEmail = State()
    GetCompany = State()
    GetPassword = State()
    GetLanguage = State()
