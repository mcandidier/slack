class ChannelMembersController {
    constructor(CompanyService, $stateParams, $uibModal) {
        'ngInject';
        this.CompanyService = CompanyService;
        this.stateParams = $stateParams;
        this.allMembers = CompanyService.members;
        this.uibModal = $uibModal;
        this.channelMembers = [];
    }

    $onInit() {
        const name = this.stateParams.channel;
        this.CompanyService.getChannelMembers(name).then( resp => {
            this.channelMembers = resp.data;
        });
    }

    inviteMember() {
        let modalInstance = this.uibModal.open({
            component: 'inviteComponent',
            resolve: {
                members: () => {
                  return this.channelMembers.map( user => user.member);
                }
            }
        });

        modalInstance.result.then( newMember => {
            this.channelMembers.push(newMember);
        }, function () {
            console.log('xx');
        });

    } 
}


let ChannelMemberComponent = {
    templateUrl: '/static/app/js/templates/channel/members.html',
    controller: ChannelMembersController,
    controllerAs: 'ctrl',
    bindings: {
        resolve: '<',
        close: '&',
        dismiss: '&',
        form: '<',
    }
}


export default ChannelMemberComponent;