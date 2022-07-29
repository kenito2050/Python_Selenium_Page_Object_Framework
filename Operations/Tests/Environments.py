class Environments(dict):

    def return_environments(environment):

        # Data Dictionary of Environments
        environments={
            'LA': 'operations.wedbush.com/',
            'DL': 'operations-dl.wedbush.com/',
            'UAT': 'uslawsuat01:8061/',
            'DEV': 'uslaentint/'
            }
        return environments[environment]