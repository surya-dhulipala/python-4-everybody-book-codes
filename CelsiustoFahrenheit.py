Celsius = input ('Enter temperature in degree Celsius: ')
try:
    Celsius = float (Celsius)
    Fahrenheit = (9/5) * Celsius + 32
    print ('The temperature in degree Fahrenheit is: ', Fahrenheit)
except:
    print('Please Enter a valid number')
