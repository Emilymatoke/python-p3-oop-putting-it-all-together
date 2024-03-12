#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand = "Adidas", size = 9) :
        self.brand = brand
        self.size = size

    @property
    def brand (self) :
        "The brand property "
        return self._brand
    
    @brand.setter
    def brand(self,brand) :
        "Adidas"
        self._brand = brand


    @property
    def size(self) :
        "The size property"
        return self._size

    @size.setter
    def size(self, size) :
        "Size must be an integer"
        if size is int :
            self._size = size
        else :
            return "not an integer"
        