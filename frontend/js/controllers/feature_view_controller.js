angular.module('featuresApp')
    .controller('featureViewController', ['$scope', '$http', '$location', '$window', '$routeParams',
        function($scope, $http, $location, $window, $routeParams) {
            console.log('featureViewController');
            $scope.feature = {};

            $scope.fetchFeature = function() {
                console.log($routeParams.featureId)
                console.log('featureId')
                $http({
                    method  : 'GET',
                    url     : API_URL + '/features/' + $routeParams.featureId,
                    headers : { 'Content-Type': 'application/json' }
                }).then(
                    function(data) {
                        $scope.feature = data.data;
                    },
                    function(error) {
                        if (error.status == 401) {
                            $location.path('/login')
                        }
                });
            }

            $scope.fetchFeature();
        }
]);
