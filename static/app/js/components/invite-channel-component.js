class InviteChannelMember {
    constructor($scope, CompanyService) {
        'ngInject';
        this.$scope = $scope;
        this.CompanyService = CompanyService;
        this.form = {};
        this.channelMembers = [];
    }

    $onInit() {
        const members =  _.map(this.CompanyService.members, user => user.member);
        this.selections = _.difference(members, this.resolve.members);
    }

    add() {
        console.log('add');
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
        form: '<',
    }
}


export default InviteComponent;