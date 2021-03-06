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

from rapid7vmconsole.models.database_connection_settings import DatabaseConnectionSettings  # noqa: F401,E501


class DatabaseSettings(object):
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
        'connection': 'DatabaseConnectionSettings',
        'host': 'str',
        'maintenance_thread_pool_size': 'int',
        'port': 'int',
        'url': 'str',
        'user': 'str',
        'vendor': 'str'
    }

    attribute_map = {
        'connection': 'connection',
        'host': 'host',
        'maintenance_thread_pool_size': 'maintenanceThreadPoolSize',
        'port': 'port',
        'url': 'url',
        'user': 'user',
        'vendor': 'vendor'
    }

    def __init__(self, connection=None, host=None, maintenance_thread_pool_size=None, port=None, url=None, user=None, vendor=None):  # noqa: E501
        """DatabaseSettings - a model defined in Swagger"""  # noqa: E501

        self._connection = None
        self._host = None
        self._maintenance_thread_pool_size = None
        self._port = None
        self._url = None
        self._user = None
        self._vendor = None
        self.discriminator = None

        if connection is not None:
            self.connection = connection
        if host is not None:
            self.host = host
        if maintenance_thread_pool_size is not None:
            self.maintenance_thread_pool_size = maintenance_thread_pool_size
        if port is not None:
            self.port = port
        if url is not None:
            self.url = url
        if user is not None:
            self.user = user
        if vendor is not None:
            self.vendor = vendor

    @property
    def connection(self):
        """Gets the connection of this DatabaseSettings.  # noqa: E501

        Details connection settings for the database.  # noqa: E501

        :return: The connection of this DatabaseSettings.  # noqa: E501
        :rtype: DatabaseConnectionSettings
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this DatabaseSettings.

        Details connection settings for the database.  # noqa: E501

        :param connection: The connection of this DatabaseSettings.  # noqa: E501
        :type: DatabaseConnectionSettings
        """

        self._connection = connection

    @property
    def host(self):
        """Gets the host of this DatabaseSettings.  # noqa: E501

        The database host.  # noqa: E501

        :return: The host of this DatabaseSettings.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this DatabaseSettings.

        The database host.  # noqa: E501

        :param host: The host of this DatabaseSettings.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def maintenance_thread_pool_size(self):
        """Gets the maintenance_thread_pool_size of this DatabaseSettings.  # noqa: E501

        The maximum number of parallel tasks when executing maintenance tasks.  # noqa: E501

        :return: The maintenance_thread_pool_size of this DatabaseSettings.  # noqa: E501
        :rtype: int
        """
        return self._maintenance_thread_pool_size

    @maintenance_thread_pool_size.setter
    def maintenance_thread_pool_size(self, maintenance_thread_pool_size):
        """Sets the maintenance_thread_pool_size of this DatabaseSettings.

        The maximum number of parallel tasks when executing maintenance tasks.  # noqa: E501

        :param maintenance_thread_pool_size: The maintenance_thread_pool_size of this DatabaseSettings.  # noqa: E501
        :type: int
        """

        self._maintenance_thread_pool_size = maintenance_thread_pool_size

    @property
    def port(self):
        """Gets the port of this DatabaseSettings.  # noqa: E501

        The database port.  # noqa: E501

        :return: The port of this DatabaseSettings.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DatabaseSettings.

        The database port.  # noqa: E501

        :param port: The port of this DatabaseSettings.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def url(self):
        """Gets the url of this DatabaseSettings.  # noqa: E501

        The database connection URL.  # noqa: E501

        :return: The url of this DatabaseSettings.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DatabaseSettings.

        The database connection URL.  # noqa: E501

        :param url: The url of this DatabaseSettings.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def user(self):
        """Gets the user of this DatabaseSettings.  # noqa: E501

        The database user.  # noqa: E501

        :return: The user of this DatabaseSettings.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DatabaseSettings.

        The database user.  # noqa: E501

        :param user: The user of this DatabaseSettings.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def vendor(self):
        """Gets the vendor of this DatabaseSettings.  # noqa: E501

        The database vendor.  # noqa: E501

        :return: The vendor of this DatabaseSettings.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this DatabaseSettings.

        The database vendor.  # noqa: E501

        :param vendor: The vendor of this DatabaseSettings.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

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
        if issubclass(DatabaseSettings, dict):
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
        if not isinstance(other, DatabaseSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
