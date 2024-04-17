def get_name():
    return input("Please enter your name: ")
def get_tshirt(brand_name,size=None):
    user_name = get_name()
    avai_brand = ['Levies brand', 'Allen solly', 'Tommy Hilfiger'] 
    if brand_name in avai_brand:
        if size:
            print("Hi",user_name,"the brand",brand_name,"in size",M,"is available in our store.")
        else:
            print("Hi",user_name,"the brand",brand_name,"is available in our store.")
    else:
        print("Hi",user_name," Unfortunately the brand",brand_name," you are looking for is not available in our store.")
brand_name=input("enter a brand name:")
M=int(input("enter a size"))
get_tshirt(brand_name, M)