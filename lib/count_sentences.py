#!/usr/bin/env python3
import re

class MyString:

  def __init__(self, value = ""):
    self._value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, new_value):
    if new_value != str:
      print("The value must be a string.")
    else:
      self._value = new_value

  def is_sentence(self):
    if self.value.endswith('.'):
      return True
    else:
      return False

  def is_question(self):
    if self.value.endswith('?'):
      return True
    else:
      return False

  def is_exclamation(self):
    if self.value.endswith('!'):
      return True
    else:
      return False

  def count_sentences(self):
    if len(self.value):
      sentences = re.split('[?!.][ ]', self._value)
      return len(sentences)
    return 0