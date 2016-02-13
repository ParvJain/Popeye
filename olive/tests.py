from django.test import TestCase
from .helper import filter_place_id, build_api_url, get_hotel_data
# Create your tests here.

class HotelDataTestCase(TestCase):

    def test_filter_place_id(self):
        hotel_data = {"https://www.tripadvisor.in/Hotel_Review-g293919-d1412904-Reviews-Holiday_Inn_Pattaya-Pattaya_Chonburi_Province.html"         : "1412904",
                      "https://www.tripadvisor.in/Hotel_Review-g293919-d300440-Reviews-Amari_Garden_Pattaya-Pattaya_Chonburi_Province.html"         : "300440",
                      "https://www.tripadvisor.in/Hotel_Review-g293919-d6390812-Reviews-Amari_Ocean_Pattaya-Pattaya_Chonburi_Province.html"         : "6390812",
                      "https://www.tripadvisor.in/Hotel_Review-g293916-d300434-Reviews-Amari_Watergate_Bangkok-Bangkok.html"                        : "300434",
                      "https://www.tripadvisor.in/Hotel_Review-g293916-d2318761-Reviews-Eastin_Grand_Hotel_Sathorn-Bangkok.html"                    : "2318761",
                      "https://www.tripadvisor.in/Hotel_Review-g293919-d1006648-Reviews-Amari_Nova_Suites_Pattaya-Pattaya_Chonburi_Province.html"   : "1006648",
                      "https://www.tripadvisor.in/Hotel_Review-g293919-d305821-Reviews-Royal_Cliff_Beach_Hotel-Pattaya_Chonburi_Province.html"      : "305821",
                      "https://www.tripadvisor.in/Hotel_Review-g293919-d572754-Reviews-Sheraton_Pattaya_Resort-Pattaya_Chonburi_Province.html"      : "572754"}

        for url, place_id in hotel_data.items():
            self.assertEqual(filter_place_id(url), place_id)
