import json

from msrest import Deserializer
from .config import endpoints
from .api_token import ApiToken
from .rest_client import RestClient
from . import models


class Client:
    """Client

    :param ApiToken api_token: API token to access TfL unified API
    """

    def __init__(self, api_token):
        self.client = RestClient(api_token)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        #print (client_models)
        self._deserialize = Deserializer(client_models)

    def _raise_exception_if_error_in_response(self, response) -> bool:
        if response.status_code != 200:
            raise Exception(response.text)
        return True

    def get_stop_points_by_line_id(self, line_id) -> dict[models.StopPoint]:
        response = self.client.send_request(endpoints['stopPointsByLineId'].format(line_id))
        if self._raise_exception_if_error_in_response(response):
            return self._deserialize('[StopPoint]', response)

    def get_line_meta_modes(self) -> dict[models.Mode]:
        response = self.client.send_request(endpoints['lineMetaModes'])
        if self._raise_exception_if_error_in_response(response):
            return self._deserialize('[Mode]', response)

    def get_lines(self, line_id=None, mode=None) -> dict[models.Line]:
        if line_id is None and mode is None:
            raise Exception(
                'Either the --line_id argument or the --mode argument needs to be specified.')
        if line_id is not None:
            endpoint = endpoints['linesByLineId'].format(line_id)
        else:
            endpoint = endpoints['linesByMode'].format(mode)
        response = self.client.send_request(endpoint)
        if self._raise_exception_if_error_in_response(response):
            return self._deserialize('[Line]', response)

    def get_line_status(self, line, include_details=None) -> dict[models.Line]:
        response = self.client.send_request(endpoints['lineStatus'].format(line), {
                                            'detail': include_details is True})
        if self._raise_exception_if_error_in_response(response):
            return self._deserialize('[Line]', response)

    def get_line_status_severity(self, severity) -> dict[models.Line]:
        response = self.client.send_request(endpoints['lineStatusBySeverity'].format(severity))
        if self._raise_exception_if_error_in_response(response):
            return self._deserialize('[Line]', response)

    def get_route_by_line_id(self, line_id) -> dict[models.Line]:
        response = self.client.send_request(endpoints['routeByLineId'].format(line_id))
        if self._raise_exception_if_error_in_response(response):
            return self._deserialize('[Line]', response)

    def get_route_by_mode(self, mode) -> dict[models.Line]:
        response = self.client.send_request(endpoints['routeByMode'].format(mode))
        if self._raise_exception_if_error_in_response(response):
            return self._deserialize('[Line]', response)

    def get_line_disruptions_by_line_id(self, line_id) -> dict[models.Disruption]:
        response = self.client.send_request(endpoints['lineDisruptionsByLineId'].format(line_id))
        if self._raise_exception_if_error_in_response(response):
            return self._deserialize('[Disruption]', response)

    def get_line_disruptions_by_mode(self, mode) -> dict[models.Disruption]:
        response = self.client.send_request(endpoints['lineDisruptionsByMode'].format(mode))
        if self._raise_exception_if_error_in_response(response):
            return self._deserialize('[Disruption]', response)

    def get_stop_points_by_id(self, stop_point_id) -> models.StopPoint:
        response = self.client.send_request(endpoints['stopPointById'].format(stop_point_id))
        if self._raise_exception_if_error_in_response(response):
            return self._deserialize('StopPoint', response)

    def get_stop_points_by_mode(self, mode) -> models.StopPointsResponse:
        response = self.client.send_request(endpoints['stopPointByMode'].format(mode))
        if self._raise_exception_if_error_in_response(response):
            return self._deserialize('StopPointsResponse', response)

    def get_stop_point_meta_modes(self) -> dict[models.Mode]:
        response = self.client.send_request(endpoints['stopPointMetaModes'])
        if self._raise_exception_if_error_in_response(response):
            return self._deserialize('[Mode]', response)

    def get_arrivals_by_stop_point(self, stop_point_id, line_id=None) -> dict[models.Prediction]:
        response = self.client.send_request(endpoints['stopPointArrivals'].format(
            stop_point_id), {'lineIds': line_id is True})
        if self._raise_exception_if_error_in_response(response):
            return self._deserialize('[Prediction]', response)

    def get_arrivals_by_line_id(self, line_id) -> dict[models.Prediction]:
        response = self.client.send_request(endpoints['arrivalsByLineId'].format(line_id))
        if self._raise_exception_if_error_in_response(response):
            return self._deserialize('[Prediction]', response)
