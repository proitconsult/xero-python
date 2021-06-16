# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BudgetLines(BaseModel):
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
        "period": "date[ms-format]",
        "amount": "int",
        "unit_amount": "int",
        "notes": "str",
    }

    attribute_map = {
        "period": "Period",
        "amount": "Amount",
        "unit_amount": "UnitAmount",
        "notes": "Notes",
    }

    def __init__(
        self, period=None, amount=None, unit_amount=None, notes=None
    ):  # noqa: E501
        """BudgetLines - a model defined in OpenAPI"""  # noqa: E501

        self._period = None
        self._amount = None
        self._unit_amount = None
        self._notes = None
        self.discriminator = None

        if period is not None:
            self.period = period
        if amount is not None:
            self.amount = amount
        if unit_amount is not None:
            self.unit_amount = unit_amount
        if notes is not None:
            self.notes = notes

    @property
    def period(self):
        """Gets the period of this BudgetLines.  # noqa: E501

        Period the amount applies to (e.g. “2019-08”)  # noqa: E501

        :return: The period of this BudgetLines.  # noqa: E501
        :rtype: date
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this BudgetLines.

        Period the amount applies to (e.g. “2019-08”)  # noqa: E501

        :param period: The period of this BudgetLines.  # noqa: E501
        :type: date
        """

        self._period = period

    @property
    def amount(self):
        """Gets the amount of this BudgetLines.  # noqa: E501

        LineItem Quantity  # noqa: E501

        :return: The amount of this BudgetLines.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BudgetLines.

        LineItem Quantity  # noqa: E501

        :param amount: The amount of this BudgetLines.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def unit_amount(self):
        """Gets the unit_amount of this BudgetLines.  # noqa: E501

        Budgeted amount  # noqa: E501

        :return: The unit_amount of this BudgetLines.  # noqa: E501
        :rtype: int
        """
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, unit_amount):
        """Sets the unit_amount of this BudgetLines.

        Budgeted amount  # noqa: E501

        :param unit_amount: The unit_amount of this BudgetLines.  # noqa: E501
        :type: int
        """

        self._unit_amount = unit_amount

    @property
    def notes(self):
        """Gets the notes of this BudgetLines.  # noqa: E501

        Any footnotes associated with this balance  # noqa: E501

        :return: The notes of this BudgetLines.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this BudgetLines.

        Any footnotes associated with this balance  # noqa: E501

        :param notes: The notes of this BudgetLines.  # noqa: E501
        :type: str
        """
        if notes is not None and len(notes) > 255:
            raise ValueError(
                "Invalid value for `notes`, "
                "length must be less than or equal to `255`"
            )  # noqa: E501

        self._notes = notes
