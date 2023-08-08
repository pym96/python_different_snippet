#导入需要的模块
import tkinter as tk
import requests


#为textField.bind设置函数
def weatherPredic(canvas):
    #从输入框得到城市的名字
    cityName = textField.get()
    #得到天气预报的api，我们可以从相关网站上获取
    api = "https://v0.yiketianqi.com/api?unescape=1&version=v61&appid=49565673%20&appsecret=m3VRLVSd&city=" + cityName
     #利用json来得到天气预报结果的字典
    json_data = requests.get(api).json()
    weather_condition = json_data['wea']
    tempture = str(json_data['tem'])
    minTempture = str(json_data['tem2'])
    maxTempture = str(json_data['tem1'])
    humidity = str(json_data['humidity'])
    wind_direction = str(json_data["win"])
    wind_speed = str(json_data['win_speed'])
    air_quality = str(json_data['air_level'])
    air_tips = str(json_data['air_tips'])

    finalInfo = weather_condition +"\n" + tempture + "\n"
    finalData = "\n" + "最高气温" + maxTempture + "\n" + "最低气温" + minTempture + "\n" + "湿度" + humidity + "\n" + "风向" + wind_direction + "\n" + "风速" + wind_speed +"\n" +"空气质量" + air_quality + "\n" + "当日建议" + air_tips
    label1.config(text=finalInfo)
    label2.config(text=finalData)

#设置canvas画布
canvas = tk.Tk()
canvas.geometry("800x500")
canvas.title("Weather prediction")

#为canvas画布设置输入框并设置相关字体属性
f = ("宋体",15,"bold")
t = ("宋体",35,"bold")

textField = tk.Entry(canvas,font=f)
textField.pack(pady=20)
textField.focus()
textField.bind("<Return>",weatherPredic)

#为信息的显示做好label
label1 = tk.Label(canvas,font=t)
label1.pack()
label2 = tk.Label(canvas,font=t)
label2.pack()

#循环
canvas.mainloop()

