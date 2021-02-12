# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BrandingThemes(BaseModel):
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
    openapi_types = {"branding_themes": "list[BrandingTheme]"}

    attribute_map = {"branding_themes": "BrandingThemes"}

    def __init__(self, branding_themes=None):  # noqa: E501
        """BrandingThemes - a model defined in OpenAPI"""  # noqa: E501

        self._branding_themes = None
        self.discriminator = None

        if branding_themes is not None:
            self.branding_themes = branding_themes

    @property
    def branding_themes(self):
        """Gets the branding_themes of this BrandingThemes.  # noqa: E501


        :return: The branding_themes of this BrandingThemes.  # noqa: E501
        :rtype: list[BrandingTheme]
        """
        return self._branding_themes

    @branding_themes.setter
    def branding_themes(self, branding_themes):
        """Sets the branding_themes of this BrandingThemes.


        :param branding_themes: The branding_themes of this BrandingThemes.  # noqa: E501
        :type: list[BrandingTheme]
        """

        self._branding_themes = branding_themes
