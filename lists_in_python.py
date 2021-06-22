
"""
+ Hello everyone!
+ Let's look at working with lists in this file.
+ First we can create a single blank list.
+ And we display its length.
+ We add an element to the set (.append () and .insert ()).
+ Displays the values and length we entered.
+ Delete collection items using the .remove () function.
+ Display collection items.
"""

"""
+ Salom hammaga !
+ Bu faylda listlar bilan ishlashni ko'rib chiqamiz.
+ Avvaliga bitta bo'sh list yaratib olamiz.
+ Va uning uzunligini ekranga chiqaramiz.
+ To'plamga element qo'shamiz ( .append() va .insert() ) funksiyasi orqali.
+ Kiritgan qiymatlarinimizni va uzunligini ekranga chiqaramiz.
+ To'plam elementlarini .remove() funksiyasi orqali o'chiramiz.
+ To'plam elementlarini ekranga chiqaramiz.
"""

"""
+ Всем привет!
+ Давайте посмотрим на работу со списками в этом файле.
+ Сначала мы можем создать единый пустой список.
+ И отображаем его длину.
+ Добавляем элемент в набор (.append () и .insert ()).
+ Отображает введенные нами значения и длину.
+ Удалить элементы коллекции с помощью функции .remove ().
+ Отображение предметов коллекции.
"""



array = []  # free lists // bo'sh to'plam 

print(len(array))   # to'plam uzunligi //
 
array.append(12)   # to'plamga element qo'shish
array.append(87)   # to'plamga element qo'shish
array.append(76)   # to'plamga element qo'shish
array.append(56)   # to'plamga element qo'shish 
array.append(44)   # to'plamga element qo'shish
array.append(23)   # to'plamga element qo'shish

print(array)    # to'plam elementlari

print(len(array))  # to'plam uzunligi


array.insert(7,988)    # 7- element qilib 988 ni kiritdik.

print(array)   # To'plamni elementlari

array.remove(76)  # to'plamdan 76 qiymatni o'chiryabmiz.

print(array)  # to'plam elementlari

print(len(array))  # To'plam uzuznligi.



#  I love Uzbekistan :)
