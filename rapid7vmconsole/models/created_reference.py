# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from rapid7vmconsole.models.link import Link  # noqa: F401,E501


class CreatedReference(object):
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
        'id': 'object',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links'
    }

    def __init__(self, id=None, links=None):  # noqa: E501
        """CreatedReference - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this CreatedReference.  # noqa: E501

        The identifier of the resource created.  # noqa: E501

        :return: The id of this CreatedReference.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreatedReference.

        The identifier of the resource created.  # noqa: E501

        :param id: The id of this CreatedReference.  # noqa: E501
        :type: object
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this CreatedReference.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this CreatedReference.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CreatedReference.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this CreatedReference.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if issubclass(CreatedReference, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreatedReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
