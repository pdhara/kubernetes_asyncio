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


class V1beta1CustomResourceDefinitionNames(object):
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
        'categories': 'list[str]',
        'kind': 'str',
        'list_kind': 'str',
        'plural': 'str',
        'short_names': 'list[str]',
        'singular': 'str'
    }

    attribute_map = {
        'categories': 'categories',
        'kind': 'kind',
        'list_kind': 'listKind',
        'plural': 'plural',
        'short_names': 'shortNames',
        'singular': 'singular'
    }

    def __init__(self, categories=None, kind=None, list_kind=None, plural=None, short_names=None, singular=None):  # noqa: E501
        """V1beta1CustomResourceDefinitionNames - a model defined in Swagger"""  # noqa: E501

        self._categories = None
        self._kind = None
        self._list_kind = None
        self._plural = None
        self._short_names = None
        self._singular = None
        self.discriminator = None

        if categories is not None:
            self.categories = categories
        self.kind = kind
        if list_kind is not None:
            self.list_kind = list_kind
        self.plural = plural
        if short_names is not None:
            self.short_names = short_names
        if singular is not None:
            self.singular = singular

    @property
    def categories(self):
        """Gets the categories of this V1beta1CustomResourceDefinitionNames.  # noqa: E501

        Categories is a list of grouped resources custom resources belong to (e.g. 'all')  # noqa: E501

        :return: The categories of this V1beta1CustomResourceDefinitionNames.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this V1beta1CustomResourceDefinitionNames.

        Categories is a list of grouped resources custom resources belong to (e.g. 'all')  # noqa: E501

        :param categories: The categories of this V1beta1CustomResourceDefinitionNames.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def kind(self):
        """Gets the kind of this V1beta1CustomResourceDefinitionNames.  # noqa: E501

        Kind is the serialized kind of the resource.  It is normally CamelCase and singular.  # noqa: E501

        :return: The kind of this V1beta1CustomResourceDefinitionNames.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1beta1CustomResourceDefinitionNames.

        Kind is the serialized kind of the resource.  It is normally CamelCase and singular.  # noqa: E501

        :param kind: The kind of this V1beta1CustomResourceDefinitionNames.  # noqa: E501
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def list_kind(self):
        """Gets the list_kind of this V1beta1CustomResourceDefinitionNames.  # noqa: E501

        ListKind is the serialized kind of the list for this resource.  Defaults to <kind>List.  # noqa: E501

        :return: The list_kind of this V1beta1CustomResourceDefinitionNames.  # noqa: E501
        :rtype: str
        """
        return self._list_kind

    @list_kind.setter
    def list_kind(self, list_kind):
        """Sets the list_kind of this V1beta1CustomResourceDefinitionNames.

        ListKind is the serialized kind of the list for this resource.  Defaults to <kind>List.  # noqa: E501

        :param list_kind: The list_kind of this V1beta1CustomResourceDefinitionNames.  # noqa: E501
        :type: str
        """

        self._list_kind = list_kind

    @property
    def plural(self):
        """Gets the plural of this V1beta1CustomResourceDefinitionNames.  # noqa: E501

        Plural is the plural name of the resource to serve.  It must match the name of the CustomResourceDefinition-registration too: plural.group and it must be all lowercase.  # noqa: E501

        :return: The plural of this V1beta1CustomResourceDefinitionNames.  # noqa: E501
        :rtype: str
        """
        return self._plural

    @plural.setter
    def plural(self, plural):
        """Sets the plural of this V1beta1CustomResourceDefinitionNames.

        Plural is the plural name of the resource to serve.  It must match the name of the CustomResourceDefinition-registration too: plural.group and it must be all lowercase.  # noqa: E501

        :param plural: The plural of this V1beta1CustomResourceDefinitionNames.  # noqa: E501
        :type: str
        """
        if plural is None:
            raise ValueError("Invalid value for `plural`, must not be `None`")  # noqa: E501

        self._plural = plural

    @property
    def short_names(self):
        """Gets the short_names of this V1beta1CustomResourceDefinitionNames.  # noqa: E501

        ShortNames are short names for the resource.  It must be all lowercase.  # noqa: E501

        :return: The short_names of this V1beta1CustomResourceDefinitionNames.  # noqa: E501
        :rtype: list[str]
        """
        return self._short_names

    @short_names.setter
    def short_names(self, short_names):
        """Sets the short_names of this V1beta1CustomResourceDefinitionNames.

        ShortNames are short names for the resource.  It must be all lowercase.  # noqa: E501

        :param short_names: The short_names of this V1beta1CustomResourceDefinitionNames.  # noqa: E501
        :type: list[str]
        """

        self._short_names = short_names

    @property
    def singular(self):
        """Gets the singular of this V1beta1CustomResourceDefinitionNames.  # noqa: E501

        Singular is the singular name of the resource.  It must be all lowercase  Defaults to lowercased <kind>  # noqa: E501

        :return: The singular of this V1beta1CustomResourceDefinitionNames.  # noqa: E501
        :rtype: str
        """
        return self._singular

    @singular.setter
    def singular(self, singular):
        """Sets the singular of this V1beta1CustomResourceDefinitionNames.

        Singular is the singular name of the resource.  It must be all lowercase  Defaults to lowercased <kind>  # noqa: E501

        :param singular: The singular of this V1beta1CustomResourceDefinitionNames.  # noqa: E501
        :type: str
        """

        self._singular = singular

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
        if not isinstance(other, V1beta1CustomResourceDefinitionNames):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
