import requests
import pandas as pd
from bs4 import BeautifulSoup
from MovieDetailsParser import movie_details, version_1_movie_information

quote_page = 'http://idlebrain.com/movie/archive'

page = requests.get(quote_page+"/index.html")
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table', attrs={'width': '100%', 'border': '0', 'cellspacing': '0', 'cellpadding': '3'})
# ff_rows = table.find_all('tr', attrs={'bgcolor': '#FFFFFF'})
# e7rows = table.find_all('tr', attrs={'bgcolor': 'e7e7e7'})
header = table.find('tr', attrs=None)
columns = header.find_next_sibling('tr')
rows = columns.find_next_siblings('tr')

movies = movie_details(rows)

print(movies.info())
# print(movies.iloc[1, 4])

urls = movies.iloc[:, 4]
movie_dict_list = []
for url in urls:
    movie_page = requests.get(quote_page + "/" + url)
    movie_dict = version_1_movie_information(movie_page)
    if len(movie_dict) > 0:
        movie_dict_list.append(movie_dict)
        # print(movie_dict)
    else:
        print(url)
print("Total Count:", len(movie_dict_list))
# if len(splits[2].split(':')) == 2:
#     punch_line = splits[2].split(':')[1]
#     my_dict['punch_line'] = punch_line.strip()
#
# if len(splits[3].split(':')) == 2:
#     genre = splits[3].split(':')[1]
#     my_dict['genre'] = genre.strip()
#
# if len(splits[4].split(':')) == 2:
#     type_s = splits[4].split(':')[1]
#     my_dict['type'] = type_s.strip()
#
# if len(splits[5].split(':')) == 2:
#     banner = splits[5].split(':')[1]
#     my_dict['banner'] = banner.strip()
# def movie_information(movie_url):
#     movie_page = requests.get(quote_page + "/" + movie_url)
#     details_soup = BeautifulSoup(movie_page.text, 'html.parser')
#     version_1 = details_soup.find('table', attrs={'height': '280', 'cellspacing': '0', 'cellpadding': '0',
#                                                       'width': '336', 'align': 'right', 'border': '1'})
#     my_dict = {}
#
#     version_2 = details_soup.find('table', attrs={'height': '250', 'cellspacing': '0', 'cellpadding': '0',
#                                                             'width': '300', 'align': 'right', 'border': '1'})
#
#     version_3 = details_soup.find('td', attrs={'valign':'top'})
#
#     if version_1 is not None:
#         content_area = version_1
#     elif version_2 is not None:
#         content_area = version_2
#     elif version_3 is not None:
#         content_area = version_3
#
#     if content_area is not None:
#         p = content_area.find_next_sibling('p')
#         font = p.find('font')
#         splits = font.text.split('\n')
#
#         for split in splits:
#             dicts = split.split(':')
#             if len(dicts) == 2:
#                 my_dict[dicts[0].strip()] = dicts[1].strip()
#
#         next_p = p.find_next_sibling('p')
#         if next_p is not None:
#             next_splits = next_p.text.replace('\r', '').split('\n')
#             # print(next_splits)
#             for split in next_splits:
#                 dicts = split.split(':')
#                 if len(dicts) == 2:
#                     my_dict[dicts[0].strip()] = dicts[1].strip()
#
#             third_p = next_p.find_next_sibling('p')
#             if third_p is not None:
#                 third_splits = third_p.text.replace('\r', '').split('\n')
#                 # print(next_splits)
#                 for split in third_splits:
#                     dicts = split.split(':')
#                     if len(dicts) == 2:
#                         my_dict[dicts[0].strip()] = dicts[1].strip()

    # else if table_details_alter is not None:
    #     p = version_2.find_next_sibling('p')
    #     font = p.find('font')
    #     splits = font.text.split('\n')
    #
    #     for split in splits:
    #         dicts = split.split(':')
    #         if len(dicts) == 2:
    #             my_dict[dicts[0].strip()] = dicts[1].strip()
    #
    #     next_p = p.find_next_sibling('p')
    #
    #     if next_p is not None:
    #         next_splits = next_p.text.replace('\r', '').split('\n')
    #         # print(next_splits)
    #         for split in next_splits:
    #             dicts = split.split(':')
    #             if len(dicts) == 2:
    #                 my_dict[dicts[0].strip()] = dicts[1].strip()
    #
    #         third_p = next_p.find_next_sibling('p')
    #         if third_p is not None:
    #             third_splits = third_p.text.replace('\r', '').split('\n')
    #             # print(next_splits)
    #             for split in third_splits:
    #                 dicts = split.split(':')
    #                 if len(dicts) == 2:
    #                     my_dict[dicts[0].strip()] = dicts[1].strip()

    # return my_dict


# def movie_details(data):
#     movie_list = []
#     ratings = []
#     release_dates = []
#     counts = []
#     links = []
#
#     for row in data:
#         first_td = row.find('td')
#         count = first_td.text
#         second_td = first_td.find_next_sibling('td')
#         if second_td is not None:
#             counts.append(count)
#             movie = second_td.text
#             link = second_td.find('a').get('href')
#             links.append(link)
#             movie_list.append(movie)
#             third_td = second_td.find_next_sibling('td')
#             release_date = third_td.text
#             release_dates.append(release_date)
#             final_td = third_td.find_next_sibling('td')
#             rating = final_td.text.replace('\n', '').replace('\r', '').replace('                         ', ' ')
#             ratings.append(rating)
#
#     movie_data = pd.DataFrame(counts)
#
#     movie_data['name'] = pd.Series(movie_list)
#     movie_data['release-date'] = pd.Series(release_dates)
#     movie_data['rating'] = pd.Series(ratings)
#     movie_data['link'] = pd.Series(links)
#
#     return movie_data