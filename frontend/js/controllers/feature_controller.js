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
                        $scope.clients = data.data.results;

                        // set default option on select.
                        if ($scope.clients.length > 0) {
                            $scope.feature.client_id = $scope.clients[0].id;
                        }
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

                        // set default option on select.
                        if ($scope.product_areas.length > 0) {
                            $scope.feature.product_area_id = $scope.product_areas[0].id;
                        }
                    },
                    function(error) { 
                        console.log(error)
                });
            }

            $scope.submitFeature = function(){
                var method_type = "POST";
                if ($scope.type_message == "Edit") {
                    method_type = "PATCH";
                }
                $http({
                    method  : method_type,
                    url     : API_URL + '/features/',
                    headers : { 'Content-Type': 'application/json' },
                    data    : JSON.stringify($scope.feature)
                }).then(
                    function(data) {
                        $scope.product_areas = data.data.results;
                        $location.path('/features')
                    },
                    function(error) { 
                        console.log(error)
                });
            }

            $scope.fetchClients();
            $scope.featchProductAreas();
        }
]);
