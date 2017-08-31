import angular from 'angular';
import 'angular-ui-router';
import 'angular-local-storage';

// app scripts
import routesConfig from './app.config';
import AppConstant from './app.constant';
import {IndexCtrl, CompanyDetailCtrl, ChannelMessagesCtrl} from './app.controller.js';
import CompanyService from './app.services';

const requires = [
    'ui.router',
    'LocalStorageModule'
];

let app = angular.module('app', requires);

app.constant('AppConstant', AppConstant);
app.controller('IndexCtrl', IndexCtrl);
app.controller('ChannelMessagesCtrl', ChannelMessagesCtrl);
app.controller('CompanyDetailCtrl', CompanyDetailCtrl);
app.service('CompanyService',CompanyService);
app.config(routesConfig);

// load angular app module manually
angular.bootstrap(document, ['app'])