from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import time
from crud_functions import *

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

initiate_db()
# set_all_products()
users = get_all_products()


# for user in users:
#     print(user[0])

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    #balance = 1000
    balance= State()

initiate_db()

@dp.message_handler(text="Регистрация")
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    await state.update_data(username=message.text)
    if is_included(message.text)==False:
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя", reply_markup="Регистрация")

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    data["balance"]=1000
    add_user(data["username"], data["email"], data["age"])
    await state.finish()


kb1 = InlineKeyboardMarkup()
button1_1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
button1_2 = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
kb1.add(button1_1)
kb1.add(button1_2)

# kb2 = InlineKeyboardMarkup()
# button2_1 = InlineKeyboardButton(text="Product1", callback_data="product_buying")
# button2_2 = InlineKeyboardButton(text="Product2", callback_data="product_buying")
# button2_3 = InlineKeyboardButton(text="Product3", callback_data="product_buying")
# button2_4 = InlineKeyboardButton(text="Product4", callback_data="product_buying")
# kb2.add(button2_1)
# kb2.add(button2_2)
# kb2.add(button2_3)
# kb2.add(button2_4)

menu_product = InlineKeyboardMarkup(row_width=4,
                                    inline_keyboard=[[
                                        InlineKeyboardButton(text="Product1", callback_data="product_buying"),
                                        InlineKeyboardButton(text="Product2", callback_data="product_buying"),
                                        InlineKeyboardButton(text="Product3", callback_data="product_buying"),
                                        InlineKeyboardButton(text="Product4", callback_data="product_buying")
                                    ]]
                                    )

menu_start = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Рассчитать"),
        KeyboardButton(text="Информация")
    ],
        [KeyboardButton(text="Купить")],
        [KeyboardButton(text="Регистрация")]
    ],
    resize_keyboard=True)


# button1 = KeyboardButton(text="Рассчитать")
# button2 = KeyboardButton(text="Информация")
# kb.add(button1)
# kb.add(button2)

@dp.message_handler(commands=['start'])
async def main_menu(message):
    await message.answer("Привет, я бот, помогающий с твои здоровьем", reply_markup=menu_start)


@dp.message_handler(text="Рассчитать")
async def starter(message):
    await message.answer("выбери опцию", reply_markup=kb1)


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    # for i in range(1, 5) :
    # await message.answer(f"Название: Product{i} | Описание: описание {i} | Цена: {i * 100}")
    # with open(f"files/1_{i}.png", "rb") as img:
    for user in users:
        await message.answer(f"Название: Product {user[1]} | Описание: описание {user[2]} | Цена: {user[3]}")
        with open(f"files/1_{user[0]}.png", "rb") as img:
            await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки:", reply_markup=menu_product)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


# рассчёт
@dp.callback_query_handler(text="calories")
async def infor1(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calorii = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) + 5
    await message.answer(f"Наш ответ по калориям {calorii}")
    await state.finish()


# формулв
@dp.callback_query_handler(text="formulas")
async def infor2(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    connection.commit()
    connection.close()
