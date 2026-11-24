price_text="499"
qty_text="3"
discount_text="10"
price=int(price_text)
qty=int(qty_text)
discount=int(discount_text)
total=price*qty
discount=total*int(discount_text)/100
final=total-discount
print("Final bill is" + str(final) + "rupees")