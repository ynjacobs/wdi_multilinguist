import requests
import json
import random

class Multilinguist:
  """This class represents a world traveller who knows 
  what languages are spoken in each country around the world
  and can cobble together a sentence in most of them
  (but not very well)
  """

  translatr_base_url = "http://bitmakertranslate.herokuapp.com"
  countries_base_url = "https://restcountries.eu/rest/v2/name"
  #{name}?fullText=true
  #?text=The%20total%20is%2020485&to=ja&from=en

  def __init__(self):
    """Initializes the multilinguist's current_lang to 'en'
    
    Returns
    -------
    Multilinguist
        A new instance of Multilinguist
    """
    self.current_lang = 'en'

  def language_in(self, country_name):
    """Uses the RestCountries API to look up one of the languages
    spoken in a given country

    Parameters
    ----------
    country_name : str
         The full name of a country.

    Returns
    -------
    bool 
        2 letter iso639_1 language code.
    """
    params = {'fullText': 'true'}
    response = requests.get(f"{self.countries_base_url}/{country_name}", params=params)
    json_response = json.loads(response.text)
    return json_response[0]['languages'][0]['iso639_1']

  def travel_to(self, country_name):
    """Sets current_lang to one of the languages spoken
    in a given country

    Parameters
    ----------
    country_name : str
        The full name of a country.

    Returns
    -------
    str
        The new value of current_lang as a 2 letter iso639_1 code.
    """
    local_lang = self.language_in(country_name)
    self.current_lang = local_lang
    return self.current_lang

  def say_in_local_language(self, msg):
    """(Roughly) translates msg into current_lang using the Transltr API

    Parameters
    ----------
    msg : str
        A message to be translated.

    Returns
    -------
    str
        A rough translation of msg.
    """
    params = {'text': msg, 'to': self.current_lang, 'from': 'en'}
    response = requests.get(self.translatr_base_url, params=params)
    json_response = json.loads(response.text)
    return json_response['translationText']

class MathGenius(Multilinguist):
      def report_total(self,lst):
       sum = 0
       for i in lst:
            sum +=i
       return 'The total is' + ' ' + str(sum)

      def multiply_total(self,lst):
        sum = 1
        for i in lst:
            sum *=i
        return 'The multiple is' + ' ' + str(sum)

class QuoteCollector(Multilinguist):
      def __init__(self):
       self.collection = [] 

      def add_quote(self, pass_quote):
        self.collection.append(pass_quote)
    

      def show_random(self):
        random_quote_index = random.randint(0, len(self.collection)-1)
        return self.collection[random_quote_index]

Hi = Multilinguist()
print(Hi.say_in_local_language('Hi how are you'))
print(Hi.language_in('Canada'))
me = MathGenius()
print(me.say_in_local_language('Hi how are you'))
print(me.language_in('Canada'))
print(me.say_in_local_language(me.report_total([23,45,676,34,5778,4,23,5465]))) # The total is 12048
me.travel_to("India")
print(me.say_in_local_language(me.report_total([6,3,6,68,455,4,467,57,4,534]))) # है को कुल 1604
print(me.multiply_total([6,3,6,68,455,4,467,57,4,534]))
me.travel_to("Italy")
print(me.say_in_local_language(me.report_total([324,245,6,343647,686545]))) # È Il totale 1030767

new_quotecollector = QuoteCollector()

new_quotecollector.add_quote('interesting quote')
print(new_quotecollector.collection)
new_quotecollector.add_quote('today we will see')
print(new_quotecollector.collection)
print(new_quotecollector.show_random())
new_quotecollector.travel_to('Italy')
print(new_quotecollector.say_in_local_language(new_quotecollector.show_random()))


