angular.module('featuresApp')
    .controller('featuresController', ['$scope', '$http', '$location', '$window',
        function($scope, $http, $location, $window) {
            $scope.features = [];

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

            $scope.clientPriorityMove = function(feature, direction) {

                if (feature.client_priority > 1 && direction == "up") {
                    var new_client_priority = feature.client_priority - 1;
                } else if (direction == "down") {
                    var new_client_priority = feature.client_priority + 1
                }

                var method_type = "PATCH";
                var url = API_URL + '/features/' + feature.id + "/";
                $http({
                    method  : method_type,
                    url     : url, 
                    headers : { 'Content-Type': 'application/json' },
                    data    : JSON.stringify({'client_priority': new_client_priority})
                }).then(
                    function(data) {
                        $scope.fetchFeatures();
                    },
                    function(error) { 
                        console.log(error)
                });
            }

            $scope.fetchFeatures();
        }
]);
