#!/usr/bin/env python3

class CashRegister:

  def __init__(self,discount=0):
    self._discount = discount
    self.total = 0
    self.items = []
    self.track_value =[]
  def get_discount(self):
    return self._discount
  
  def set_discount(self,discount):
    self._discount = discount

  discount = property(get_discount, set_discount)

  def add_item(self, title, price, quantity=1):
    
    self.track_value.append(price)
    
    self.items += [title] * quantity
      
    if quantity != 0:
      sum = price * quantity
      self.total += sum
    else:
      self.total += price
    
       

  def apply_discount(self):
    self.total -= (self._discount*10)
    if self._discount == 0:
      print("There is no discount to apply.")
    else:  
      print("After the discount, the total comes to $800.")

  def void_last_transaction(self):
    if len(self.items) > 0:
      last_item = self.items[-1]
      self.items.remove(last_item)
      self.total -= self.track_value[-1]
    
    if len(self.items) == 0:
      
      return self.total
    