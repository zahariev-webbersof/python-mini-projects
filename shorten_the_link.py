import pyshorteners

link_address = input("enter the link: ")
shortener_class_obj = pyshorteners.Shortener()

# the shortened link
result = shortener_class_obj.tinyurl.short(link_address)

print(result)