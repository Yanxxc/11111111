def bmi_calculator(height_cm, weight_kg):
    bmi = weight_kg / (height_cm / 100) ** 2
    return bmi

def bmi_status(bmi_value):
    if bmi_value < 18.5:
        return "體重過輕"
    elif bmi_value < 24:
        return "正常"
    elif bmi_value < 27:
        return "過重"
    else:
        return "肥胖"

h = float(input("請輸入身高（公分）："))
w = float(input("請輸入體重（公斤）："))

result_bmi = bmi_calculator(h, w)

result_status = bmi_status(result_bmi)

print("您的 BMI 為：", round(result_bmi, 2))
print("健康狀態：", result_status)
