angular.module('featuresApp')
    .controller('dashboardController', ['$scope', '$http', '$location', '$window', '$routeParams', 
        'UserService', 'ClientService', 'FeatureService',
        function($scope, $http, $location, $window, $routeParams, UserService, ClientService, FeatureService) {
            console.log('dashboardController');

            $scope.clientFeatures = {};
            $scope.productAreaFeatures = {};
            $scope.masterFeatureList = [];
            $scope.isSuper = false;

            $scope.fetchFeatures = function() {
                FeatureService.fetchFeatures().then(function(data) {
                        $scope.identity = angular.identity;
                        $scope.clientFeatures = {};
                        $scope.masterFeatureList = [];
                        
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
                FeatureService.masterPriorityMove(feature, direction).then(
                    function(data) {
                        $scope.fetchFeatures();
                    });
            }

            $scope.clientPriorityMove = function(feature, direction) {
                FeatureService.clientPriorityMove(feature, direction, $scope.clients)
                    .then(function(data) {
                        $scope.fetchFeatures();
                    });
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
