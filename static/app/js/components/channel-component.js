class ChannelController {
    constructor(CompanyService, $stateParams) {
        'ngInject';
        this.CompanyService = CompanyService;
        this.stateParams = $stateParams;
    }

    $onInit() {
    }

    submit(form) {
        /* Create new channel for active project. 
         * push new data after creation.
         */
        console.log(this.form)
        if(form.$valid) {
            this.CompanyService.createChannel(this.stateParams.company, this.form).then( resp => { 
                this.CompanyService.channels.push(resp.data);
                this.close({$value: 'close'});
            });
        }
    }
}

/* new channel as component
*/
let ChannelFormComponent =  {
    templateUrl: '/static/app/js/templates/channel_create.html',
    controller: ChannelController,
    controllerAs: 'ctrl',
    bindings: {
        resolve: '<',
        close: '&',
        dismiss: '&',
        form: '<'
    }
}

export default ChannelFormComponent;