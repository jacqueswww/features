angular.module('featuresApp')
    .service('UserService', function($http) {
    this.fetchUserProfile = function() {
        return $http({
            method  : 'GET',
            url     : API_URL + '/users/profile',
            headers : { 'Content-Type': 'application/json' }
        });
    } 
});

angular.module('featuresApp')
    .service('ClientService', function($http) {
    this.fetchClients = function() {
        return $http({
            method  : 'GET',
            url     : API_URL + '/clients/',
            headers : { 'Content-Type': 'application/json' }
        });
    };
});

angular.module('featuresApp')
    .service('FeatureService', function($http) {
    var self = this;

    self.fetchFeatures = function() {
        return $http({
            method  : 'GET',
            url     : API_URL + '/features/',
            headers : { 'Content-Type': 'application/json' }
            });
    };

    self.deleteFeature = function(feature_id) {
        return $http({
            method  : 'DELETE',
            url     : API_URL + '/features/' + feature_id + "/",
            headers : { 'Content-Type': 'application/json' }
        });
    }

    self.priorityRequest = function(feature, data) {
        var method_type = "PATCH";
        var url = API_URL + '/features/' + feature.id + "/";
        return $http({
            method  : method_type,
            url     : url, 
            headers : { 'Content-Type': 'application/json' },
            data    : JSON.stringify(data)
        });
    }

    self.getClientById = function(clients, client_id) {
        for (var key in clients) {
            var client = clients[key];
            if (client.id == client_id) {
                return client;
            }
        }

        return null;
    }

    self.clientPriorityMove = function(feature, direction, clients) {
        console.log(clients)
        console.log('!!!!!')
        var current_client = self.getClientById(clients, feature.client_id);
        console.log(current_client)
        console.log(feature.client_priority)
        if ( direction == "up" && feature.client_priority > 1) {
            var new_client_priority = feature.client_priority - 1;
        } else if (direction == "down" && 
                   feature.client_priority < current_client.max_client_priority) {
            var new_client_priority = feature.client_priority + 1
        } else {
            return null; // don't continue with the request.
        }

        return self.priorityRequest(feature, {'client_priority': new_client_priority});
    }

    self.masterPriorityMove = function(feature, direction) {
        console.log('MASTER MOVE!')
        if (feature.master_priority > 1 && direction == "up") {
            var new_master_priority = feature.master_priority - 1;
        } else if (direction == "down") {
            var new_master_priority = feature.master_priority + 1
        } else {
            return null; // don't continue with the request.
        }
        return self.priorityRequest(feature, {'master_priority': new_master_priority});
    }

});