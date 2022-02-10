# import <
from selenium import webdriver
from backend.utility import jsonLoad, jsonDump
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# >


# function <
def scrapeMyProject(user: str) -> None:
    '''  '''

    # local <
    options = Options()
    options.headless = True
    setting = jsonLoad(file = '/backend/scrape.json')['scrapeMyProject']
    myProjectData, queue = jsonLoad(file = '/frontend/data/myProject.json'), []
    driver = webdriver.Chrome(ChromeDriverManager().install())#, options = options)

    # >

    # if (new user) <
    # add user to dictionary <
    if (user not in myProjectData.keys()): myProjectData[user] = {

        'queue' : [

        ],

        'project' : {

        }

    }

    # >

    # to website <
    driver.get(setting['website'].replace('<>', user))

    # >

    # while (page) <
    while (True):

        # iterate (project) <
        for i in [str(i) for i in range(1, 31)]:

            # try (if project) <
            try:

                # get description and title <
                # add title to queue <
                description = driver.find_element_by_xpath(setting['repositoryDescription'].replace('<>', i)).text
                title = driver.find_element_by_xpath(setting['repositoryTitle'].replace('<>', i)).text
                queue.append(title)

                # >

                # if (new project) <
                if (title not in myProjectData[user]['project'].keys()):

                    myProjectData[user]['project'][title] = {

                        'description' : description,
                        'hide' : False,
                        'feed' : {}

                    }

                # >

            # >

            # except (then no project) <
            except NoSuchElementException: pass

            # >

        # >

        # try (if new page) <
        # except (then no new page) <
        try: driver.find_element_by_link_text('Next').click()
        except NoSuchElementException:

            myProjectData[user]['queue'] = queue
            break

        # >

    # >

    # output <
    jsonDump(file = '/frontend/data/myProject.json', data = myProjectData)

    # >


def scrapeAboutMe(user: str) -> None:
    '''  '''

    # local <
    options = Options()
    options.headless = True
    aboutMeData = jsonLoad(file = '/frontend/data/aboutMe.json')
    setting = jsonLoad(file = '/backend/scrape.json')['scrapeAboutMe']
    driver = webdriver.Chrome(ChromeDriverManager().install())#, options = options)
    myProjectData = jsonLoad(file = '/frontend/data/myProject.json')[user]['project']

    # >

    # reset user data <
    aboutMeData[user] = {

        'topic' : [],
        'language' : []

    }

    # >

    # iterate (project) <
    for project in myProjectData.keys():

        # to website <
        driver.get(setting['website'].replace('<>', user) + project)

        # >

        # iterate topic and language <
        for i in [f'[{i}]' for i in range(25)]:

            # local <
            topic = None
            language = None

            # >

            # try (if topic) <
            # except (then no topic) <
            try:

                topic = driver.find_element_by_xpath(setting['topic'].replace('<>', i)).text
                topic = topic.replace('-', ' ')

            except NoSuchElementException: pass

            # >

            # try (if languageA) <
            # except (then languageB) <
            try: language = driver.find_element_by_xpath(setting['languageA'].replace('<>', i)).text
            except NoSuchElementException:

                # try (if languageB) <
                # except (then no languageB) <
                try: language = driver.find_element_by_xpath(setting['languageB'].replace('<>', i)).text
                except NoSuchElementException: pass

                # >

            # >

            # split and title topic <
            # add topic and language <
            if (language is not None): aboutMeData[user]['language'].append(language)
            if (topic is not None): aboutMeData[user]['topic'].append(topic)

            # >

    # >

    # output <
    jsonDump(file = '/frontend/data/aboutMe.json', data = aboutMeData)

    # >

# >
