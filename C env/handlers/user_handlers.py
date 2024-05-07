from copy import deepcopy

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.utils.formatting import Text, Bold
from aiogram.types import CallbackQuery, Message
from database.database import user_dict_template, users_db
# from filters.filters import IsDelBookmarkCallbackData, IsDigitCallbackData
# from keyboards.bookmarks_kb import (create_bookmarks_keyboard,
#                                     create_edit_keyboard)
# from keyboards.pagination_kb import create_pagination_keyboard
from keyboards.start_kb import start_kb, return_diagnoses_kb, bottom_keyboard
from keyboards.symptoms_kb import create_symptoms_keyboard,\
      create_diagnosis_keyboard
from lexicon.lexicon_en import LEXICON
from services.file_handling import DISEASES, SYMPTOMS_LIST
from functions.handlers_funcsions import start_f, cancel_f, \
     go_diagnostic_f, get_description_f, get_prob_diagnosis_f,\
     bacward_f, forward_f,  any_symptom_f,\
     return_to_symptoms_f


router: Router = Router()


# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@router.message(CommandStart())
async def process_start_command(message: Message):
    start_f(message=message)
    await message.answer(text=LEXICON['/start_2'],
                         reply_markup=bottom_keyboard)


# Этот хэндлер будет срабатывать на команду "/run diagnostics"
# и отправлять пользователю сообщение со списком доступных команд в боте
@router.message(Command(commands='run_diagnostics'))
async def process_run_diagnostics_command(message: Message):
    symptoms, text = go_diagnostic_f(id=message.from_user.id)
    await message.answer(
        text=text, reply_markup=create_symptoms_keyboard(*symptoms)
        )



# Этот хэндлер будет срабатывать на команду "/help"
# и отправлять пользователю сообщение со списком доступных команд в боте
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON['/help'])


# Этот хэндлер будет срабатывать на команду "/cancel"
# прекращать диагностику м сбрасывать параметры юзера до начальных
@router.message(Command(commands='cancel'))
async def process_cancel_command(message: Message):
    cancel_f(message=message)
    await message.answer(LEXICON['/cancel'])


# Этот хэндлер будет срабатывать
# на апдейт типа CallbackQuery c кнопки 'start of diagnostics'
@router.callback_query(Text(text=['go_diagnostic', 'repeat_diagnostic']))
async def process_go_diagnostics_press(callback: CallbackQuery):
    symptoms, text = go_diagnostic_f(id=callback.from_user.id)
    await callback.message.edit_text(
        text=text, reply_markup=create_symptoms_keyboard(*symptoms)
        )


# Этот хэндлер будет срабатывать
# на апдейт типа CallbackQuery с кнопки 'backward'
@router.callback_query(Text(text=['backward']))
async def process_backward_press(callback: CallbackQuery):
    symptoms, text = bacward_f(callback)
    await callback.message.edit_text(
        text=text, reply_markup=create_symptoms_keyboard(*symptoms)
        )


# Этот хэндлер будет срабатывать
# на апдейт типа CallbackQuery с кнопки 'forward'
@router.callback_query(Text(text=['forward']))
async def process_forward_press(callback: CallbackQuery):
    symptoms, text = forward_f(callback)
    await callback.message.edit_text(
        text=text, reply_markup=create_symptoms_keyboard(*symptoms)
        )


# Этот хэндлер будет срабатывать
# на апдейт типа CallbackQuery с кнопки 'return_to_symptoms_kb'
@router.callback_query(Text(text=['return_to_symptoms']))
async def process_return_to_symptoms_press(callback: CallbackQuery):
    symptoms, text = return_to_symptoms_f(callback)
    await callback.message.edit_text(
        text=text, reply_markup=create_symptoms_keyboard(*symptoms)
        )




# Этот хэндлер будет срабатывать
# на апдейт типа CallbackQuery с любой кнопки с симптомом
@router.callback_query(Text(text=SYMPTOMS_LIST))
async def process_any_symptom_press(callback: CallbackQuery):
    alert_text, text = any_symptom_f(callback)
    await callback.message.edit_text(
        text=text, reply_markup=callback.message.reply_markup
        )
    # await callback.answer(text=alert_text, show_alert=True)


# Этот хэндлер будет срабатывать
# на апдейт типа CallbackQuery с любой кнопки с диагнозом болезни
@router.callback_query(Text(text=DISEASES))
async def process_any_disease_press(callback: CallbackQuery):
    text = get_description_f(callback)
    # await callback.message.edit_text(
    #     text=text, reply_markup=callback.message.reply_markup
    #     )
    await callback.message.edit_text(
        text=text, reply_markup=return_diagnoses_kb
        )





# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# скнопки 'get_diagnosis'
@router.callback_query(Text(text=['get_diagnosis']))
async def process_get_diagnostics_press(callback: CallbackQuery):
    text, diagnoses = get_prob_diagnosis_f(callback)

    await callback.message.edit_text(
            text=text, reply_markup=create_diagnosis_keyboard(*diagnoses)
            )



# Этот хэндлер будет срабатывать на текст feedback
@router.message(F.text.startswith('feedback'))
async def send_echo(message: Message):
    with open('feedback.txt', 'a') as f:
        f.write(f"\n id {message.from_user.id}\n \
                las_name  {message.from_user.last_name}\n\
                first_name {message.from_user.first_name}\n \
                username {message.from_user.username} \n")
        f.write(f"date     {message.date}\n")
        f.write(message.text + '\n ******** \n')
    await message.answer(text='feedback принят . Спасибо.')
