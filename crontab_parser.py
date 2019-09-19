"""
A crontab command is made up of 5 fields in a space separated string:

minute: 0-59
hour: 0-23
day of month: 1-31
month: 1-12
day of week: 0-6 (0 == Sunday)
Each field can be a combination of the following values:

a wildcard * which equates to all valid values.
a range 1-10 which equates to all valid values between start-end inclusive.
a step */2 which equates to every second value starting at 0, or 1 for day of month and month.
a single value 2 which would be 2.
a combination of the above separated by a ,
Note: In the case of multiple values in a single field, the resulting values should be sorted.

Note: Steps and ranges can also be combined 1-10/2 would be every second value in the 1-10 range 1 3 5 7 9.

For an added challenge day of week and month will both support shortened iso formats:

SUN MON TUE ...
JAN FEB MAR ...
Examples
* should output every valid value 0 1 2 3 4 5 6 ...

1 should output the value 1.

1,20,31 should output the values 1 20 31.

1-10 should output the values 1 2 3 4 5 6 7 8 9 10.

*/2 should output every second value 0 2 4 6 8 10 ....

*/2 should output 1 3 5 7 9 ... in the cases, day of month and month.

1-10/2 should output 1 3 5 7 9.

*/15,3-5 should output the values 0 3 4 5 15 30 45 when applied to the minute field.

Output
The purpose of this kata is to take in a crontab command, and render it in a nice human readable format.

The output format should be in the format field_name values. The field name should be left justified and padded to 15 characters. The values should be a space separated string of the returned values.

For example the crontab */15 0 1,15 * 1-5 would have the following output:

minute          0 15 30 45
hour            0
day of month    1 15
month           1 2 3 4 5 6 7 8 9 10 11 12
day of week     1 2 3 4 5
All test cases will receive a valid crontab, there is no need to handle an incorrect number of values.

Super handy resource for playing with different values to find their outputs: https://crontab.guru/
"""

import re

D = {
'minute': {"start": 0, "end": 59},
'hour': {"start": 0, "end": 23},
'day of month': {"start": 1, "end": 31},
'month': {"start": 1, "end": 12},
'day of week': {"start": 0, "end": 6} }

M = {
"JAN": 1,
"FEB": 2,
"MAR": 3,
"APR": 4,
"MAY": 5,
"JUN": 6,
"JUL": 7,
"AUG": 8,
"SEP": 9,
"OCT": 10,
"NOV": 11,
"DEC": 12 
}

d = {
"SUN": 0,
"MON": 1,
"TUE": 2,
"WED": 3,
"THU": 4,
"FRI": 5,
"SAT": 6 
}

class Solution:
    def range_parse(self, ran, st):
        # change something like 2-6 => 2, 3, 4, 5, 6. return type is string
        self.ans = ""
        R = [int(i) for i in ran.split('-')]
        for i in range(R[0], R[1]+1, int(st)):
            self.ans += str(i) + ' '
        return self.ans.strip(' ')

    def ast_slash_parse(self, s, type):
        # change something like */2 for month to 1 3 5 7 9 11
        self.ans = ""
        st = int(s.split('/')[1])
        for i in range(D[type]['start'], D[type]['end']+1, st):
            self.ans += str(i) + ' '
        return self.ans.strip(' ')
    
    def comma_parse(self, value):
        # in this you only split things by a comma:
        # return type is string
        return " ".join(value.split(','))


    def parse(self, crontab):
        T = {
            0: 'minute',
            1: 'hour',
            2: 'day of month',
            3: 'month',
            4: 'day of week'
        }

        info = crontab.split()
        
        for i, entry in enumerate(info):
            # if entry value is a "*"
            if entry == "*":
                entry = ' '.join(map(str, range(D[T[i]]['start'], D[T[i]]['end'] + 1)))


            # replace the month being in charachter (JAN-DEC/2) to 1-12/2:
            if re.search(r'([A-Z]{3}-[A-Z]{3})(/\d+){0,1}', entry) and i in [3, 4]:
                # replace the months
                S = re.search(r'([A-Z]{3})-([A-Z]{3})', entry)
                if i == 3: # replace for months
                    repl = "%s-%s" % (str(M[S.group(1)]), str(M[S.group(2)]))
                elif i == 4: # replace for days
                    repl = "%s-%s" % (str(d[S.group(1)]), str(d[S.group(2)]))
                entry = re.sub("%s" % S.group(0), repl, entry)


            # if entry value contains ","
            while re.search(r',', entry):
                entry = Solution.comma_parse(self, entry)


            # if entry value contains pattern of "*/num"
            while re.search(r'\*/(\d+)', entry):
                S = re.search(r'\*/(\d+)', entry)
                repl = Solution.ast_slash_parse(self, S.group(0), T[i])
                entry = re.sub(r"\%s" % S.group(0), repl, entry)
            

            # if entry has pattern of range 5-10
            while re.search(r'(\d+-\d+)(/\d+){0,1}', entry):
                S = re.search(r'(\d+-\d+)(/\d+){0,1}', entry)
                ran = S.group(1)
                if not S.group(2):
                    st = 1
                else:
                    st = int(S.group(2).lstrip('/'))
                repl = Solution.range_parse(self, ran, st)
                entry = re.sub("%s" % S.group(0), repl, entry)


            # sort the entry output
            E = map(int, entry.split(' '))
            E.sort()
            entry = " ".join(map(str, E))
            ind = "%s" % T[i] + ' ' * (15 - len(T[i]))
            print("%s%s" % (ind, entry))


S = Solution()
S.parse('*/15 0 1,15 JAN-DEC/2 *')