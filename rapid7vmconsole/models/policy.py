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


class Policy(object):
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
        'enabled': 'list[int]',
        'links': 'list[Link]',
        'recursive_windows_fs_search': 'bool',
        'store_scap': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'links': 'links',
        'recursive_windows_fs_search': 'recursiveWindowsFSSearch',
        'store_scap': 'storeSCAP'
    }

    def __init__(self, enabled=None, links=None, recursive_windows_fs_search=None, store_scap=None):  # noqa: E501
        """Policy - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._links = None
        self._recursive_windows_fs_search = None
        self._store_scap = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if links is not None:
            self.links = links
        if recursive_windows_fs_search is not None:
            self.recursive_windows_fs_search = recursive_windows_fs_search
        if store_scap is not None:
            self.store_scap = store_scap

    @property
    def enabled(self):
        """Gets the enabled of this Policy.  # noqa: E501

        The identifiers of the policies enabled to be checked during a scan. No policies are enabled by default.  # noqa: E501

        :return: The enabled of this Policy.  # noqa: E501
        :rtype: list[int]
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Policy.

        The identifiers of the policies enabled to be checked during a scan. No policies are enabled by default.  # noqa: E501

        :param enabled: The enabled of this Policy.  # noqa: E501
        :type: list[int]
        """

        self._enabled = enabled

    @property
    def links(self):
        """Gets the links of this Policy.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this Policy.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Policy.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this Policy.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def recursive_windows_fs_search(self):
        """Gets the recursive_windows_fs_search of this Policy.  # noqa: E501

        Whether recursive windows file searches are enabled, if your internal security practices require this capability. Recursive file searches can increase scan times by several hours, depending on the number of files and other factors, so this setting is disabled for Windows systems by default. Defaults to `false`.  # noqa: E501

        :return: The recursive_windows_fs_search of this Policy.  # noqa: E501
        :rtype: bool
        """
        return self._recursive_windows_fs_search

    @recursive_windows_fs_search.setter
    def recursive_windows_fs_search(self, recursive_windows_fs_search):
        """Sets the recursive_windows_fs_search of this Policy.

        Whether recursive windows file searches are enabled, if your internal security practices require this capability. Recursive file searches can increase scan times by several hours, depending on the number of files and other factors, so this setting is disabled for Windows systems by default. Defaults to `false`.  # noqa: E501

        :param recursive_windows_fs_search: The recursive_windows_fs_search of this Policy.  # noqa: E501
        :type: bool
        """

        self._recursive_windows_fs_search = recursive_windows_fs_search

    @property
    def store_scap(self):
        """Gets the store_scap of this Policy.  # noqa: E501

        Whether Asset Reporting Format (ARF) results are stored. If you are required to submit reports of your policy scan results to the U.S. government in ARF for SCAP certification, you will need to store SCAP data so that it can be exported in this format. Note that stored SCAP data can accumulate rapidly, which can have a significant impact on file storage. Defaults to `false`.  # noqa: E501

        :return: The store_scap of this Policy.  # noqa: E501
        :rtype: bool
        """
        return self._store_scap

    @store_scap.setter
    def store_scap(self, store_scap):
        """Sets the store_scap of this Policy.

        Whether Asset Reporting Format (ARF) results are stored. If you are required to submit reports of your policy scan results to the U.S. government in ARF for SCAP certification, you will need to store SCAP data so that it can be exported in this format. Note that stored SCAP data can accumulate rapidly, which can have a significant impact on file storage. Defaults to `false`.  # noqa: E501

        :param store_scap: The store_scap of this Policy.  # noqa: E501
        :type: bool
        """

        self._store_scap = store_scap

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
        if issubclass(Policy, dict):
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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other