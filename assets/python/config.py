from selenium.webdriver.chrome.options import Options

class driver_config:
    driver_path = 'C:\\Users\\Pilou\\AppData\\Local\\Temp\\Rar$EXa24408.24094\\chromedriver.exe' # add chrome driver path here
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--headless')
    options.add_argument('--incognito')

class js_code:
    js_script_path = '.\\js\\load_js_methods.js'
    js_script = open(js_script_path).read()