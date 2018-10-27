# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.11.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V2beta1PodsMetricStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'current_average_value': 'str',
        'metric_name': 'str'
    }

    attribute_map = {
        'current_average_value': 'currentAverageValue',
        'metric_name': 'metricName'
    }

    def __init__(self, current_average_value=None, metric_name=None):  # noqa: E501
        """V2beta1PodsMetricStatus - a model defined in Swagger"""  # noqa: E501

        self._current_average_value = None
        self._metric_name = None
        self.discriminator = None

        self.current_average_value = current_average_value
        self.metric_name = metric_name

    @property
    def current_average_value(self):
        """Gets the current_average_value of this V2beta1PodsMetricStatus.  # noqa: E501

        currentAverageValue is the current value of the average of the metric across all relevant pods (as a quantity)  # noqa: E501

        :return: The current_average_value of this V2beta1PodsMetricStatus.  # noqa: E501
        :rtype: str
        """
        return self._current_average_value

    @current_average_value.setter
    def current_average_value(self, current_average_value):
        """Sets the current_average_value of this V2beta1PodsMetricStatus.

        currentAverageValue is the current value of the average of the metric across all relevant pods (as a quantity)  # noqa: E501

        :param current_average_value: The current_average_value of this V2beta1PodsMetricStatus.  # noqa: E501
        :type: str
        """
        if current_average_value is None:
            raise ValueError("Invalid value for `current_average_value`, must not be `None`")  # noqa: E501

        self._current_average_value = current_average_value

    @property
    def metric_name(self):
        """Gets the metric_name of this V2beta1PodsMetricStatus.  # noqa: E501

        metricName is the name of the metric in question  # noqa: E501

        :return: The metric_name of this V2beta1PodsMetricStatus.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this V2beta1PodsMetricStatus.

        metricName is the name of the metric in question  # noqa: E501

        :param metric_name: The metric_name of this V2beta1PodsMetricStatus.  # noqa: E501
        :type: str
        """
        if metric_name is None:
            raise ValueError("Invalid value for `metric_name`, must not be `None`")  # noqa: E501

        self._metric_name = metric_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, V2beta1PodsMetricStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
