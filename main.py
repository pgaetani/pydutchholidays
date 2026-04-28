import requests
from bs4 import BeautifulSoup
from datetime import datetime
import locale


def get_dutch_holidays(next_year=False):
    url = "https://www.rijksoverheid.nl/onderwerpen/schoolvakanties/vraag-en-antwoord/officiele-feestdagen"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    year = datetime.now().year
    if next_year:
        year += 1

    year_str = str(year)
    
    h2 = soup.find('h2', string=lambda text: text and text.startswith(f'Feestdagen {year}'))
    if not h2:
        raise ValueError(f"Could not find the section for Feestdagen {year}")
    
    ul = h2.find_next('ul')
    if not ul:
        raise ValueError("Could not find the list of holidays")
    
    holidays = {}

    # set the locale to Dutch (or datetime parsing will fail for month names)
    locale.setlocale(locale.LC_TIME, 'nl_NL.UTF-8')
    
    for li in ul.find_all('li'):
        text = li.get_text()
        parts = text.split(':')
        if len(parts) < 2:
            continue
        
        holiday_name = parts[0].strip()
        dates_text = parts[1].strip()
        
        if ' en ' in dates_text:
            date_parts = dates_text.split(' en ')

            dates = []

            for date_part in date_parts:
                if year_str not in date_part:
                    date_part += f' {year_str}'

                dates.append(datetime.strptime(date_part.strip(), '%A %d %B %Y'))
        else:
            if year_str not in dates_text:
                dates_text += f' {year_str}'
            dates = [datetime.strptime(dates_text.strip(), '%A %d %B %Y')]
        
        holidays[holiday_name] = dates if len(dates) > 1 else dates[0]

    return holidays


def main():
    print(get_dutch_holidays())


if __name__ == "__main__":
    main()
