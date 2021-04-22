class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        m_to_days = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        def leap_year(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        def days_since_ref(date):
            y, m, d = map(int, date.split('-'))
            days = (y - 1971) * 365 + m_to_days[m] + d
            for year in filter(leap_year, range(1971, y + 1)):
                if year < y: days += 1
                if year == y and m >= 3: days += 1
            return days

        return abs(days_since_ref(date1) - days_since_ref(date2))
