angular.module('featuresApp')
    .controller('dashboardController', ['$scope', '$http', '$location', '$window', '$routeParams', 
        'UserService', 'ClientService', 'FeatureService',
        function($scope, $http, $location, $window, $routeParams, UserService, ClientService, FeatureService) {
            console.log('dashboardController');

            $scope.clientFeatures = {};
            $scope.productAreaFeatures = {};
            $scope.masterFeatureList = [];
            $scope.isSuper = false;
            $scope.loading_text = "Loading...";

            $scope.fetchFeatures = function() {
                FeatureService.fetchFeatures().then(function(data) {
                        $scope.loading_text = "";
                        $scope.identity = angular.identity;
                        $scope.clientFeatures = {};
                        $scope.masterFeatureList = [];
                        $scope.productAreaFeatures = {};

                        for(var key in data.data.results) {
                            var feature = data.data.results[key];
                            if(!(feature.client_name in $scope.clientFeatures)) {
                                $scope.clientFeatures[feature.client_name] = [];
                            }
                            if(!(feature.product_area_name in $scope.productAreaFeatures)) {
                                $scope.productAreaFeatures[feature.product_area_name] = [];
                            }
                            $scope.clientFeatures[feature.client_name].push(feature);
                            $scope.productAreaFeatures[feature.product_area_name].push(feature);
                            $scope.masterFeatureList.push(feature);
                        }
                    },
                    function(error) {
                        if (error.status == 401) {
                            $location.path('/login')
                        } else {
                            console.log(error)
                        }
                    });
            };

            $scope.masterPriorityMove = function(feature, direction) {
                $scope.loading_text = "Saving..."
                FeatureService.masterPriorityMove(feature, direction).then(
                    function(data) {
                        $scope.loading_text = "";
                        $scope.fetchFeatures();
                    });
                if (feature.master_priority > 1 && direction == "up" ) {
                    feature.master_priority = feature.master_priority - 1.5;
                } else if (feature.master_priority < $scope.masterFeatureList.length && direction == "down") {
                    feature.master_priority = feature.master_priority + 1.5;
                }
            }

            $scope.clientPriorityMove = function(feature, direction) {
                $scope.loading_text = "Saving..."
                FeatureService.clientPriorityMove(feature, direction, $scope.clients)
                    .then(function(data) {
                        $scope.loading_text = "";
                        $scope.fetchFeatures();
                    });
                if (direction == "up") {
                    feature.client_priority = feature.client_priority - 1.5;
                } else if (direction == "down") {
                    feature.client_priority = feature.client_priority + 1.5;
                }
            }

            ClientService.fetchClients().then(  // load client before loading features.
                function(data) {
                    $scope.clients = data.data.results;
                });

            // fetch user profile.
            UserService.fetchUserProfile().
                then(function(data) {
                    $scope.isSuper = data.data.is_super;
                    $scope.fetchFeatures();
                })
        }
])
