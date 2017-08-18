#!/bin/sh

curl -s https://weather.yahoo.co.jp/weather/jp/40/8210/40133/8100001.html | tr '\n' ' ' | sed -e 's/<[^>]*>//g' | grep -oE ' - [0-9].*明日' | tr ' ' '\n' | grep -v ^$ | head -47 | tr '\n' '\t' | awk '{sub("時間", "\n時間 ");sub("天気", "\n天気 ");sub("気温（℃）", "\n気温（℃）");sub("湿度（％）", "\n湿度（％）");sub("降水量（mm/h）", "\n降水量（mm/h）");print}'
