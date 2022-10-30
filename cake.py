# Author:               Shea Craft
# File Description:     This file contains templates for Cake API calls.
import xmltodict
import requests
from datetime import datetime, timedelta
# AWS Instance runs on 3.8.5. ZoneInfo no available until 3.9.0. This is a workaround.
try:
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo

tz = ZoneInfo('America/New_York')

DOMAIN = ''
API_KEY = ''


# Description:  Creates request to the Cake Export Offer API for a single offer
# References:   https://support.getcake.com/support/solutions/articles/5000655203-export-offers-api-version-6
def exportCakeOffer(offer_id=0,
                    offer_name='',
                    advertiser_id=0,
                    vertical_id=0,
                    offer_type_id=0,
                    media_type_id=0,
                    tag_id=0,
                    start_at_row=0,
                    row_limit=1,
                    sort_field='offer_id',
                    sort_descending='False',
                    offer_status_id=0):

    url = requests.get(f'https://{DOMAIN}/api/6/export.asmx/Offers',
                       params={
                           'api_key': API_KEY,
                           'offer_id': offer_id,
                           'offer_name': offer_name,
                           'advertiser_id': advertiser_id,
                           'vertical_id': vertical_id,
                           'offer_type_id': offer_type_id,
                           'media_type_id': media_type_id,
                           'tag_id': tag_id,
                           'start_at_row': start_at_row,
                           'row_limit': row_limit,
                           'sort_field': sort_field,
                           'sort_descending': sort_descending,
                           'offer_status_id': offer_status_id
                       })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents


# Description:  Creates request to the Cake Export Offer API for multiple offers (Forces list to allow for iteration over calls with a single offer)
# References:   https://support.getcake.com/support/solutions/articles/5000655203-export-offers-api-version-6
def exportCakeOffers(offer_id=0,
                     offer_name='',
                     advertiser_id=0,
                     vertical_id=0,
                     offer_type_id=0,
                     media_type_id=0,
                     tag_id=0,
                     start_at_row=0,
                     row_limit=0,
                     sort_field='offer_id',
                     sort_descending='False',
                     offer_status_id=0):

    url = requests.get(f'https://{DOMAIN}/api/6/export.asmx/Offers',
                       params={
                           'api_key': API_KEY,
                           'offer_id': offer_id,
                           'offer_name': offer_name,
                           'advertiser_id': advertiser_id,
                           'vertical_id': vertical_id,
                           'offer_type_id': offer_type_id,
                           'media_type_id': media_type_id,
                           'tag_id': tag_id,
                           'start_at_row': start_at_row,
                           'row_limit': row_limit,
                           'sort_field': sort_field,
                           'sort_descending': sort_descending,
                           'offer_status_id': offer_status_id
                       })

    contents = xmltodict.parse(url.text,
                               dict_constructor=dict,
                               force_list={'offer': True})

    return contents


# Description:  Creates request to the Cake Export Advertiser API
# References:   https://support.getcake.com/support/solutions/articles/13000001689-export-advertisers-api-version-6
def exportCakeAdvertiser(advertiser_id=0,
                         advertiser_name='',
                         account_manager_id=0,
                         tag_id=0,
                         start_at_row=0,
                         row_limit=1,
                         sort_field=0,
                         sort_descending='False'):

    url = requests.get(f'https://{DOMAIN}/api/6/export.asmx/Advertisers',
                       params={
                           'api_key': API_KEY,
                           'advertiser_id': advertiser_id,
                           'advertiser_name': advertiser_name,
                           'account_manager_id': account_manager_id,
                           'tag_id': tag_id,
                           'start_at_row': start_at_row,
                           'row_limit': row_limit,
                           'sort_field': sort_field,
                           'sort_descending': sort_descending
                       })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents


# Description:  Creates request to the Cake Export Affiliate API
# References:   https://support.getcake.com/support/solutions/articles/5000546174-export-affiliates-api-version-5
def exportCakeAffiliate(affiliate_id=0,
                        affiliate_name='',
                        account_manager_id=0,
                        tag_id=0,
                        start_at_row=0,
                        row_limit=50,
                        sort_field='affiliate_id',
                        sort_descending='False'):

    url = requests.get(f'https://{DOMAIN}/api/5/export.asmx/Affiliates',
                       params={
                           'api_key': API_KEY,
                           'affiliate_id': affiliate_id,
                           'affiliate_name': affiliate_name,
                           'account_manager_id': account_manager_id,
                           'tag_id': tag_id,
                           'start_at_row': start_at_row,
                           'row_limit': row_limit,
                           'sort_field': sort_field,
                           'sort_descending': sort_descending
                       })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents


# Description:  Creates request to the Cake Export Campaign API
# References: https://support.getcake.com/support/solutions/articles/13000046530-export-campaigns-api-version-8
def exportCakeCampaign(campaign_id=0,
                       site_offer_id=0,
                       source_affiliate_id=0,
                       channel_id=0,
                       account_status_id=0,
                       media_type_id=0,
                       start_at_row=0,
                       row_limit=0,
                       sort_field='date_created',
                       sort_descending='True'):

    url = requests.get(f'https://{DOMAIN}/api/8/export.asmx/Campaigns',
                       params={
                           'api_key': API_KEY,
                           'campaign_id': campaign_id,
                           'site_offer_id': site_offer_id,
                           'source_affiliate_id': source_affiliate_id,
                           'channel_id': channel_id,
                           'account_status_id': account_status_id,
                           'media_type_id': media_type_id,
                           'start_at_row': start_at_row,
                           'row_limit': row_limit,
                           'sort_field': sort_field,
                           'sort_descending': sort_descending
                       })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents


# Description: Create request to the Cake Export Advertiser API
# References: https://support.getcake.com/support/solutions/articles/13000001689-export-advertisers-api-version-6
def exportCakeAdvertiser(advertiser_id=0,
                         advertiser_name='',
                         account_manager_id=0,
                         tag_id=0,
                         start_at_row=0,
                         row_limit=0,
                         sort_field='advertiser_id',
                         sort_descending='False'):

    url = requests.get(f'https://{DOMAIN}/api/6/export.asmx/Advertisers',
                       params={
                           'api_key': API_KEY,
                           'advertiser_id': advertiser_id,
                           'advertiser_name': advertiser_name,
                           'account_manager_id': account_manager_id,
                           'tag_id': tag_id,
                           'start_at_row': start_at_row,
                           'row_limit': row_limit,
                           'sort_field': sort_field,
                           'sort_descending': sort_descending
                       })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents


# Description:  Creates request to the Cake Cap Reports API
# References:   https://support.getcake.com/support/solutions/articles/5000546021-reports-caps-api-version-4
def reportCakeCaps(start_date=datetime.now(tz).strftime("%m/%d/%y"),
                   end_date=datetime.now(tz).strftime("%m/%d/%y"),
                   search='',
                   advertiser_id=0,
                   offer_id=0,
                   affiliate_id=0,
                   advertiser_tag_id=0,
                   offer_tag_id=0,
                   affiliate_tag_id=0,
                   advertiser_manager_id=0,
                   affiliate_manager_id=0,
                   advertiser_billing_cycle_id=0,
                   affiliate_billing_cycle_id=0,
                   cap_type_id=0,
                   cap_entity='offer',
                   cap_interval_id=0,
                   traffic_only='FALSE',
                   start_at_row=0,
                   row_limit=0,
                   sort_field='offer_id',
                   sort_descending='TRUE'):

    url = requests.get(f'https://{DOMAIN}/api/4/reports.asmx/Caps',
                       params={
                           'api_key': API_KEY,
                           'start_date': start_date,
                           'end_date': end_date,
                           'search': search,
                           'advertiser_id': advertiser_id,
                           'offer_id': offer_id,
                           'affiliate_id': affiliate_id,
                           'advertiser_tag_id': advertiser_tag_id,
                           'offer_tag_id': offer_tag_id,
                           'affiliate_tag_id': affiliate_tag_id,
                           'advertiser_manager_id': advertiser_manager_id,
                           'affiliate_manager_id': affiliate_manager_id,
                           'advertiser_billing_cycle_id':
                           advertiser_billing_cycle_id,
                           'affiliate_billing_cycle_id':
                           affiliate_billing_cycle_id,
                           'cap_type_id': cap_type_id,
                           'cap_entity': cap_entity,
                           'cap_interval_id': cap_interval_id,
                           'traffic_only': traffic_only,
                           'start_at_row': start_at_row,
                           'row_limit': row_limit,
                           'sort_field': sort_field,
                           'sort_descending': sort_descending
                       })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents


# Description:  Creates request to the Advertiser Summary Reports API
# References:   https://support.getcake.com/support/solutions/articles/5000545868-reports-advertisersummary-api-version-2
def reportCakeAdvertiser(start_date=datetime.now(tz).strftime("%m/%d/%y"),
                         end_date=(datetime.now(tz) +
                                   timedelta(days=1)).strftime("%m/%d/%y"),
                         advertiser_id=0,
                         advertiser_tag_id=0,
                         advertiser_manager_id=0,
                         event_id=0,
                         revenue_filter='conversions_and_events'):

    url = requests.get(
        f'https://{DOMAIN}/api/2/reports.asmx/AdvertiserSummary',
        params={
            'api_key': API_KEY,
            'start_date': start_date,
            'end_date': end_date,
            'advertiser_id': advertiser_id,
            'advertiser_manager_id': advertiser_manager_id,
            'advertiser_tag_id': advertiser_tag_id,
            'event_id': event_id,
            'revenue_filter': revenue_filter
        })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents


# Description:  Creates request to the Affiliate Summary Reports API
# References:   https://support.getcake.com/support/solutions/articles/13000011545-reports-sourceaffiliatesummary-api-version-3
def reportCakeAffiliate(start_date=datetime.now(tz).strftime("%m/%d/%y"),
                        end_date=(datetime.now(tz) +
                                  timedelta(days=1)).strftime("%m/%d/%y"),
                        source_affiliate_id=0,
                        source_affiliate_manager_id=0,
                        source_affiliate_tag_id=0,
                        site_offer_tag_id=0,
                        event_id=0,
                        event_type='all'):

    url = requests.get(
        f'https://{DOMAIN}/api/3/reports.asmx/SourceAffiliateSummary',
        params={
            'api_key': API_KEY,
            'start_date': start_date,
            'end_date': end_date,
            'source_affiliate_id': source_affiliate_id,
            'source_affiliate_manager_id': source_affiliate_manager_id,
            'source_affiliate_tag_id': source_affiliate_tag_id,
            'site_offer_tag_id': site_offer_tag_id,
            'event_id': event_id,
            'event_type': event_type
        })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents


# Description:  Creates request to the Site Offer Summary Reports API
# References:   https://support.getcake.com/support/solutions/articles/13000003975-reports-siteoffersummary-api-version-4
def reportCakeOffer(start_date=datetime.now(tz).strftime("%m/%d/%y"),
                    end_date=(datetime.now(tz) +
                              timedelta(days=1)).strftime("%m/%d/%y"),
                    brand_advertiser_id=0,
                    brand_advertiser_manager_id=0,
                    site_offer_id=0,
                    site_offer_tag_id=0,
                    source_affiliate_tag_id=0,
                    event_id=0,
                    event_type='all'):

    url = requests.get(f'https://{DOMAIN}/api/4/reports.asmx/SiteOfferSummary',
                       params={
                           'api_key': API_KEY,
                           'start_date': start_date,
                           'end_date': end_date,
                           'brand_advertiser_id': brand_advertiser_id,
                           'brand_advertiser_manager_id':
                           brand_advertiser_manager_id,
                           'site_offer_id': site_offer_id,
                           'site_offer_tag_id': site_offer_tag_id,
                           'source_affiliate_tag_id': source_affiliate_tag_id,
                           'event_id': event_id,
                           'event_type': event_type
                       })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents


# Description:  Creates offer in Cake with user-specified input
# References:   https://support.getcake.com/support/solutions/articles/5000546173-addedit-offer-api-version-5
def createCakeOffer(offer_id=0,
                    advertiser_id=0,
                    vertical_id=0,
                    offer_name=0,
                    third_party_name=0,
                    offer_status_id=0,
                    offer_type_id=0,
                    currency_id=0,
                    ssl=0,
                    click_cookie_days=0,
                    impression_cookie_days=0,
                    enable_view_thru_conversions=0,
                    click_trumps_impression=0,
                    disable_click_deduplication=0,
                    last_touch=0,
                    enable_transaction_id_deduplication=0,
                    offer_contract_name=0,
                    price_format_id=0,
                    payout=0,
                    received=0,
                    received_percentage=0,
                    offer_link=0,
                    thankyou_link=0,
                    offer_contract_hidden=0,
                    preview_link=0,
                    offer_description=0,
                    restrictions=0,
                    advertiser_extended_terms=0,
                    testing_instructions=0,
                    tags=0,
                    hidden=0,
                    redirect_offer_contract_id=0,
                    redirect_404=0,
                    postbacks_only=0,
                    pixel_html=0,
                    postback_url=0,
                    postback_url_ms_delay=0,
                    fire_global_pixel=0,
                    fire_pixel_on_non_paid_conversions=0,
                    static_suppression=0,
                    conversion_cap_behavior=0,
                    conversion_behavior_on_redirect=0,
                    expiration_date=0,
                    expiration_date_modification_type=0,
                    thumbnail_file_import_url=0,
                    allow_affiliates_to_create_creatives=0,
                    unsubscribe_link=0,
                    from_lines=0,
                    subject_lines=0,
                    conversions_from_whitelist_only=0,
                    allowed_media_type_modification_type=0,
                    allowed_media_type_ids=0,
                    redirect_domain=0,
                    cookie_domain=0,
                    track_search_terms_from_non_supported_search_engines=0,
                    auto_disposition_type=0,
                    auto_disposition_delay_hours=0,
                    session_regeneration_seconds=0,
                    session_regeneration_type_id=0,
                    payout_modification_type=0,
                    received_modification_type=0,
                    tags_modification_type=0):

    url = requests.post(
        f'https://{DOMAIN}/api/5/addedit.asmx/Offer',
        params={
            'api_key': API_KEY,
            'offer_id': offer_id,
            'advertiser_id': advertiser_id,
            'vertical_id': vertical_id,
            'offer_name': offer_name,
            'third_party_name': third_party_name,
            'offer_status_id': offer_status_id,
            'offer_type_id': offer_type_id,
            'currency_id': currency_id,
            'ssl': ssl,
            'click_cookie_days': click_cookie_days,
            'impression_cookie_days': impression_cookie_days,
            'enable_view_thru_conversions': enable_view_thru_conversions,
            'click_trumps_impression': click_trumps_impression,
            'disable_click_deduplication': disable_click_deduplication,
            'last_touch': last_touch,
            'enable_transaction_id_deduplication':
            enable_transaction_id_deduplication,
            'offer_contract_name': offer_contract_name,
            'price_format_id': price_format_id,
            'payout': payout,
            'received': received,
            'received_percentage': received_percentage,
            'offer_link': offer_link,
            'thankyou_link': thankyou_link,
            'offer_contract_hidden': offer_contract_hidden,
            'preview_link': preview_link,
            'offer_description': offer_description,
            'restrictions': restrictions,
            'advertiser_extended_terms': advertiser_extended_terms,
            'testing_instructions': testing_instructions,
            'tags': tags,
            'hidden': hidden,
            'redirect_offer_contract_id': redirect_offer_contract_id,
            'redirect_404': redirect_404,
            'postbacks_only': postbacks_only,
            'pixel_html': pixel_html,
            'postback_url': postback_url,
            'postback_url_ms_delay': postback_url_ms_delay,
            'fire_global_pixel': fire_global_pixel,
            'fire_pixel_on_non_paid_conversions':
            fire_pixel_on_non_paid_conversions,
            'static_suppression': static_suppression,
            'conversion_cap_behavior': conversion_cap_behavior,
            'conversion_behavior_on_redirect': conversion_behavior_on_redirect,
            'expiration_date': expiration_date,
            'expiration_date_modification_type':
            expiration_date_modification_type,
            'thumbnail_file_import_url': thumbnail_file_import_url,
            'allow_affiliates_to_create_creatives':
            allow_affiliates_to_create_creatives,
            'unsubscribe_link': unsubscribe_link,
            'from_lines': from_lines,
            'subject_lines': subject_lines,
            'conversions_from_whitelist_only': conversions_from_whitelist_only,
            'allowed_media_type_modification_type':
            allowed_media_type_modification_type,
            'allowed_media_type_ids': allowed_media_type_ids,
            'redirect_domain': redirect_domain,
            'cookie_domain': cookie_domain,
            'track_search_terms_from_non_supported_search_engines':
            track_search_terms_from_non_supported_search_engines,
            'auto_disposition_type': auto_disposition_type,
            'auto_disposition_delay_hours': auto_disposition_delay_hours,
            'session_regeneration_seconds': session_regeneration_seconds,
            'session_regeneration_type_id': session_regeneration_type_id,
            'payout_modification_type': payout_modification_type,
            'received_modification_type': received_modification_type,
            'tags_modification_type': tags_modification_type
        })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents


# Description:  Creates request to Click Reports API
# References:   https://support.getcake.com/support/solutions/articles/13000035266-reports-clicks-api-version-12
def reportCakeClicks(start_date=datetime.now(tz).strftime("%m/%d/%y"),
                     end_date=(datetime.now(tz) +
                               timedelta(days=1)).strftime("%m/%d/%y"),
                     affiliate_id=0,
                     advertiser_id=0,
                     offer_id=0,
                     campaign_id=0,
                     creative_id=0,
                     price_format_id=0,
                     include_tests='false',
                     start_at_row=0,
                     row_limit=0,
                     include_duplicates='false'):

    url = requests.get(f'https://{DOMAIN}/api/12/reports.asmx/Clicks',
                       params={
                           'api_key': API_KEY,
                           'start_date': start_date,
                           'end_date': end_date,
                           'affiliate_id': affiliate_id,
                           'advertiser_id': advertiser_id,
                           'offer_id': offer_id,
                           'campaign_id': campaign_id,
                           'creative_id': creative_id,
                           'price_format_id': price_format_id,
                           'include_tests': include_tests,
                           'start_at_row': start_at_row,
                           'row_limit': row_limit,
                           'include_duplicates': include_duplicates
                       })

    print(url.url)

    contents = xmltodict.parse(url.text, dict_constructor=dict,
                               force_list={'click': True})

    return contents


# Description:  Creates request to Campaign Reports API
# References:   https://support.getcake.com/support/solutions/articles/13000003854-reports-campaignsummary-api-version-5
def reportCakeCampaign(start_date=datetime.now(tz).strftime("%m/%d/%y"),
                       end_date=(datetime.now(tz) +
                                 timedelta(days=1)).strftime("%m/%d/%y"),
                       campaign_id=0,
                       source_affiliate_id=0,
                       subid_id="",
                       site_offer_id=0,
                       source_affiliate_tag_id=0,
                       site_offer_tag_id=0,
                       source_affiliate_manager_id=0,
                       brand_advertiser_manager_id=0,
                       event_id=0,
                       event_type='all'):

    url = requests.get(f'https://{DOMAIN}/api/5/reports.asmx/CampaignSummary',
                       params={
                           'api_key': API_KEY,
                           'start_date': start_date,
                           'end_date': end_date,
                           'campaign_id': campaign_id,
                           'source_affiliate_id': source_affiliate_id,
                           'subid_id': subid_id,
                           'site_offer_id': site_offer_id,
                           'source_affiliate_tag_id': source_affiliate_tag_id,
                           'site_offer_tag_id': site_offer_tag_id,
                           'source_affiliate_manager_id':
                           source_affiliate_manager_id,
                           'brand_advertiser_manager_id':
                           brand_advertiser_manager_id,
                           'event_id': event_id,
                           'event_type': event_type
                       })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents


# Description:   Creates request to Tracking Domains API
# References:    https://support.getcake.com/support/solutions/articles/5000546263-get-trackingdomains-api-version-1
def getCakeTrackingDomains(domain_type='all'):

    url = requests.get(f'https://{DOMAIN}/api/1/get.asmx/TrackingDomains',
                       params={
                           'api_key': API_KEY,
                           'domain_type': domain_type
                       })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents

# Description:  Creates a conversion in Cake
# References:   https://support.getcake.com/support/solutions/articles/13000068564-track-massconversioninsert-api-version-3
def insertCakeConversion(affiliate_id,
                         campaign_id,
                         sub_affiliate,
                         creative_id,
                         payout,
                         received,
                         transaction_ids='',
                         note='',
                         total_to_insert=1,
                         unpaid_disposition_id=0,
                         conversion_date=datetime.now(tz).strftime("%m/%d/%y")):

    url = requests.get(f'https://{DOMAIN}/api/3/track.asmx/MassConversionInsert',
                       params={
                           'api_key': API_KEY,
                           'conversion_date': conversion_date,
                           'affiliate_id': affiliate_id,
                           'campaign_id': campaign_id,
                           'sub_affiliate': sub_affiliate,
                           'creative_id': creative_id,
                           'total_to_insert': total_to_insert,
                           'payout': payout,
                           'received': received,
                           'note': note,
                           'transaction_ids': transaction_ids,
                           'unpaid_disposition_id': unpaid_disposition_id
                       })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents


# Description:  Reports Cake Conversion events
# References: https://support.getcake.com/support/solutions/articles/13000035430-reports-eventsconversions-api-version-17
def reportCakeConversion(start_date=datetime.now(tz).strftime("%m/%d/%y"),
                         end_date=(datetime.now(tz) +
                                   timedelta(days=1)).strftime("%m/%d/%y"),
                         source_affiliate_id=0,
                         brand_advertiser_id=0,
                         site_offer_id=0,
                         campaign_id=0,
                         creative_id=0,
                         event_type='all',
                         event_id=0,
                         channel_id=0,
                         site_offer_contract_id=0,
                         source_affiliate_tag_id=0,
                         brand_advertiser_tag_id=0,
                         site_offer_tag_id=0,
                         price_format_id=0,
                         source_type='manual_insertion',
                         payment_percentage_filter='both',
                         disposition_type='all',
                         disposition_id=0,
                         source_affiliate_billing_status='all',
                         brand_advertiser_billing_status='all',
                         test_filter='non_tests',
                         start_at_row=0,
                         row_limit=3000,
                         sort_field='request_session_id',
                         sort_descending='TRUE'):

    url = requests.get(f'https://{DOMAIN}/api/17/reports.asmx/EventConversions',
                       params={
                           'api_key': API_KEY,
                           'start_date': start_date,
                           'end_date': end_date,
                           'source_affiliate_id': source_affiliate_id,
                           'brand_advertiser_id': brand_advertiser_id,
                           'site_offer_id': site_offer_id,
                           'campaign_id': campaign_id,
                           'creative_id': creative_id,
                           'event_type': event_type,
                           'event_id': event_id,
                           'channel_id': channel_id,
                           'site_offer_contract_id': site_offer_contract_id,
                           'source_affiliate_tag_id': source_affiliate_tag_id,
                           'brand_advertiser_tag_id': brand_advertiser_tag_id,
                           'site_offer_tag_id': site_offer_tag_id,
                           'price_format_id': price_format_id,
                           'source_type': source_type,
                           'payment_percentage_filter': payment_percentage_filter,
                           'disposition_type': disposition_type,
                           'disposition_id': disposition_id,
                           'source_affiliate_billing_status': source_affiliate_billing_status,
                           'brand_advertiser_billing_status': brand_advertiser_billing_status,
                           'test_filter': test_filter,
                           'start_at_row': start_at_row,
                           'row_limit': row_limit,
                           'sort_field': sort_field,
                           'sort_descending': sort_descending
                       })

    print(url.url)

    contents = xmltodict.parse(url.text, dict_constructor=dict, force_list={
                               'event_conversion': True})

    return contents


# Description:  Updates Cake Conversion events
# Reference: https://support.getcake.com/support/solutions/articles/5000631028-track-updateconversion-api-version-4
def updateCakeConversion(offer_id=0,
                         conversion_id=0,
                         request_session_id=0,
                         transaction_id=0,
                         payout=0,
                         add_to_existing_payout='TRUE',
                         received=0,
                         received_option='no_change',
                         disposition_type='no_change',
                         disposition_id=0,
                         update_revshare_payout='FALSE',
                         effective_date_option='conversion_date',
                         custom_date='01/01/2022 00:00:00',
                         note_to_append='',
                         disallow_on_billing_status='ignore'):

    url = requests.get(f'https://{DOMAIN}/api/4/track.asmx/UpdateConversion',
                       params={
                           'api_key': API_KEY,
                           'offer_id': offer_id,
                           'conversion_id': conversion_id,
                           'request_session_id': request_session_id,
                           'transaction_id': transaction_id,
                           'payout': payout,
                           'add_to_existing_payout': add_to_existing_payout,
                           'received': received,
                           'received_option': received_option,
                           'disposition_type': disposition_type,
                           'disposition_id': disposition_id,
                           'update_revshare_payout': update_revshare_payout,
                           'effective_date_option': effective_date_option,
                           'custom_date': custom_date,
                           'note_to_append': note_to_append,
                           'disallow_on_billing_status': disallow_on_billing_status
                       })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents


# Description: Uses Cake authentication
# Reference: https://support.getcake.com/support/solutions/articles/5000545840-auth-login-api-version-2
def authCakeLogin(username, password, ip_address):

    url = requests.get(f'https://{DOMAIN}/api/2/auth.asmx/Login',
                       params={
                           'username': username,
                           'password': password,
                           'ip_address': ip_address
                       })

    contents = xmltodict.parse(url.text, dict_constructor=dict)

    return contents
