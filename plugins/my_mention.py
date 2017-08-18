# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない
@respond_to('おつかれ')
def mention_func(message):
    message.reply('おつだよ') # メンション
    message.react('+1')

@listen_to('python')
def listen_func(message):
    message.send('pythonしゅき')      # ただの投稿

@listen_to('mac')
def listen_func(message):
    message.send('macはいいぞ〜')      # ただの投稿

@listen_to('win')
def listen_func(message):
    message.send('windowsきらい')      # ただの投稿

@respond_to('古河')
def listen_func(message):
    import jsm
    q = jsm.Quotes()
    price = q.get_price(5801).close # furukawa
    message.send("株価は "+str(price)+"円だよ")

@respond_to('株価')
def listen_func(message):
    import jsm
    q = jsm.Quotes()
    price = q.get_price(5801).close
    message.send("古河電工 {0} ({1})".format(price, price-2990))
    price = q.get_price(3382).close
    message.send("7&iHD {0} ({1})".format(price, price-4450))
    price = q.get_price(5401).close
    message.send("新日鉄住金 {0} ({1})".format(price, price-2633))
    price = q.get_price(6643).close
    message.send("戸上電機 {0} ({1})".format(price, price-459))
    price = q.get_price(7203).close
    message.send("トヨタ自 {0} ({1})".format(price, price-6239))
    price = q.get_price(8306).close
    message.send("三菱UFJ {0} ({1:.1f})".format(price, price-702.4))
    price = q.get_price(9022).close
    message.send("JR東海 {0} ({1})".format(price, price-17781))
    price = q.get_price(9437).close
    message.send("NTTドコモ {0} ({1:.1f})".format(price, price-2600))
    price = q.get_price(9613).close
    message.send("NTTデータ {0} ({1})".format(price, price-1215))
    price = q.get_price(9501).close
    message.send("東京電力 {0} ({1})".format(price, price-472))

import pya3rt
@default_reply()
def send_message(message):
    apikey = ""
    client = pya3rt.TalkClient(apikey)
    reply_message = client.talk(message.body['text'])
    # 以下の形式でjsonが返ってくるので、replyの部分をとりだす
    # {'status': 0, 'message': 'ok', 'results': [{'perplexity': 1.2802554542585969, 'reply': '私にはよくわからないです'}]}
    message.reply("あっ、あっ、、（"+reply_message['results'][0]['reply'] + "）" )

from plugins.scripts.confirm_weather import ConfirmWeather
# 今日のお天気を教えてくれる機能
@respond_to('(^.*今日.*天気.*)')
def confirm_today_weather(message, something):
    weather_class = ConfirmWeather()
    weather_class.return_today_weather(message)
