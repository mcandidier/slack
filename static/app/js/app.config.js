function routesConfig($stateProvider, $urlRouterProvider, AppConstant) {
    $stateProvider
        .state('company', {
            url: '/',
            controller: 'IndexCtrl',
            controllerAs: 'ctrl',
            templateUrl: AppConstant.templateUrl + 'home.html'
        })
        .state('company.detail', {
            url: '{company}:string/',
            controller: 'CompanyDetailCtrl',
            controllerAs: 'ctrl',
            templateUrl: AppConstant.templateUrl + 'company_detail.html'
        })
        .state('company.detail.channel', {
            url: '{channel}:string/',
            controller: 'ChannelMessagesCtrl',
            controllerAs: 'ctrl',
            templateUrl: AppConstant.templateUrl + 'channel_messages.html'
        })
    ;

    $urlRouterProvider.otherwise('/');
}

function csrfConfig($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}


export {
    routesConfig,
    csrfConfig
};
