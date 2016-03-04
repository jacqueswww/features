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
        // route for the login page.
        .when('/register', {
            templateUrl : 'pages/register.html',
            controller  : 'registerController',
            title: 'Register'
        })
        // route for the dashboard page.
        .when('/dashboard', {
            templateUrl : 'pages/dashboard.html',
            controller  : 'dashboardController',
            title: 'Dashboard'
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

// This filter converts an associative array to an array, so we can sort it.
featuresApp.filter('toArray', function() { return function(obj) { 
    if (!(obj instanceof Object)) return obj;
    res =  _.map(obj, function(val, key) {
        return Object.defineProperty(val, '$key', {__proto__: null, value: key});
    });
    // console.log(res)
    return res;
}});
