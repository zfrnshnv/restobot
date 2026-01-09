from aiogram import F
from aiogram.types import Message, CallbackQuery

from bot.buttons.inline import menu_inline_buttons
from bot.dispatcher import dp
from bot.models import Product, session, Category

foods = session.query(Product).all()
for food in foods:
    print(food.photo)


@dp.message(F.text == "🍽 Restoran menyusi")
async def resto_menu_handler(message: Message):
    categories = session.query(Category).all()
    btns = [(category.name, f"category_{category.id}") for category in categories]
    kategoriyalar = menu_inline_buttons(btns, [1], True)
    await message.answer(text="Mavjud bo'limlar", reply_markup=kategoriyalar)

@dp.callback_query(F.data.startswith("category_"))
async def category_handler(callback: CallbackQuery):
    await callback.message.delete()
    category_id: int = int(callback.data.split("_")[1])
    products = session.query(Product).filter(Product.category_id == category_id).all()
    btns = [(food.name, f"food_{food.id}") for food in products]
    btns.append(("Restoran menyusiga qaytish", "🍽 Restoran menyusi"))
    markup = menu_inline_buttons(btns, size=[1], repeat=True)
    await callback.message.answer(text="Ro'yhat", reply_markup=markup)

@dp.callback_query(F.data.startswith("food_"))
async def food_handler(callback: CallbackQuery):
    await callback.message.delete()
    food_id: int = int(callback.data.split("_")[1])
    food = session.query(Product).filter(Product.id == food_id).first()
    caption = f"""{food.name}\n{food.description}\n sotuvda {food.quantity} ta bor \n Narxi {food.price}"""
    btns = [("Savatga qo'shish", f"order_add_{food_id}"), ("Ortga qaytish", "food_")]
    markup = menu_inline_buttons(btns, size=[1], repeat=True)
    await callback.message.answer(text=caption, reply_markup=markup)
