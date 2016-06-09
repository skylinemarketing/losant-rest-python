""" Module for Losant API Webhook wrapper class """
# pylint: disable=C0301

class Webhook(object):
    """ Class containing all the actions for the Webhook Resource """

    def __init__(self, client):
        self.client = client

    def delete(self, **kwargs):
        """
        Deletes a webhook

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} webhookId - ID associated with the webhook
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - If webhook was successfully deleted (https://api.losant.com/#/definitions/success)

        Errors:
        *  404 - Error if webhook was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "webhookId" in kwargs:
            path_params["webhookId"] = kwargs["webhookId"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/webhooks/{webhookId}".format(**path_params)

        return self.client.request("DELETE", path, params=query_params, headers=headers, body=body)

    def get(self, **kwargs):
        """
        Retrieves information on a webhook

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} webhookId - ID associated with the webhook
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Webhook information (https://api.losant.com/#/definitions/webhook)

        Errors:
        *  404 - Error if webhook was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "webhookId" in kwargs:
            path_params["webhookId"] = kwargs["webhookId"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/webhooks/{webhookId}".format(**path_params)

        return self.client.request("GET", path, params=query_params, headers=headers, body=body)

    def patch(self, **kwargs):
        """
        Updates information about a webhook

        Parameters:
        *  {string} applicationId - ID associated with the application
        *  {string} webhookId - ID associated with the webhook
        *  {hash} webhook - Object containing new properties of the webhook (https://api.losant.com/#/definitions/webhookPatch)
        *  {boolean} _actions - Return resource actions in response
        *  {boolean} _links - Return resource link in response
        *  {boolean} _embedded - Return embedded resources in response

        Responses:
        *  200 - Updated webhook information (https://api.losant.com/#/definitions/webhook)

        Errors:
        *  400 - Error if malformed request (https://api.losant.com/#/definitions/error)
        *  404 - Error if webhook was not found (https://api.losant.com/#/definitions/error)
        """

        query_params = {"_actions": "false", "_links": "true", "_embedded": "true"}
        path_params = {}
        headers = {}
        body = None

        if "applicationId" in kwargs:
            path_params["applicationId"] = kwargs["applicationId"]
        if "webhookId" in kwargs:
            path_params["webhookId"] = kwargs["webhookId"]
        if "webhook" in kwargs:
            body = kwargs["webhook"]
        if "_actions" in kwargs:
            query_params["_actions"] = kwargs["_actions"]
        if "_links" in kwargs:
            query_params["_links"] = kwargs["_links"]
        if "_embedded" in kwargs:
            query_params["_embedded"] = kwargs["_embedded"]

        path = "/applications/{applicationId}/webhooks/{webhookId}".format(**path_params)

        return self.client.request("PATCH", path, params=query_params, headers=headers, body=body)

