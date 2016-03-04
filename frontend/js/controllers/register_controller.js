angular.module('featuresApp')
    .controller('registerController', ['$scope', '$http', '$location', '$window', '$routeParams',
        function($scope, $http, $location, $window, $routeParams) {
            console.log('registerController');

            $scope.registration_details = {};
            $scope.error_message = "";

            $scope.submitRegister = function() {
                $error_message = "";
                $http({
                    method  : 'POST',
                    url     : '/api/v1/users/register',
                    headers : { 'Content-Type': 'application/json' },
                    data: JSON.stringify($scope.registration_details)
                }).then(
                    function(data) {
                        $location.path('features');
                    },
                    function(error) {
                        console.log(error)
                        $scope.error_message = error.data.message;
                });
            }
        }
]);
