export default class CompanyService {
    constructor($http, AppConstant, localStorageService) {
        'ngInject';

        this.http = $http;
        this.AppConstant = AppConstant;
        this.localStorageService = localStorageService;
        this.members = {};
        this.channels = [];
        this.currentChannel = undefined;

        this.getAllChannels();
    }

    companyList() {
        return this.http.get(this.AppConstant.apiUrl + 'companies/');
    }

    setupCompany() {
        const companyId = this.localStorageService.get('companyId');
        return this.http.get('/config/'+ companyId +'/');
    }

    getAllChannels() {
        return this.http.get(this.AppConstant.apiUrl + 'channels/').then( resp => {
            this.channels = resp.data;
        });
    }

    getAllMembers() {
        return this.http.get(this.AppConstant.apiUrl + 'members/');
    }

    getAllMessages(channel_name) {
        return this.http.get(this.AppConstant.apiUrl + 'messages/?channel='+channel_name);
    }

    sendChannelMessage(form) {
        return this.http.post(this.AppConstant.apiUrl + 'messages/', form);
    }


    createChannel(form) {
        return this.http.post(this.AppConstant.apiUrl + 'channels/', form);
    }

    getChannelMembers(channel) {
        /* get all members for private channels only
         */
        return this.http.get(this.AppConstant.apiUrl + 'channel-members/?channel='+channel);
    }

    inviteToChannel(form) {
        /* invite selected user 
         */
        return this.http.post(this.AppConstant.apiUrl + 'channel-members/', form);
    }


}