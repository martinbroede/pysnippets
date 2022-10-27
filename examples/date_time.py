# Example usage of datetime module.
# Keywords:
# datetime / now / format / fromisoformat / timedelta

from datetime import datetime

formatter = '%Y/%m/%d %H:%M:%S'
days_since_2000 = (datetime.now() - datetime.fromisoformat('2000-01-01')).days
# you can subtract two datetimes (returning type is timedelta)

print(f"current time and date: {datetime.now().strftime(formatter)}\n"
      f"21st century day count: {days_since_2000}")

# current time and date: 2022/10/20 21:35:38
# 21st century day count: 8328
