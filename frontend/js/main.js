API_URL = "/api/v1";


var featuresApp = angular.module('featuresApp', ['ngRoute', 'datePicker', 'yaru22.md']);

// configure our routes
featuresApp.config(function($routeProvider) {
    $routeProvider
        // route for the home page.
        .when('/features', {
            templateUrl : 'pages/features.html',
            controller  : 'featuresController',
            title: 'List Features'
        })
        // route for feature create and edit.
        .when('/feature/:featureId', {
            templateUrl : 'pages/feature.html',
            controller  : 'featureController',
            title: ''
        })
        .when('/feature/view/:featureId', {
            templateUrl : 'pages/feature_view.html',
            controller  : 'featureViewController',
            title: ''
        })
        // route for the login page.
        .when('/login', {
            templateUrl : 'pages/login.html',
            controller  : 'loginController',
            title: 'Login'
        })
        .otherwise({ // TODO: create a 404 page.
            redirectTo: '/features'
        })
});

// set title on switch.
featuresApp.run(['$rootScope', '$route', function($rootScope, $route) {
    $rootScope.$on('$routeChangeSuccess', function() {
        document.title = $route.current.title;
    });
}]);

// create the controller and inject Angular's $scope
featuresApp.controller('mainController', function($scope) {
    console.log('mainController')

    $scope.logged_in = false;
});
