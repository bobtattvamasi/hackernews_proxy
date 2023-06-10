# path: hackernews/views.py
from django.http import HttpResponse
import requests
import re
from django.shortcuts import render
from logging import getLogger
from django.shortcuts import redirect
from django.http import Http404
from .forms import TextInputForm
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import News

logger = getLogger("proxy")

def handleFiles(modified_content):
    '''
    Handle static files
    '''

    # if "favicon.ico" in modified_content:
    #     print(f"modified_content: {modified_content}")
    #     modified_content = modified_content.replace("favicon.ico", "https://news.ycombinator.com/favicon.ico")
    #     print(f"MODIFIED_CONTENT: {modified_content}")
    # modified_content = re.sub(r"favicon\.ico", "https://news.ycombinator.com/favicon.ico", modified_content)
    # if "y18.svg" in modified_content:
    #     modified_content = modified_content.replace("y18.svg", "{% static 'images/y18.svg' %}")
    # if "news.css?ufxBzekqGIeRVQP6GVxS" in modified_content:
    #     modified_content = modified_content.replace("news.css", "{% static 'css/news.css?ufxBzekqGIeRVQP6GVxS.css' %}")
    # if "hn.js?ufxBzekqGIeRVQP6GVxS" in modified_content:
    #     modified_content = modified_content.replace("hn.js", "{% static 'js/hn.js?ufxBzekqGIeRVQP6GVxS' %}")



    return modified_content

def modify_text(text):
    soup = BeautifulSoup(text, 'html.parser')

    for element in soup.find_all(text=True):
        if element.parent.name not in ['script', 'style']:
            words = element.split()
            modified_words = []

            for word in words:
                if (
                    len(word) == 6
                    and word[-1] != '™'
                    and not bool(re.search(r'[()1234567890 _:.,;“”+=?!\']', word))
                ):
                    modified_words.append(word + '™')
                else:
                    modified_words.append(word)

            element.replace_with(' '.join(modified_words))

    return str(soup)

def proxy_home(request):

    if request.path == '/news/' or request.path == '/item/news/':
        return redirect('/')
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)
    create_news_from_html(response.text)

    return render(request, 'test.html', {'content': modified_content })

def proxy_item(request):
    item_id = request.GET.get('id')
    path = request.path

    if not item_id:
        # Если нет id, возвращаем страницу "Элемент не найден"
        raise Http404("Элемент не найден")

    if path.startswith('/item/item/'):
        # Remove the "item" part from the URL
        modified_path = path.replace('/item/item/', f'/item?id={item_id}', 1)
        return redirect(modified_path)

    url = f'https://news.ycombinator.com/item?id={item_id}'
    response = requests.get(url)
    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)
    #return HttpResponse(modified_content)
    return render(request, 'item.html', {'content': modified_content})

def text_input_view(request):
    form = TextInputForm()

    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text_input']
            # Обработка введенного текста, если необходимо

    return render(request, 'home.html', {'form': form})

def create_news_from_html(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    news_elements = soup.select('.athing')
    substring_elements = soup.select('.subtext')

    for news_element, substring_element in zip(news_elements, substring_elements):
        id_ = int(news_element['id'])
        #News.objects.
        existing_news = News.objects.filter(id_news=id_).exists()
        if not existing_news:
            rank_text = news_element.select_one('.rank').text
            # Convert the rank text to an integer
            rank = int(rank_text[:-1])

            sitestr = news_element.select_one('.sitestr').text if news_element.select_one('.sitestr') else ''

            score = substring_element.select_one('.score').text.split()[0] if substring_element.select_one('.score') else 0

            url = news_element.select_one('.titleline a')['href']

            user_element = substring_element.select_one('.hnuser')
            user_name = user_element.text if user_element else ''

            text = news_element.select_one('.titleline').text

            time_ago_element = substring_element.select_one('.age a')
            time_ago = time_ago_element.text if time_ago_element else ''

            comments_element = substring_element.select_one('.comment')
            comments = comments_element.text.split()[0] if comments_element else 0
            comments_count = int(comments)

            # Create a new instance of the News model and save it to the database
            news = News(id_news = id_, rank=rank, url=url, user_name=user_name, text=text, time_ago=time_ago,
                        comments_count = comments_count, score=score, sitestr=sitestr)
            news.save()

def user(request):
    user_name = request.GET.get('id')

    if not user_name:
        # Если нет user_name, возвращаем страницу "Элемент не найден"
        raise Http404("Элемент не найден")

    url = f'https://news.ycombinator.com/user?id={user_name}'
    response = requests.get(url)
    modified_content = modify_text(response.text)

    return HttpResponse(modified_content)

def newest(request):
    url = 'https://news.ycombinator.com/newest'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)

    return HttpResponse(modified_content)

def past(request):
    url = 'https://news.ycombinator.com/front'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)

    return HttpResponse(modified_content)

def newcomments(request):
    url = 'https://news.ycombinator.com/newcomments'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)

    return HttpResponse(modified_content)

def ask(request):
    url = 'https://news.ycombinator.com/ask'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)

    return HttpResponse(modified_content)

def show(request):
    url = 'https://news.ycombinator.com/show'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)

    return HttpResponse(modified_content)

def jobs(request):
    url = 'https://news.ycombinator.com/jobs'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)

    return HttpResponse(modified_content)

def submit(request):
    url = 'https://news.ycombinator.com/submit'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)

    return HttpResponse(modified_content)

def login(request):
    url = 'https://news.ycombinator.com/login?goto=news'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)

    return HttpResponse(modified_content)

def newsguidelines(request):
    url = 'https://news.ycombinator.com/newsguidelines.html'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)

    return render(request, 'newsguidelines.html', {'content': modified_content})

def newsfaq(request):
    url = 'https://news.ycombinator.com/newsfaq.html'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)

    return render(request, 'newsfaq.html', {'content': modified_content})

def lists(request):
    url = 'https://news.ycombinator.com/lists'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)

    return HttpResponse(modified_content)

def security(request):
    url = 'https://news.ycombinator.com/security.html'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)

    return render(request, 'security.html', {'content': modified_content})

def legal(request):
    url = 'https://news.ycombinator.com/legal'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)


    return HttpResponse(modified_content)

def apply(request):
    url = 'https://news.ycombinator.com/apply'
    response = requests.get(url)

    modified_content = modify_text(response.text)
    modified_content = handleFiles(modified_content)


    return HttpResponse(modified_content)

def from_site(request):
    print(request.GET['site'])
    site_url = request.GET['site']
    url = f'{site_url}'

    return redirect(site_url)