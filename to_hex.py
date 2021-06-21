
def to_hex(number):
    if (number < 0 or number > 255):
        return 'Number must be between 0 and 255 inclusive.'
    lookup = {
        10:'a',
        11:'b',
        12:'c',
        13:'d',
        14:'e',
        15:'f'
    }
    result=number
    ans=''
    while (result > 0):
        remainder=result%16
        if (remainder >= 10):
            ans = lookup.get(remainder) + ans
        else:
            ans = str(remainder) + ans
        result=int(result/16)
    
    return print(ans)
    
# to_hex(12)

def hex_code(red,green,blue):
    if (red > 255 or red < 0 or green > 255 or green < 0 or blue > 255 or blue < 0): return None
    ans = '#'
    part1 = to_hex(red)
    part2 = to_hex(green)
    part3 = to_hex(blue)
    
    ans += part1 if len(part1) > 1 else '0'+part1
    ans += part2 if len(part2) > 1 else '0'+part2
    ans += part3 if len(part3) > 1 else '0'+part3

    return print(ans)

# hex_code(10,32,255)