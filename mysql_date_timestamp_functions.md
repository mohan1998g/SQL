# MySQL Date and Timestamp Functions Cheat Sheet

## TIMESTAMP Difference

### Difference in Hours
```sql
SELECT TIMESTAMPDIFF(HOUR,
                     '2026-08-27 10:00:00',
                     '2026-08-27 15:30:00');
-- 5
```

### Difference in Minutes
```sql
SELECT TIMESTAMPDIFF(MINUTE,
                     '2026-08-27 10:00:00',
                     '2026-08-27 15:30:00');
-- 330
```

### Difference in Seconds
```sql
SELECT TIMESTAMPDIFF(SECOND,
                     '2026-08-27 10:00:00',
                     '2026-08-27 15:30:00');
-- 19800
```

### Supported Units
```sql
MICROSECOND
SECOND
MINUTE
HOUR
DAY
WEEK
MONTH
QUARTER
YEAR
```

## Current Date and Time

```sql
CURDATE()
CURTIME()
NOW()
SYSDATE()
UTC_DATE()
UTC_TIME()
UTC_TIMESTAMP()
```

## Date Extraction Functions

```sql
YEAR(date)
MONTH(date)
MONTHNAME(date)
DAY(date)
DAYOFMONTH(date)
DAYOFWEEK(date)
DAYOFYEAR(date)
DAYNAME(date)
WEEK(date)
WEEKDAY(date)
QUARTER(date)
HOUR(datetime)
MINUTE(datetime)
SECOND(datetime)
MICROSECOND(datetime)
EXTRACT(part FROM date)
```

## Date Arithmetic

```sql
DATE_ADD(date, INTERVAL n DAY)
DATE_SUB(date, INTERVAL n DAY)
ADDDATE(date, INTERVAL n DAY)
SUBDATE(date, INTERVAL n DAY)
ADDTIME(datetime, time)
SUBTIME(datetime, time)
TIMESTAMPADD(unit, value, datetime)
```

## Difference Functions

```sql
DATEDIFF(date1, date2)
TIMEDIFF(time1, time2)
TIMESTAMPDIFF(unit, start_date, end_date)
```

## Formatting Functions

```sql
DATE_FORMAT(date, format)
TIME_FORMAT(time, format)
GET_FORMAT(DATE, 'USA')
```

Common Format Tokens:

```text
%Y Year (2026)
%y Year (26)
%m Month Number
%M Month Name
%d Day
%W Weekday Name
%H Hour
%i Minutes
%s Seconds
```

## Conversion Functions

```sql
DATE(datetime)
TIME(datetime)
STR_TO_DATE(string, format)
FROM_UNIXTIME(unix_ts)
UNIX_TIMESTAMP()
CONVERT_TZ(dt, from_tz, to_tz)
FROM_DAYS(days)
TO_DAYS(date)
TO_SECONDS(datetime)
```

## Month and Quarter Functions

```sql
LAST_DAY(date)
QUARTER(date)
PERIOD_ADD(period, months)
PERIOD_DIFF(period1, period2)
```

## Date Creation Functions

```sql
MAKEDATE(year, dayofyear)
MAKETIME(hour, minute, second)
TIMESTAMP(date, time)
```

## Most Common Interview Functions

```sql
NOW()
CURDATE()
DATE_ADD()
DATE_SUB()
DATEDIFF()
TIMESTAMPDIFF()
DATE_FORMAT()
STR_TO_DATE()
YEAR()
MONTH()
DAY()
EXTRACT()
LAST_DAY()
```
