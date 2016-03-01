angular.module('featuresApp')
    .controller('featuresController', ['$scope', '$http', '$location', '$window',
        function($scope, $http, $location, $window) {
            $scope.features = [];
            $scope.clients = []
            $scope.isSuper = false;

            $scope.getClientById = function(client_id) {
                for (var key in $scope.clients) {
                    var client = $scope.clients[key];

                    if (client.id == client_id) {
                        return client;
                    }
                }

                return null;
            }

            $scope.fetchFeatures = function() {
                $http({
                    method  : 'GET',
                    url     : API_URL + '/features/',
                    headers : { 'Content-Type': 'application/json' }
                }).then(
                    function(data) {
                        $scope.features = data.data.results;
                    },
                    function(error) { 
                        if (error.status == 401) {
                            $location.path('/login')
                        } else {
                            console.log(error)
                        }
                    }
                );
            }

            $scope.deleteFeature = function(feature_id) {
                $http({
                    method  : 'DELETE',
                    url     : API_URL + '/features/' + feature_id + "/",
                    headers : { 'Content-Type': 'application/json' }
                }).then(
                    function(data) {
                        $scope.fetchFeatures();
                    },
                    function(error) {
                        console.log(error);
                    }
                ); 
            }

            $scope.editFeature = function(feature_id) {
                $location.path('/feature/' + feature_id);
            }
            $scope.viewFeature = function(feature_id) {
                $location.path('/feature/view/' + feature_id);
            }

            $scope.priorityRequest = function(feature, data) {
                var method_type = "PATCH";
                var url = API_URL + '/features/' + feature.id + "/";
                $http({
                    method  : method_type,
                    url     : url, 
                    headers : { 'Content-Type': 'application/json' },
                    data    : JSON.stringify(data)
                }).then(
                    function(data) {
                        $scope.fetchFeatures();
                    },
                    function(error) { 
                        console.log(error)
                });
            }

            $scope.clientPriorityMove = function(feature, direction) {

                var current_client = $scope.getClientById(feature.client_id);
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

                $scope.priorityRequest(feature, {'client_priority': new_client_priority});
            }

            $scope.masterPriorityMove = function(feature, direction) {
                if (direction == "up") {
                    var new_master_priority = feature.master_priority - 1;
                } else if (direction == "down") {
                    var new_master_priority = feature.master_priority + 1
                } else {
                    return null; // don't continue with the request.
                }
                $scope.priorityRequest(feature, {'master_priority': new_master_priority});
            }

            $scope.fetchClients = function() {
                return $http({
                    method  : 'GET',
                    url     : API_URL + '/clients/',
                    headers : { 'Content-Type': 'application/json' }
                });
            }

            $scope.fetchUserProfile = function() {
                $http({
                    method  : 'GET',
                    url     : API_URL + '/users/profile',
                    headers : { 'Content-Type': 'application/json' }
                }).then(
                    function(data) {
                        $scope.isSuper = data.data.is_super;
                    },
                    function(error) {
                        if (error.status == 401) {
                            $location.path('/login')
                        }
                    });
            } 

            $scope.fetchUserProfile();
            $scope.fetchClients().then(
                function(data) {
                    $scope.clients = data.data.results;
                    $scope.fetchFeatures();
                });
        }
]);
