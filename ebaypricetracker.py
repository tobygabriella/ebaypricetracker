from bs4 import BeautifulSoup
import requests

#get link
link = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=fridge&_sacat=0&_ipg=240&_pgn={}"

#get user's maximum price
user_price =float(input('What is the maximum price you want to pay for a fridge? $'))

#loop through multiple pages
for page in range(1,7):
    url = link.format(page)
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, 'lxml')
    #get the links for the fridge
    ul_tag = soup.find("ul", class_="srp-results srp-list clearfix")
    if ul_tag:
        li_tags = ul_tag.find_all("li", class_="s-item s-item__pl-on-bottom")
        for li_tag in (li_tags):
            div_tag = li_tag.find("div", class_="s-item__info clearfix")
            if div_tag:
                a_tag = div_tag.find("a")
                if a_tag:
                    fridge_link = a_tag["href"]
    #get the prices for the fridge
    fridges = soup.find("ul", class_="srp-results srp-list clearfix").find_all("li", class_="s-item s-item__pl-on-bottom")
    for fridge in (fridges):
        price_text = fridge.find("span", class_ = "s-item__price").text
        if "to" in price_text:
            continue
        #convert to a float dat type
        price = float(price_text [1:].replace(",",""))
        if price < user_price:
            print(f"The fridge Price is {price} -- {fridge_link}")














