def changeUnit(temp,unit,desunit):
    if unit=='farenheit':
        if desunit=='celsius':
            return (temp - 32) * 5/9
        elif desunit=='kelvin':
            return (temp - 32) * 5/9 + 273.15
    elif unit=='celsius':
        if desunit=='farenheit':
                return (temp * 9/5) + 32
        elif desunit=='kelvin':
            return (temp + 273.15)
    elif unit=='kelvin':
        if desunit=='farenheit':
             return (temp - 273.15) * 9/5 + 32
        elif desunit=='celsius':
            return (temp - 273.15)
    else:
        print("invalid")  
def main():
    choice=input('enter the unit to be converted:')
    temp=float(input('enter the temperature:'))
    desunit=input('the desired unit is:')
    answer=changeUnit(temp,choice,desunit)
    print('Answer',answer)
if __name__=='__main__':
    main()        
        


    
