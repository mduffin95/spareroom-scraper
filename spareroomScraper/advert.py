import re

class Advert:
    def __init__(self, basic_details):
        self._set_price(basic_details)
        self.url = basic_details.select('.listing-results-content.desktop > a')
        self.short_desc = basic_details.find('em', class_='shortDescription').contents[0]
        self.location = basic_details.find('span', class_='listingLocation').text.strip()

    def __str__(self):
        return self.short_desc + ' ' + self.location + ' ' + str(self.get_pcm_price())

    def add_details(self):
        """ Add details by making a request to the url and scraping more details.

        """
        return


    def _set_price(self, basic_details):
        price_str = basic_details.find('strong', class_='listingPrice').text.strip()
        self.frequency = ''
        if re.search(r'pcm', price_str):
            self.frequency = 'pcm'
        if re.search(r'pw', price_str):
            self.frequency = 'pw'

        res = re.findall(r'\d+', price_str)
        if len(res) == 1:
            self.price = int(res[0]) #Just take the first price if there are more than one.
        else:
            raise Exception("Too many prices.")


    def get_pcm_price(self):
        if self.frequency == 'pcm':
            return self.price
        else:
            return self.price * 4.34524
