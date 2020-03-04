import datetime

from moco_wrapper.models.base import MWRAPBase
from moco_wrapper.const import API_PATH

class ProjectPaymentSchedule(MWRAPBase):
    """
    Class for handling billing schedules for fixed price projects
    
    Fixed Price projects can have a target date they should be billed on (in the future). With this class you can create this target entry (and how much should be billed).

    For Example you can create a project that will be billed in four (4) steps over the year.

    .. code-block:: python

        from moco_wrapper import Moco
        from datetime import date

        m = Moco()
        leader_id = 1
        customer_id = 2

        #create fixed price projects
        project = m.Project.create(
            "my fixed price project",
            "EUR",
            leader_id,
            customer_id,
            fixed_price=True,
            budget=4000
        ).data

        first_payment = ProjectPaymentSchedule.create(project.id, 1000.0, date(2020, 3, 1))
        second_payment = ProjectPaymentSchedule.create(project.id, 1000.0, date(2020, 6, 1))
        third_payment = ProjectPaymentSchedule.create(project.id, 1000.0, date(2020, 9, 1))
        fourth_payment = ProjectPaymentSchedule.create(project.id, 1000.0, date(2020, 12, 1))

    .. seealso::

        :meth:`moco_wrapper.models.Project.create`
    """

    def __init__(self, moco):
        """
        Class Constructor

        :param moco: An instance of :class:`moco_wrapper.Moco`
        """
        self._moco = moco

    def create(
        self,
        project_id: int,
        net_total: float,
        schedule_date: datetime.date,
        title: str = None,
        checked: bool = False,
        ):
        """
        Creates a new project payment schedule.

        :oaran project_id: The id of the project the entry belongs to
        :param net_total: How much should be billed on this schedule
        :param schedule_date: Date of the entry
        :param title: Title string
        :param checked: Mark entry as checked
        :returns: The created schedule item
        """

        data = {
            "net_total": net_total,
            "date": schedule_date
        }

        for date_key in ["date"]:
            if isinstance(data[date_key], datetime.date):
                data[date_key] = self._convert_date_to_iso(data[date_key])

        for key, value in (
            ("title", title),
            ("checked", checked)
        ):
            if value is not None:
                data[key] = value

        return self._moco.post(API_PATH["project_payment_schedule_create"].format(project_id=project_id), data=data)

    def update(
        self,
        project_id: int,
        schedule_id: int,
        net_total: float = None,
        schedule_date: datetime.date = None,
        title: str = None,
        checked: bool = None
        ):
        """
        Updates an existing project payment schedule.

        :param project_id: Project id the schedule item belongs to
        :param schedule_id: Id of the schedule item to update
        :param net_total: Total amount to be billed
        :param schedule_date: Date the billing will take place
        :param title: Title of the item
        :param checked: Mark entry as checked
        :returns: The updated schedule item
        """
        data = {}

        for key, value in (
            ("net_total", net_total),
            ("date", schedule_date),
            ("title", title),
            ("checked", checked),
        ):
            if value is not None:
                if key in ["date"] and isinstance(value, datetime.date):
                    data[key] = self._convert_date_to_iso(value)
                else:
                    data[key] = value

        return self._moco.put(API_PATH["project_payment_schedule_update"].format(project_id=project_id, schedule_id=schedule_id), data=data)

    def get(
        self,
        project_id,
        schedule_id,
        ):
        """
        Retrieves project payment schedule.

        :param project_id: Id of the project to schedule item belongs to
        :param schedule_id: Id of the schedule to retrieve
        :returns: The schedule item
        """

        return self._moco.get(API_PATH["project_payment_schedule_get"].format(project_id=project_id, schedule_id=schedule_id))

    def getlist(
        self,
        project_id,
        sort_by: str = None,
        sort_order: str = 'asc',
        page: int = 1
        ):
        """
        Retrieve a list of project payment schedules

        :param project_id: Project id of the schedule items
        :param sort_by: Field to sort the results by
        :param sort_order: asc or desc
        :param page: Page number (default 1)
        """

        params = {}

        for key, value in (
            ("page", page),
        ):
            if value is not None:
                params[key] = value

        if sort_by is not None:
            params["sort_by"] = "{} {}".format(sort_by, sort_order)

        return self._moco.get(API_PATH["project_payment_schedule_getlist"].format(project_id=project_id), params=params)

    def delete(
        self,
        project_id,
        schedule_id
        ):
        """
        Delete a project payment schedule item

        :param project_id: Project the payment schedule belongs to
        :param schedule_id: Id of the schedule item to delete
        :returns: The deleted response on success
        """

        return self._moco.delete(API_PATH["project_payment_schedule_delete"].format(project_id=project_id, schedule_id=schedule_id))
    



    