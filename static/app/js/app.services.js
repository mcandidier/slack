export default class CompanyService {
    constructor($http, AppConstant, localStorageService) {
        'ngInject';

        this.http = $http;
        this.AppConstant = AppConstant;
        this.localStorageService = localStorageService;
        this.members = {};
        this.channels = [];
    }

    companyList() {
        return this.http.get(this.AppConstant.apiUrl + 'companies/');
    }

    getAllChannels(company) {
        return this.http.get(this.AppConstant.apiUrl + `companies/${company}/channels/`).then( resp => this.channels = resp.data);
    }

    getAllMembers(company) {
        return this.http.get(this.AppConstant.apiUrl + `companies/${company}/members/`);
    }

    getAllMessages(company, channel) {
        return this.http.get(this.AppConstant.apiUrl + `companies/${company}/channels/${channel}/messages/`);
    }

    sendChannelMessage(company, channel, form) {
        return this.http.post(this.AppConstant.apiUrl + `companies/${company}/channels/${channel}/messages/`, form);
    }

    createChannel(form) {
        return this.http.post(this.AppConstant.apiUrl + 'channels/', form);
    }

    getChannelMembers(company, channel) {
        // get all members for private channels only
        return this.http.get(this.AppConstant.apiUrl + `companies/${company}/channels/${channel}/members/`);
    }

    inviteToChannel(form) {
        // invite selected user
        return this.http.post(this.AppConstant.apiUrl + 'channel-members/', form);
    }

    removeMember(form) {
        return this.http.delete(this.AppConstant.apiUrl + 'channel-members/', form)
    }


}