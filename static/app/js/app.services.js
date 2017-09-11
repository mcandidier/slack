export default class CompanyService {
    constructor($http, AppConstant, localStorageService) {
        'ngInject';

        this.http = $http;
        this.AppConstant = AppConstant;
        this.localStorageService = localStorageService;
        this.members = {};
    }

    companyList() {
        return this.http.get(this.AppConstant.apiUrl + 'companies/');
    }

    setupCompany() {
        const companyId = this.localStorageService.get('companyId');
        return this.http.get('/config/'+ companyId +'/');
    }

    getAllChannels() {
        return this.http.get(this.AppConstant.apiUrl + 'channels/');
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
        return this.http.post(this.AppConstant.apiUrl + 'channels/', post);
    }
}