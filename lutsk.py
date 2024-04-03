import aiogram 
from aiogram import Dispatcher, Bot, types
from aiogram.utils import executor
import time
from magic_filter import F

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
REG= "Луцьк"
TOKEN ='6880051355:AAErJpdMcDSm76dzmXQoIdHuf07VUMfB5NQ'

bot = Bot(TOKEN)
dp = Dispatcher(bot)


chat_id_set= -1002004258698

region=ReplyKeyboardMarkup(resize_keyboard=True,row_width=(2))


STARTM =f"Привіт, це адмін телеграм каналу {REG}. Якщо ти маєш певну новину чи звістку, надішли її сюди і ми відреагуємо" #тукст для 


reg1="Луцький"
region.add(KeyboardButton(text=reg1))
@dp.message_handler(text=["Луцький"] )
async def change_reg1(message: types.Message):
        global set_reg 
        set_reg=reg1
        
        await message.answer(text=f"Привіт, {user}.Ви потрапили за адресою на канал Славний {REG} 🇺🇦. Якщо у Вас є ексклюзивна інфа: фото/відео або новина — відправте її сюди.Вкажіть місце та дату/час знімання.Дякуємо за довіру 💙💛",reply_markup=types.ReplyKeyboardRemove())
reg2="Володимирський"
region.add(KeyboardButton(text=reg2))
@dp.message_handler(text=["Володимирський"] )
async def change_reg1(message: types.Message):
        global set_reg 
        set_reg=reg2
        await message.answer(text=f"Привіт, {user}.Ви потрапили за адресою на канал Славний {REG} 🇺🇦. Якщо у Вас є ексклюзивна інфа: фото/відео або новина — відправте її сюди.Вкажіть місце та дату/час знімання.Дякуємо за довіру 💙💛",reply_markup=types.ReplyKeyboardRemove())
reg3="Камінь-Каширський"
region.add(KeyboardButton(text=reg3))
@dp.message_handler(text=["Камінь-Каширський"] )
async def change_reg1(message: types.Message):
        global set_reg 
        set_reg=reg3
        await message.answer(text=f"Привіт, {user}.Ви потрапили за адресою на канал Славний {REG} 🇺🇦. Якщо у Вас є ексклюзивна інфа: фото/відео або новина — відправте її сюди.Вкажіть місце та дату/час знімання.Дякуємо за довіру 💙💛",reply_markup=types.ReplyKeyboardRemove())
reg4="Ковельський"
region.add(KeyboardButton(text=reg4))
@dp.message_handler(text=["Ковельський"] )
async def change_reg1(message: types.Message):
        global set_reg 
        set_reg=reg4
        await message.answer(text=f"Привіт, {user}.Ви потрапили за адресою на канал Славний {REG} 🇺🇦. Якщо у Вас є ексклюзивна інфа: фото/відео або новина — відправте її сюди.Вкажіть місце та дату/час знімання.Дякуємо за довіру 💙💛",reply_markup=types.ReplyKeyboardRemove())


    



    
    
    
    
    

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    global user 
    user = message.from_user.first_name
    await message.delete()
    time.sleep(0.7)
    await message.answer(text=f"Вітаємо {user}.")
    time.sleep(0.4)
    await message.answer(text="Виберіть район Львову", reply_markup=region )
    
    
  


 
 
@dp.message_handler(content_types=['any'])
async def echo(message: types.Message):
   await bot.send_message(chat_id_set, text=f"нік:{user} регіон:{set_reg}")
   await bot.forward_message(chat_id_set, message.from_user.id, message.message_id)
   time.sleep (5)
   await bot.send_message( chat_id=message.from_id, text="ваша новина була надіслана")




if __name__ == '__main__':
   
    executor.start_polling(dp)


