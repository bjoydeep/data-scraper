# Data Scraping

To run start this data collection
- fill out the pwd.env file.
- Then:
    ```
    cd scrape
    python driver.py
    ```

This will save the data being gathered in the database referred to in pwd.env file

### Sample pwd.env file
- This files is protected by .gitignore, so it is not checked in

```
{"promurl":"https://thanos-querier-openshift-monitoring.apps.abc.com",
"token":"shaxyzabcetcetc",
"startOffsetMinute":10080,
"endOffsetMinute":0,
"stepsMinute":"10m"}
```