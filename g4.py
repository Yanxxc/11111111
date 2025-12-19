# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 11:10:27 2025

@author: ST
"""

height = float(input("請輸入身高（公分）："))
weight = float(input("請輸入體重（公斤）："))

if height <= 0 or weight <= 0:
    print("身高與體重必須大於 0")
else:
    bmi = weight / (height / 100) ** 2

    if bmi < 18.5:
        result = "體重過輕"
    elif bmi < 24:
        result = "正常範圍"
    elif bmi < 27:
        result = "過重"
    else:
        result = "肥胖"

    print(f"您的 BMI 為：{bmi:.2f}")
    print(f"健康狀態：{result}")






