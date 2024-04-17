def get_name():
    return input("please enter your name-")
def get_tshirt(brand_name):
    user_name = get_name()
    avai_brand = ['Levies brand', 'Allen solly', 'Tommy Hilfiger'] 
    if brand_name in avai_brand:
        print("Hi ",user_name,"the brand you are looking for is available in our store.")
    else:
        print("Hi",user_name,"Unfortunately the brand you are looking for is not available in our store.")
brand_name=input("Enter a brand name-")
get_tshirt(brand_name)