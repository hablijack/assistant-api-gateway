#!/usr/bin/python3
# -*- coding: utf-8 -*-


class ChefkochRecipe(dict):
    def __init__(self, name="", description="", image="", ingredients=[]):
        self.name = name
        self.description = description
        self.image = image
        self.ingredients = ingredients
        