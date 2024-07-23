class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        days = {
            "1st": "01",
            "2nd": "02",
            "3rd": "03",
            "4th": "04",
            "5th": "05",
            "6th": "06",
            "7th": "07",
            "8th": "08",
            "9th": "09",
            "10th": "10",
            "11st": "11",
            "11th": "11",
            "12nd": "12",
            "12th": "12",
            "13rd": "13",
            "13th": "13",
            "14th": "14",
            "15th": "15",
            "16th": "16",
            "17th": "17",
            "18th": "18",
            "19th": "19",
            "20th": "20",
            "21st": "21",
            "21th": "21",
            "22nd": "22",
            "22th": "22",
            "23rd": "23",
            "23th": "23",
            "24th": "24",
            "25th": "25",
            "26th": "26",
            "27th": "27",
            "28th": "28",
            "29th": "29",
            "30th": "30",
            "31st": "31"
        }

        months = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }

        day, month, year = date.split()
        return year + "-" + months[month] + "-" + days[day]


date = "20th Oct 2052"
date = "6th Jun 1933"
date = "26th May 1960"

solution = Solution()
print(solution.reformatDate(date))
