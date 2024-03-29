# python-pom

使用 Pytest 、Selenium 和 Page Object Model，建立物件導向的 Web UI 測試模式，增加腳本的可讀性和可靠性，降低相同程式碼的編寫，方便後續的管理與維護。
<p align="center" width="100%">
    <img src="https://imgur.com/oluUCBS.gif" alt="example" width="85%"/>
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
├── reports/                    # 測試報告
├── scripts/                    # 測試腳本，關注商業邏輯
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
# pages/base_page.py
class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.logger = Logger('Page')
        self.ac = ActionChains(self.driver)

    def get_title(self):
        return self.driver.title

    def find_element(self, loc):
        try:
            element = WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_element(loc[0], loc[1]));
        except Exception as e:
            self.logger.error(f'Error when find element {loc}')
            self.logger.exception(e)
        else:
            return element
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
    <img src="https://imgur.com/yLQfx48.png" alt="report-image" width="85%"/>
</p>
