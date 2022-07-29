class Browsers(dict):

    def return_browsers(browser):

        # Data Dictionary of Environments
        browsers={
            'CHROME': 'Chrome',
            'FIREFOX': 'Firefox',
            'EDGE': 'Edge',
            'IE': 'Internet Explorer',
            }
        return browsers[browser]