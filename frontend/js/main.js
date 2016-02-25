var featuresApp = angular.module('featuresApp', ['ngRoute']);

// configure our routes
featuresApp.config(function($routeProvider) {
    $routeProvider
        // route for the home page
        .when('/', {
            templateUrl : 'pages/features.html',
            controller  : 'featuresController',
        })
        // route for the login page
        .when('/login', {
            templateUrl : 'pages/login.html',
            controller  : 'loginController',
        });
});

// set title on switch.
// featuresApp.run(['$rootScope', '$route', function($rootScope, $route) {
//     $rootScope.$on('$routeChangeSuccess', function() {
//         document.title = $route.current.title;
//     });
// }]);

// create the controller and inject Angular's $scope
featuresApp.controller('mainController', function($scope) {

});
