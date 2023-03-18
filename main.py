import openai
from aiogram import Bot, Dispatcher, executor, types

import logging



logging.basicConfig(level=logging.INFO)

bot_token = '5780124827:AAGnEbULQPfhWx7JFkIp79guBTUDgbg499o'
chatgpt_token = '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'

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я ChatGPT, бот, основанный на модели GPT-3.5. Я могу с вами общаться и отвечать на ваши вопросы!")

@dp.message_handler()
async def echo(message: types.Message):
    prompt = message.text
    response = await get_chatgpt_response(prompt)
    await message.reply(response)

async def get_chatgpt_response(prompt):
    openai.api_key = chatgpt_token
    model_engine = "text-davinci-003"
    completation = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    response = completation.choices[0].text
    return response


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
