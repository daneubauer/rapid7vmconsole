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

from rapid7vmconsole.models.scan_template_web_spider_paths import ScanTemplateWebSpiderPaths  # noqa: F401,E501
from rapid7vmconsole.models.scan_template_web_spider_patterns import ScanTemplateWebSpiderPatterns  # noqa: F401,E501
from rapid7vmconsole.models.scan_template_web_spider_performance import ScanTemplateWebSpiderPerformance  # noqa: F401,E501


class ScanTemplateWebSpider(object):
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
        'dont_scan_multi_use_devices': 'bool',
        'include_query_strings': 'bool',
        'paths': 'ScanTemplateWebSpiderPaths',
        'patterns': 'ScanTemplateWebSpiderPatterns',
        'performance': 'ScanTemplateWebSpiderPerformance',
        'test_common_usernames_and_passwords': 'bool',
        'test_xss_in_single_scan': 'bool',
        'user_agent': 'str'
    }

    attribute_map = {
        'dont_scan_multi_use_devices': 'dontScanMultiUseDevices',
        'include_query_strings': 'includeQueryStrings',
        'paths': 'paths',
        'patterns': 'patterns',
        'performance': 'performance',
        'test_common_usernames_and_passwords': 'testCommonUsernamesAndPasswords',
        'test_xss_in_single_scan': 'testXssInSingleScan',
        'user_agent': 'userAgent'
    }

    def __init__(self, dont_scan_multi_use_devices=None, include_query_strings=None, paths=None, patterns=None, performance=None, test_common_usernames_and_passwords=None, test_xss_in_single_scan=None, user_agent=None):  # noqa: E501
        """ScanTemplateWebSpider - a model defined in Swagger"""  # noqa: E501

        self._dont_scan_multi_use_devices = None
        self._include_query_strings = None
        self._paths = None
        self._patterns = None
        self._performance = None
        self._test_common_usernames_and_passwords = None
        self._test_xss_in_single_scan = None
        self._user_agent = None
        self.discriminator = None

        if dont_scan_multi_use_devices is not None:
            self.dont_scan_multi_use_devices = dont_scan_multi_use_devices
        if include_query_strings is not None:
            self.include_query_strings = include_query_strings
        if paths is not None:
            self.paths = paths
        if patterns is not None:
            self.patterns = patterns
        if performance is not None:
            self.performance = performance
        if test_common_usernames_and_passwords is not None:
            self.test_common_usernames_and_passwords = test_common_usernames_and_passwords
        if test_xss_in_single_scan is not None:
            self.test_xss_in_single_scan = test_xss_in_single_scan
        if user_agent is not None:
            self.user_agent = user_agent

    @property
    def dont_scan_multi_use_devices(self):
        """Gets the dont_scan_multi_use_devices of this ScanTemplateWebSpider.  # noqa: E501

        Whether scanning of multi-use devices, such as printers or print servers should be avoided.  # noqa: E501

        :return: The dont_scan_multi_use_devices of this ScanTemplateWebSpider.  # noqa: E501
        :rtype: bool
        """
        return self._dont_scan_multi_use_devices

    @dont_scan_multi_use_devices.setter
    def dont_scan_multi_use_devices(self, dont_scan_multi_use_devices):
        """Sets the dont_scan_multi_use_devices of this ScanTemplateWebSpider.

        Whether scanning of multi-use devices, such as printers or print servers should be avoided.  # noqa: E501

        :param dont_scan_multi_use_devices: The dont_scan_multi_use_devices of this ScanTemplateWebSpider.  # noqa: E501
        :type: bool
        """

        self._dont_scan_multi_use_devices = dont_scan_multi_use_devices

    @property
    def include_query_strings(self):
        """Gets the include_query_strings of this ScanTemplateWebSpider.  # noqa: E501

        Whether query strings are using in URLs when web spidering. This causes the web spider to make many more requests to the Web server. This will increase overall scan time and possibly affect the Web server's performance for legitimate users.  # noqa: E501

        :return: The include_query_strings of this ScanTemplateWebSpider.  # noqa: E501
        :rtype: bool
        """
        return self._include_query_strings

    @include_query_strings.setter
    def include_query_strings(self, include_query_strings):
        """Sets the include_query_strings of this ScanTemplateWebSpider.

        Whether query strings are using in URLs when web spidering. This causes the web spider to make many more requests to the Web server. This will increase overall scan time and possibly affect the Web server's performance for legitimate users.  # noqa: E501

        :param include_query_strings: The include_query_strings of this ScanTemplateWebSpider.  # noqa: E501
        :type: bool
        """

        self._include_query_strings = include_query_strings

    @property
    def paths(self):
        """Gets the paths of this ScanTemplateWebSpider.  # noqa: E501

        Paths to use when web spidering.  # noqa: E501

        :return: The paths of this ScanTemplateWebSpider.  # noqa: E501
        :rtype: ScanTemplateWebSpiderPaths
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this ScanTemplateWebSpider.

        Paths to use when web spidering.  # noqa: E501

        :param paths: The paths of this ScanTemplateWebSpider.  # noqa: E501
        :type: ScanTemplateWebSpiderPaths
        """

        self._paths = paths

    @property
    def patterns(self):
        """Gets the patterns of this ScanTemplateWebSpider.  # noqa: E501

        Patterns to match responses during web spidering.  # noqa: E501

        :return: The patterns of this ScanTemplateWebSpider.  # noqa: E501
        :rtype: ScanTemplateWebSpiderPatterns
        """
        return self._patterns

    @patterns.setter
    def patterns(self, patterns):
        """Sets the patterns of this ScanTemplateWebSpider.

        Patterns to match responses during web spidering.  # noqa: E501

        :param patterns: The patterns of this ScanTemplateWebSpider.  # noqa: E501
        :type: ScanTemplateWebSpiderPatterns
        """

        self._patterns = patterns

    @property
    def performance(self):
        """Gets the performance of this ScanTemplateWebSpider.  # noqa: E501

        Performance settings used during web spidering.  # noqa: E501

        :return: The performance of this ScanTemplateWebSpider.  # noqa: E501
        :rtype: ScanTemplateWebSpiderPerformance
        """
        return self._performance

    @performance.setter
    def performance(self, performance):
        """Sets the performance of this ScanTemplateWebSpider.

        Performance settings used during web spidering.  # noqa: E501

        :param performance: The performance of this ScanTemplateWebSpider.  # noqa: E501
        :type: ScanTemplateWebSpiderPerformance
        """

        self._performance = performance

    @property
    def test_common_usernames_and_passwords(self):
        """Gets the test_common_usernames_and_passwords of this ScanTemplateWebSpider.  # noqa: E501

        Whether to determine if discovered logon forms accept commonly used user names or passwords. The process may cause authentication services with certain security policies to lock out accounts with these credentials.  # noqa: E501

        :return: The test_common_usernames_and_passwords of this ScanTemplateWebSpider.  # noqa: E501
        :rtype: bool
        """
        return self._test_common_usernames_and_passwords

    @test_common_usernames_and_passwords.setter
    def test_common_usernames_and_passwords(self, test_common_usernames_and_passwords):
        """Sets the test_common_usernames_and_passwords of this ScanTemplateWebSpider.

        Whether to determine if discovered logon forms accept commonly used user names or passwords. The process may cause authentication services with certain security policies to lock out accounts with these credentials.  # noqa: E501

        :param test_common_usernames_and_passwords: The test_common_usernames_and_passwords of this ScanTemplateWebSpider.  # noqa: E501
        :type: bool
        """

        self._test_common_usernames_and_passwords = test_common_usernames_and_passwords

    @property
    def test_xss_in_single_scan(self):
        """Gets the test_xss_in_single_scan of this ScanTemplateWebSpider.  # noqa: E501

        Whether to test for persistent cross-site scripting during a single scan. This test helps to reduce the risk of dangerous attacks via malicious code stored on Web servers. Enabling it may increase Web spider scan times.  # noqa: E501

        :return: The test_xss_in_single_scan of this ScanTemplateWebSpider.  # noqa: E501
        :rtype: bool
        """
        return self._test_xss_in_single_scan

    @test_xss_in_single_scan.setter
    def test_xss_in_single_scan(self, test_xss_in_single_scan):
        """Sets the test_xss_in_single_scan of this ScanTemplateWebSpider.

        Whether to test for persistent cross-site scripting during a single scan. This test helps to reduce the risk of dangerous attacks via malicious code stored on Web servers. Enabling it may increase Web spider scan times.  # noqa: E501

        :param test_xss_in_single_scan: The test_xss_in_single_scan of this ScanTemplateWebSpider.  # noqa: E501
        :type: bool
        """

        self._test_xss_in_single_scan = test_xss_in_single_scan

    @property
    def user_agent(self):
        """Gets the user_agent of this ScanTemplateWebSpider.  # noqa: E501

        The `User-Agent` to use when web spidering. Defaults to `\"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)\"`.  # noqa: E501

        :return: The user_agent of this ScanTemplateWebSpider.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this ScanTemplateWebSpider.

        The `User-Agent` to use when web spidering. Defaults to `\"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)\"`.  # noqa: E501

        :param user_agent: The user_agent of this ScanTemplateWebSpider.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

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
        if issubclass(ScanTemplateWebSpider, dict):
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
        if not isinstance(other, ScanTemplateWebSpider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
