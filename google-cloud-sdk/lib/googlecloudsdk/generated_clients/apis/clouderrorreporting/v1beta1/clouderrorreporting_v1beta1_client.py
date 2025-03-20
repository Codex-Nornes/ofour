"""Generated client library for clouderrorreporting version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.clouderrorreporting.v1beta1 import clouderrorreporting_v1beta1_messages as messages


class ClouderrorreportingV1beta1(base_api.BaseApiClient):
  """Generated client library for service clouderrorreporting version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://clouderrorreporting.googleapis.com/'
  MTLS_BASE_URL = 'https://clouderrorreporting.mtls.googleapis.com/'

  _PACKAGE = 'clouderrorreporting'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1beta1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'ClouderrorreportingV1beta1'
  _URL_VERSION = 'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new clouderrorreporting handle."""
    url = url or self.BASE_URL
    super(ClouderrorreportingV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_events = self.ProjectsEventsService(self)
    self.projects_groupStats = self.ProjectsGroupStatsService(self)
    self.projects_groups = self.ProjectsGroupsService(self)
    self.projects_locations_events = self.ProjectsLocationsEventsService(self)
    self.projects_locations_groupStats = self.ProjectsLocationsGroupStatsService(self)
    self.projects_locations_groups = self.ProjectsLocationsGroupsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsEventsService(base_api.BaseApiService):
    """Service class for the projects_events resource."""

    _NAME = 'projects_events'

    def __init__(self, client):
      super(ClouderrorreportingV1beta1.ProjectsEventsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists the specified events.

      Args:
        request: (ClouderrorreportingProjectsEventsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListEventsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/events',
        http_method='GET',
        method_id='clouderrorreporting.projects.events.list',
        ordered_params=['projectName'],
        path_params=['projectName'],
        query_params=['groupId', 'pageSize', 'pageToken', 'serviceFilter_resourceType', 'serviceFilter_service', 'serviceFilter_version', 'timeRange_period'],
        relative_path='v1beta1/{+projectName}/events',
        request_field='',
        request_type_name='ClouderrorreportingProjectsEventsListRequest',
        response_type_name='ListEventsResponse',
        supports_download=False,
    )

    def Report(self, request, global_params=None):
      r"""Report an individual error event and record the event to a log. This endpoint accepts **either** an OAuth token, **or** an [API key](https://support.google.com/cloud/answer/6158862) for authentication. To use an API key, append it to the URL as the value of a `key` parameter. For example: `POST https://clouderrorreporting.googleapis.com/v1beta1/{projectName}/events:report?key=123ABC456` **Note:** [Error Reporting] (https://cloud.google.com/error-reporting) is a service built on Cloud Logging and can analyze log entries when all of the following are true: * Customer-managed encryption keys (CMEK) are disabled on the log bucket. * The log bucket satisfies one of the following: * The log bucket is stored in the same project where the logs originated. * The logs were routed to a project, and then that project stored those logs in a log bucket that it owns.

      Args:
        request: (ClouderrorreportingProjectsEventsReportRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ReportErrorEventResponse) The response message.
      """
      config = self.GetMethodConfig('Report')
      return self._RunMethod(
          config, request, global_params=global_params)

    Report.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/events:report',
        http_method='POST',
        method_id='clouderrorreporting.projects.events.report',
        ordered_params=['projectName'],
        path_params=['projectName'],
        query_params=[],
        relative_path='v1beta1/{+projectName}/events:report',
        request_field='reportedErrorEvent',
        request_type_name='ClouderrorreportingProjectsEventsReportRequest',
        response_type_name='ReportErrorEventResponse',
        supports_download=False,
    )

  class ProjectsGroupStatsService(base_api.BaseApiService):
    """Service class for the projects_groupStats resource."""

    _NAME = 'projects_groupStats'

    def __init__(self, client):
      super(ClouderrorreportingV1beta1.ProjectsGroupStatsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists the specified groups.

      Args:
        request: (ClouderrorreportingProjectsGroupStatsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListGroupStatsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/groupStats',
        http_method='GET',
        method_id='clouderrorreporting.projects.groupStats.list',
        ordered_params=['projectName'],
        path_params=['projectName'],
        query_params=['alignment', 'alignmentTime', 'groupId', 'order', 'pageSize', 'pageToken', 'serviceFilter_resourceType', 'serviceFilter_service', 'serviceFilter_version', 'timeRange_period', 'timedCountDuration'],
        relative_path='v1beta1/{+projectName}/groupStats',
        request_field='',
        request_type_name='ClouderrorreportingProjectsGroupStatsListRequest',
        response_type_name='ListGroupStatsResponse',
        supports_download=False,
    )

  class ProjectsGroupsService(base_api.BaseApiService):
    """Service class for the projects_groups resource."""

    _NAME = 'projects_groups'

    def __init__(self, client):
      super(ClouderrorreportingV1beta1.ProjectsGroupsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Get the specified group.

      Args:
        request: (ClouderrorreportingProjectsGroupsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ErrorGroup) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/groups/{groupsId}',
        http_method='GET',
        method_id='clouderrorreporting.projects.groups.get',
        ordered_params=['groupName'],
        path_params=['groupName'],
        query_params=[],
        relative_path='v1beta1/{+groupName}',
        request_field='',
        request_type_name='ClouderrorreportingProjectsGroupsGetRequest',
        response_type_name='ErrorGroup',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Replace the data for the specified group. Fails if the group does not exist.

      Args:
        request: (ErrorGroup) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ErrorGroup) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/groups/{groupsId}',
        http_method='PUT',
        method_id='clouderrorreporting.projects.groups.update',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='<request>',
        request_type_name='ErrorGroup',
        response_type_name='ErrorGroup',
        supports_download=False,
    )

  class ProjectsLocationsEventsService(base_api.BaseApiService):
    """Service class for the projects_locations_events resource."""

    _NAME = 'projects_locations_events'

    def __init__(self, client):
      super(ClouderrorreportingV1beta1.ProjectsLocationsEventsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists the specified events.

      Args:
        request: (ClouderrorreportingProjectsLocationsEventsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListEventsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/events',
        http_method='GET',
        method_id='clouderrorreporting.projects.locations.events.list',
        ordered_params=['projectName'],
        path_params=['projectName'],
        query_params=['groupId', 'pageSize', 'pageToken', 'serviceFilter_resourceType', 'serviceFilter_service', 'serviceFilter_version', 'timeRange_period'],
        relative_path='v1beta1/{+projectName}/events',
        request_field='',
        request_type_name='ClouderrorreportingProjectsLocationsEventsListRequest',
        response_type_name='ListEventsResponse',
        supports_download=False,
    )

  class ProjectsLocationsGroupStatsService(base_api.BaseApiService):
    """Service class for the projects_locations_groupStats resource."""

    _NAME = 'projects_locations_groupStats'

    def __init__(self, client):
      super(ClouderrorreportingV1beta1.ProjectsLocationsGroupStatsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists the specified groups.

      Args:
        request: (ClouderrorreportingProjectsLocationsGroupStatsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListGroupStatsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/groupStats',
        http_method='GET',
        method_id='clouderrorreporting.projects.locations.groupStats.list',
        ordered_params=['projectName'],
        path_params=['projectName'],
        query_params=['alignment', 'alignmentTime', 'groupId', 'order', 'pageSize', 'pageToken', 'serviceFilter_resourceType', 'serviceFilter_service', 'serviceFilter_version', 'timeRange_period', 'timedCountDuration'],
        relative_path='v1beta1/{+projectName}/groupStats',
        request_field='',
        request_type_name='ClouderrorreportingProjectsLocationsGroupStatsListRequest',
        response_type_name='ListGroupStatsResponse',
        supports_download=False,
    )

  class ProjectsLocationsGroupsService(base_api.BaseApiService):
    """Service class for the projects_locations_groups resource."""

    _NAME = 'projects_locations_groups'

    def __init__(self, client):
      super(ClouderrorreportingV1beta1.ProjectsLocationsGroupsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Get the specified group.

      Args:
        request: (ClouderrorreportingProjectsLocationsGroupsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ErrorGroup) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/groups/{groupsId}',
        http_method='GET',
        method_id='clouderrorreporting.projects.locations.groups.get',
        ordered_params=['groupName'],
        path_params=['groupName'],
        query_params=[],
        relative_path='v1beta1/{+groupName}',
        request_field='',
        request_type_name='ClouderrorreportingProjectsLocationsGroupsGetRequest',
        response_type_name='ErrorGroup',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Replace the data for the specified group. Fails if the group does not exist.

      Args:
        request: (ErrorGroup) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ErrorGroup) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/groups/{groupsId}',
        http_method='PUT',
        method_id='clouderrorreporting.projects.locations.groups.update',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='<request>',
        request_type_name='ErrorGroup',
        response_type_name='ErrorGroup',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(ClouderrorreportingV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def DeleteEvents(self, request, global_params=None):
      r"""Deletes all error events of a given project.

      Args:
        request: (ClouderrorreportingProjectsLocationsDeleteEventsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DeleteEventsResponse) The response message.
      """
      config = self.GetMethodConfig('DeleteEvents')
      return self._RunMethod(
          config, request, global_params=global_params)

    DeleteEvents.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/events',
        http_method='DELETE',
        method_id='clouderrorreporting.projects.locations.deleteEvents',
        ordered_params=['projectName'],
        path_params=['projectName'],
        query_params=[],
        relative_path='v1beta1/{+projectName}/events',
        request_field='',
        request_type_name='ClouderrorreportingProjectsLocationsDeleteEventsRequest',
        response_type_name='DeleteEventsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(ClouderrorreportingV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def DeleteEvents(self, request, global_params=None):
      r"""Deletes all error events of a given project.

      Args:
        request: (ClouderrorreportingProjectsDeleteEventsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DeleteEventsResponse) The response message.
      """
      config = self.GetMethodConfig('DeleteEvents')
      return self._RunMethod(
          config, request, global_params=global_params)

    DeleteEvents.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/events',
        http_method='DELETE',
        method_id='clouderrorreporting.projects.deleteEvents',
        ordered_params=['projectName'],
        path_params=['projectName'],
        query_params=[],
        relative_path='v1beta1/{+projectName}/events',
        request_field='',
        request_type_name='ClouderrorreportingProjectsDeleteEventsRequest',
        response_type_name='DeleteEventsResponse',
        supports_download=False,
    )
