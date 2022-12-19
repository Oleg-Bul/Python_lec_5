from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *




app = ApplicationBuilder().token("5946837678:AAE6zM8eHqbrtX1xIahyFy6iMFHT9WLgrYU").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
print('server start')
app.run_polling()











# import matplotlib.pyplot as plt
# import numpy as np

# list = [1,2,3,2,7]
# plt.plot(list)
# plt.show()









# import emoji


# print(emoji.emojize('Python is :thumbs_up:'))






# from progress.bar import PixelBar
# import time
# bar = PixelBar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()









# from isOdd import isOdd

# print(isOdd(0))
# print(isOdd(1+4))
