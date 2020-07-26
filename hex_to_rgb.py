while(True):
    h = input('Enter hex: ').lstrip('#')
    print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))
    print("\n")
    
