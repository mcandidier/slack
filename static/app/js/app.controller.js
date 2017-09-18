class IndexCtrl {
    constructor($scope, CompanyService, localStorageService, $state) {
        'ngInject';
        this.state = $state;
        this.localStorageService = localStorageService;
        this.CompanyService = CompanyService;
        
        // get all companies for current user
        CompanyService.companyList().then(resp =>{
            this.companies = resp.data;
        });
    }

    companySelect(company) {
        this.state.go('company.detail', {'company': company.name});
    }
}

class CompanyDetailCtrl {
    constructor($scope, CompanyService, $stateParams, localStorageService, $uibModal, $state) {
        'ngInject';
        this.CompanyService = CompanyService;
        this.$uibModal = $uibModal;
        this.$scope = $scope;
        this.$state = $state;
        this.stateParams = $stateParams;
        this.localStorageService = localStorageService;
        this.init();
    }

    addChannel() {
        this.$uibModal.open({
          component: 'channelFormComponent'
        });
    }

    gotoChannelDetail(channel) {
        this.$state.go('company.detail.channel', {'channel': channel.name});
    }

    init() {
        const company = this.stateParams.company;
        this.CompanyService.getAllChannels(company);
        this.$scope.$watchCollection('ctrl.CompanyService.channels', data => this.channels = data);
        this.CompanyService.getAllMembers(company).then( resp => {
            resp.data.map( user => {
                this.CompanyService.members[user.member] = user;
            });
        });
    }
}


class ChannelMessagesCtrl {
    constructor($scope, CompanyService, localStorageService, $stateParams, $uibModal) {
        'ngInject';
        this.CompanyService = CompanyService;
        this.channelName = $stateParams.channel;
        this.msgForm = {};     
        this.$uibModal = $uibModal;
        this.localStorageService = localStorageService;

        CompanyService.getAllMessages($stateParams.company, $stateParams.channel).then(resp => {
            this.messages = resp.data;
        });
    }

    sendMessage(form, data) {
        data.channel = this.channelName;
        this.CompanyService.sendChannelMessage(data).then( resp => {
            this.messages.push(resp.data);
            form.$setPristine();
            this.msgForm = {}; //reset form data
        });
    } 
}


export {
    IndexCtrl,
    CompanyDetailCtrl,
    ChannelMessagesCtrl
};