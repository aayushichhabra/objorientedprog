dec=369
bool_a=0b101110001
hexa_a=0x171
octa_a=0o561
sum_bho=bool_a+hexa_a+octa_a
sum_o=3*dec
if sum_bho==sum_o:
    print(u"\U0001f600")
else:
    print(u"\U0001f622")
