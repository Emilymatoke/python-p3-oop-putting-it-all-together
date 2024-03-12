#!/usr/bin/env python3
from book import Book

class Book :
    def __init__(self, title = "And Then There Were None", page_count = 272) :
        self.title = title
        self.page_count = page_count
    
    
    @property
    def title(self) :
        "The title property"
        return self._title
    
    @title.setter
    def title(self, title) :
        "And Then There Were None"
        self._title = title


    @property
    def page_count(self) :
        "The page_count property"
        return self. _page_count
    
    @page_count.setter
    def page_count (self, page_count) :
        "Should be an integer"
        if page_count is int :
            self._page_count = page_count
        else:
            return "It is not an integer" 


    
        
    
        