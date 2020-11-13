from ..core import OrthodoxCalendar, MON
from ..registry_tools import iso_register


@iso_register('RU')
class Russia(OrthodoxCalendar):
    'Russia'
    shift_new_years_day = True

    # Civil holidays
    include_labour_day = True

    FIXED_HOLIDAYS = OrthodoxCalendar.FIXED_HOLIDAYS + (
        (1, 2, "Day After New Year"),
        (1, 7, "Christmas"),
        (2, 23, "Defendence of the Fatherland"),
        (3, 8, "International Women's Day"),
        (5, 9, "Victory Day"),
        (6, 12, "National Day"),
        (11, 4, "Day of Unity"),
    )

    def get_calendar_holidays(self, year):
        holidays = super().get_calendar_holidays(year)
        shifts = []
        for day, label in holidays:
            if day.weekday() in self.get_weekend_days():
                shifts.append((
                    self.get_first_weekday_after(day, MON),
                    label + " shift"
                ))
        holidays.extend(shifts)
        return holidays
