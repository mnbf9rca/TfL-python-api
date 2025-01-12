base_url = "https://api.tfl.gov.uk/"

endpoints = {
    'stopPointsByLineId': 'Line/{0}/StopPoints',
    'lineMetaModes': 'Line/Meta/Modes',
    'linesByLineId': 'Line/{0}',
    'linesByMode': 'Line/Mode/{0}',
    'lineStatus': 'Line/{0}/Status',
    'lineStatusBySeverity': 'Line/Status/{0}',
    'routeByLineId': 'Line/{0}/Route',
    'routeByMode': 'Line/Mode/{0}/Route',
    'lineDisruptionsByLineId': 'Line/{0}/Disruption',
    'lineDisruptionsByMode': 'Line/Mode/{0}/Disruption',

    'stopPointMetaModes': 'StopPoint/Meta/Modes',
    'stopPointById': 'StopPoint/{0}',
    'stopPointByMode': 'StopPoint/Mode/{0}',
    'stopPointArrivals': 'StopPoint/{0}/Arrivals',

    'arrivalsByLineId': 'Line/{0}/Arrivals'
}
