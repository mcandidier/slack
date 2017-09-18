class InviteChannelMember {
    constructor($scope, CompanyService, $stateParams) {
        'ngInject';
        this.$scope = $scope;
        this.CompanyService = CompanyService;
        this.form = {};
        this.$stateParams = $stateParams;
    }

    $onInit() {        
        const members =  _.map(this.CompanyService.members, user => user.member);
        this.selections = _.difference(members, this.resolve.members);
    }

    invite(user) {
        const form = {'member': user, 'channel': this.$stateParams.channel};
        this.CompanyService.inviteToChannel(form).then( resp => {
            this.close({$value: resp.data});
        });
    }
}

let InviteComponent = {
    templateUrl: '/static/app/js/templates/channel/invite.html',
    controller: InviteChannelMember,
    controllerAs: 'ctrl',
    bindings: {
        resolve: '<',
        close: '&',
        dismiss: '&',
    }
}


export default InviteComponent;