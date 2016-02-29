class HotelScraper(object):

    def __init__(self, url, start_date, adult, night, room):
        self.url = url
        self.start_date = start_date
        self.adult = adult or 1
        self.night = night or 1
        self.room = room or 1

    def get_data(self):
        host = self.check_hotel_host(self.url)
        if host == "tripadvisor":
            place_id = self.filter_place_id(self.url)
            api_url = self.build_api_url(place_id, self.start_date, self.adult, self.night, self.room)
            generated_data = self.get_hotel_data(api_url)
            return generated_data
        elif host == "hostelworld":
            return 0
        else:
            return host

    def check_hotel_host(self, url):
        from urlparse import urlparse
        host = urlparse(url).hostname
        if host.lower() == "tripadvisor.in" or host.lower() == "www.tripadvisor.in":
            return "tripadvisor"
        elif host.lower() == "hostelworld.com" or host.lower() == "www.hostelworld.com":
            return "hostelworld"
        else:
            return host

    def filter_place_id(self, url):
        import re
        place_id = re.search(r"(?<=-d).*?(?=-)", url)
        return place_id.group()

    def build_api_url(self, place_id, start_date, adult, night, room):
        url = "https://api.tripadvisor.com/api/internal/1.10/meta_hac/{place_id}?limit=50&lod=detail&bookable=true&dieroll=1&lang=en_US&currency=USD&ip=infer&commerceonly=false&checkin={start_date}&bcom_offers=true&roomtype=lowest_price&subcategory=hotel&adults={adult}&nights={night}&devicetype=mobile&subcategory_hotels=hotel&mcid=0&mobile=true&rooms={room}".format(place_id=place_id, start_date=start_date, adult=adult, night=night, room=room)
        return url

    def get_hotel_data(self, url):
        import requests
        head = {"X-TripAdvisor-Unique"  : "%1%enc%3AE%2FBSJQVWpXQgpcx1Kny84oG1E5WQcMEx%2FVy1QhY9y9zT5BsMYvhPlw%3D%3D",
                "X-TripAdvisor-UUID"    : "b25c4d71-f986-470f-bca4-92defd5729a5",
                "User-Agent"            : "Mobile Android TAaApp TARX13 taAppDeviceFeatures=131076 taAppVersion=160201024 appLang=en_US osName='Android' deviceName=google_du_sprout_Android One osVer=4.4.4 hdpi normal mcc=405 mnc=806 connection=wifi",
                "Cookie"                : "TASession=%1%V2ID.B57788949E96475E6FAC74AF8CB678C2*SQ.1*LS.MobileNativeSettings*GR.10*TCPAR.98*TBR.69*EXEX.93*ABTR.1*PPRP.85*PHTB.96*FS.76*CPU.69*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.dateRecent*FPS.oldFirst*FA.1*DF.0*LP.%2FMobileNativeSettings-a_currency%5C.USD*TRA.true;",
                "Authorization"         : "token :2:zR-Xr1-R4Trh_I8zW9nrGQ:U6F_rdBkjQyzn6hB1NSFCbuNvB5le3zlXd4KSX9fHvh1al7xpPMGImddWYi0tX6QhivpQKG_hdjnwPrY8bIbH4JDaZ1jG4JFPlWUWzdzP8pOCszoq2JXMVsRbrl1-7UC3dXGwElk0W5QBiiTL4Swyw",
                "X-TripAdvisor-API-Key" : "ce957ab2-0385-40f2-a32d-ed80296ff67f"}
        r = requests.get(url + "&newrequest=true" , headers=head)
        n = requests.get(url + "&newrequest=false", headers=head)
        return n.content
