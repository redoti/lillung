from requests_html import HTMLSession

def scrape_news():
    session = HTMLSession()
    r = session.get('https://news.google.com/search?q=pneumonia%20anak&hl=id&gl=ID&ceid=ID%3Aid')
    
    articles = r.html.find('.Ccj79') # Container utama
    newslist = []

    limit = 0

    for item in articles:
        try:
            newstitle = item.find('.JtKRv', first=True)  # Class Title
            newslink = item.find('.WwrzSb', first=True)  # Class Link
            newsmedia = item.find('.vr1PYe', first=True) # Class Media
            newsimage = item.find('.Quavad', first=True) # Class Image
            newstime = item.find('.hvbAAd', first=True)  # Class Time

            title = newstitle.text
            link_set = newslink.absolute_links
            link_list = list(link_set)
            link = link_list[0]
            media = newsmedia.text
            image = newsimage.attrs.get('src', '')
            time = newstime.text
            
            
            newsarticle = {
            'title': title,
            'link': link,
            'media': media,
            'image': image,
            'time': time
            }
            newslist.append(newsarticle)

            limit += 1
            if limit == 3:
                break
        except:
            pass

    return newslist
