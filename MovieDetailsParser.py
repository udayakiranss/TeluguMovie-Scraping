import pandas as pd
from bs4 import BeautifulSoup


def movie_details(data):
    movie_list = []
    ratings = []
    release_dates = []
    counts = []
    links = []

    for row in data:
        first_td = row.find('td')
        count = first_td.text
        second_td = first_td.find_next_sibling('td')
        if second_td is not None:
            counts.append(count)
            movie = second_td.text
            link = second_td.find('a').get('href')
            links.append(link)
            movie_list.append(movie)
            third_td = second_td.find_next_sibling('td')
            release_date = third_td.text
            release_dates.append(release_date)
            final_td = third_td.find_next_sibling('td')
            rating = final_td.text.replace('\n', '').replace('\r', '').replace('                         ', ' ')
            ratings.append(rating)

    movie_data = pd.DataFrame(counts)

    movie_data['name'] = pd.Series(movie_list)
    movie_data['release-date'] = pd.Series(release_dates)
    movie_data['rating'] = pd.Series(ratings)
    movie_data['link'] = pd.Series(links)

    return movie_data


def version_1_movie_information(movie_page):
    # movie_page = requests.get(quote_page + "/" + movie_url)
    details_soup = BeautifulSoup(movie_page.text, 'html.parser')
    version_1 = details_soup.find('table', attrs={'height': '280', 'cellspacing': '0', 'cellpadding': '0',
                                                      'width': '336', 'align': 'right', 'border': '1'})
    my_dict = {}

    version_2 = details_soup.find('table', attrs={'height': '250', 'cellspacing': '0', 'cellpadding': '0',
                                                            'width': '300', 'align': 'right', 'border': '1'})

    version_3 = details_soup.find('table', attrs={'width': '100%', 'border': '0', 'cellspacing': '4',
                                                  'cellpadding': '4'})
    version_4 = details_soup.find('table', attrs={'width': '100%', 'border': '0', 'cellspacing': '0',
                                                  'cellpadding': '3'})
    # if version_1 is not None:
    #     content_area = version_1
    # elif version_2 is not None:
    #     content_area = version_2
    # elif version_3 is not None:
    #     content_area = version_3

    if version_1 is not None:
        p = version_1.find_next_sibling('p')
        font = p.find('font')
        splits = font.text.split('\n')

        for split in splits:
            dicts = split.split(':')
            if len(dicts) == 2:
                my_dict[dicts[0].strip()] = dicts[1].strip()

        next_p = p.find_next_sibling('p')
        if next_p is not None:
            next_splits = next_p.text.replace('\r', '').split('\n')
            # print(next_splits)
            for split in next_splits:
                dicts = split.split(':')
                if len(dicts) == 2:
                    my_dict[dicts[0].strip()] = dicts[1].strip()

            third_p = next_p.find_next_sibling('p')
            if third_p is not None:
                third_splits = third_p.text.replace('\r', '').split('\n')
                # print(next_splits)
                for split in third_splits:
                    dicts = split.split(':')
                    if len(dicts) == 2:
                        my_dict[dicts[0].strip()] = dicts[1].strip()

    elif version_2 is not None:
        p = version_2.find_next_sibling('p')
        font = p.find('font')
        splits = font.text.split('\n')

        for split in splits:
            dicts = split.split(':')
            if len(dicts) == 2:
                my_dict[dicts[0].strip()] = dicts[1].strip()

        next_p = p.find_next_sibling('p')

        if next_p is not None:
            next_splits = next_p.text.replace('\r', '').split('\n')
            # print(next_splits)
            for split in next_splits:
                dicts = split.split(':')
                if len(dicts) == 2:
                    my_dict[dicts[0].strip()] = dicts[1].strip()

            third_p = next_p.find_next_sibling('p')
            if third_p is not None:
                third_splits = third_p.text.replace('\r', '').split('\n')
                # print(next_splits)
                for split in third_splits:
                    dicts = split.split(':')
                    if len(dicts) == 2:
                        my_dict[dicts[0].strip()] = dicts[1].strip()
    elif version_3 is not None:
        td = version_3.find('td', attrs={'valign': 'top'})
        p = td.find('p')
        splits = p.text.split('\n')

        for split in splits:
            dicts = split.split(':')
            if len(dicts) == 2:
                my_dict[dicts[0].strip()] = dicts[1].strip()
    elif version_4 is not None:

        tr = version_4.find_all('tr')[3]
        p = tr.find('p')

        if p is not None:
            splits = p.text.split('\n')

            for split in splits:
                dicts = split.split(':')
                if len(dicts) == 2:
                    my_dict[dicts[0].strip()] = dicts[1].strip()
        else:
            tr = version_4.find_all('tr')[4]
            # print(tr)
            p = tr.find('p')
            splits = p.text.split('\n')

            for split in splits:
                dicts = split.split(':')
                if len(dicts) == 2:
                    my_dict[dicts[0].strip()] = dicts[1].strip()

    return my_dict
