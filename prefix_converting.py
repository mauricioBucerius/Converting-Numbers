##################################################################################################
# Mittels dieser Funktion wird der berechnete Widerstandswert eingelesen und ggf. auf den
# passenden Präfix gekürzt
# Rückgabeparameter ist ein String
# Beispiel:
# Eingabe 1000 (float) -> Ausgabe "1 k" (String)

def integer2string(eingabeParameter:float) -> str:
    try:
        if eingabeParameter >= 1 or eingabeParameter < 1000:
            if eingabeParameter < 10:
                stringValue = "  " + str(eingabeParameter)
            elif eingabeParameter < 100:
                stringValue = " " + str(eingabeParameter)
            elif eingabeParameter < 1000:
                stringValue = str(eingabeParameter)
            # print("falscher Parameter")
        else:
            return ""
    except:
        print("Error")
        return ""
    return stringValue


def time2msec(float_val:float) -> str:
    msecs = int((float_val - int(float_val % 60)) * 1000)
    if msecs < 10:
        return f'00{msecs}'
    elif msecs < 100:
        return f'0{msecs}'
    else:
        return str(msecs)


def time2sec(float_val:float) -> str:
    secs = int(float_val)

    if secs < 10:
        return f'0{secs}.{time2msec(float_val-secs)}'
    else:
        return f'{secs}.{time2msec(float_val-secs)}'


def time2min(float_val:float) -> str:
    """
    converted input into mins:secs.millisecs
    :param float_val: time in float or int
    :return: string of time
    """
    mins = int(float_val / 60)
    if mins < 10:
        return f'0{mins}:{time2sec(float_val % 60)}'
    else:
        # return f'{mins}:{round(float_val % 60, 3)}'
        return f'{mins}:{time2sec(float_val % 60)}'


def time2hour(float_val:float) -> str:
    """
    # Converted float value into hours:mins:secs.millisecs
    # :param float_val: time in float or int
    # :return: string of time
    """
    hours = int(float_val / 3600)
    if hours < 10:
        return f'0{hours}:' + time2min(float_val % 3600)
    else:
        return f'{hours}:' + time2min(float_val % 3600)


def time2prefix(float_val: float, nachkommastelle: int=1):
    if float_val < 60:
        return number2prefix(float_val, nachkommastelle) + 's'
    elif float_val / 60 >= 1 and float_val / 3600 < 1:
        return time2min(float_val) + ' min'
    elif float_val / 3600 >= 1:
        return time2hour(float_val) + ' h'


def number2prefix(eingabeParameter: str, nachkommastellen: int=1):
    wert = eingabeParameter
    # nachkommastellen = 0
    calcIndex = 0
    prefix = ""

    # Wenn Eingabe None ist -> Rückgabe von None
    if eingabeParameter is None:
        return None
    if eingabeParameter == 0:
        return '0 '
    elif eingabeParameter < 0:
        return f'-{number2prefix(abs(eingabeParameter), nachkommastellen)}'

    if eingabeParameter < 1:
        # Wenn die Berechnung in diesem Zwei durchgeführt wird -> Leistungsberechnung
        while wert < 1:
            wert *= 1000
            calcIndex += 1

        if calcIndex == 1:
            prefix = "m"
        elif calcIndex == 2:
            prefix = "u"
        elif calcIndex == 3:
            prefix = "n"
        elif calcIndex == 4:
            prefix = "p"
        elif calcIndex == 5:
            prefix = "f"
        elif calcIndex == 6:
            prefix = "a"
        elif calcIndex == 7:
            prefix = "z"
        elif calcIndex == 8:
            prefix = "y"

    # Der berechnete Werte für die Leistung muss immer gerundet werden!
    # wert = str(round(wert, nachkommastellen)) #"round(Wert, Nachkommastelle)" Rundet den auf beliebig viele Nachkommastellen
    elif eingabeParameter >= 1000:
        # In diesem Zweig wird die Berechnung für die Widerstände durchgeführt
        while wert >= 1000:
            wert /= 1000
            calcIndex += 1

        if calcIndex == 1:
            prefix = "k"
        elif calcIndex == 2:
            prefix = "M"
        elif calcIndex == 3:
            prefix = "G"
        elif calcIndex == 4:
            prefix = "T"
        elif calcIndex == 5:
            prefix = "P"
        elif calcIndex == 6:
            prefix = "E"
        elif calcIndex == 7:
            prefix = "Z"
        elif calcIndex == 8:
            prefix = "Y"
    # wert = round(wert, nachkommastellen)
    # else:
    # Die Ausgabe soll so formatiert werden, dass Werte < 10 (z.B. 1.2 oder 6.8) als float
    # ausgegeben werden und größere Werte (z.B. 10 oder 22 ) als Integer
    if wert > 100:
        wert = str(int(round(wert, 0)))
    elif wert < 10 or nachkommastellen > 0:
        wert = str(round(wert, nachkommastellen))
    # print(wert + " < 10")
    else:
        wert = str(int(round(wert, 0)))
    # print(wert + " > 10")

    # Werte zwischen 1 und 1000 werden nicht in einen String umgewandelt -> "doppelte"
    # Umwandlung im Rückgabeparameter notwendig!
    return (wert + " " + prefix)


def is_unit(item: str) -> bool:
    """
        checks if the item is a valid unit and returns True -> else False
    """
    unit: list=['m', 'ft', 'in', 'mi',              # unit in length
                'dB', 'dBc', 'dBW', 'dBm', 'dBV',   # logarithmic units
                '°C', 'Â°C', 'F'
                'kg', 'lb', 'oz',                   # mass
                's', 'min', 'h', 'd', 'yr',         # time
                'K', '°C', 'Â°C', 'Â°F', '°F',      # Temperature
                'A', 'V', 'Ω', 'Ohm',               # electrical units
                'W', 'J',
                'Pa', 'bar', 'atm', 'psi',          # pressure
                'Hz', 
                'm/s', 'km/h', 'mph',               # speed
                'm/s²', 'g',                        # acceleration (g - gravitation)
                'N', 'lbf',                         # force
                'kg/m³', 'g/cm³',                   # mass density
                'm³', 'L', 'cm³', 'gal',            # volume
                'm²', 'cm²', 'ft²', 'in²',          # area
                '°', 'rad',                         # angle
                'T', 'Wb', 'H',                     # magnetic
                'Bq', 'Ci'                          # radioactivity
                ]
    
    if item in unit:
        return True
    else:
        return False

##################################################################################################
# Ein vom Benutzer eingegebener String wird konvertiert von einem gemischten Sting (z.B. 1k) in 
# eine Zahl (1k -> 1000). Somit können Benutzerfreundliche Werte eingelesen und ausgegeben werden
# Rückgabeparameter ist ein float

def prefix2number(eingabe_parameter: str) -> float:
    # Extrahieren der Zahlen innerhalb des Strings:
    string = []
    prefix_detected = False

    # ".isalpha()" überprüft ob es sich um einen Buchstaben handelt -> gibt True oder False zurück
    # ".isdigit()" überprüft ob es sich um eine Zahl handelt -> gibt True oder False zurück
    if not eingabe_parameter.lower().find('e') > -1:
        i = 0
        while i <= len(eingabe_parameter) and not eingabe_parameter[i].isalpha():
            i += 1
        prefix_detected = True
        pos = i
    else:
        pos = -1

    if is_unit(eingabe_parameter):
        return 1
    
    # Unterscheidung um welchen Prefix es sich handelt:
    if prefix_detected:
        # Theoretisch könnte Yotta erkannt werden, die Spechertiefe in Python reicht nicht aus, um diese
        # darzustellen
        if eingabe_parameter[i] == "Y":
            # Yotta
            multiplier = pow(10, 24)
        elif eingabe_parameter[i] == "Z":
            # Zetta
            multiplier = pow(10, 21)
        elif eingabe_parameter[i] == "E":
            # Exa
            multiplier = pow(10, 18)
        elif eingabe_parameter[i] == "P":
            # Peta
            multiplier = pow(10, 15)
        elif eingabe_parameter[i] == "T":
            # Tera
            multiplier = pow(10, 12)
        elif eingabe_parameter[i] == "G":
            # Giga
            multiplier = pow(10, 9)
        elif eingabe_parameter[i] == "M":
            # Mega
            multiplier = pow(10, 6)
        elif eingabe_parameter[i] == "k":
            # Kilo
            multiplier = pow(10, 3)
        elif eingabe_parameter[i] == "h":
            # Hekto
            multiplier = pow(10, 2)
        elif eingabe_parameter[i] == "da":
            # Deka
            multiplier = pow(10, 2)
        elif eingabe_parameter[i] == "d":
            # Dezi
            multiplier = pow(10, -1)
        elif eingabe_parameter[i] == "c":
            # Zenti
            multiplier = pow(10, -2)
        elif eingabe_parameter[i] == "m":
            # Milli
            multiplier = pow(10, -3)
        elif eingabe_parameter[i] == "u":
            # Mikro
            multiplier = pow(10, -6)
        elif eingabe_parameter[i] == "n":
            # Nano
            multiplier = pow(10, -9)
        elif eingabe_parameter[i] == "p":
            # Piko
            multiplier = pow(10, -12)
        elif eingabe_parameter[i] == "f":
            # Femto
            multiplier = pow(10, -15)
        elif eingabe_parameter[i] == "a":
            # Atto
            multiplier = pow(10, -18)
        elif eingabe_parameter[i] == "z":
            # Zepto
            multiplier = pow(10, -21)
        # Theoretisch könnte Yokto erkannt werden, die Spechertiefe in Python reicht jedoch nicht aus, um diese
        # darzustellen
        elif eingabe_parameter[i] == "y":
            # Yokto
            multiplier = pow(10, -24)

        # Berechnung des Wertes durch die Zahl + Muliplikator, der durch das Präfix ermittelt wird
        if pos>0:
            return float(eingabe_parameter[0:pos]) * multiplier
        else:
            return multiplier
    else:
        # Berechnung des Wertes durch die Zahl + Muliplikator, der durch das Präfix ermittelt wird
        return float(eingabe_parameter[0::])


if __name__ == '__main__':
    print(time2prefix(7198.5))
    print(time2prefix(125.5))
    print(time2prefix(0.0603))
    print(number2prefix(-10))
    print(number2prefix(-36.22659904607586,0))
    print(prefix2number('G'))

