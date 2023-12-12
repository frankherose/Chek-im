import telebot,requests

bot = telebot.TeleBot('6896780488:AAFEBh11s1x3I6vmY6L6UXUMGNytmZEmzHQ')

@bot.message_handler(commands='start')
def send_welcome(message):
    bot.reply_to(message, "مرحبا بك ، ارسل الايمي[imei] لفحصه")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    ses=requests.Session()
    headers = {'Host':'www.imei.sy','connection':'keep-alive','user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36'}
    col={'cookies':'XSRF-TOKEN=eyJpdiI6ImRla3JRbm9NVGo0MjRcL1l5ZEk4SzlBPT0iLCJ2YWx1ZSI6IlErNmQxUjBvWkdIYmh2QU1QemFTTnVoSENiVkZWWnZhaHh0MWpmWDUwVHh3SkxqTUNjeVZmbzV5SGs2cDhUb25uS3B0UDh2WCtKQnYyTVwvVDJ3ZlphUT09IiwibWFjIjoiZTI2MWNmNGRmY2Y4MzlkYWM3ZDcwN2ExYWQzODhmNjkyYjVjM2Q5NzQzMTZhZDY4ZjI5ZDQyZTQ0ZmQ5MGVmNSJ9; imei_session=eyJpdiI6IkgrZjFURVwvbEtCOEo3eHdUR0dSWDdRPT0iLCJ2YWx1ZSI6IjBtOE1lQ2E0YVB1UllPYzIyc04wNHVZdFdmVjFCTEI3XC9DcXlMQ0V6SjB2eFlPazl1XC80VERKdEF3TUJidlVkRGRudDA0QjJ5Zm9Kd2tyQ3BQc3V0K3c9PSIsIm1hYyI6ImM2MGJlNjI2MzEwZDlkZGQxNzNlM2UyZjBlNWM4NmRhYTExYzMxYTcxYjQ4MGI0MmM1OWRlYjIzMmQ3MmJmYWIifQ%3D%3D'}
    ime=message.text
    data={'_token':'NXFNtq2lNeZhGkxXvrdiewdoEn8KS6WHtvs1ZX28','imei':ime}
    k=ses.post('http://www.imei.sy/imei',data=data,headers=headers,cookies=col)
    print(k.json)
    
    if  'قابل'in k.text:
    	mes='✅الهاتف قابل للعمل على الشبكة السورية '
    	bot.reply_to(message, mes)
    elif 'غير صالح' in k.text:
    	mes='🚫خطأ في الايمي يرجى ادخال ايمي صالح'
    	bot.reply_to(message, mes)
    elif len(ime)<15:
    	mes='❌يوجد خطأ في كتابة الايمي اكتبه مرة اخرى'
    	bot.reply_to(message, mes)
    elif 'يستوجب'in k.text:
    	mes='📵الجهاز غير قابل للعمل على الشبكة السورية'
    	bot.reply_to(message, mes)
    else:
    	bot.reply_to(message, str('حدث خطأ ما'))

bot.polling()
