def dis_price(price,rate): #함수명(가격, 할인률)
    discount= price*(rate/100) #할인 금액
    final = price-discount  #가격-할인금액 -> 최종금액
    return final        #최종금액을 반환

#a상품: 10000원 할인률: 10%
price_a = dis_price(10000,10)
print(f"a상품은 {price_a}원입니다")  #할인금액을 뺀 금액 출력

#b상품: 50000원 할인률: 20%
price_b = dis_price(50000,20)
print(f"b상품은 {price_b}원입니다")  #할인금액을 뺀 금액 출력
