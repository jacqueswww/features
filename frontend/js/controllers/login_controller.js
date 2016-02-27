angular.module('featuresApp')
    .controller('loginController', ['$scope', '$http', '$location', '$window', '$routeParams',
        function($scope, $http, $location, $window, $routeParams) {
            console.log('loginController');
            $scope.user = "";
            $scope.password = "";
            $scope.error_message = "";

            $scope.submitLogin = function() {
                $error_message = "";
                $http({
                    method  : 'POST',
                    url     : '/api/v1/users/login',
                    headers : { 'Content-Type': 'application/json' },
                    data: JSON.stringify({
                        'user': $scope.user,
                        'password': $scope.password
                    })
                }).then(
                    function(data) {
                        $location.path('/features')
                    },
                    function(error) { 
                        $scope.error_message = 'Login failed';
                });
            }
        }
]);
