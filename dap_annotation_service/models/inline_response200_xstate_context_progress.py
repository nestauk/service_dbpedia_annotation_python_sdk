# coding: utf-8

"""
    Nesta Annotation Service

    DBpedia Spotlight Annotation service for large datasets.  Please refer to the <a href=\"https://github.com/nestauk/dap_dv_backends/tree/dev/src/services/annotation\" target=\"_blank\">docs</a> for a complete guide on how to use the service.  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse200XstateContextProgress(object):
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
        'total': 'float',
        'email': 'str',
        'id': 'str',
        'current': 'float',
        'start_time': 'float',
        'end_time': 'float',
        'index': 'str',
        'domain': 'str',
        'bucket': 'str',
        'key': 'str'
    }

    attribute_map = {
        'total': 'total',
        'email': 'email',
        'id': 'id',
        'current': 'current',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'index': 'index',
        'domain': 'domain',
        'bucket': 'bucket',
        'key': 'key'
    }

    def __init__(self, total=None, email=None, id=None, current=None, start_time=None, end_time=None, index=None, domain=None, bucket=None, key=None):  # noqa: E501
        """InlineResponse200XstateContextProgress - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._email = None
        self._id = None
        self._current = None
        self._start_time = None
        self._end_time = None
        self._index = None
        self._domain = None
        self._bucket = None
        self._key = None
        self.discriminator = None
        if total is not None:
            self.total = total
        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if current is not None:
            self.current = current
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if index is not None:
            self.index = index
        if domain is not None:
            self.domain = domain
        if bucket is not None:
            self.bucket = bucket
        if key is not None:
            self.key = key

    @property
    def total(self):
        """Gets the total of this InlineResponse200XstateContextProgress.  # noqa: E501


        :return: The total of this InlineResponse200XstateContextProgress.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InlineResponse200XstateContextProgress.


        :param total: The total of this InlineResponse200XstateContextProgress.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def email(self):
        """Gets the email of this InlineResponse200XstateContextProgress.  # noqa: E501


        :return: The email of this InlineResponse200XstateContextProgress.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InlineResponse200XstateContextProgress.


        :param email: The email of this InlineResponse200XstateContextProgress.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this InlineResponse200XstateContextProgress.  # noqa: E501


        :return: The id of this InlineResponse200XstateContextProgress.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse200XstateContextProgress.


        :param id: The id of this InlineResponse200XstateContextProgress.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def current(self):
        """Gets the current of this InlineResponse200XstateContextProgress.  # noqa: E501


        :return: The current of this InlineResponse200XstateContextProgress.  # noqa: E501
        :rtype: float
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this InlineResponse200XstateContextProgress.


        :param current: The current of this InlineResponse200XstateContextProgress.  # noqa: E501
        :type: float
        """

        self._current = current

    @property
    def start_time(self):
        """Gets the start_time of this InlineResponse200XstateContextProgress.  # noqa: E501


        :return: The start_time of this InlineResponse200XstateContextProgress.  # noqa: E501
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InlineResponse200XstateContextProgress.


        :param start_time: The start_time of this InlineResponse200XstateContextProgress.  # noqa: E501
        :type: float
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this InlineResponse200XstateContextProgress.  # noqa: E501


        :return: The end_time of this InlineResponse200XstateContextProgress.  # noqa: E501
        :rtype: float
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this InlineResponse200XstateContextProgress.


        :param end_time: The end_time of this InlineResponse200XstateContextProgress.  # noqa: E501
        :type: float
        """

        self._end_time = end_time

    @property
    def index(self):
        """Gets the index of this InlineResponse200XstateContextProgress.  # noqa: E501


        :return: The index of this InlineResponse200XstateContextProgress.  # noqa: E501
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this InlineResponse200XstateContextProgress.


        :param index: The index of this InlineResponse200XstateContextProgress.  # noqa: E501
        :type: str
        """

        self._index = index

    @property
    def domain(self):
        """Gets the domain of this InlineResponse200XstateContextProgress.  # noqa: E501


        :return: The domain of this InlineResponse200XstateContextProgress.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this InlineResponse200XstateContextProgress.


        :param domain: The domain of this InlineResponse200XstateContextProgress.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def bucket(self):
        """Gets the bucket of this InlineResponse200XstateContextProgress.  # noqa: E501


        :return: The bucket of this InlineResponse200XstateContextProgress.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this InlineResponse200XstateContextProgress.


        :param bucket: The bucket of this InlineResponse200XstateContextProgress.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def key(self):
        """Gets the key of this InlineResponse200XstateContextProgress.  # noqa: E501


        :return: The key of this InlineResponse200XstateContextProgress.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this InlineResponse200XstateContextProgress.


        :param key: The key of this InlineResponse200XstateContextProgress.  # noqa: E501
        :type: str
        """

        self._key = key

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
        if issubclass(InlineResponse200XstateContextProgress, dict):
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
        if not isinstance(other, InlineResponse200XstateContextProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
