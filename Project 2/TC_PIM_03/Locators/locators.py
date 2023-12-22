class WebApp_Locators:
    username_input_box = "username"
    password_input_box = "password"
    submit_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    admin_button = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'
    search_bar = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input'
    option_tab = [
            '//span[text()="Admin"]',
            '//span[text()="PIM"]', 
            '//span[text()="Leave"]', 
            '//span[text()="Time"]', 
            '//span[text()="Recruitment"]', 
            '//span[text()="My Info"]', 
            '//span[text()="Performance"]', 
            '//span[text()="Dashboard"]', 
            '//span[text()="Directory"]', 
            '//span[text()="Maintenance"]', 
            '//span[text()="Buzz"]'
            ]
    
    searched_item = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    maintenance_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/purgeEmployee'
    confirm_button = '//*[@id="app"]/div[1]/div[1]/form/div[4]/button[2]'