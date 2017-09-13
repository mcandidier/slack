import angular from 'angular';
import 'angular-ui-router';
import 'angular-local-storage';
import 'angular-ui-bootstrap';

// app scripts
import {routesConfig, csrfConfig} from './app.config';
import AppConstant from './app.constant';
import {IndexCtrl, CompanyDetailCtrl, ChannelMessagesCtrl} from './app.controller';
import CompanyService from './app.services';
import ChannelFormComponent from './components/channel-component';
import ChannelMemberComponent from './components/channel-members-component';
import InviteComponent from './components/invite-channel-component';


const requires = [
    'ui.router',
    'ui.bootstrap',
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

// app components
app.component('channelFormComponent', ChannelFormComponent)
app.component('channelMemberComponent', ChannelMemberComponent)
app.component('inviteComponent', InviteComponent)

// app configs
app.config(routesConfig);
app.config(csrfConfig);

// load angular app module manually
angular.bootstrap(document, ['app'])