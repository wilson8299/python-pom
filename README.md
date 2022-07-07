# python-pom

使用 Pytest 、Selenium 和 Page Object Model，建立物件導向的 Web UI 測試模式，增加腳本的可讀性和可靠性，降低相同程式碼的編寫，方便後續的管理與維護。
<p align="center" width="100%">
    <img src="https://uc9caf355a131a56c23d445dc189.previews.dropboxusercontent.com/p/thumb/ABkjxW7_NK5ajW4ZEjW8vuLGZZU1jrYtjBBNlECsD4dGHE8wkl0NrEtRzRdPI0BStA3Qys6gVZs60CUJsr5CwsPaVVxZ9Wq0qOXW5_LvZeI_YGysBRTwtZDgkcJy5UjRgoeV_5HzU4e5Gvmd7V1khfcotQmGieHIQzQHRyNNGxDd0xyJMNLDkOZcGTwQmQn2GfxvTAs6a8ERHUxDjBFt3_ItS4QG-TMCIqhuahTAoNEUvryUBnZCZ8dc49_cwlsCClSa40UJCboW3WZwzsieRO96pFkQgZzmlnMJMlWJWTqN8CRixCMDTogckamV3TAxe_xSI2bdmpdvgN-QxysrEeDuOW80WtXnPvzjyzQbNDnWlKCFUjghqvkzQdBjYnRkR56mq9Umyjq2kqEQfPPx29-z0Me_KRjZ6IDmiw0rUms-9g/p.gif" alt="example" width="85%"/>
</p>


## Table of contents

- [Built With](#built-with)
- [Usage](#usage)
- [Structure](#structure)
- [Driver](#driver)
- [Page](#page)
- [Script](#script)
- [Report](#report)



## Built With

- Python 3.6
- [POM](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- [Selenium](https://github.com/SeleniumHQ/selenium)
- [Pytest](https://github.com/pytest-dev/pytest)
- [Pytest-html](https://github.com/pytest-dev/pytest-html)



## Usage

```cmd
$ git clone https://github.com/wilson8299/python-pom.git

$ pip3 install -r requirements.txt

$ pytest
```

> 默認使用 chrome，可以從 configuration.py 更改 BROWSER。



## Structure

```
File Tree
├── config/                     # 配置
│ └── configuration.py
├── data/                       # 測試資料
├── logs/                       # 測試日誌
├── pages/                      # 制定一系列 Selenium 的基本操作 
│ ├── base_page.py
│ └── search_page.py
├── reports/                    # 測試報告
├── scripts/                    # 測試腳本，關注商業邏輯
│ └── test_search.py
├── utils/
│ ├── browser.py                # 下載及啟動瀏覽器
│ ├── logger.py                 # 日誌模組
│ ├── read_config.py            # 存取 config 文件
│ └── read_yaml.py              # 存取 yaml 文件
├── conftest.py                 # 自訂 pytest hook
└── pytest.ini                  # pytest 配置檔案
```



## Driver

不需要自行下載 driver，而是透過 webdriver_manager 自動在主機內安裝相對應的 driver 版本，並且設定好路徑和權限。

```python
# utils/browser.py
if Global.BROWSER == 'chrome':
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    self.logger.info('Starting chrome browser.')
elif Global.BROWSER == 'firefox':
    self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    self.logger.info('Starting firefox browser.')
elif Global.BROWSER == 'edge':
    self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    self.logger.info('Starting edge browser.')
```



## Page

每個頁面都有一個 page 檔案，制定一系列 Selenium 的基本操作 。

````python
# pages/search_page.py
class SearchPage(BasePage):
    search_input = By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    search_button = By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]'

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def input_content(self, text):
        self.send_keys(self.search_input, text)

    def focus_searchbar(self):
        self.focus(self.search_input)

    def click_search_button(self):
        self.click(self.search_button)
````



## Script

專注於商業邏輯層面，使用 page 所提供的方法來模擬使用者的操作。測試框架使用 pytest，並透過裝飾器實現需要的功能， e.g., pytest.fixture set_browser 實現 setUpClass / tearDownClass。

```python
# scripts/test_search.py
@pytest.fixture(scope='class', name='browser')
def set_browser():
    browser = Browser()
    driver = browser.open_browser()
    yield driver
    browser.close_browser()

@pytest.mark.usefixtures('browser')
class TestSearch:
    @pytest.fixture(scope='function', name='search_page')
    def set_search_page(self, browser):
        browser.get('https://www.google.com')
        yield SearchPage(browser)

    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    @pytest.mark.parametrize('content', read_yaml('search_data')['search_content'])
    def test_search_content_use_enter(self, search_page, content):
        search_page.input_content(content)
        search_page.input_content(Keys.ENTER)
        assert content in search_page.get_title()
```



## Report

pytest-html 生成報告，也可以自行替換成其他報告庫或透過 pytest hook 自定義報告。 

<p align="center" width="100%">
    <img src="https://ucf9d94b9e1e68b4a705c1cf0d76.previews.dropboxusercontent.com/p/thumb/ABnibgmOHOefqD3BlgcmyM3mK74x-Ve-8y2Biiui_cbbkYJtYqeWToKt2e-lu4Ut-LUcIOIUbBJsgHAfOcYOHm8VY1N9hM3S8WfSq2x8CN5lhU71eXE-PCQ9cpRJeDPoAn5zSYSRRwKpJvx8OBxRvS5YR_SvXTjldXafPGY_5rRgxzPVZgoVF8MBqwxmuRSy5i_-Ve6NBkdd7O3ljmmS559a3Ac5vhkSHjgL7xpM2GuybUfEtvZcUZDSBjn7D8D_Zk0TrbJVFkiPj2TpgsBis8HSe-jUN3UZ-NCA4e0hh8v1SgSs_1dn0BFaVf23VPMu7eVeP1nO90DzJp_q0w9PZss17WK86bWOVp-va7I6w81aMsHgU2sffyGgedVnwKLLKwggg4-WBQsvHvcF3jgOdPqcV4UANs3fxOjreyE4Gba_0w/p.png" alt="report-image" width="85%"/>
</p>
