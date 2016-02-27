angular.module('featuresApp')
    .controller('featuresController', ['$scope', '$http', '$location', '$window',
        function($scope, $http, $location, $window) {
            $scope.features = [];

            $scope.featchFeatures = function() {
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

            $scope.featchFeatures();
        }
]);
