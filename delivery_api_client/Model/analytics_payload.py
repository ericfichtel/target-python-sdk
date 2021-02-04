# coding: utf-8

"""
    Adobe Target Delivery API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AnalyticsPayload(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'pe': 'str',
        'tnta': 'str'
    }

    attribute_map = {
        'pe': 'pe',
        'tnta': 'tnta'
    }

    def __init__(self, pe=None, tnta=None):  # noqa: E501
        """AnalyticsPayload - a model defined in OpenAPI"""  # noqa: E501

        self._pe = None
        self._tnta = None
        self.discriminator = None

        if pe is not None:
            self.pe = pe
        if tnta is not None:
            self.tnta = tnta

    @property
    def pe(self):
        """Gets the pe of this AnalyticsPayload.  # noqa: E501

        Indicates to Adobe Analytics that the payload is an Adobe Target type  # noqa: E501

        :return: The pe of this AnalyticsPayload.  # noqa: E501
        :rtype: str
        """
        return self._pe

    @pe.setter
    def pe(self, pe):
        """Sets the pe of this AnalyticsPayload.

        Indicates to Adobe Analytics that the payload is an Adobe Target type  # noqa: E501

        :param pe: The pe of this AnalyticsPayload.  # noqa: E501
        :type: str
        """

        self._pe = pe

    @property
    def tnta(self):
        """Gets the tnta of this AnalyticsPayload.  # noqa: E501

        Contains Target metadata that describes the activity and experience  # noqa: E501

        :return: The tnta of this AnalyticsPayload.  # noqa: E501
        :rtype: str
        """
        return self._tnta

    @tnta.setter
    def tnta(self, tnta):
        """Sets the tnta of this AnalyticsPayload.

        Contains Target metadata that describes the activity and experience  # noqa: E501

        :param tnta: The tnta of this AnalyticsPayload.  # noqa: E501
        :type: str
        """

        self._tnta = tnta

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnalyticsPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other