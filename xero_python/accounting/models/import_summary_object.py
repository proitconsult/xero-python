# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ImportSummaryObject(BaseModel):
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
    openapi_types = {"import_summary": "ImportSummary"}

    attribute_map = {"import_summary": "ImportSummary"}

    def __init__(self, import_summary=None):  # noqa: E501
        """ImportSummaryObject - a model defined in OpenAPI"""  # noqa: E501

        self._import_summary = None
        self.discriminator = None

        if import_summary is not None:
            self.import_summary = import_summary

    @property
    def import_summary(self):
        """Gets the import_summary of this ImportSummaryObject.  # noqa: E501


        :return: The import_summary of this ImportSummaryObject.  # noqa: E501
        :rtype: ImportSummary
        """
        return self._import_summary

    @import_summary.setter
    def import_summary(self, import_summary):
        """Sets the import_summary of this ImportSummaryObject.


        :param import_summary: The import_summary of this ImportSummaryObject.  # noqa: E501
        :type: ImportSummary
        """

        self._import_summary = import_summary