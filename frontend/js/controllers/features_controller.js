angular.module('featuresApp')
    .controller('featuresController', ['$scope', '$http', '$location', '$window', 
        'UserService', 'ClientService', 'FeatureService',
        function($scope, $http, $location, $window, UserService, ClientService, FeatureService) {
            $scope.features = [];
            $scope.clients = []
            $scope.isSuper = false;

            $scope.fetchFeatures = function() {
                FeatureService.fetchFeatures().then(
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
                FeatureService.deleteFeature(feature_id).then(
                    function(data) {
                        $scope.fetchFeatures();
                    }); 
            }

            $scope.editFeature = function(feature_id) {
                $location.path('/feature/' + feature_id);
            }

            $scope.viewFeature = function(feature_id) {
                $location.path('/feature/view/' + feature_id);
            }

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

            UserService.fetchUserProfile().
                then(
                function(data) {
                    $scope.isSuper = data.data.is_super;
                },
                function(error) {
                    if (error.status == 401) {
                        $location.path('/login')
                    }
                });

            ClientService.fetchClients().then(  // load client before loading features.
                function(data) {
                    $scope.clients = data.data.results;
                    $scope.fetchFeatures();
                });
        }
]);
