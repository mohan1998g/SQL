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

Since your previous question was about MySQL, here's a practical cheat sheet of the most commonly used MySQL Date and Time Functions. MySQL provides functions for getting current dates, extracting parts of dates, formatting dates, date arithmetic, and calculating differences.

1. Current Date & Time Functions
CURDATE()

Returns the current date.

SELECT CURDATE();
-- 2026-08-27

CURTIME()

Returns the current time.

SELECT CURTIME();
-- 14:30:25

NOW()

Returns current date and time.

SELECT NOW();
-- 2026-08-27 14:30:25

SYSDATE()

Returns the exact execution time of the function.

SELECT SYSDATE();

UTC_DATE(), UTC_TIME(), UTC_TIMESTAMP()

Returns UTC values.

SELECT UTC_DATE();
SELECT UTC_TIME();
SELECT UTC_TIMESTAMP();

2. Extracting Date Parts

Assume:

SET @dt = '2026-08-27 15:45:30';

YEAR()
SELECT YEAR(@dt);
-- 2026

MONTH()
SELECT MONTH(@dt);
-- 8

MONTHNAME()
SELECT MONTHNAME(@dt);
-- August

DAY()
SELECT DAY(@dt);
-- 27

DAYNAME()
SELECT DAYNAME(@dt);
-- Thursday

DAYOFMONTH()
SELECT DAYOFMONTH(@dt);
-- 27

DAYOFWEEK()
SELECT DAYOFWEEK(@dt);
-- 5

DAYOFYEAR()
SELECT DAYOFYEAR(@dt);
-- 239

WEEK()
SELECT WEEK(@dt);

QUARTER()
SELECT QUARTER(@dt);
-- 3

HOUR(), MINUTE(), SECOND()
SELECT HOUR(@dt);
SELECT MINUTE(@dt);
SELECT SECOND(@dt);

EXTRACT()

Extract any specific part.

SELECT EXTRACT(YEAR FROM @dt);
SELECT EXTRACT(MONTH FROM @dt);
SELECT EXTRACT(DAY FROM @dt);

3. Date Arithmetic
DATE_ADD()

Add interval.

SELECT DATE_ADD('2026-08-27', INTERVAL 5 DAY);

SELECT DATE_ADD('2026-08-27', INTERVAL 2 MONTH);

SELECT DATE_ADD('2026-08-27', INTERVAL 1 YEAR);

ADDDATE()

Same as DATE_ADD().

SELECT ADDDATE('2026-08-27', INTERVAL 10 DAY);

DATE_SUB()

Subtract interval.

SELECT DATE_SUB('2026-08-27', INTERVAL 5 DAY);

SUBDATE()

Same as DATE_SUB().

SELECT SUBDATE('2026-08-27', INTERVAL 2 MONTH);

4. Date Difference Functions
DATEDIFF()

Difference in days.

SELECT DATEDIFF('2026-08-27', '2026-08-20');
-- 7

TIMESTAMPDIFF()

Difference in specified unit.

SELECT TIMESTAMPDIFF(DAY,
                     '2026-08-20',
                     '2026-08-27');

SELECT TIMESTAMPDIFF(MONTH,
                     '2026-01-01',
                     '2026-08-27');

TIMEDIFF()

Difference between times.

SELECT TIMEDIFF('15:30:00',
                '10:00:00');

5. Formatting Dates
DATE_FORMAT()

Very important for interviews.

SELECT DATE_FORMAT(NOW(), '%d-%m-%Y');
-- 27-08-2026

SELECT DATE_FORMAT(NOW(), '%W');
-- Thursday

SELECT DATE_FORMAT(NOW(), '%M');
-- August


Common format specifiers:

%Y  = 2026
%y  = 26
%m  = 08
%d  = 27
%M  = August
%W  = Thursday
%H  = Hour (24)
%i  = Minutes
%s  = Seconds

TIME_FORMAT()
SELECT TIME_FORMAT('15:45:30', '%H:%i');

6. Conversion Functions
STR_TO_DATE()

Convert string to date.

SELECT STR_TO_DATE('27-08-2026',
                   '%d-%m-%Y');

DATE()

Extract only date portion.

SELECT DATE('2026-08-27 15:45:30');
-- 2026-08-27

TIME()

Extract only time portion.

SELECT TIME('2026-08-27 15:45:30');
-- 15:45:30

FROM_UNIXTIME()
SELECT FROM_UNIXTIME(1756281600);

UNIX_TIMESTAMP()
SELECT UNIX_TIMESTAMP();

7. Month-End and Quarter Functions
LAST_DAY()

Returns last day of month.

SELECT LAST_DAY('2026-02-10');
-- 2026-02-28

QUARTER()
SELECT QUARTER('2026-08-27');
-- 3

Common Interview Queries
Get yesterday's data
SELECT *
FROM orders
WHERE order_date = CURDATE() - INTERVAL 1 DAY;

Get current month records
SELECT *
FROM orders
WHERE MONTH(order_date) = MONTH(CURDATE())
  AND YEAR(order_date) = YEAR(CURDATE());

Get records from last 7 days
SELECT *
FROM orders
WHERE order_date >= CURDATE() - INTERVAL 7 DAY;

Find age
SELECT TIMESTAMPDIFF(
       YEAR,
       '1998-05-20',
       CURDATE()
);

First day of current month
SELECT DATE_SUB(
       CURDATE(),
       INTERVAL DAY(CURDATE()) - 1 DAY
);

Last day of current month
SELECT LAST_DAY(CURDATE());


For SQL interviews and LeetCode, focus especially on:

NOW()
CURDATE()
DATE()
DATE_ADD()
DATE_SUB()
DATEDIFF()
TIMESTAMPDIFF()
EXTRACT()
YEAR()
MONTH()
DAY()
DATE_FORMAT()
STR_TO_DATE()
LAST_DAY()


These cover about 90% of date-related questions.
