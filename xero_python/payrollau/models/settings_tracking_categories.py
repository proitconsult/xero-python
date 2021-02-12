# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class SettingsTrackingCategories(BaseModel):
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
    openapi_types = {
        "employee_groups": "SettingsTrackingCategoriesEmployeeGroups",
        "timesheet_categories": "SettingsTrackingCategoriesTimesheetCategories",
    }

    attribute_map = {
        "employee_groups": "EmployeeGroups",
        "timesheet_categories": "TimesheetCategories",
    }

    def __init__(self, employee_groups=None, timesheet_categories=None):  # noqa: E501
        """SettingsTrackingCategories - a model defined in OpenAPI"""  # noqa: E501

        self._employee_groups = None
        self._timesheet_categories = None
        self.discriminator = None

        if employee_groups is not None:
            self.employee_groups = employee_groups
        if timesheet_categories is not None:
            self.timesheet_categories = timesheet_categories

    @property
    def employee_groups(self):
        """Gets the employee_groups of this SettingsTrackingCategories.  # noqa: E501


        :return: The employee_groups of this SettingsTrackingCategories.  # noqa: E501
        :rtype: SettingsTrackingCategoriesEmployeeGroups
        """
        return self._employee_groups

    @employee_groups.setter
    def employee_groups(self, employee_groups):
        """Sets the employee_groups of this SettingsTrackingCategories.


        :param employee_groups: The employee_groups of this SettingsTrackingCategories.  # noqa: E501
        :type: SettingsTrackingCategoriesEmployeeGroups
        """

        self._employee_groups = employee_groups

    @property
    def timesheet_categories(self):
        """Gets the timesheet_categories of this SettingsTrackingCategories.  # noqa: E501


        :return: The timesheet_categories of this SettingsTrackingCategories.  # noqa: E501
        :rtype: SettingsTrackingCategoriesTimesheetCategories
        """
        return self._timesheet_categories

    @timesheet_categories.setter
    def timesheet_categories(self, timesheet_categories):
        """Sets the timesheet_categories of this SettingsTrackingCategories.


        :param timesheet_categories: The timesheet_categories of this SettingsTrackingCategories.  # noqa: E501
        :type: SettingsTrackingCategoriesTimesheetCategories
        """

        self._timesheet_categories = timesheet_categories
