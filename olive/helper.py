def filter_place_id(url):
    import re
    place_id = re.search(r"(?<=-d).*?(?=-)", url)
    return place_id.group()

def build_api_url(place_id, start_date, currency="USD", adult=1, night=1, room=1):
    url = "https://api.tripadvisor.com/api/internal/1.10/meta_hac/{place_id}?limit=50&lod=detail&bookable=true&dieroll=1&lang=en_US&currency={currency}&ip=infer&commerceonly=false&checkin={start_date}&bcom_offers=true&roomtype=lowest_price&subcategory=hotel&adults={adult}&nights={night}&devicetype=mobile&newrequest=true&subcategory_hotels=hotel&mcid=0&mobile=true&rooms={room}".format(place_id=place_id, currency=currency, start_date=start_date, adult=adult, night=night, room=room)
    return url

def build_api_url2(place_id, start_date, currency="USD", adult=1, night=1, room=1):
    url = "https://api.tripadvisor.com/api/internal/1.10/meta_hac/{place_id}?limit=50&lod=detail&bookable=true&dieroll=1&lang=en_US&currency={currency}&ip=infer&commerceonly=false&checkin={start_date}&bcom_offers=true&roomtype=lowest_price&subcategory=hotel&adults={adult}&nights={night}&devicetype=mobile&newrequest=false&subcategory_hotels=hotel&mcid=0&mobile=true&rooms={room}".format(place_id=place_id, currency=currency, start_date=start_date, adult=adult, night=night, room=room)
    return url

def get_hotel_data(url, url2):
    import requests
    head = {"X-TripAdvisor-Unique"  : "%1%enc%3AE%2FBSJQVWpXQgpcx1Kny84oG1E5WQcMEx%2FVy1QhY9y9zT5BsMYvhPlw%3D%3D",
            "X-TripAdvisor-UUID"    : "b25c4d71-f986-470f-bca4-92defd5729a5",
            "User-Agent"            : "Mobile Android TAaApp TARX13 taAppDeviceFeatures=131076 taAppVersion=160201024 appLang=en_US osName='Android' deviceName=google_du_sprout_Android One osVer=4.4.4 hdpi normal mcc=405 mnc=806 connection=wifi",
            "Cookie"                : "TASession=%1%V2ID.B57788949E96475E6FAC74AF8CB678C2*SQ.1*LS.MobileNativeSettings*GR.10*TCPAR.98*TBR.69*EXEX.93*ABTR.1*PPRP.85*PHTB.96*FS.76*CPU.69*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.dateRecent*FPS.oldFirst*FA.1*DF.0*LP.%2FMobileNativeSettings-a_currency%5C.USD*TRA.true;",
            "Authorization"         : "token :2:zR-Xr1-R4Trh_I8zW9nrGQ:U6F_rdBkjQyzn6hB1NSFCbuNvB5le3zlXd4KSX9fHvh1al7xpPMGImddWYi0tX6QhivpQKG_hdjnwPrY8bIbH4JDaZ1jG4JFPlWUWzdzP8pOCszoq2JXMVsRbrl1-7UC3dXGwElk0W5QBiiTL4Swyw",
            "X-TripAdvisor-API-Key" : "ce957ab2-0385-40f2-a32d-ed80296ff67f"}
    r = requests.get(url, headers=head)
    n = requests.get(url2, headers=head)
    return n.content

# build_api_url("1635880", "2016-02-17", "INR")
# get_hotel_date("https://api.tripadvisor.com/api/internal/1.10/meta_hac/1635880?limit=50&lod=detail&bookable=true&dieroll=1&lang=en_US&currency=INR&ip=infer&commerceonly=false&checkin=2016-02-17&bcom_offers=true&roomtype=lowest_price&subcategory=hotel&adults=1&nights=1&devicetype=mobile&newrequest=true&subcategory_hotels=hotel&mcid=0&mobile=true&rooms=1")
