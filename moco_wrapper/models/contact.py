import datetime

from moco_wrapper.models.base import MWRAPBase
from moco_wrapper.const import API_PATH

from enum import Enum

class ContactGender(str, Enum):
    MALE = "M"
    FEMALE = "F"
    UNDEFINED = "U"

class Contact(MWRAPBase):
    """
    Class for handling contacts
    
    """

    def __init__(self, moco):
        """
        Class Constructor

        :param moco: An instance of :class:`moco_wrapper.Moco`
        """
        self._moco = moco

    def create(
        self,
        firstname: str,
        lastname: str,
        gender: ContactGender,
        company_id: int = None,
        title: str = None,
        job_position: str = None,
        mobile_phone: str = None,
        work_fax: str = None,
        work_phone: str = None,
        work_email: str = None,
        work_address: str = None,
        home_address: str = None,
        home_email: str = None,
        birthday: datetime.date = None,
        info: str = None,
        tags: list = None):
        """
        Creates a contact.

        :param firstname: The first name of the contact
        :param lastname: The last name of the contact
        :param gender: gender of the contact. For allowed values see :class:`.ContactGender`.
        :param company_id: Id of the company the contact belongs to
        :param title: Job title the contact has
        :param job_position: Name of the job position this contact has
        :param mobile_phone: Mobile phone number the contact has
        :param work_fax: Work fax number
        :param work_phone: Work phone number
        :param work_email: Work email address
        :param work_address: Physical work address
        :param home_address: Physical home address
        :param home_email: Home email address
        :param birthday: Birthday date
        :param info: More information about the contact
        :param tags: Array of additional tags
        :returns: The created contact object
        """

        data = {
            "firstname" : firstname,
            "lastname" : lastname,
            "gender" : gender
        }

        for key, value in (
            ("customer_id", company_id),
            ("title", title),
            ("job_position", job_position),
            ("mobile_phone", mobile_phone),
            ("work_fax", work_fax),
            ("work_phone", work_phone),
            ("work_email", work_email),
            ("work_address", work_address),
            ("home_address", home_address),
            ("home_email", home_email),
            ("birthday", birthday),
            ("info", info),
            ("tags", tags)
        ):
            if value is not None:
                if isinstance(value, datetime.date):
                    data[key] = value.isoformat()
                else:
                    data[key] = value

        return self._moco.post(API_PATH['contact_create'], data=data);

    def update(
        self,
        id: int,
        firstname: str = None,
        lastname: str = None,
        gender: ContactGender = None,
        company_id: int = None,
        title: str = None,
        job_position: str = None,
        mobile_phone: str = None,
        work_fax: str = None,
        work_phone: str = None,
        work_email: str = None,
        work_address: str = None,
        home_address: str = None,
        home_email: str = None,
        birthday: datetime.date = None,
        info: str = None,
        tags: list = None
        ):
        """updates a contact.

        :param id: id of the contact
        :param firstname: The first name of the contact
        :param lastname: The last name of the contact
        :param gender: either F, M, U
        :param company_id: Id of the company the contact belongs to
        :param title: Title the contact has
        :param job_position: name of the job position this contact has
        :param mobile_phone: Mobile phone number the contact has
        :param work_fax: Fax number for work purposes
        :param work_phone: Phone number for work purposes
        :param work_email: Work email address
        :param work_address: Work address
        :param home_address: Home address
        :param home_email: home email address
        :param birthday: Birthday (format YYYY-MM-DD)
        :param info: More information about the contact
        :param tags: Array of additional tags
        :returns: the created contact object
        """


        data = {}
        for key, value in (
            ("firstname", firstname),
            ("lastname", lastname),
            ("gender", gender),
            ("customer_id", company_id),
            ("title", title),
            ("job_position", job_position),
            ("mobile_phone", mobile_phone),
            ("work_fax", work_fax),
            ("work_phone", work_phone),
            ("work_email", work_email),
            ("work_address", work_address),
            ("home_address", home_address),
            ("home_email", home_email),
            ("birthday", birthday),
            ("info", info),
            ("tags", tags)
            ):

            if value is not None:
                if key == "birthday" and isinstance(value, datetime.date):
                    data[key] = value.isoformat()
                else:
                    data[key] = value

        return self._moco.put(API_PATH["contact_update"].format(id=id), data=data)

    def get(
        self,
        id: int
        ):
        """retrieve a single contact object

        :param id: id of the contact
        :returns: the contact object
        """
        return self._moco.get(API_PATH["contact_get"].format(id=id))

    def getlist(
        self,
        tags: list = None,
        sort_by: str = None,
        sort_order: str = 'asc',
        page: int = 1
        ):
        """retrieve a list of contact objects

        :param tags: array of tags
        :param sort_by: field to the results by
        :param sort_order: asc or desc
        :param page: page number (default 1)
        :returns: list of contact objects
        """
        params = {}
        for key, value in (
            ("tags", tags),
            ("page", page)
        ):
            if value is not None:
                params[key] = value

        if sort_by is not None:
            params["sort_by"] = "{} {}".format(sort_by, sort_order)

        return self._moco.get(API_PATH["contact_getlist"], params=params)

