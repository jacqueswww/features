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

            $scope.fetchFeatures();
        }
]);
