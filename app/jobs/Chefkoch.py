#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import feedparser
from library.ChefkochRecipe import ChefkochRecipe
import logging


class Chefkoch():

    @staticmethod
    def fetch():
        logger = logging.getLogger("Chefkoch")
        logger.info("parsing Chefkoch recipe of the day")
        chefkoch_recipe_url = "https://www.chefkoch.de/rezepte/"
        chefkoch_recipe_of_the_day_rss_url = "https://www.chefkoch.de/rss/rezept-des-tages.php"
        feed = feedparser.parse(chefkoch_recipe_of_the_day_rss_url)
        url = feed['entries'][0]['links'][0]['href']
        url = url.replace(chefkoch_recipe_url, "")
        recipe_id =  url.split("/")[0]
        recipe = ChefkochRecipe()
        url = chefkoch_recipe_url + str(recipe_id)
        req = requests.get(url)
        contents = BeautifulSoup(req.text, 'lxml')
        recipe.name = contents.select_one('article h1').text
        ingredients_table = contents.find('table', class_='ingredients')
        recipe.description = contents.select_one('.ds-recipe-meta').parent.select_one('div.ds-box').text.strip()

        for row in ingredients_table.findAll('tr'):
            col = row.findAll('td')
            ingredient = "{} {}".format(col[0].text.strip(), col[1].text.strip())
            ingredient = ingredient.replace("\xa0", "")
            recipe.ingredients.append(ingredient)
        return recipe
