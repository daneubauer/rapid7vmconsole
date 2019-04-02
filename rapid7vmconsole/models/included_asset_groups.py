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


class IncludedAssetGroups(object):
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
        'asset_group_i_ds': 'list[int]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'asset_group_i_ds': 'assetGroupIDs',
        'links': 'links'
    }

    def __init__(self, asset_group_i_ds=None, links=None):  # noqa: E501
        """IncludedAssetGroups - a model defined in Swagger"""  # noqa: E501

        self._asset_group_i_ds = None
        self._links = None
        self.discriminator = None

        if asset_group_i_ds is not None:
            self.asset_group_i_ds = asset_group_i_ds
        if links is not None:
            self.links = links

    @property
    def asset_group_i_ds(self):
        """Gets the asset_group_i_ds of this IncludedAssetGroups.  # noqa: E501

        List of asset group identifiers. Each element is an integer.  # noqa: E501

        :return: The asset_group_i_ds of this IncludedAssetGroups.  # noqa: E501
        :rtype: list[int]
        """
        return self._asset_group_i_ds

    @asset_group_i_ds.setter
    def asset_group_i_ds(self, asset_group_i_ds):
        """Sets the asset_group_i_ds of this IncludedAssetGroups.

        List of asset group identifiers. Each element is an integer.  # noqa: E501

        :param asset_group_i_ds: The asset_group_i_ds of this IncludedAssetGroups.  # noqa: E501
        :type: list[int]
        """

        self._asset_group_i_ds = asset_group_i_ds

    @property
    def links(self):
        """Gets the links of this IncludedAssetGroups.  # noqa: E501


        :return: The links of this IncludedAssetGroups.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IncludedAssetGroups.


        :param links: The links of this IncludedAssetGroups.  # noqa: E501
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
        if issubclass(IncludedAssetGroups, dict):
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
        if not isinstance(other, IncludedAssetGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
