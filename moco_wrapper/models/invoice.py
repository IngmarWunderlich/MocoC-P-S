import datetime

from moco_wrapper.models.base import MWRAPBase
from moco_wrapper.const import API_PATH

from enum import Enum

class InvoiceStatus(str, Enum):
    """
    Enumeration for allowed values that can be supplied for the ``status`` argument of :meth:`Invoice.getlist`, :meth:`Invoice.update_status` and :meth:`Invoice.create`.

    Example usage:

    .. code-block:: python

        from moco_wrapper.models.invoice import InvoiceStatus
        from moco_wrapper import Moco

        m = Moco()
        new_invoice = m.Invoice.create(
            ..
            status = InvoiceStatus.DRAFT
        )
    """
    DRAFT = "draft"
    CREATED = "created"
    SENT = "sent"
    PARTIALLY_PAID = "partially_paid"
    PAID = "paid"
    OVERDUE = "overdue"
    IGNORED = "ignored"
    """
    .. warning:: 
        Do not use this status for creating invoices, only updating and filtering
    """

class InvoiceChangeAddress(str, Enum):
    """
    Enumeration for allowed values that can be supplied for ``change_address`` argument of :meth:`Invoice.create`.

    .. code-block:: python

        from moco_wrapper.models.invoice import InvoiceChangeAddress
        from moco_wrapper import Moco

        m = Moco()
        new_invoice = m.Invoice.create(
            ..
            change_address = InvoiceChangeAddress.PROJECT
            )
            
    """
    INVOICE = "invoice"
    PROJECT = "project"
    CUSTOMER = "customer"

class Invoice(MWRAPBase):
    """
    Models for handling invoices.
    """

    def __init__(self, moco):
        """
        Class Constructor

        :param moco: An instance of :class:`moco_wrapper.Moco`
        """
        self._moco = moco

    def getlist(
        self,
        status: InvoiceStatus = None,
        date_from: datetime.date = None,
        date_to: datetime.date = None,
        tags: list = None,
        identifier: str = None,
        term: str = None,
        sort_by: str = None,
        sort_order: str = 'asc',
        page: int = 1
        ):
        """
        Retrieve a list of invoices.

        :param status: State of the invoice. For allowed values see :class:`.InvoiceStatus`
        :param date_from: Starting date
        :param date_to: End date
        :param tags: List of tags
        :param identifier: Identifier string (e.g. R1903-003)
        :param term: Wildcard search term
        :param sort_by: Field to sort results by
        :param sort_order: asc or desc (default asc)
        :param page: Page number (default 1)
        :returns: List of invoice objects
        """
        params = {}
        for key, value in (
            ("status", status),
            ("date_from", date_from),
            ("date_to", date_to),
            ("tags", tags),
            ("identifier", identifier),
            ("term", term),
            ("page", page),
        ):
            
            if value is not None:
                if key in ["date_from", "date_to"] and isinstance(value, datetime.date):
                    params[key] = self.convert_date_to_iso(value)
                elif key in ["tags"] and isinstance(value, list):
                    params[key] = ",".join(value)
                else:
                    params[key] = value

        if sort_by is not None:
            params["sort_by"] = "{} {}".format(sort_by, sort_order)

        return self._moco.get(API_PATH["invoice_getlist"], params=params)
 
    def locked(
        self,
        status: InvoiceStatus = None,
        date_from: datetime.date = None,
        date_to: datetime.date = None,
        identifier: str = None,
        sort_by: str = None,
        sort_order: str = 'asc',
        page: int = 1
        ):        
        """
        Retrieve a list of locked invoices.

        :param status: State of the invoice. For allowed values see :class:`.InvoiceStatus`. 
        :param date_from: Start date
        :param date_to: End date
        :param identifier: Identifier string (ex. R1903-003)
        :param sort_by: Field to sort results by
        :param sort_order: asc or desc (default asc)
        :param page: Page number (default 1)
        :returns: List of invoice objects
        """
        params = {}
        for key, value in (
            ("status", status),
            ("date_from", date_from),
            ("date_to", date_to),
            ("identifier", identifier),
            ("page", page)
        ):          
            if value is not None:
                if key in ["date_from", "date_to"] and isinstance(value, datetime.date):
                    params[key] = self.convert_date_to_iso(value)
                else:
                    params[key] = value

        if sort_by is not None:
            params["sort_by"] = "{} {}".format(sort_by, sort_order)

        return self._moco.get(API_PATH["invoice_locked"], params=params)


    def get(
        self,
        id: int
        ):
        """
        Retrieve a single invoice.

        :param id: Invoice id
        :returns: Single invoice object
        """
        return self._moco.get(API_PATH["invoice_get"].format(id=id))

    def pdf(
        self,
        id: int
        ):
        """
        Retrieve the invoice document as pdf. 

        :param id: Invoice id
        :returns: Invoice pdf
        """
        return self._moco.get(API_PATH["invoice_pdf"].format(id=id))

    def timesheet(
        self,
        id: int
        ):
        """
        Retrieve the invoice timesheet document as pdf.

        Invoices that have timesheets cannot be created with the api and must be created manully by billing unbilled tasks.

        :param id: Invoice id
        :return: Invoice timesheet as pdf
        """
        return self._moco.get(API_PATH["invoice_timesheet"].format(id=id))

    def update_status(
        self,
        id: int,
        status: InvoiceStatus
        ):
        """
        Updates the state of an invoices.

        :param id: Invoice id
        :param status: New state of the invoice. For allowed values see :class:`.InvoiceStatus`.
        :return: Empty response on success
        """
        data = {
            "status": status
        }

        return self._moco.put(API_PATH["invoice_update_status"].format(id=id), data=data)

    def create(
        self,
        customer_id: int,
        recipient_address: str,
        created_date: datetime.date,
        due_date: datetime.date,
        service_period_from: datetime.date,
        service_period_to: datetime.date,
        title: str,
        tax: float,
        currency: str,
        items: list,
        status: InvoiceStatus = InvoiceStatus.CREATED,
        change_address: InvoiceChangeAddress = InvoiceChangeAddress.INVOICE,
        salutation: str = None,
        footer: str= None,
        discount: float = None,
        cash_discount: float = None,
        cash_discount_days: int = None,
        project_id: int = None
        ):
        """
        Creates a new invoice.

        :param customer_id: Id of the customer/company
        :param recipient_address: Entry text for the customer (e.g. "My Customer\\nMainStreet 5\\nExample Town")
        :param created_date: Creation date of the invoice
        :param due_date: Date the invoice is due
        :param service_period_from: Service period start date
        :param service_period_to: Service period end date
        :param title: Title of the invoice
        :param tax: Tax percent (between 0.0 and 100.0)
        :param currency: Currency code (e.g. EUR)
        :param items: Invoice items
        :param status: State of the invoice. For allowed values see :class:`.InvoiceStatus`, default: "created".
        :param change_address: Address propagation. For allowed values see :class:`.InvoiceChangeAddress`, default: "invoice".
        :param salutation: Salutation text
        :param footer: Footer text
        :param discount: Discount in percent (between 0.0 and 100.0)
        :param cash_discount: Cash discount in percent (between 0.0 and 100.0)
        :param cash_discount_days: How many days is the cash discount valid (ex. 4)
        :param project_id: Id of the project the invoice belongs to

        .. note::
            Note that if you create an invoice with a project, that project must also belong to the customer the invoice was created for.

        :returns: the created invoice
        

        """
        data = {
            "customer_id" : customer_id,
            "recipient_address": recipient_address,
            "date": created_date,
            "due_date": due_date,
            "service_period_from": service_period_from,
            "service_period_to": service_period_to,
            "title": title,
            "tax": tax,
            "currency": currency,
            "items": items,
        }

        #overwrite all date fields in data with isoformat
        for date_key in ["date", "due_date", "service_period_from", "service_period_to"]:
            if isinstance(data[date_key], datetime.date):
                data[date_key] = self.convert_date_to_iso(data[date_key])

        for key, value in (
            ("status", status),
            ("change_address", change_address),
            ("salutation", salutation),
            ("footer", footer),
            ("discount", discount),
            ("cash_discount", cash_discount),
            ("cash_discount_days", cash_discount_days),
            ("project_id", project_id)
        ):
            if value is not None:
                data[key] = value

        return self._moco.post(API_PATH["invoice_create"], data=data)





    

