# coding: utf-8

import json
import subprocess
import os

class ConfirmWeather():

    def __init__(self):
        pass

    def return_today_weather(self, message):
        # 本スクリプトが置いてあるパスを取得
        script_dir = os.path.abspath(os.path.dirname(__file__))
        cmd = os.path.join(script_dir, "confirm_today_weather.sh")
        # 同じディレクトリに置いたシェルスクリプトの実行結果を変数に格納
        weather_info = subprocess.check_output(cmd)
        print(weather_info.decode('utf-8'))
        # slackにPOSTする
        #message.send("今日の天気だお：")
        message.send(weather_info)
