# Python Program - Convert Hexadecimal to Decimal

print("Enter 'x' for exit.");
hexdec = input("Enter number in Hexadecimal Format: ");
if hexdec == 'x':
    exit();
else:
    dec = int(hexdec, 16);
    print(hexdec,"in Decimal =",str(dec));
