from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

def main():
    print "start"
    url = 'https://scrapebook22.appspot.com'
    html = urlopen(url).read()
    data =  BeautifulSoup(html)
    print data.html.head.title.string

    file = open("email.csv","w+")

    for link in data.findAll("a"):
        if link.string == "See full profile":
            subpage_url = url + link["href"]
            subpage = urlopen(subpage_url).read()
            subdata = BeautifulSoup(subpage)
            for span in subdata.find("span", attrs={"class":"email"}):
                print span.string
                file.write(span.string + "----------")
            for h1 in subdata.findAll("h1")[1]:
                    print h1.string
                    file.write(h1.string + "----------")
            for span in subdata.findAll("span"):
                if span.has_key("data-city"):
                    print span.string
                    file.write(span.string + "\n")



    file.close()


if __name__ == '__main__':
    main()