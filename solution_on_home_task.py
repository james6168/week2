input_temperature_Celsiums = float(input("Введите температуру в Цельсиях: "))
if input_temperature_Celsiums < -273.15:
    print(f"Температура {input_temperature_Celsiums} не действительна")
elif input_temperature_Celsiums == -273.15:
    print(f"Температура равна абсолютному нулю")
elif input_temperature_Celsiums < 0 and input_temperature_Celsiums > -273.15:
    print(f"Температура {input_temperature_Celsiums} ниже точки замерзания")
elif input_temperature_Celsiums == 0:
    print(f"Температура находится в точке замерзания")
elif input_temperature_Celsiums > 0 and input_temperature_Celsiums < 100:
    print(f"Температура {input_temperature_Celsiums} находится в нормальном диапазоне.")
elif input_temperature_Celsiums == 100:
    print(f"Температура находится в точке кипения")
elif input_temperature_Celsiums > 100:
    print(f"Температура {input_temperature_Celsiums} выше точки кипения")

