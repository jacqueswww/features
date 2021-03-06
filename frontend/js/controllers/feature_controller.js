angular.module('featuresApp')
    .controller('featureController', ['$scope', '$http', '$location', '$window', '$routeParams', 'UserService', 'ClientService', 'FeatureService',
        function($scope, $http, $location, $window, $routeParams, UserService, ClientService, FeatureService) {
            console.log('featureController');

            $scope.clients = [];
            $scope.product_areas = [];
            $scope.type_message = "";
            $scope.feature = {
                'client_priority': 1,
                'master_priority': 1
            };
            $scope.max_client_priority = 1;
            $scope.isSuper = false;

            $scope.loadParams = function() {
                if ($routeParams.featureId !== undefined && $routeParams.featureId == "create") {
                    $scope.type_message = "Add";
                } else {
                    $scope.type_message = "Edit";
                    $scope.fetchFeature($routeParams.featureId);
                }
            }

            $scope.fetchFeature = function(feature_id) {
                $http({
                    method  : 'GET',
                    url     : API_URL + '/features/' + feature_id,
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

            $scope.setMaxClientPriority = function(client_id) {
                console.log(client_id);
                angular.forEach($scope.clients, function(client, key) {
                    if (client.id == client_id) {
                        $scope.max_client_priority = client.max_client_priority + 1;
                        if ($scope.feature.client_priority > $scope.max_client_priority) {
                            $scope.feature.client_priority = $scope.max_client_priority;
                        }
                        return;
                    }
                });
            }

            $scope.fetchProductAreas = function() {
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
                var url = API_URL + '/features/';
                if ($scope.type_message == "Edit") {
                    method_type = "PATCH";
                    url += $scope.feature.id + "/";
                }
                $http({
                    method  : method_type,
                    url     : url, 
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

            $scope.deleteFeature = function(feature_id) {
                FeatureService.deleteFeature(feature_id).then(
                    function(data) {
                        $location.path('/features');
                    });
            }
            
            // fetch user profile.
            UserService.fetchUserProfile().
                then(function(data) {
                    $scope.isSuper = data.data.is_super;
                });

            //fetch clients.
            ClientService.fetchClients().then(
                function(data) {
                    $scope.clients = data.data.results;

                    // set default option on select.
                    if ($scope.clients.length > 0) {
                        $scope.feature.client_id = $scope.clients[0].id;
                        $scope.max_client_priority = $scope.clients[0].max_client_priority + 1;
                    }
                },
                function(error) {
                    if (error.status == 401) {
                        $location.path('/login')
                    }
            });

            $scope.loadParams();
            $scope.fetchProductAreas();
        }
]);
