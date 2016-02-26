angular.module('featuresApp')
    .controller('featureController', ['$scope', '$http', '$location', '$window', '$routeParams',
        function($scope, $http, $location, $window, $routeParams) {
            console.log('featureController');

            $scope.clients = [];
            $scope.product_areas = [];
            $scope.type_message = "";
            $scope.feature = {};

            console.log($routeParams)
            if ($routeParams.featureId !== undefined && $routeParams.featureId == "create") {
                $scope.type_message = "Add";
            } else {
                $scope.type_message = "Edit";
            }

            $scope.fetchClients = function() {
                $http({
                    method  : 'GET',
                    url     : API_URL + '/clients/',
                    headers : { 'Content-Type': 'application/json' }
                }).then(
                    function(data) {
                        $scope.clients = data.data.results
                    },
                    function(error) { 
                        console.log(error)
                });
            }

            $scope.featchProductAreas = function() {
                $http({
                    method  : 'GET',
                    url     : API_URL + '/product_areas/',
                    headers : { 'Content-Type': 'application/json' }
                }).then(
                    function(data) {
                        $scope.product_areas = data.data.results;
                    },
                    function(error) { 
                        console.log(error)
                });
            }

            $scope.fetchClients();
            $scope.featchProductAreas();
        }
]);
