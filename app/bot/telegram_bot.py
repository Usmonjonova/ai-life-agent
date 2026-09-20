import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
)

from app.config import BOT_TOKEN
from app.db.database import (
    create_or_update_user,
    init_db,
    update_onboarding,
)


dp = Dispatcher()


class Onboarding(StatesGroup):
    main_goal = State()
    focus_area = State()
    daily_time = State()


focus_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎓 O‘qish"),
            KeyboardButton(text="💼 Karyera"),
        ],
        [
            KeyboardButton(text="🧠 Shaxsiy rivojlanish"),
            KeyboardButton(text="🏃 Sog‘liq"),
        ],
        [
            KeyboardButton(text="💰 Moliya"),
        ],
    ],
    resize_keyboard=True,
)


@dp.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    user = message.from_user

    create_or_update_user(
        telegram_id=user.id,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
    )

    await state.set_state(Onboarding.main_goal)

    await message.answer(
        "Salom! 👋\n\n"
        "Men AI Life Agentman.\n"
        "Sizga maqsadlaringizni rejalashtirish, "
        "vazifalarni boshqarish va kuningizni tashkil "
        "qilishda yordam beraman.\n\n"
        "Avval sizni yaxshiroq tushunib olishim kerak.\n\n"
        "1/3\n"
        "Hozirgi hayotingizdagi eng muhim maqsadingiz nima?"
    )


@dp.message(Onboarding.main_goal)
async def main_goal_handler(message: Message, state: FSMContext):
    await state.update_data(main_goal=message.text)

    await state.set_state(Onboarding.focus_area)

    await message.answer(
        "2/3\n"
        "Hozir eng ko‘p qaysi yo‘nalishga fokus qilmoqchisiz?",
        reply_markup=focus_keyboard,
    )


@dp.message(Onboarding.focus_area)
async def focus_area_handler(message: Message, state: FSMContext):
    await state.update_data(focus_area=message.text)

    await state.set_state(Onboarding.daily_time)

    await message.answer(
        "3/3\n"
        "Kuniga maqsadlaringiz uchun taxminan "
        "qancha vaqt ajrata olasiz?\n\n"
        "Masalan: 1 soat, 2 soat yoki 90 daqiqa."
    )


@dp.message(Onboarding.daily_time)
async def daily_time_handler(message: Message, state: FSMContext):
    text = message.text.strip()

    try:
        if "soat" in text.lower():
            number = float(
                text.lower()
                .replace("soat", "")
                .strip()
            )
            daily_minutes = int(number * 60)
        else:
            daily_minutes = int(text)

    except ValueError:
        await message.answer(
            "Iltimos, vaqtni masalan:\n\n"
            "2 soat\n"
            "yoki\n"
            "90 daqiqa\n\n"
            "ko‘rinishida yozing."
        )
        return

    data = await state.get_data()

    update_onboarding(
        telegram_id=message.from_user.id,
        main_goal=data["main_goal"],
        focus_area=data["focus_area"],
        daily_available_minutes=daily_minutes,
    )

    await state.clear()

    await message.answer(
        "✅ Ajoyib! Onboarding tugadi.\n\n"
        f"🎯 Maqsad: {data['main_goal']}\n"
        f"📌 Fokus: {data['focus_area']}\n"
        f"⏱ Kunlik vaqt: {daily_minutes} daqiqa\n\n"
        "Endi men siz bilan maqsadlaringizni "
        "rejalashtirishni boshlashga tayyorman. 🚀"
    )


async def main():
    init_db()

    bot = Bot(token=BOT_TOKEN)

    print("AI Life Agent Telegram bot is running...")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())