class InviteChannelMember {
    constructor($scope, CompanyService) {
        'ngInject';
        this.$scope = $scope;
        this.CompanyService = CompanyService;
        this.form = {};
    }

    $onInit() {
        console.log('init invite member');
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
        form: '<'
    }
}


export default InviteComponent;