import angular from 'angular';
import 'angular-ui-router';
import 'angular-local-storage';

// app scripts
import {routesConfig, csrfConfig} from './app.config';
import AppConstant from './app.constant';
import {IndexCtrl, CompanyDetailCtrl, ChannelMessagesCtrl} from './app.controller.js';
import CompanyService from './app.services';

const requires = [
    'ui.router',
    'LocalStorageModule'
];

// instantiate angular app
let app = angular.module('app', requires);

// app constant
app.constant('AppConstant', AppConstant);

// app services 
app.service('CompanyService',CompanyService);

// app controllers 
app.controller('IndexCtrl', IndexCtrl);
app.controller('ChannelMessagesCtrl', ChannelMessagesCtrl);
app.controller('CompanyDetailCtrl', CompanyDetailCtrl);

// app configs
app.config(routesConfig);
app.config(csrfConfig);

// load angular app module manually
angular.bootstrap(document, ['app'])