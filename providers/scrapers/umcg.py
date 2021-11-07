from typing import Optional, TypedDict

from ..util import soup_find_string
from .base import Scraper, ScraperServiceOffering, ScraperServiceTime, TF, TM, ADOLESCENTS, ADULTS

INDIVIDUAL_TEXT = 'individueel'


class ScraperServiceUMCG(TypedDict):
    match: str
    offering: ScraperServiceOffering


SERVICES: list[ScraperServiceUMCG] = [{
    'match': 'Psychiatrie - Intake Genderteam',
    'offering': {
        'service': 'Intake',
        'types': [TF, TM],
        'age_groups': [ADOLESCENTS, ADULTS]
    }
}, {
    'match': 'Gynaecologie - Hysterectomie',
    'offering': {
        'service': 'Hysterectomy',
        'types': [TM],
        'age_groups': [ADULTS]
    }
}, {
    'match': 'Plastische Chirurgie - Mastectomie',
    'offering': {
        'service': 'Mastectomy',
        'types': [TM],
        'age_groups': [ADULTS]
    }
}, {
    'match': 'Plastische Chirurgie - Vaginaplastiek',
    'offering': {
        'service': 'Vaginaplasty',
        'types': [TF],
        'age_groups': [ADULTS]
    }
}, {
    'match': 'Plastische Chirurgie - Secundaire genitale correcties',
    'offering': {
        'service': 'Secondary corrections',
        'types': [TF],
        'age_groups': [ADULTS]
    }
}, {
    'match': 'Plastische Chirurgie - Mamma-augmentatie',
    'offering': {
        'service': 'Breast augmentation',
        'types': [TF],
        'age_groups': [ADULTS]
    }
}, {
    'match': 'Plastische Chirurgie - Feminisatieoperaties',
    'offering': {
        'service': 'Facial surgery',
        'types': [TF],
        'age_groups': [ADULTS]
    }
}, {
    'match': 'KNO - Intake Logopedist',
    'offering': {
        'service': 'Speech therapy',
        'types': [TF, TM],
        'age_groups': [ADOLESCENTS, ADULTS]
    }
}]


class ScraperUMCG(Scraper):

    def get_provider_handle(self) -> str:
        return 'umcg'

    def get_source_url(self) -> str:
        return 'https://www.umcg.nl/NL/Zorg/Volwassenen/Wachttijden/Paginas/Genderteam.aspx'

    def scrape(self) -> list[ScraperServiceTime]:
        soup = self.fetch_html_page(self.get_source_url())

        table = soup.find('table', class_='ms-rteTable-UMCG')
        table_body = table.tbody
        last_header: Optional[str] = None

        service_times: list[ScraperServiceTime] = []

        for table_row in table_body.children:
            title = soup_find_string(table_row.th)
            if not title:
                continue

            is_header = table_row.th.strong is not None
            if is_header:
                last_header = title
                continue

            title = title.split('(')[0].strip()
            name = f'{last_header} - {title}'

            weeks: Optional[int] = None
            is_individual: bool = False
            for table_column in table_row.children:
                content = soup_find_string(table_column)
                if content:
                    if INDIVIDUAL_TEXT in content:
                        is_individual = True
                        break

                    try:
                        weeks = int(content.replace('>', ''))
                    except ValueError:
                        continue

                    if weeks:
                        break

            if weeks or is_individual:
                print(name)
                print(f'{weeks} weeks')
                print('individual', is_individual)

                for service in SERVICES:
                    if service['match'] == name:
                        # NOTE: the object spread operator would be nicer here, but Python's typing is terrible
                        service_time: ScraperServiceTime = service['offering'].copy()
                        service_time['days'] = None if is_individual else weeks * 7
                        service_time['is_individual'] = is_individual
                        service_time['has_stop'] = False
                        service_times.append(service_time)
                        break
                else:
                    print('no match')

        return service_times
