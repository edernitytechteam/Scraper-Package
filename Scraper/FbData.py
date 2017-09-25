from datetime import datetime
import json
import urllib.request

class FbData:
    b_url = "https://graph.facebook.com/v2.10/"
    access_url = 'batch=[{"method" : "GET", "relative_url" : }]'
    def __init__(self, **kwargs):
        self.data = {'reach' : 'NA', 'cost_per_result' : 'NA', 'amount_spent' : 'NA', 'end_date' : 'NA', 'page_likes' : 'NA',
                        'clicks_all' : 'NA', 'cos_per_click' : 'NA', 'cost_per_impressions' : 'NA', 'CTR' : 'NA', 'impressions' : 'NA',
                        'gross_impressions' : 'NA', 'objective' : 'NA', 'social_clicks' : 'NA', 'social_impressions' : 'NA', 'social_reach' : 'NA',
                        'total_conversion' : 'NA', 'unique_CTR' : 'NA', 'link_clicks' : 'NA', 'page_engagement' : 'NA', 'photo_views' : 'NA',
                        'post_shares' : 'NA', 'post_comments' : 'NA', 'post_engagement' : 'NA', 'post_reactions' : 'NA', '3_sec_vid_views' : 'NA' }
        #initialized required data in a Dictionary
        self.advert_id = kwargs.get('advert_id', "None")
        self.post_id = kwargs.get('post_id', "None")
        self.page_id = kwargs.get('page_id', "None")
        self.token = kwargs.get('token', "None")
        #initialized api fetch credentials and details

    def printo(self):
        print(self.advert_id, self.post_id, self.page_id)
