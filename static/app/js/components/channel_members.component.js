class ChannelMembersController {
    constructor(CompanyService, $stateParams) {
        'ngInject';
        this.CompanyService = CompanyService;
        this.stateParams = $stateParams;
    }

    $onInit() {
        const name = this.stateParams.channel;
        this.CompanyService.getChannelMembers(name).then( resp => {
            this.channelMembers = resp.data;
        });
    }
}


let ChannelMemberComponent = {
    templateUrl: '/static/app/js/templates/private_channel_members.html',
    controller: ChannelMembersController,
    controllerAs: 'ctrl'
}


export default ChannelMemberComponent;