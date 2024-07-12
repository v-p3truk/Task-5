import re
import json
import requests
import sqlite3

def task():
    response = requests.get('https://www.lejobadequat.com/emplois')
    content = response.text
    job = re.findall(r'>([^<]+ H/F)<', content)
    url = re.findall(r'https:\/\/www\.lejobadequat\.com\/emplois\/\d[\w-]+', content)
    print(job)
    print(url)

    data = [
        {'JOB': job, 'URL': url}
        for job, url in zip(job, url)
    ]

    with open('parsed_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    filename = 'parse_data.db'

    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    sql = """
        create table if not exists parse_data (
            id integer primary key,
            job text,
            url text
        )
    """
    cursor.execute(sql)

    for entry in data:
        cursor.execute("""
            insert into parse_data (job, url)
            values (?, ?)
        """, (entry['JOB'], entry['URL']))


    conn.commit()
    conn.close()

if __name__ == "__main__":
    task()