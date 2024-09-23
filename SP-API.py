from sp_api.api import Reports
from sp_api.base import Marketplaces, ReportType, ProcessingStatus 
import time 
# import requests 
# import csv 
# import json

credentials=(
    refresh_token=''
    Twa_app_id=''
    lwa_client_secret=''
)
marketPlace = Marketplaces.US


def getorders():
    report_type = ReportType.GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL
    res = Reports(credentials=credentials, marketplace=marketPlace)
    data = res.create_report(reportType=report_type, dataStartTime="2021-01-15")
    print(data)
    time. sleep (1000)
getorders()

def getorders():
    print("Getting Orders")
    report_type = ReportType. GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL
    res = Reports(credentials=credentials, marketplace=marketPlace)
    data = res.create_report(reportType=report_type, dataStartTime="2021-01-30")
    reportid = data.payload[ 'reportId']
    res.get_report(reportId)
    while data.payload.get('processingStatus') not in [ProcessingStatus.DONE, ProcessingStatus. FATAL,
        ProcessingStatus.CANCELLED]:
        time.sleep (2)
        data = res.get_report(reportId)
        print(data.payload.get('processingStatus'))
    if data.payload.get('processingStatus') in [ProcessingStatus.FATAL, ProcessingStatus.CANCELLED]:
        print("Report Failed")
        reportData = res.get_report_document(data.payload['reportDocumentId'], decrypt=True)
        ceportUrl = reportData.payload.get('url')
        res = requests.get(reportUrl)
        print(reportUrl)
getOrdersO
